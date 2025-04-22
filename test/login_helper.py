from playwright.sync_api import sync_playwright

class Login():
    
    def __init__(self,page):
        self.page = page

    def goto(self, URL : str):
        self.page.goto(URL)


    def input_username(self,username):
        self.page.locator("#username").fill(username)
        
    def input_password(self,password):
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator(".radius").click()
    

    def is_login_successful(self) -> bool:
        self.page.wait_for_selector(".subheader", timeout=3000)
        return self.page.locator(".subheader", has_text = "Welcome to the Secure Area. When you are done click logout below.").is_visible()
    
    def username_input_value(self) -> str:
        return self.page.locator("#username").input_value()
    
    def password_input_value(self) -> str:
        return self.page.locator("#password").input_value()
    
    def is_login_result_successful(self):
        try:
            self.page.wait_for_selector("#flash", timeout=3000)
            return self.page.locator("#flash", has_text="You logged into a secure area!").is_visible()
        except:
            return False
        
    def login_false_reason(self):
        if self.page.locator('#flash', has_text = "Your username is invalid!").is_visible() is True :
            return "Please Enter Valid Username"
        else :
            return "Please Enter Valid Password"  
        