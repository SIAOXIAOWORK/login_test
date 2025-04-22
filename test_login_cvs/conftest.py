from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")

def browser_page(request):
    browser_name = request.param
    with sync_playwright() as p:
        browser = getattr(p,browser_name).launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()