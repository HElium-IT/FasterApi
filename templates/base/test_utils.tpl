from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.$$router_name$$ import $$class_name$$Create
from app.tests.utils.utils import random_lower_string

def create_random_$$router_name$$(db: Session, *) -> models.$$class_name$$:
    name = random_lower_string()
    $$router_name$$_in = $$class_name$$Create(name=name)
    return crud.$$router_name$$.create(db=db, obj_in=$$router_name$$_in)