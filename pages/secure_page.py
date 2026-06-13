import re

from locators.secure_page_locators import SecurePageLocators
from playwright.sync_api import Page, expect


class SecurePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = SecurePageLocators

    def expect_opened(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/secure$"))
        expect(self.locators.success_alert(self.page)).to_contain_text("You logged into a secure area!")
        expect(self.locators.logout_link(self.page)).to_be_visible()

    def logout(self) -> None:
        self.locators.logout_link(self.page).click()
