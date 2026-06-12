from playwright.sync_api import Page


class InputsPageLocators:
    @staticmethod
    def number_input(page: Page):
        return page.locator("#input-number")

    @staticmethod
    def text_input(page: Page):
        return page.locator("#input-text")

    @staticmethod
    def password_input(page: Page):
        return page.locator("#input-password")

    @staticmethod
    def date_input(page: Page):
        return page.locator("#input-date")

    @staticmethod
    def display_inputs_button(page: Page):
        return page.locator("#btn-display-inputs")

    @staticmethod
    def clear_inputs_button(page: Page):
        return page.locator("#btn-clear-inputs")

    @staticmethod
    def output_number(page: Page):
        return page.locator("#output-number")

    @staticmethod
    def output_text(page: Page):
        return page.locator("#output-text")

    @staticmethod
    def output_password(page: Page):
        return page.locator("#output-password")

    @staticmethod
    def output_date(page: Page):
        return page.locator("#output-date")
