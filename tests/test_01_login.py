from playwright.sync_api import Page, expect
from conftest import USER, PASSWORD


def login(page: Page, email: str, password: str):
    page.goto("/auth/login")
    page.locator("[data-test=email]").fill(email)
    page.locator("[data-test=password]").fill(password)
    page.locator("[data-test=login-submit]").click()


def test_login_valid_credentials(page: Page):
    login(page, USER, PASSWORD)
    expect(page).to_have_url(lambda u: u.endswith("/account"))
    expect(page.locator("[data-test=page-title]")).to_have_text("My account")


def test_login_wrong_password(page: Page):
    login(page, USER, "wrong-password")
    expect(page.locator("[data-test=login-error]")).to_be_visible()
    expect(page).to_have_url(lambda u: "/auth/login" in u)


def test_login_empty_fields_show_validation(page: Page):
    page.goto("/auth/login")
    page.locator("[data-test=login-submit]").click()
    expect(page.locator("[data-test=email-error]")).to_be_visible()
    expect(page.locator("[data-test=password-error]")).to_be_visible()


def test_logout(logged_in: Page):
    logged_in.locator("[data-test=nav-menu]").click()
    logged_in.locator("[data-test=nav-sign-out]").click()
    expect(logged_in).to_have_url(lambda u: "/auth/login" in u)
