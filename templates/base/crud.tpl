from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.$$router_name$$ import $$class_name$$
from app.schemas.$$router_name$$ import $$class_name$$Create, $$class_name$$Update


class CRUD$$class_name$$(CRUDBase[$$class_name$$, $$class_name$$Create, $$class_name$$Update]):
    pass


$$router_name$$ = CRUD$$class_name$$($$class_name$$)
