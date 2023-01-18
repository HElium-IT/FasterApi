from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.$$class_name$$])
def read_$$router_name$$s(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve $$router_name$$s.
    """
    $$router_name$$s = crud.$$router_name$$.get_multi(db, skip=skip, limit=limit)

    return $$router_name$$s


@router.post("/", response_model=schemas.$$class_name$$)
def create_$$router_name$$(
    *,
    db: Session = Depends(deps.get_db),
    $$router_name$$_in: schemas.$$class_name$$Create,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new $$router_name$$.
    """
    $$router_name$$ = crud.$$router_name$$.create(db=db, obj_in=$$router_name$$_in)
    return $$router_name$$


@router.put("/{id}", response_model=schemas.$$class_name$$)
def update_$$router_name$$(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    $$router_name$$_in: schemas.$$class_name$$Update,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an $$router_name$$.
    """
    $$router_name$$ = crud.$$router_name$$.get(db=db, id=id)
    if not $$router_name$$:
        raise HTTPException(status_code=404, detail="$$class_name$$ not found")
    $$router_name$$ = crud.$$router_name$$.update(db=db, db_obj=$$router_name$$, obj_in=$$router_name$$_in)
    return $$router_name$$


@router.get("/{id}", response_model=schemas.$$class_name$$)
def read_$$router_name$$(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get $$router_name$$ by ID.
    """
    $$router_name$$ = crud.$$router_name$$.get(db=db, id=id)
    if not $$router_name$$:
        raise HTTPException(status_code=404, detail="$$class_name$$ not found")
    return $$router_name$$


@router.delete("/{id}", response_model=schemas.$$class_name$$)
def delete_$$router_name$$(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an $$router_name$$.
    """
    $$router_name$$ = crud.$$router_name$$.get(db=db, id=id)
    if not $$router_name$$:
        raise HTTPException(status_code=404, detail="$$class_name$$ not found")
    $$router_name$$ = crud.$$router_name$$.remove(db=db, id=id)
    return $$router_name$$
