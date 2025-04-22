from playwright.sync_api import sync_playwright
from login_helper import Login

def test_login_with_storage_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        new_context = browser.new_context(storage_state="storage_state.json")
        new_page = new_context.new_page()
        page = Login(new_page)
        page.goto("https://the-internet.herokuapp.com/secure")
        assert page.is_login_successful()