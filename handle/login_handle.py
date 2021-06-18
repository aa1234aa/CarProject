from base.base_handle import BaseHandle
from page.login_page import LoginPage


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)
        # self.login_page.find_username().clear()
        # self.login_page.find_username().send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)
        # self.login_page.find_password().clear()
        # self.login_page.find_password().send_keys(password)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)
        # self.login_page.find_code().clear()
        # self.login_page.find_code().send_keys(code)

    # 点击登录按钮
    def click_login(self):
        self.login_page.find_login().click()