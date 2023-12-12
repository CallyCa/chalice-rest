from sqlalchemy.orm import DeclarativeBase

from chalice_rest.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
