from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import allure
import pytest

from api.clients.notes_api_client import NotesApiClient
from schemas.assertions import assert_matches_schema
from schemas.notes_api_schemas import ERROR_RESPONSE_SCHEMA
from test_data.api_notes import CREATED_NOTE


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Negative authorization")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_login_with_unknown_user_returns_unauthorized() -> None:
    client = NotesApiClient()

    with allure.step("Try to login with unknown user"):
        response = client.login("unknown@example.com", "WrongPassword123!")
        body = response.json()

    with allure.step("Validate unauthorized response"):
        assert response.status_code == 401
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "Incorrect email address or password"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Missing token")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_get_notes_without_token_returns_unauthorized() -> None:
    client = NotesApiClient()

    with allure.step("Request notes list without token"):
        response = client.get_notes_without_token()
        body = response.json()

    with allure.step("Validate missing token response"):
        assert response.status_code == 401
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "No authentication token specified in x-auth-token header"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Missing token")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_create_note_without_token_returns_unauthorized() -> None:
    client = NotesApiClient()

    with allure.step("Create note without token"):
        response = client.create_note_without_token(CREATED_NOTE)
        body = response.json()

    with allure.step("Validate missing token response"):
        assert response.status_code == 401
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "No authentication token specified in x-auth-token header"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Validation errors")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_create_note_without_title_returns_validation_error(registered_api_client: NotesApiClient) -> None:
    with allure.step("Create note without title"):
        response = registered_api_client.create_note_raw({"description": "Missing title", "category": "Work"})
        body = response.json()

    with allure.step("Validate title error response"):
        assert response.status_code == 400
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "Title must be between 4 and 100 characters"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Validation errors")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_create_note_with_invalid_category_returns_validation_error(registered_api_client: NotesApiClient) -> None:
    with allure.step("Create note with invalid category"):
        response = registered_api_client.create_note_raw(
            {"title": "Invalid category note", "description": "Bad category", "category": "Bad"}
        )
        body = response.json()

    with allure.step("Validate category error response"):
        assert response.status_code == 400
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "Category must be one of the categories: Home, Work, Personal"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Missing note")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.schema
def test_get_missing_note_returns_not_found(registered_api_client: NotesApiClient) -> None:
    with allure.step("Get missing note by id"):
        response = registered_api_client.get_note("000000000000000000000000")
        body = response.json()

    with allure.step("Validate not found response"):
        assert response.status_code == 404
        assert_matches_schema(body, ERROR_RESPONSE_SCHEMA)
        assert body["success"] is False
        assert body["message"] == "No note was found with the provided ID, Maybe it was deleted"
