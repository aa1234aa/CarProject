# 地图操作层
from base.base_handle import BaseHandle
from page.map_page import MapPage
import re


class MapHandle(BaseHandle):
	def __init__(self):
		self.map_page = MapPage()
		
	# 点击接入车辆总数
	def click_total_number(self):
		self.map_page.find_total_line().click()
		
	# 点击从未上线
	def click_not_line(self):
		self.map_page.find_not_line().click()
		
	# 查找无定位上线
	def click_not_online(self):
		self.map_page.find_not_online().click()
		
	# 查看接入车辆总数
	def cat_total_number(self):
		re.findall('\d+',self.map_page.find_total_line().text)
		
	# 查看从未上线数
	def cat_not_line(self):
		re.findall('\d+',self.map_page.find_not_line().text)
		
	# 查看无定位车辆数
	def cat_not_online(self):
		re.findall('\d+',self.map_page.find_not_online().text)