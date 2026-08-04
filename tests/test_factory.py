"""Tests for factory functions."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from skeleton.config import Config
from skeleton.factory import create_app, create_kafka_producer


def test_create_kafka_producer_returns_producer(config: Config) -> None:
    """Test that create_kafka_producer returns a MessageProducer."""
    producer = create_kafka_producer(config)
    # Verify the producer has the expected methods from the protocol
    assert hasattr(producer, "produce")
    assert hasattr(producer, "flush")


def test_create_app_returns_fastapi(config: Config) -> None:
    """Test that create_app returns a FastAPI instance."""
    app = create_app(config)
    assert isinstance(app, FastAPI)
    assert app.title == "skeleton"
    assert app.version == config.build_version


def test_create_app_stores_config_in_state(config: Config) -> None:
    """Test that create_app stores config in app state."""
    app = create_app(config)
    assert hasattr(app.state, "config")
    assert app.state.config == config


def test_create_app_includes_routers(config: Config) -> None:
    """Test that create_app includes health and metrics routers."""
    # Asserted by reaching the endpoints rather than by walking app.routes:
    # FastAPI >=0.141 keeps included routers as opaque wrapper objects there,
    # so structural introspection breaks on dependency bumps. Behaviour does not.
    app = create_app(config)
    with TestClient(app) as client:
        assert client.get("/healthz").status_code == 200
        assert client.get("/readiness").status_code == 200
        assert client.get("/metrics").status_code == 200
