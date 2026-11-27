"""FastAPI application entrypoint.

Security invariant: the server MUST bind to 127.0.0.1 only.
This app is intended for strictly local use; never expose it on other hosts.
"""

import os

from fastapi import FastAPI

app = FastAPI(title="Medical Research DB", version="0.1.0")

# Hard bind host for local-only operation. Do not change to 0.0.0.0.
HOST = "127.0.0.1"


@app.get("/health")
def health() -> dict:
    """Liveness probe."""
    return {"status": "ok"}


def main() -> None:
    """Run the local server, bound to loopback only."""
    import uvicorn

    uvicorn.run(app, host=HOST, port=int(os.environ.get("APP_PORT", "8000")))


if __name__ == "__main__":
    main()
