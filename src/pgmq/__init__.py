from typing import TYPE_CHECKING, Optional

from pgmq.queue import Message, PGMQueue  # type: ignore
from pgmq.decorators import transaction, async_transaction

if TYPE_CHECKING:  # pragma: no cover
    from fastapi import FastAPI


def create_app(queue: Optional[PGMQueue] = None):
    """Create a FastAPI application for interacting with PGMQ."""

    from pgmq.api import create_app as _create_app

    return _create_app(queue=queue)


__all__ = ["Message", "PGMQueue", "transaction", "async_transaction", "create_app"]
