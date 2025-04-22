from playwright.sync_api import sync_playwright
from login_helper import Login
import pytest

xfail_data = pytest.mark.xfail(reason="invalid login expected")
@pytest.mark.parametrize("browser_page",["chromium","firefox"],indirect = True)
@pytest.mark.parametrize("username , password",[("tomsmith","SuperSecretPassword!"),
                                                pytest.param("1234567","SuperSecretPassword!",marks = pytest.mark.xfail(reason = "Invalid username")),
                                                pytest.param("tomsmith","    " , marks = pytest.mark.xfail(reason = "Invalid password")) ])
def test_login_save_storage(browser_page,username,password):
    
        page = Login(browser_page)
        page.goto("https://the-internet.herokuapp.com/login")
        page.input_username(username)
        page.input_password(password)
        page.click_login()
        assert page.is_login_result_successful()

        if page.is_login_result_successful() is True :
            browser_page.context.storage_state(path = 'storage_state.json')

        else :
            print(page.login_false_reason())