import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from test_data.users import VALID_PASSWORD, VALID_USERNAME


@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.positive
def test_logout_returns_to_login_page(page: Page) -> None:
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    secure_page.expect_opened()

    secure_page.logout()

    expect(page).to_have_url(re.compile(r".*/login$"))
    login_page.expect_logout_message("You logged out of the secure area!")
