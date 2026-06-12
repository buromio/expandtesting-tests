from playwright.sync_api import Page


class LoginPageLocators:
    @staticmethod
    def username_input(page: Page):
        return page.locator("#username")

    @staticmethod
    def password_input(page: Page):
        return page.locator("#password")

    @staticmethod
    def login_button(page: Page):
        return page.get_by_role("button", name="Login")

    @staticmethod
    def alert_message(page: Page):
        return page.locator(".alert")
