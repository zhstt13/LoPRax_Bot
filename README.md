# LoPRax Bot

A modular Telegram bot and API layer built around a reusable download core.

## Architecture

- `core/` reusable download engine
- `backend/` API and application services
- `telegram/` Telegram client layer

The core must remain independent from Telegram so future clients can use the same engine.
