# Task 5: UI automation (Playwright + Python + pytest) on Sauce Demo

Run (one command after setup):
```
cd 05-automation
pip install -r requirements.txt && playwright install chromium
pytest
```
Add `--headed` to watch it run.

- **Structure:** page objects in `pages/`, tests in `tests/`, shared fixtures in `tests/conftest.py`.
- **Locators:** `data-test` attributes only. **Waits:** Playwright auto-waiting and `expect(...)`, no sleeps.
- **Independence:** every test gets a new browser context and logs in itself.
- **Assertions** check what the user sees (title, error text, badge count, confirmation text).
- **CI:** `.github/workflows/tests.yml` at the repo root runs this on every push. Passing run: <link after first run>
