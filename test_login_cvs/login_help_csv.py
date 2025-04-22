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
        self.page.locator("[type=submit]").click()

    def login_result(self):
        message = self.page.locator("#message").text_content().strip()

        if message == "Login successful!" :
            return Loginresult(True,"")
        else : 
            return Loginresult(False,message)
        


class Loginresult:

    def __init__(self,success:bool , message : str):
        self.success = success
        self.message = message


