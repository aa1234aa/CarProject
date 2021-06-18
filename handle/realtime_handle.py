# 车辆实时的操作层
from base.base_handle import BaseHandle
from page.realtime_page import RealTimePage

import time


class RealTimeHandle(BaseHandle):
	def __init__(self):
		self.real_time_page = RealTimePage()
		
		# 点击车辆在线状态
	def click_online_status(self):
		self.real_time_page.find_online_status().click()
		
		# 查看上过线的状态
	def is_over_the_line(self):
		
		return self.real_time_page.find_over_the_line().text
	
		#  查看车辆总数
	def get_car_num(self):
		int(self.real_time_page.find_car_num().text)
	
	# 点击首页
	def click_find_home_page(self):
		self.real_time_page.find_home_page().click()
	
	# 点击展开
	def click_find_open_select(self):
		self.real_time_page.find_open_select().click()
	
	# 获取gps定位里面的值
	def get_gps_no_position(self):
		return self.real_time_page.find_gps_no_position().text
	
	# 获取gps是否定位的展开框
	def get_gps_status(self):
		return self.real_time_page.find_gps_status().click()
