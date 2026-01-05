"""Dependency injection factory functions."""

import logging

from fastapi import FastAPI

from skeleton.config import Config
from skeleton.handlers.health import router as health_router
from skeleton.handlers.metrics import router as metrics_router
from skeleton.kafka.producer import KafkaMessageProducer, MessageProducer

logger = logging.getLogger(__name__)


def create_kafka_producer(config: Config) -> MessageProducer:
    """Create a Kafka producer instance.

    Args:
        config: Application configuration

    Returns:
        MessageProducer implementation
    """
    return KafkaMessageProducer(brokers=config.kafka_brokers)


def create_app(config: Config) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        config: Application configuration

    Returns:
        Configured FastAPI application
    """
    app = FastAPI(
        title="skeleton",
        version=config.build_version,
        description="Python project skeleton with FastAPI and Kafka",
    )

    # Include routers
    app.include_router(health_router)
    app.include_router(metrics_router)

    # Store config in app state for access in handlers
    app.state.config = config

    logger.info("Application created successfully")
    return app
