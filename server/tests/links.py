from fastapi import status
from fastapi.testclient import TestClient
from src.app import get_application
from src.resources.strings import LINK_DOES_NOT_EXIST

client = TestClient(get_application())


def test_short_link_creation():
    response = client.post("/links/", json={"link": "https://github.com/"})
    assert response.status_code == 200
    assert response.json() == {
        "token": "PN24VD",
        "long_link": "https://github.com/"
    }


def test_read_long_link():
    response = client.get("/links/", headers={"token": "PN24VD"})
    assert response.status_code == 200
    assert response == "https://github.com/"


def test_read_inexistent_long_link():
    response = client.get("/links/", headers={"token": "PN24VA"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': LINK_DOES_NOT_EXIST}
