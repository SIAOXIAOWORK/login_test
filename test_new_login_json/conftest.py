from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def browser_page(request):
   
    browser_name = request.param    
    with sync_playwright() as p :
        browser = getattr(p,browser_name).launch()
        context = browser.new_context()
        page = context.new_page()
        yield {"page": page, "browser_name": browser_name}
        browser.close()

