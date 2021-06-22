from base.base_handle import BaseHandle
from page.car_terminal_model_page import CarTerminalModelPage
from utils.UtilsDriver import UtilsDriver,choice_operator
import allure


class CarTerminalModelHandle(BaseHandle):
	def __init__(self):
		self.car_terminal_model_page = CarTerminalModelPage()
		self.driver = UtilsDriver.get_driver()
		
	# 点击新增
	@allure.step(title="点击新增")
	def click_add_car_model(self):
		self.car_terminal_model_page.find_add_car_model().click()
		
	# 输入终端型号
	@allure.step(title="输入终端型号")
	def input_car_model(self,car_model):
		self.input_text(self.car_terminal_model_page.find_car_model(),car_model)
	
	# 选择终端种类
	@allure.step(title="选择终端种类")
	def select_terminal_category(self,category):
		choice_operator(self.driver,self.car_terminal_model_page.find_terminal_category(),category)
	
	# 查找支持加密芯片
	@allure.step(title="查找支持加密芯片")
	def click_support_encryption_chip(self):
		self.car_terminal_model_page.find_support_encryption_chip().click()
		
	# 查找终端生产企业
	@allure.step(title="查找终端生产企业")
	def click_terminal_manufacturer(self):
		self.car_terminal_model_page.find_terminal_manufacturer().click()
		
	# 查找单位名称
	@allure.step(title="查找单位名称")
	def input_unit_name(self,unit_name):
		self.input_text(self.car_terminal_model_page.find_unit_name(),unit_name)
		
	# 单位查询
	@allure.step(title="单位查询")
	def click_inquiry_unit(self):
		self.car_terminal_model_page.find_inquiry_unit().click()
		
	# 选择单位
	@allure.step(title="选择单位")
	def click_select_unit(self):
		self.car_terminal_model_page.find_select_unit().click()
		
	# 确定
	@allure.step(title="确定")
	def click_determine(self):
		self.car_terminal_model_page.find_determine().click()
		
	# 上传终端检测报告扫描件
	@allure.step(title="终端检测报告扫描件")
	def upload_scan_of_sport_file(self,image):
		self.send_image(self.car_terminal_model_page.find_scan_of_sport_file(),image)