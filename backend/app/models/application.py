import enum
from uuid import uuid4

from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class AppLifecycle(str, enum.Enum):
    NEW = "NEW"
    ACTIVE = "ACTIVE"
    RETIRE = "RETIRE"


class Application(Base):
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, unique=True, nullable=False)
    lifecycle = Column(Enum(AppLifecycle), default=AppLifecycle.NEW)
    costs = relationship("CostEntry", back_populates="application")
