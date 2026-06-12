from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from playwright.sync_api import Page

from pages.inputs_page import InputsPage
from test_data.web_inputs import INPUT_DATE, INPUT_NUMBER, INPUT_PASSWORD, INPUT_TEXT


@pytest.mark.ui
@pytest.mark.form
@pytest.mark.positive
@pytest.mark.smoke
def test_web_inputs_display_entered_values(page: Page) -> None:
    inputs_page = InputsPage(page)

    inputs_page.open()
    inputs_page.fill_inputs(INPUT_NUMBER, INPUT_TEXT, INPUT_PASSWORD, INPUT_DATE)
    inputs_page.display_inputs()

    inputs_page.expect_outputs(INPUT_NUMBER, INPUT_TEXT, INPUT_PASSWORD, INPUT_DATE)
