from uuid import uuid4

from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class CostEntry(Base):
    __tablename__ = "cost_entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id"))
    amount = Column(Float, nullable=False)
    application = relationship("Application", back_populates="costs")
