from uuid import uuid4

from api.clients.notes_api_client import ApiUser, NotePayload


API_USER_PASSWORD = "Password123!"


def unique_api_user() -> ApiUser:
    unique_id = uuid4().hex
    return ApiUser(
        name="Automation API User",
        email=f"autotest_api_{unique_id}@example.com",
        password=API_USER_PASSWORD,
    )


CREATED_NOTE = NotePayload(
    title="Automation API note",
    description="Created by automated API test",
    category="Work",
)

UPDATED_NOTE = NotePayload(
    title="Automation API note updated",
    description="Updated by automated API test",
    category="Personal",
    completed=False,
)
