from app.tests.utils.utils import random_lower_string

def test_create_$$router_name$$(db: Session) -> None:
    name = random_lower_string()
    payload = { "name": name }
    $$router_name$$ = crud.$$router_name$$.create(db=db, obj_in=payload)
    assert $$router_name$$.id is not None
    for key, value in payload.items():
        assert value == $$router_name$$[key]

def test_get_$$router_name$$(db: Session) -> None:
    name = random_lower_string()
    payload = { "name": name }
    $$router_name$$ = crud.$$router_name$$.create(db=db, obj_in=payload)
    stored_$$router_name$$ = crud.$$router_name$$.get(db=db, id=$$router_name$$.id)
    assert stored_$$router_name$$
    assert $$router_name$$.id == stored_$$router_name$$.id
    for key, value in payload.items():
        assert value == stored_$$router_name$$[key]

def test_update_$$router_name$$(db: Session) -> None:
    payload = { }
    $$router_name$$ = crud.$$router_name$$.create_with_owner(db=db, obj_in=payload)
    new_name = random_lower_string()
    update_payload = { "name": new_name }
    updated_$$router_name$$ = crud.$$router_name$$.update(db=db, db_obj=$$router_name$$, obj_in=update_payload)
    assert $$router_name$$.id == updated_$$router_name$$.id
    for key, value in update_payload.items():
        asser value == updated_$$router_name$$[key]