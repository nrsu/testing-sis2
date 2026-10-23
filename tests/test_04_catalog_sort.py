from playwright.sync_api import Page, expect


def test_catalog_shows_products(page: Page):
    page.goto("/")
    expect(page.locator(".card").first).to_be_visible()
    assert page.locator(".card").count() > 0


def test_sort_by_price_low_to_high(page: Page):
    page.goto("/")
    with page.expect_response(lambda r: "sort=price" in r.url):
        page.locator("[data-test=sort]").select_option("price,asc")
    expect(page.locator("[data-test=product-price]").first).to_be_visible()
    prices = [
        float(t.replace("$", "").strip())
        for t in page.locator("[data-test=product-price]").all_inner_texts()
    ]
    assert len(prices) > 1
    assert prices == sorted(prices)


def test_sort_by_name_a_z(page: Page):
    page.goto("/")
    with page.expect_response(lambda r: "sort=name" in r.url):
        page.locator("[data-test=sort]").select_option("name,asc")
    expect(page.locator("[data-test=product-name]").first).to_be_visible()
    names = [n.strip() for n in page.locator("[data-test=product-name]").all_inner_texts()]
    assert names == sorted(names, key=str.lower)


def test_pagination_next_page(page: Page):
    page.goto("/")
    page.locator("a[aria-label*=Next]").first.click()
    expect(page.locator(".card").first).to_be_visible()
