from typing import Optional

from pydantic import BaseModel


# Shared properties
class $$class_name$$Base(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class $$class_name$$Create($$class_name$$Base):
    title: str


# Properties to receive on item update
class $$class_name$$Update($$class_name$$Base):
    pass


# Properties shared by models stored in DB
class $$class_name$$InDBBase($$class_name$$Base):
    id: str
    title: str
    owner_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class $$class_name$$($$class_name$$InDBBase):
    pass


# Properties stored in DB
class $$class_name$$InDB($$class_name$$InDBBase):
    pass
