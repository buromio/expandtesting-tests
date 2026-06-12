from locators.inputs_page_locators import InputsPageLocators
from playwright.sync_api import Page, expect


class InputsPage:
    path = "/inputs"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = InputsPageLocators

    def open(self) -> None:
        self.page.goto(self.path, wait_until="domcontentloaded")
        expect(self.locators.display_inputs_button(self.page)).to_be_visible()

    def fill_inputs(self, number: str, text: str, password: str, date: str) -> None:
        self.locators.number_input(self.page).fill(number)
        self.locators.text_input(self.page).fill(text)
        self.locators.password_input(self.page).fill(password)
        self.locators.date_input(self.page).fill(date)

    def display_inputs(self) -> None:
        self.locators.display_inputs_button(self.page).click()

    def expect_outputs(self, number: str, text: str, password: str, date: str) -> None:
        expect(self.locators.output_number(self.page)).to_have_text(number)
        expect(self.locators.output_text(self.page)).to_have_text(text)
        expect(self.locators.output_password(self.page)).to_have_text(password)
        expect(self.locators.output_date(self.page)).to_have_text(date)
