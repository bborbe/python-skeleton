"""Application configuration using Pydantic BaseSettings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Kafka configuration
    kafka_brokers: str = Field(
        default="localhost:9092",
        description="Comma-separated list of Kafka brokers",
    )

    # Sentry configuration
    sentry_dsn: str = Field(
        default="",
        description="Sentry DSN for error tracking",
    )

    # Build metadata
    build_version: str = Field(
        default="dev",
        alias="BUILD_VERSION",
        description="Build version from CI/CD",
    )
    build_commit: str = Field(
        default="none",
        alias="BUILD_COMMIT",
        description="Git commit hash",
    )
    build_date: str = Field(
        default="unknown",
        alias="BUILD_DATE",
        description="Build date",
    )
