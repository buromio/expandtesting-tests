"""HTTP client for Expand Testing Notes API."""

from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class ApiUser:
    name: str
    email: str
    password: str


@dataclass(frozen=True)
class NotePayload:
    title: str
    description: str
    category: str
    completed: bool | None = None


class NotesApiClient:
    def __init__(self, base_url: str = "https://practice.expandtesting.com/notes/api") -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.token: str | None = None

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _auth_headers(self) -> dict[str, str]:
        if not self.token:
            raise RuntimeError("API token is not set. Call login() first.")
        return {"x-auth-token": self.token}

    def health_check(self) -> requests.Response:
        return self.session.get(self._url("/health-check"), timeout=30)

    def register_user(self, user: ApiUser) -> requests.Response:
        return self.session.post(
            self._url("/users/register"),
            data={"name": user.name, "email": user.email, "password": user.password},
            timeout=30,
        )

    def login(self, email: str, password: str) -> requests.Response:
        response = self.session.post(
            self._url("/users/login"),
            data={"email": email, "password": password},
            timeout=30,
        )
        if response.ok:
            self.token = response.json()["data"]["token"]
        return response

    def delete_account(self) -> requests.Response:
        return self.session.delete(self._url("/users/delete-account"), headers=self._auth_headers(), timeout=30)

    def create_note(self, note: NotePayload) -> requests.Response:
        return self.session.post(
            self._url("/notes"),
            data={"title": note.title, "description": note.description, "category": note.category},
            headers=self._auth_headers(),
            timeout=30,
        )

    def create_note_raw(self, data: dict[str, str]) -> requests.Response:
        return self.session.post(self._url("/notes"), data=data, headers=self._auth_headers(), timeout=30)

    def create_note_without_token(self, note: NotePayload) -> requests.Response:
        return self.session.post(
            self._url("/notes"),
            data={"title": note.title, "description": note.description, "category": note.category},
            timeout=30,
        )

    def get_note(self, note_id: str) -> requests.Response:
        return self.session.get(self._url(f"/notes/{note_id}"), headers=self._auth_headers(), timeout=30)

    def get_notes(self) -> requests.Response:
        return self.session.get(self._url("/notes"), headers=self._auth_headers(), timeout=30)

    def get_notes_without_token(self) -> requests.Response:
        return self.session.get(self._url("/notes"), timeout=30)

    def update_note(self, note_id: str, note: NotePayload) -> requests.Response:
        if note.completed is None:
            raise ValueError("completed is required for full note update")
        return self.session.put(
            self._url(f"/notes/{note_id}"),
            data={
                "title": note.title,
                "description": note.description,
                "category": note.category,
                "completed": str(note.completed).lower(),
            },
            headers=self._auth_headers(),
            timeout=30,
        )

    def update_note_completed(self, note_id: str, completed: bool) -> requests.Response:
        return self.session.patch(
            self._url(f"/notes/{note_id}"),
            data={"completed": str(completed).lower()},
            headers=self._auth_headers(),
            timeout=30,
        )

    def delete_note(self, note_id: str) -> requests.Response:
        return self.session.delete(self._url(f"/notes/{note_id}"), headers=self._auth_headers(), timeout=30)
