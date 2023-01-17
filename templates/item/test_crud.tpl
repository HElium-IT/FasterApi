from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string

def test_create_$$router_name$$(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    payload = { "title": title, "description": description }
    user = create_random_user(db)
    $$router_name$$ = crud.$$router_name$$.create_with_owner(db=db, obj_in=payload, owner_id=user.id)
    assert $$router_name$$.id is not None
    for key, value in payload.items():
        assert value == $$router_name$$[key]
    assert $$router_name$$.owner_id == user.id

def test_get_$$router_name$$(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    payload = { "title": title, "description": description }
    user = create_random_user(db)
    $$router_name$$ = crud.$$router_name$$.create_with_owner(db=db, obj_in=payload, owner_id=user.id)
    stored_$$router_name$$ = crud.$$router_name$$.get(db=db, id=$$router_name$$.id)
    assert stored_$$router_name$$
    assert $$router_name$$.id == stored_$$router_name$$.id
    for key, value in payload.items():
        assert value == stored_$$router_name$$[key]
    assert $$router_name$$.owner_id == stored_$$router_name$$.owner_id

def test_update_$$router_name$$(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    payload = { "title": title, "description": description }
    user = create_random_user(db)
    $$router_name$$ = crud.$$router_name$$.create_with_owner(db=db, obj_in=payload, owner_id=user.id)
    new_description = random_lower_string()
    update_payload = {"description": new_description}
    updated_$$router_name$$ = crud.$$router_name$$.update(db=db, db_obj=$$router_name$$, obj_in=update_payload)
    assert $$router_name$$.id == updated_$$router_name$$.id
    for key, value in update_payload.items():
        asser value == updated_$$router_name$$[key]