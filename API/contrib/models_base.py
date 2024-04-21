from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)