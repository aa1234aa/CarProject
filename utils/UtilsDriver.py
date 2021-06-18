# 定义一个工具类
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class UtilsDriver:
    _driver = None
    _quit_driver = True
    
    # 定义一个获取浏览器驱动对象的方法
    @classmethod   # 表示这个方法是一个类级别的方法
    def get_driver(cls):
        if cls._driver is None:  # 判断driver是否已创建，如果为None就需要去创建浏览器驱动对象，如果不为None，则直接返回driver
            option = webdriver.ChromeOptions()
            # 防止打印一些无用的日志
            option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            cls._driver = webdriver.Chrome(chrome_options=option)
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("https://cn6platformpreprod.vocscn.com:6060/login")
        return cls._driver

    # 定义一个退出浏览器驱动对象的方法  浏览器驱动对象退出之后，还有一串效的字符串存在
    @classmethod
    def quit_driver(cls):
        if cls._driver and cls._quit_driver:
            cls.get_driver().quit()
            cls._driver = None


# 定义一个获取弹出框消息的方法
def get_msg():
    time.sleep(1)
    # driver = UtilsDriver()
    return UtilsDriver.get_driver().find_element(By.XPATH, "//span[@class='el-breadcrumb__inner']").text


def get_case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case_data = json.load(f)
    list_case_data = []
    for case in case_data:
        for x in case.values():  # values() 用来获取字典对象里面的键值
            case_tuple = x.values()
            list_case_data.append(tuple(case_tuple))
    return list_case_data


def case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case_data = json.load(f)
    list_case_data = []
    for case in case_data.values():
        list_case_data.append(tuple(case.values()))
    return list_case_data

# print(case_data("../data/login.json"))


# 鼠标移到底端
def action_down():
    try:
        target = UtilsDriver.get_driver().find_element_by_xpath("//body/div[@id='app']/div[@class='main']/div[@class='submain']/div[@class='xy-main el-scrollbar']/div[@class='scroll-y el-scrollbar__wrap']/div[@class='el-scrollbar__view']/div[@class='monitor-center']/div[@class='xy-container']/div[@class='xy-grid-container']/div/div[@class='xy-table']/div[@class='margin-bottom20 text-align-right']/div[1]")
        actions = ActionChains(UtilsDriver.get_driver())
        actions.move_to_element(target)
        actions.perform()
    except TimeoutException:
        action_down()
    # 鼠标移到新增页面底部
def action_down():
    try:
        target = UtilsDriver.get_driver().find_element_by_xpath(
            "//div[@class='text-align-center']//button[@class='el-button el-button--primary el-button--small']")
        actions = ActionChains(UtilsDriver.get_driver())
        actions.move_to_element(target)
        actions.perform()
    except TimeoutException:
        action_down()
        
# 封装一个选择运营商的方法
def choice_operator(driver, element, channel):
    """
    :param driver:  浏览器驱动对象
    :param element:  元素对象
    :param channel:  要选择的文本内容
    :return:
    """
    element.click()
    time.sleep(1)
    xpath = "//div[@class='el-scrollbar']//div//ul/li//span[text()='{}']".format(channel)
    driver.find_element(By.XPATH, xpath).click()


# 封装一个方法判断元素是否存在
def is_exist(driver, text):
    """
    :param driver:  浏览器驱动对象
    :param text:   定位元素的文本内容
    :return:
    """
    xpath = "//*[contains(text(), '{}')]".format(text)
         #   //*[contains(text(), '新增文章成功']
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False