from playwright.sync_api import Page, expect


def open_first_product(page: Page) -> str:
    page.goto("/")
    first = page.locator("[data-test=product-name]").first
    name = first.inner_text().strip()
    first.click()
    expect(page.locator("[data-test=product-name]")).to_have_text(name)
    return name


def test_product_details_page(page: Page):
    open_first_product(page)
    expect(page.locator("[data-test=unit-price]")).to_be_visible()
    expect(page.locator("[data-test=add-to-cart]")).to_be_enabled()


def test_add_product_to_cart(page: Page):
    name = open_first_product(page)
    page.locator("[data-test=add-to-cart]").click()
    expect(page.locator("[data-test=cart-quantity]")).to_have_text("1")
    page.locator("[data-test=nav-cart]").click()
    expect(page.locator("[data-test=product-title]")).to_contain_text(name)


def test_change_quantity_updates_total(page: Page):
    open_first_product(page)
    page.locator("[data-test=add-to-cart]").click()
    page.locator("[data-test=nav-cart]").click()
    qty = page.locator("[data-test=product-quantity]")
    with page.expect_response(lambda r: "/carts/" in r.url and r.request.method == "PUT"):
        qty.fill("3")
        qty.press("Tab")
    unit = float(page.locator("[data-test=product-price]").first.inner_text().replace("$", ""))
    total = float(page.locator("[data-test=cart-total]").inner_text().replace("$", "").replace(",", ""))
    assert abs(total - unit * 3) < 0.01


def test_remove_product_from_cart(page: Page):
    open_first_product(page)
    page.locator("[data-test=add-to-cart]").click()
    page.locator("[data-test=nav-cart]").click()
    page.locator("[data-test=delete]").first.click()
    expect(page.get_by_text("The cart is empty")).to_be_visible()
