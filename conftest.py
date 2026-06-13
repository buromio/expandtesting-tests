import pytest
from playwright.sync_api import Page

MOBILE_VIEWPORT = {"width": 390, "height": 844}
DESKTOP_VIEWPORT = {"width": 1400, "height": 900}


def pytest_collection_modifyitems(config, items):
    selected_browsers = config.getoption("browser") or []
    primary_browser = selected_browsers[0] if selected_browsers else None

    if not primary_browser:
        return

    for item in items:
        if item.get_closest_marker("ui"):
            continue

        callspec = getattr(item, "callspec", None)
        if not callspec:
            continue

        browser_name = callspec.params.get("browser_name")
        if browser_name and browser_name != primary_browser:
            item.add_marker(
                pytest.mark.skip(
                    reason="Non-UI tests run only once on the primary browser to avoid duplicated API checks."
                )
            )


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": DESKTOP_VIEWPORT,
        "locale": "en-US",
    }


@pytest.fixture
def mobile_page(page: Page, request):
    if request.node.get_closest_marker("mobile"):
        page.set_viewport_size(MOBILE_VIEWPORT)
    return page


@pytest.fixture(autouse=True)
def configure_page(page: Page) -> None:
    page.set_default_timeout(10_000)
    page.set_default_navigation_timeout(60_000)
