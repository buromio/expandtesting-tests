import pytest

from api.clients.notes_api_client import NotesApiClient
from test_data.api_notes import unique_api_user


@pytest.fixture
def registered_api_client() -> NotesApiClient:
    client = NotesApiClient()
    user = unique_api_user()
    token_created = False

    register_response = client.register_user(user)
    assert register_response.status_code == 201, register_response.text

    login_response = client.login(user.email, user.password)
    assert login_response.status_code == 200, login_response.text
    token_created = True

    try:
        yield client
    finally:
        if token_created:
            delete_response = client.delete_account()
            assert delete_response.status_code == 200, delete_response.text
