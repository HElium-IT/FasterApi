from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.$$router_name$$ import $$class_name$$
from app.schemas.$$router_name$$ import $$class_name$$Create, $$class_name$$Update


class CRUD$$class_name$$(CRUDBase[$$class_name$$, $$class_name$$Create, $$class_name$$Update]):
    def create_with_owner(
        self, db: Session, *, obj_in: $$class_name$$Create, owner_id: int
    ) -> $$class_name$$:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[$$class_name$$]:
        return (
            db.query(self.model)
            .filter($$class_name$$.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


$$router_name$$ = CRUD$$class_name$$($$class_name$$)
