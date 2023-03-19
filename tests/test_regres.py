from pytest_voluptuous import S
from schemas.schemas import *


def test_create_user(reqres):
    created_user = reqres.post("api/users", {"name": "Asel", "job": "QA"})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "Asel"
    assert created_user.json()["job"] == "QA"


def test_update_user(reqres):
    update_user = reqres.put("api/users/2", {"name": "bisengalieva", "job": "tester"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "bisengalieva"
    assert update_user.json()["job"] == "tester"


def test_delete_user(reqres):
    delete_user = reqres.delete("api/users/2")

    assert delete_user.status_code == 204


def test_login_successful(reqres):
    login_successfully = reqres.post("api/register", {"email": "eve.holt@reqres.in", "password": "pistol"})

    assert login_successfully.status_code == 200
    assert S(register_user) == login_successfully.json()
    assert login_successfully.json()['id']
    assert login_successfully.json()["token"]


def test_login_unsuccessful(reqres):
    login_unsuccessful = reqres.post("api/register", {"email": "neit.@f"})

    assert login_unsuccessful.status_code == 400
    assert S(unregister_user) == login_unsuccessful.json()
    assert len(login_unsuccessful.content) != 0