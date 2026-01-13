"""Tests for health check endpoints."""

from fastapi.testclient import TestClient


def test_healthz_returns_ok(app: TestClient) -> None:
    """Test that /healthz returns ok status."""
    response = app.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_returns_ready(app: TestClient) -> None:
    """Test that /readiness returns ready status."""
    response = app.get("/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
