import re

import pytest
from playwright.sync_api import Page, expect

from pages.inputs_page import InputsPage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from test_data.users import VALID_PASSWORD, VALID_USERNAME
from test_data.web_inputs import INPUT_DATE, INPUT_NUMBER, INPUT_PASSWORD, INPUT_TEXT


@pytest.mark.ui
@pytest.mark.mobile
@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.smoke
def test_mobile_valid_user_can_login(page: Page) -> None:
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    secure_page.expect_opened()


@pytest.mark.ui
@pytest.mark.mobile
@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (VALID_USERNAME, "wrong_password", "Your password is invalid!"),
    ],
    ids=["invalid-password"],
)
def test_mobile_login_with_invalid_credentials_shows_error(
    page: Page, username: str, password: str, expected_error: str
) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    login_page.expect_error(expected_error)


@pytest.mark.ui
@pytest.mark.mobile
@pytest.mark.auth
@pytest.mark.positive
def test_mobile_logout_returns_to_login_page(page: Page) -> None:
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    secure_page.expect_opened()

    secure_page.logout()

    expect(page).to_have_url(re.compile(r".*/login$"))
    login_page.expect_logout_message("You logged out of the secure area!")


@pytest.mark.ui
@pytest.mark.mobile
@pytest.mark.form
@pytest.mark.positive
@pytest.mark.smoke
def test_mobile_web_inputs_display_entered_values(page: Page) -> None:
    inputs_page = InputsPage(page)

    inputs_page.open()
    inputs_page.fill_inputs(INPUT_NUMBER, INPUT_TEXT, INPUT_PASSWORD, INPUT_DATE)
    inputs_page.display_inputs()

    inputs_page.expect_outputs(INPUT_NUMBER, INPUT_TEXT, INPUT_PASSWORD, INPUT_DATE)
