from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.$$router_name$$ import $$class_name$$Create
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string

def create_random_$$router_name$$(db: Session, *, owner_id: Optional[int] = None) -> models.$$class_name$$:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    $$router_name$$_in = $$class_name$$Create(title=title, description=description)
    return crud.$$router_name$$.create_with_owner(db=db, obj_in=$$router_name$$_in, owner_id=owner_id)