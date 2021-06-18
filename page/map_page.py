from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time

# 地图对象库层
class MapPage(BasePage):
	def __init__(self):
		super().__init__()
		# 接入车辆总数
		self.total_line = By.XPATH,"//div[@class='el-card__body']//span[1]"
		# 从未上线
		self.not_line = By.XPATH,"//div[@class='el-card__body']//span[2]"
		# 无定位上线
		self.not_online = By.XPATH,"//div[@class='el-card__body']//span[3]"

	# 查找接入车辆总数
	def find_total_line(self):
		return self.get_element(self.total_line)
	
	# 查找从未上线
	def find_not_line(self):
		return self.get_element(self.not_line)
	
	# 查找无定位上线
	def find_not_online(self):
		return self.get_element(self.not_online)
