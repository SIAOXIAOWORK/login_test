class Login():
    def __init__(self,page) :
        self.page = page

    def goto(self,URL):
        self.page.goto(URL)

    def input_username(self,username:str):
        self.page.locator("#username").fill(username)    

    def input_password(self,password:str):
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator("[type=submit]").click()

    def is_login_successful(self):
        locator = self.page.locator("#message")
        message = locator.text_content(timeout=3000).strip()
        if message ==  "Login successful!":
            return True,message
        else :
            return False,message
        



class Loginresult:

    def __init__(self,success:bool , message : str):
        self.success = success
        self.message = message


        

    
    
