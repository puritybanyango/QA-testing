from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test=title]")
        self.items = page.locator("[data-test=inventory-item]")
        self.cart_badge = page.locator("[data-test=shopping-cart-badge]")
        self.cart_link = page.locator("[data-test=shopping-cart-link]")

    def add_to_cart(self, slug: str):
        self.page.locator(f"[data-test=add-to-cart-{slug}]").click()

    def open_cart(self):
        self.cart_link.click()
