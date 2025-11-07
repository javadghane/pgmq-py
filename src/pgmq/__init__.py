from typing import Optional

from pgmq.queue import Message, PGMQueue  # type: ignore
from pgmq.decorators import transaction, async_transaction


def create_app(queue: Optional[PGMQueue] = None) -> "FastAPI":
    """Create a FastAPI application for interacting with PGMQ.

    Raises:
        ImportError: If FastAPI is not installed. Install with: pip install pgmq[api]
    """
    try:
        from pgmq.api import create_app as _create_app
    except ImportError as e:
        raise ImportError(
            "FastAPI is required to use the API functionality. "
            "Install it with: pip install 'pgmq[api]' or pip install fastapi uvicorn"
        ) from e

    return _create_app(queue=queue)


__all__ = ["Message", "PGMQueue", "transaction", "async_transaction", "create_app"]
