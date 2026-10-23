from playwright.sync_api import Page, expect


def search(page: Page, term: str):
    page.goto("/")
    page.locator("[data-test=search-query]").fill(term)
    page.locator("[data-test=search-submit]").click()


def test_search_existing_product(page: Page):
    search(page, "Pliers")
    expect(page.locator("[data-test=search_completed]")).to_be_visible()
    expect(page.locator("[data-test=product-name]").first).to_contain_text("Pliers")


def test_search_no_results(page: Page):
    search(page, "zzzxxyyqq")
    expect(page.locator("[data-test=no-results]")).to_contain_text("There are no products found")


def test_search_reset_clears_query(page: Page):
    search(page, "Hammer")
    expect(page.locator("[data-test=search_completed]")).to_be_visible()
    page.locator("[data-test=search-reset]").click()
    expect(page.locator("[data-test=search-query]")).to_have_value("")
