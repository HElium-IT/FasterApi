from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from app.database.base import Base


class $$class_name$$(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)

