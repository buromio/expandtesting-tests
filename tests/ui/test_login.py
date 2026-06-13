import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from test_data.users import (
    INVALID_PASSWORD,
    INVALID_USERNAME,
    VALID_PASSWORD,
    VALID_USERNAME,
)


@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.smoke
def test_valid_user_can_login(page: Page) -> None:
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    secure_page.expect_opened()


@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (INVALID_USERNAME, VALID_PASSWORD, "Your username is invalid!"),
        (VALID_USERNAME, INVALID_PASSWORD, "Your password is invalid!"),
    ],
    ids=["invalid-username", "invalid-password"],
)
def test_login_with_invalid_credentials_shows_error(
    page: Page, username: str, password: str, expected_error: str
) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    login_page.expect_error(expected_error)
