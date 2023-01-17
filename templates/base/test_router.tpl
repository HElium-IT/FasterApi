from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.$$router_name$$ import create_random_$$router_name$$

def test_create_$$router_name$$(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"/api/$$api_version$$/$$router_name$$/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()

    assert "id" in content
    for key, value in data.items():
        assert content[key] == value
    

def test_read_$$router_name$$(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    $$router_name$$ = create_random_$$router_name$$(db)
    response = client.get(
        f"/api/$$api_version$$/$$router_name$$/{$$router_name$$.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()

    for key, value in $$router_name$$.items():
        assert content[key] == value


def test_update_$$router_name$$(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    $$router_name$$ = create_random_$$router_name$$(db)
    new_description = random_lower_string()
    data = {"description": new_description}
    response = client.put(
        f"/api/$$api_version$$/$$router_name$$/{$$router_name$$.id}",
        headers=superuser_token_headers,
        json=data
    )
    assert response.status_code == 200
    content = response.json()

    assert content["id"] == $$router_name$$.id
    for key, value in data.items():
        assert content[key] == value


def test_delete_$$router_name$$(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    $$router_name$$ = create_random_$$router_name$$(db)
    response = client.delete(
    f"/api/$$api_version$$/$$router_name$$/{$$router_name$$.id}",
    headers=superuser_token_headers
    )
    assert response.status_code == 200
    $$router_name$$_db = crud.$$router_name$$.get(db, id=$$router_name$$.id)
    assert $$router_name$$_db is None