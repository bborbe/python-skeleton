"""Health check endpoints for Kubernetes probes."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe endpoint.

    Returns 200 if the application is running.
    Used by Kubernetes liveness probes.
    """
    return {"status": "ok"}


@router.get("/readiness")
def readiness() -> dict[str, str]:
    """Readiness probe endpoint.

    Returns 200 if the application is ready to receive traffic.
    Used by Kubernetes readiness probes.
    """
    return {"status": "ready"}
