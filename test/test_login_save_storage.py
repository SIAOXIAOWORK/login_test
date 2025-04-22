from playwright.sync_api import sync_playwright
from login_helper import Login


def test_login_save_storage():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        new_context = browser.new_context()
        new_page = new_context.new_page()
        page = Login(new_page)
        page.goto("https://the-internet.herokuapp.com/login")
        page.input_username("tomsmith")
        page.input_password("SuperSecretPassword!")
        page.click_login()
        assert page.is_login_successful()
        
        if page.is_login_successful() == True :
            new_context.storage_state(path="storage_state.json")