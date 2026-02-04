"""Pytest fixtures for handler tests."""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from skeleton.config import Config
from skeleton.factory import create_app


@pytest.fixture
def app(config: Config) -> Generator[TestClient]:
    """Create a test client for the FastAPI application."""
    fastapi_app = create_app(config)
    with TestClient(fastapi_app) as client:
        yield client
