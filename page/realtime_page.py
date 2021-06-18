# 定义车辆实时状态
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class RealTimePage(BasePage):
	def __init__(self):
		super().__init__()
		# 终端在线状态选择下拉框中
		self.online_status = By.CSS_SELECTOR,"div.el-select.el-select--small div.el-input.el-input--small.el-input--suffix > input.el-input__inner"
		# 终端在线状态下拉框中的值
		self.over_the_line = By.XPATH,"//body/div[@class='el-select-dropdown el-popper']/div[@class='el-scrollbar']/div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul[@class='el-scrollbar__view el-select-dropdown__list']/li[@class='el-select-dropdown__item selected']/span"
		# 车辆总数
		self.car_num = By.CSS_SELECTOR,"div.main div.submain div.xy-main.el-scrollbar div.scroll-y.el-scrollbar__wrap:nth-child(1) div.el-scrollbar__view div.monitor-center div.xy-container:nth-child(2) div.xy-grid-container:nth-child(2) div.xy-table div.margin-bottom20.text-align-right div.rg-pagination span.base-tip-size.margin-right10:nth-child(1) > span.pagination-total"
		# 回到首页
		self.home_page = By.XPATH,"//i[@class='iconfont icon-shouye']"
		# 页面底部
		self.action_down = By.XPATH,"//div[@class='page-inner']"
		# 展开搜索选择的按钮
		self.open_select = By.XPATH,"//i[contains(@class,'fa-angle-double-down')]"
		# gps是否定位下拉框
		self.gps_status = By.XPATH,"//div[@class='xy-container']//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//input[1]"
		# gps无定位的值
		self.gps_no_position = By.XPATH,"//body/div[@class='el-select-dropdown el-popper']/div[@class='el-scrollbar']/div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul[@class='el-scrollbar__view el-select-dropdown__list']/li[@class='el-select-dropdown__item selected']/span[1]"
		
	# 查找选择的上过线
	def find_online_status(self):
		return self.get_element(self.online_status)
	
	# 确认下拉框中的值
	def find_over_the_line(self):
		return self.get_element(self.over_the_line)
	
	# 确认分页中的车辆总数
	def find_car_num(self):
		return self.get_element(self.car_num)
	
	# 点击首页，跳转首页
	def find_home_page(self):
		return self.get_element(self.home_page)
	
	# 确认展开查询
	def find_open_select(self):
		return self.get_element(self.open_select)
	
	# 确认gps无定位
	def find_gps_no_position(self):
		return self.get_element(self.gps_no_position)
	
	# 查找无定位的gps下拉框
	def find_gps_status(self):
		return self.get_element(self.gps_status)