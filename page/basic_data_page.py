from base.base_page import BasePage
from selenium.webdriver.common.by import By


# 基础数据车辆列表
class BasicDataPage(BasePage):
	def __init__(self):
		super().__init__()
		# 基础数据图标
		self.basic_logo = By.XPATH,"//i[@class='icon iconfont icon-jichushuju']"
		# 零配件二级标题
		self.spare_parts = By.XPATH,"//div[@class='sub-menu-container']//li[2]//div[1]"
		# sim卡管理
		self.sim_card_mange = By.XPATH,"//li[@class='el-menu-item']//span[contains(text(),'SIM')]"
		# 点击sim新增按钮
		self.add_sim_card = By.XPATH,"//i[@class='fa margin-right5 fa-plus']"
		# 点击车辆终端信息
		self.car_terminal_info=By.XPATH,"//li[@class='el-submenu is-opened']//li[1]//span[1]"
		# 点击车辆终端型号
		self.car_terminal_model=By.XPATH,"//div[@id='tab-vehTerminalModel']"
		

	# 获取基础数据
	def find_basic_logo(self):
		return self.get_element(self.basic_logo)
	
	# 获取零配件
	def find_spare_parts(self):
		return self.get_element(self.spare_parts)
	
	# 获取sim卡管理
	def find_sim_card_mange(self):
		return self.get_element(self.sim_card_mange)
	
	# 获取新增按钮
	def find_add_sim_card(self):
		return self.get_element(self.add_sim_card)
	
	# 获取终端型号信息
	def find_car_terminal_info(self):
		return self.get_element(self.car_terminal_info)
	
	# 获取终端型号tab
	def find_car_terminal_model(self):
		return self.get_element(self.car_terminal_model)

