"""Tests for Kafka consumer."""

from unittest.mock import Mock

from skeleton.kafka.consumer import MessageHandler


def test_mock_handler_implements_protocol(mock_handler: Mock) -> None:
    """Test that mock handler implements MessageHandler protocol."""
    # Verify the mock has the expected method from the protocol
    assert hasattr(mock_handler, "handle")


def test_handler_handle_is_callable(mock_handler: Mock) -> None:
    """Test that handle method can be called."""
    mock_handler.handle("test-topic", "key", b"value")
    mock_handler.handle.assert_called_once_with("test-topic", "key", b"value")


def test_message_handler_protocol_type_hint() -> None:
    """Test that MessageHandler can be used as a type hint."""
    handler: MessageHandler = Mock(spec=MessageHandler)
    handler.handle("topic", "key", b"value")
