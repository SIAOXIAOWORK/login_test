from playwright.sync_api import sync_playwright
import pytest
from utils import load_json_data
from login_help_new_json import Login
from login_help_new_json import Loginresult
import os
import test_new_login_json.login_help_new_json as login_help_new_json
print("Login from:", login_help_new_json.__file__)


@pytest.mark.parametrize("browser_page",["chromium","firefox"],indirect = True)
@pytest.mark.parametrize("username,password,expected",load_json_data())
def test_login_json(browser_page,username,password,expected,request):
        print("Login from:", login_help_new_json.__file__)
        browser_name = browser_page["browser_name"]
        page = Login(browser_page["page"])
        page.goto("https://siaoxiaowork.github.io/login_test/")
        page.input_username(username)
        page.input_password(password)
        page.click_login()
        login_result,login_message = page.is_login_successful()
        result = Loginresult(login_result,login_message)
        
        if result.success :
                print(expected)
                print(result.message)
                assert expected == result.message

        else :

                os.makedirs("screenshots", exist_ok=True)
                safe_username = username if username else "empty"
                screenshot_path = f"screenshots/xfail_{browser_name}_{safe_username}.png"
                browser_page["page"].screenshot(path=screenshot_path)
                assert expected == result.message
        




        








