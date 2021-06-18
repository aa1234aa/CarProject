from base.base_handle import BaseHandle
from page.basic_data_page import BasicDataPage

from time import sleep
# 基础数据业务层
class BasicDataHandle(BaseHandle):
	
	def __init__(self):
		self.basic_data_page = BasicDataPage()
	
	# 点击基础数据
	def click_basic_logo(self):
		self.basic_data_page.find_basic_logo().click()
	
	# 点击零配件信息
	def click_spare_parts(self):
		self.basic_data_page.find_spare_parts().click()
	
	# 点击sim卡管理
	def click_sim_card_mange(self):
		self.basic_data_page.find_sim_card_mange().click()
	
	# 点击新增按钮
	def click_add_sim_card(self):
		self.basic_data_page.find_add_sim_card().click()
		
	# 点击车辆终端信息
	def click_car_terminal_info(self):
		self.basic_data_page.find_car_terminal_info().click()
		
	# 点击车辆终端型号
	def click_car_terminal_model(self):
		self.basic_data_page.find_car_terminal_model().click()
	
