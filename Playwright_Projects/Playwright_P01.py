import unittest
from playwright.sync_api import sync_playwright

class TestGoogle(unittest.TestCase):

    def test_google(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://google.com")

            title = page.title()
            print(title)

            self.assertIn("Google", title)

            browser.close()


if __name__ == "__main__":
    unittest.main()