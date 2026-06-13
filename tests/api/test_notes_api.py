import allure
import pytest

from api.clients.notes_api_client import NotesApiClient
from schemas.assertions import assert_matches_schema
from schemas.notes_api_schemas import BASE_RESPONSE_SCHEMA, NOTE_RESPONSE_SCHEMA, NOTES_LIST_RESPONSE_SCHEMA
from test_data.api_notes import CREATED_NOTE, UPDATED_NOTE


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Health check")
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.schema
def test_notes_api_health_check() -> None:
    client = NotesApiClient()

    with allure.step("Request Notes API health-check"):
        response = client.health_check()
        body = response.json()

    with allure.step("Validate health-check response"):
        assert response.status_code == 200
        assert_matches_schema(body, BASE_RESPONSE_SCHEMA)
        assert body["success"] is True
        assert body["message"] == "Notes API is Running"


@allure.epic("Expand Testing Practice")
@allure.feature("Notes API")
@allure.story("Notes CRUD")
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.crud
@pytest.mark.schema
@pytest.mark.smoke
def test_registered_user_can_manage_note(registered_api_client: NotesApiClient) -> None:
    with allure.step("Create note"):
        create_response = registered_api_client.create_note(CREATED_NOTE)
        create_body = create_response.json()
        note_id = create_body["data"]["id"]

        assert create_response.status_code == 200
        assert_matches_schema(create_body, NOTE_RESPONSE_SCHEMA)
        assert create_body["success"] is True
        assert create_body["data"]["title"] == CREATED_NOTE.title
        assert create_body["data"]["completed"] is False

    with allure.step("Get created note by id"):
        get_response = registered_api_client.get_note(note_id)
        get_body = get_response.json()

        assert get_response.status_code == 200
        assert_matches_schema(get_body, NOTE_RESPONSE_SCHEMA)
        assert get_body["data"]["id"] == note_id
        assert get_body["data"]["description"] == CREATED_NOTE.description

    with allure.step("Update note fields"):
        update_response = registered_api_client.update_note(note_id, UPDATED_NOTE)
        update_body = update_response.json()

        assert update_response.status_code == 200
        assert_matches_schema(update_body, NOTE_RESPONSE_SCHEMA)
        assert update_body["data"]["title"] == UPDATED_NOTE.title
        assert update_body["data"]["category"] == UPDATED_NOTE.category

    with allure.step("Mark note as completed"):
        complete_response = registered_api_client.update_note_completed(note_id, completed=True)
        complete_body = complete_response.json()

        assert complete_response.status_code == 200
        assert_matches_schema(complete_body, NOTE_RESPONSE_SCHEMA)
        assert complete_body["data"]["completed"] is True

    with allure.step("Check note appears in notes list"):
        list_response = registered_api_client.get_notes()
        list_body = list_response.json()

        assert list_response.status_code == 200
        assert_matches_schema(list_body, NOTES_LIST_RESPONSE_SCHEMA)
        assert any(note["id"] == note_id for note in list_body["data"])

    with allure.step("Delete note"):
        delete_response = registered_api_client.delete_note(note_id)
        delete_body = delete_response.json()

        assert delete_response.status_code == 200
        assert_matches_schema(delete_body, BASE_RESPONSE_SCHEMA)
        assert delete_body["success"] is True
