import time
from playwright.sync_api import Page, expect


def test_register_empty_form_shows_errors(page: Page):
    page.goto("/auth/register")
    page.locator("[data-test=register-submit]").click()
    expect(page.locator("[data-test=first-name-error]")).to_be_visible()
    expect(page.locator("[data-test=email-error]")).to_be_visible()
    expect(page.locator("[data-test=password-error]")).to_be_visible()


def test_register_weak_password_rejected(page: Page):
    page.goto("/auth/register")
    page.locator("[data-test=password]").fill("123")
    page.locator("[data-test=register-submit]").click()
    expect(page.locator("[data-test=password-error]")).to_be_visible()


def test_register_new_user_success(page: Page):
    email = f"sis2.{int(time.time())}@example.com"
    page.goto("/auth/register")
    page.locator("[data-test=first-name]").fill("Test")
    page.locator("[data-test=last-name]").fill("User")
    page.locator("[data-test=dob]").fill("1995-05-20")
    page.locator("[data-test=street]").fill("1 Main St")
    page.locator("[data-test=postal_code]").fill("12345")
    page.locator("[data-test=city]").fill("Almaty")
    page.locator("[data-test=state]").fill("Almaty")
    page.locator("[data-test=country]").select_option("KZ")
    page.locator("[data-test=phone]").fill("0123456789")
    page.locator("[data-test=email]").fill(email)
    page.locator("[data-test=password]").fill("Str0ng!Passw0rd#2026")
    page.locator("[data-test=register-submit]").click()
    expect(page).to_have_url(lambda u: "/auth/login" in u)
