"""Pytest fixtures for Kafka tests."""

from unittest.mock import Mock

import pytest

from skeleton.kafka.consumer import MessageHandler
from skeleton.kafka.producer import MessageProducer


@pytest.fixture
def mock_producer() -> Mock:
    """Create a mock Kafka producer."""
    return Mock(spec=MessageProducer)


@pytest.fixture
def mock_handler() -> Mock:
    """Create a mock Kafka message handler."""
    return Mock(spec=MessageHandler)
