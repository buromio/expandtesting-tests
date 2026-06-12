# Expand Testing Practice Tests

Autotests for https://practice.expandtesting.com/ using Python, pytest, Playwright, requests, JSON Schema, and Allure.

## Project structure

- `tests/ui/` - UI test scenarios.
- `tests/api/` - API test scenarios.
- `pages/` - page objects with user actions and assertions.
- `locators/` - stable UI locators.
- `test_data/` - users, form data, and API payloads.
- `api/` - API clients for service-level tests.
- `schemas/` - JSON Schema contracts and schema assertion helpers.

## Covered scenarios

- Valid login with `practice / SuperSecretPassword!`.
- Invalid username login error.
- Invalid password login error.
- Web inputs form displays entered values.
- Notes API health-check.
- Notes API user registration/login and note CRUD flow.
- Negative Notes API checks: invalid login, missing token, invalid note payloads, missing note.
- JSON Schema validation for API success, error, note, and notes-list responses.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Install all browsers for cross-browser UI runs:

```powershell
python -m playwright install chromium firefox webkit
```

## Run all tests

```powershell
pytest
```

Run only API tests:

```powershell
pytest -m api
```

Run only UI tests:

```powershell
pytest -m ui
```

Run smoke tests:

```powershell
pytest -m smoke
```

Run negative API tests:

```powershell
pytest -m "api and negative"
```

Run positive API CRUD tests:

```powershell
pytest -m "api and crud"
```

Run schema-validation tests:

```powershell
pytest -m schema
```

## Browser parameterization

By default, tests run in Chromium. Browser selection is configured in `pytest.ini`:

```ini
addopts =
    --browser chromium
    # --browser firefox
    # --browser webkit
```

To run UI tests in multiple browsers, uncomment the browser lines you need:

```ini
addopts =
    --browser chromium
    --browser firefox
    --browser webkit
```

Then run:

```powershell
pytest -m ui
```

API tests do not need a browser. When several browsers are selected, non-UI tests are kept on the primary browser only, so API checks are not duplicated for Firefox/WebKit.

You can also override browsers from CLI:

```powershell
pytest -m ui --browser chromium --browser firefox
```


## GitHub Actions

The CI workflow lives in `.github/workflows/tests.yml`.

It runs on pushes and pull requests to `main`/`master`, and can also be started manually with `workflow_dispatch`.

Default browser: `chromium`.

Manual runs allow choosing one browser:

- `chromium`
- `firefox`
- `webkit`

The workflow runs API tests first, then UI tests, and uploads Playwright and Allure artifacts.

## Allure report

Generate Allure result files:

```powershell
pytest --alluredir=allure-results
```

Open the report if Allure CLI is installed:

```powershell
allure serve allure-results
```

## Browser window mode

In `pytest.ini`, uncomment this line to run UI tests with a visible browser window:

```ini
    --headed
```

Comment it back to run headless:

```ini
    # --headed
```
