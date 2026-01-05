"""Kafka producer with Protocol-based dependency injection."""

import logging
from typing import Protocol

from confluent_kafka import Producer

logger = logging.getLogger(__name__)


class MessageProducer(Protocol):
    """Protocol for message producers."""

    def produce(self, topic: str, key: str, value: bytes) -> None:
        """Produce a message to a topic.

        Args:
            topic: Kafka topic name
            key: Message key
            value: Message value as bytes
        """
        ...

    def flush(self, timeout: float = 10.0) -> int:
        """Flush pending messages.

        Args:
            timeout: Maximum time to wait in seconds

        Returns:
            Number of messages still in queue
        """
        ...


class KafkaMessageProducer:
    """Kafka producer implementation."""

    def __init__(self, brokers: str) -> None:
        """Initialize the Kafka producer.

        Args:
            brokers: Comma-separated list of Kafka brokers
        """
        self._producer = Producer({"bootstrap.servers": brokers})
        logger.info(f"Kafka producer initialized: brokers={brokers}")

    def produce(self, topic: str, key: str, value: bytes) -> None:
        """Produce a message to a topic.

        Args:
            topic: Kafka topic name
            key: Message key
            value: Message value as bytes
        """

        def delivery_callback(err: object, msg: object) -> None:
            if err:
                logger.error(f"Message delivery failed: {err}")
            else:
                logger.debug(f"Message delivered: topic={topic}, key={key}")

        self._producer.produce(
            topic=topic,
            key=key.encode("utf-8"),
            value=value,
            callback=delivery_callback,
        )
        self._producer.poll(0)

    def flush(self, timeout: float = 10.0) -> int:
        """Flush pending messages.

        Args:
            timeout: Maximum time to wait in seconds

        Returns:
            Number of messages still in queue
        """
        return self._producer.flush(timeout)
