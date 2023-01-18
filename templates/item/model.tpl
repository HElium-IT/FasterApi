from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.database.base import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class $$class_name$$(Base):
    id: str = Column(String, default=str(uuid4()), primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey("user.id"))
    
    owner: "User" = relationship("User", back_populates="$$pluralized_router_name$$")
