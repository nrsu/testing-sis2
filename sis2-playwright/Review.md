# Review

## What the AI produced
A Python/pytest-playwright project: 5 suites, 18 tests (login, registration, search, catalog sort/pagination, product + cart), `pytest.ini`, shared `conftest.py` fixture, Description.md and Prompt.md.

## How I reviewed / modified
- Locators: `data-test` attributes (used by the Toolshop app) instead of CSS/XPath, so they are more stable. **They must be verified against the live DOM.**
- Python chosen because Node.js is not installed on this machine.
- Replaced fixed sleeps with `expect` auto-waiting and `expect_response` for sorting and cart quantity (async API re-render).
- Registration test uses a timestamp-based unique email so it is repeatable.

## Honest limitations
- **Tests have NOT been executed**: the sandbox had no access to practicesoftwaretesting.com and installing `playwright` was blocked. Selectors and texts (error messages, "The cart is empty") are unverified and may need adjusting after the first run.
- Still to do by the student: run `pytest`, fix failing selectors, add screenshots of the AI response and run results to `screenshots/`, publish to a public GitHub repo, submit the Google Form.
