"""Pytest fixtures for testing."""

import pytest

from skeleton.config import Config


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
