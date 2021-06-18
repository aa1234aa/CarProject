# 车辆实时业务层
from handle.realtime_handle import RealTimeHandle
import time


class RealTimeProxy:
	def __init__(self):
		self.real_time_handle=RealTimeHandle()
		
	# 点击选择框
	def get_online_status(self):
		self.real_time_handle.click_online_status()
		
	# 获取已经勾选的值
	def get_is_over_the_line(self):
		return self.real_time_handle.is_over_the_line()
		
	# 获取车辆上过线的总数
	def get_find_car_num(self):
		self.real_time_handle.get_car_num()
	
	# 获取首页
	def get_find_home_page(self):
		self.real_time_handle.click_find_home_page()
	
	# 选择项展开
	def get_find_open_select(self):
		self.real_time_handle.click_find_open_select()
	
	# 获取gps是否定位里面的无定位
	def get_find_no_position(self):
		return self.real_time_handle.get_gps_no_position()
	
	# 获取gps下拉框
	def get_find_gps_status(self):
		return self.real_time_handle.get_gps_status()
		

