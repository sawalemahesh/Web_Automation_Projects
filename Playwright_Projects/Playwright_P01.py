from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://app.vwo.com/#/login")
    page.get_by_role("textbox", name="Email address").click()
    page.get_by_role("textbox", name="Email address").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Sign in", exact=True).click()
