
from handle.login_handle import LoginHandle
import time
# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()
        
    # 实现登录功能
    def login(self, username, password,code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_code(code)
        
        # 点击登录按钮
        self.login_handle.click_login()