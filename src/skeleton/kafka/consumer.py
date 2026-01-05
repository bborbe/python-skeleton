"""Kafka consumer with Protocol-based message handling."""

import logging
from typing import Protocol

from confluent_kafka import Consumer, KafkaException, Message

logger = logging.getLogger(__name__)


class MessageHandler(Protocol):
    """Protocol for message handlers."""

    def handle(self, topic: str, key: str, value: bytes) -> None:
        """Handle a consumed message.

        Args:
            topic: Kafka topic name
            key: Message key
            value: Message value as bytes
        """
        ...


class KafkaMessageConsumer:
    """Kafka consumer implementation with message handler injection."""

    def __init__(
        self,
        brokers: str,
        group_id: str,
        topics: list[str],
        handler: MessageHandler,
    ) -> None:
        """Initialize the Kafka consumer.

        Args:
            brokers: Comma-separated list of Kafka brokers
            group_id: Consumer group ID
            topics: List of topics to subscribe to
            handler: Message handler for processing messages
        """
        self._consumer = Consumer(
            {
                "bootstrap.servers": brokers,
                "group.id": group_id,
                "auto.offset.reset": "earliest",
                "enable.auto.commit": True,
            }
        )
        self._topics = topics
        self._handler = handler
        self._running = False

        logger.info(f"Kafka consumer initialized: brokers={brokers}, group_id={group_id}")

    def start(self) -> None:
        """Start consuming messages."""
        self._consumer.subscribe(self._topics)
        self._running = True
        logger.info(f"Subscribed to topics: {self._topics}")

        try:
            while self._running:
                msg = self._consumer.poll(timeout=1.0)
                if msg is None:
                    continue

                if msg.error():
                    self._handle_error(msg)
                    continue

                self._process_message(msg)
        finally:
            self._consumer.close()
            logger.info("Consumer closed")

    def stop(self) -> None:
        """Stop consuming messages."""
        self._running = False
        logger.info("Consumer stop requested")

    def _handle_error(self, msg: Message) -> None:
        """Handle consumer errors.

        Args:
            msg: Kafka message with error
        """
        error = msg.error()
        if error is None:
            return
        # KafkaError._PARTITION_EOF is -191
        if error.code() == -191:  # PARTITION_EOF
            logger.debug(f"Reached end of partition: {msg.topic()}[{msg.partition()}]")
        else:
            raise KafkaException(error)

    def _process_message(self, msg: Message) -> None:
        """Process a consumed message.

        Args:
            msg: Kafka message to process
        """
        topic = msg.topic() or ""
        raw_key = msg.key()
        key = raw_key.decode("utf-8") if raw_key else ""
        value = msg.value() or b""

        logger.debug(f"Processing message: topic={topic}, key={key}")

        try:
            self._handler.handle(topic, key, value)
        except Exception:
            logger.exception(f"Error handling message: topic={topic}, key={key}")
