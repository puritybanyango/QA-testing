from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test=username]")
        self.password = page.locator("[data-test=password]")
        self.login_button = page.locator("[data-test=login-button]")
        self.error = page.locator("[data-test=error]")

    def open(self):
        self.page.goto("/")

    def login(self, user: str, password: str = "secret_sauce"):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()
