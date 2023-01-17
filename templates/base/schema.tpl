from typing import Optional

from pydantic import BaseModel


# Shared properties
class $$class_name$$Base(BaseModel):
    name: Optional[str] = None


# Properties to receive on item creation
class $$class_name$$Create($$class_name$$Base):
    name: str


# Properties to receive on item update
class $$class_name$$Update($$class_name$$Base):
    pass


# Properties shared by models stored in DB
class $$class_name$$InDBBase($$class_name$$Base):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class $$class_name$$($$class_name$$InDBBase):
    pass


# Properties stored in DB
class $$class_name$$InDB($$class_name$$InDBBase):
    pass
