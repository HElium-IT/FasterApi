from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from uuid import uuid4
from app.database.base import Base


class $$class_name$$(Base):
    id: str = Column(String, default=uuid4, primary_key=True, index=True)
    name: str = Column(String)

