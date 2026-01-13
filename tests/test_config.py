"""Tests for application configuration."""

from skeleton.config import Config


def test_config_defaults() -> None:
    """Test that Config has sensible defaults."""
    config = Config()
    assert config.kafka_brokers == "localhost:9092"
    assert config.sentry_dsn == ""
    assert config.build_version == "dev"
    assert config.build_commit == "none"
    assert config.build_date == "unknown"


def test_config_custom_values() -> None:
    """Test that Config accepts custom values."""
    config = Config(
        kafka_brokers="broker1:9092,broker2:9092",
        sentry_dsn="https://example@sentry.io/123",
    )
    assert config.kafka_brokers == "broker1:9092,broker2:9092"
    assert config.sentry_dsn == "https://example@sentry.io/123"


def test_config_from_fixture(config: Config) -> None:
    """Test that config fixture provides valid configuration."""
    assert config.kafka_brokers == "localhost:9092"
    assert config.sentry_dsn == ""
