import pytest
from playwright.sync_api import sync_playwright
from login_help_json import Login
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
        


        if result.success:
            assert expected == "Login successful!"  # 預期成功時 expected 是空的
        else:
            assert result.message == expected

