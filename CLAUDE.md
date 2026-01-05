# Claude Code Instructions

Python project skeleton following production patterns.

## Architecture

- **Entry point**: `src/skeleton/__main__.py` - CLI with subcommands
- **Config**: `src/skeleton/config.py` - Pydantic BaseSettings from env
- **DI**: `src/skeleton/factory.py` - Factory functions, constructor injection
- **HTTP**: FastAPI in `handlers/` (health, metrics)
- **Kafka**: Protocol-based producer/consumer in `kafka/`

## Key Patterns

### CLI Arguments (python-cli-arguments-guide.md)
- argparse with env var defaults
- Subcommand pattern (`serve`, `version`)

### Dependency Injection (python-ioc-guide.md)
- Protocol for interfaces
- Constructor injection
- Factory functions in `factory.py`

### Logging (python-logging-guide.md)
- `basicConfig()` once in `__main__.py`
- Module-level loggers: `logger = logging.getLogger(__name__)`

### Pydantic (python-pydantic-guide.md)
- BaseSettings for config (from pydantic_settings)
- Validate at boundary only

## Commands

```bash
make precommit  # format + lint + typecheck + test
make run        # Run server
make test       # Run tests
```

## Adding Features

1. New HTTP endpoint: Add to `handlers/`, include router in `factory.py`
2. New Kafka handler: Implement `MessageHandler` protocol
3. New config: Add field to `Config` class with env alias
