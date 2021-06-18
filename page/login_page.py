# 表示的登录页面对象
from selenium.webdriver.common.by import By
from base.base_page import BasePage


# 对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = By.XPATH, "//input[@placeholder='请输入用户名']"  # 用户名输入框
        self.password = By.XPATH, "//input[@placeholder='请输入密码']"  # 密码输入框
        self.code = By.XPATH, "//input[@placeholder='请输入验证码']"   # 验证码输入框
        self.login_btn = By.ID, "submit"  # 表示的是登录按钮

    # 用户名输入框
    def find_username(self):
        return self.get_element(self.username)
        # return self.driver.find_element(*self.username)

    # 密码输入框
    def find_password(self):
        return self.get_element(self.password)
        # return self.driver.find_element(*self.password)

    # 验证码输入框
    def find_code(self):
        return self.get_element(self.code)
        # return self.driver.find_element(*self.code)

    # 登陆按钮
    def find_login(self):
        return self.get_element(self.login_btn)
