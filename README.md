# Medical Research Database

Local-first medical research database. FastAPI backend (Python 3.11+), Tauri desktop frontend (coming later).

## Development

Install and run tests:

```bash
pip install -e ".[dev]"
pytest
```

Run the local server (binds to 127.0.0.1 only):

```bash
python -m backend.app.main
```

## Layout

- `backend/` — FastAPI app (`backend/app`) and tests (`backend/tests`)
- `frontend/` — Tauri desktop app (placeholder)
- `.github/workflows/ci.yml` — CI (pytest on Python 3.11)

## Security invariant

The local server binds to `127.0.0.1` only. Never expose it on other hosts.
