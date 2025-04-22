import pytest
from playwright.sync_api import sync_playwright
from login_help import Login
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import load_json_data


@pytest.mark.parametrize("browser_page",["chromium","firefox"],indirect = True)
@pytest.mark.parametrize("username, password, expected",load_json_data())
def test_login_save_storage(browser_page,username,password,expected,request):
    
        page = Login(browser_page)
        page.goto("https://siaoxiaowork.github.io/login_test/")
        page.input_username(username)
        page.input_password(password)
        page.click_login()
        print(expected)
        result = page.login_result()
        
        browser_name = page.context.browser._name
        is_xfail = request.node.get_closest_marker("xfail") is not None 

        if is_xfail:
            os.makedirs("screenshots", exist_ok=True)
            safe_username = username if username else "empty"
            screenshot_path = f"screenshots/xfail_{browser_name}_{safe_username}.png"
            browser_page.screenshot(path=screenshot_path)

        if result.success:
            assert expected == ""  # 預期成功時 expected 是空的
        else:
            assert result.message == expected

