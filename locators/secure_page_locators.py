from playwright.sync_api import Page


class SecurePageLocators:
    @staticmethod
    def logout_link(page: Page):
        return page.get_by_role("link", name="Logout")

    @staticmethod
    def success_alert(page: Page):
        return page.locator(".alert")
