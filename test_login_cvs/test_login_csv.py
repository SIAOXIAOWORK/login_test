import pytest
from playwright.sync_api import sync_playwright
from login_help import Login
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import load_csv_data


@pytest.mark.parametrize("browser_page",["chromium","firefox"],indirect = True)
@pytest.mark.parametrize("username, password, expected",load_csv_data())
def test_login_save_storage(browser_page,username,password,expected):
    
        page = Login(browser_page)
        page.goto("http://localhost:8000/")
        page.input_username(username)
        page.input_password(password)
        page.click_login()
        print(expected)
        result = page.login_result()
        if result.success:
            assert expected == ""  # 預期成功時 expected 是空的
        else:
              print("錯誤訊息",result.message)
              assert result.message == expected
