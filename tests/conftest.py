"""Pytest fixtures for testing."""

from collections.abc import Generator
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from skeleton.config import Config
from skeleton.factory import create_app
from skeleton.kafka.producer import MessageProducer


@pytest.fixture
def config() -> Config:
    """Create a test configuration."""
    return Config(
        kafka_brokers="localhost:9092",
        sentry_dsn="",
        build_version="test",
        build_commit="abc123",
        build_date="2024-01-01",
    )


@pytest.fixture
def app(config: Config) -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application."""
    fastapi_app = create_app(config)
    with TestClient(fastapi_app) as client:
        yield client


@pytest.fixture
def mock_producer() -> Mock:
    """Create a mock Kafka producer."""
    return Mock(spec=MessageProducer)
