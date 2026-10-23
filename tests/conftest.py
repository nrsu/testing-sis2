import pytest
from playwright.sync_api import Page, expect

USER = "customer@practicesoftwaretesting.com"
PASSWORD = "welcome01"


@pytest.fixture
def logged_in(page: Page) -> Page:
    page.goto("/auth/login")
    page.locator("[data-test=email]").fill(USER)
    page.locator("[data-test=password]").fill(PASSWORD)
    page.locator("[data-test=login-submit]").click()
    expect(page).to_have_url(lambda u: u.endswith("/account"))
    return page
