from locators.login_page_locators import LoginPageLocators
from playwright.sync_api import Page, expect


class LoginPage:
    path = "/login"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = LoginPageLocators

    def open(self) -> None:
        self.page.goto(self.path, wait_until="domcontentloaded")
        expect(self.locators.login_button(self.page)).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.locators.username_input(self.page).fill(username)
        self.locators.password_input(self.page).fill(password)
        self.locators.login_button(self.page).click()

    def expect_error(self, message: str) -> None:
        expect(self.locators.alert_message(self.page)).to_be_visible()
        expect(self.locators.alert_message(self.page)).to_have_text(message)

    def expect_logout_message(self, message: str) -> None:
        expect(self.locators.alert_message(self.page)).to_be_visible()
        expect(self.locators.alert_message(self.page)).to_contain_text(message)
