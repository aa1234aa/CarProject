# 定义地图业务层
from handle.map_handle import MapHandle


class MapProxy:
	def __init__(self):
		self.map_handle = MapHandle()
		
	# 接入车辆总数
	def map_span1(self):
		self.map_handle.click_total_number()
		
	# 从未上线
	def map_span2(self):
		self.map_handle.click_not_line()
	
	# 无定位车辆
	def map_span3(self):
		self.map_handle.click_not_online()
	
	# 确认车辆总数
	def span1_num(self):
		self.map_handle.cat_total_number()
		
	# 确认从未上线数
	def span2_num(self):
		self.map_handle.cat_not_line()
	
	# 确认无定位车辆
	def span3_num(self):
		self.map_handle.cat_not_online()