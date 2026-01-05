"""Tests for Kafka producer and consumer."""

from unittest.mock import Mock

from skeleton.kafka.producer import MessageProducer


def test_mock_producer_implements_protocol(mock_producer: Mock) -> None:
    """Test that mock producer implements MessageProducer protocol."""
    # Verify the mock has the expected methods from the protocol
    assert hasattr(mock_producer, "produce")
    assert hasattr(mock_producer, "flush")


def test_producer_produce_is_callable(mock_producer: Mock) -> None:
    """Test that produce method can be called."""
    mock_producer.produce("test-topic", "key", b"value")
    mock_producer.produce.assert_called_once_with("test-topic", "key", b"value")


def test_producer_flush_is_callable(mock_producer: Mock) -> None:
    """Test that flush method can be called."""
    mock_producer.flush.return_value = 0
    result = mock_producer.flush(timeout=5.0)
    assert result == 0
    mock_producer.flush.assert_called_once_with(timeout=5.0)


def test_message_producer_protocol_type_hint() -> None:
    """Test that MessageProducer can be used as a type hint."""
    producer: MessageProducer = Mock(spec=MessageProducer)
    producer.produce("topic", "key", b"value")
    producer.flush()
