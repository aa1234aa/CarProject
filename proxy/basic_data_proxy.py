from handle.basic_data_handle import BasicDataHandle

from time import sleep
class BasicDataProxy:
	def __init__(self):
		self.basic_data_handle = BasicDataHandle()
	
	# 找到sim卡新增页
	def get_find_sim_card_mange(self):
		self.basic_data_handle.click_basic_logo()
		self.basic_data_handle.click_spare_parts()
		self.basic_data_handle.click_sim_card_mange()
		self.basic_data_handle.click_add_sim_card()
	
	# 找到车辆型号页面
	def get_find_car_terminal_model(self):
		self.basic_data_handle.click_basic_logo()
		self.basic_data_handle.click_spare_parts()
		self.basic_data_handle.click_car_terminal_info()
		self.basic_data_handle.click_car_terminal_model()