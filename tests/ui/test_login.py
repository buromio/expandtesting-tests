from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from test_data.users import INVALID_PASSWORD, INVALID_USERNAME, VALID_PASSWORD, VALID_USERNAME


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
def test_invalid_username_shows_error(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)

    login_page.expect_error("Your username is invalid!")


@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.negative
def test_invalid_password_shows_error(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)

    login_page.expect_error("Your password is invalid!")
