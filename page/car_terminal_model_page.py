from base.base_page import BasePage
from selenium.webdriver.common.by import By


# 车辆终端型号
class CarTerminalModelPage(BasePage):
	def __init__(self):
		super().__init__()
		# 新增
		self.add_car_model = By.XPATH,"//div[@id='pane-vehTerminalModel']//div[@class='el-col el-col-16']//div[1]//button[1]//span[1]"
		# 终端型号
		self.car_model = By.XPATH,"//div[@class='el-form-item is-required el-form-item--mini']//div[@class='el-input el-input--mini']//input[@class='el-input__inner']"
		# 终端种类
		self.terminal_category = By.XPATH,"//input[@placeholder='请选择']"
		# 支持加密芯片
		self.support_encryption_chip = By.XPATH,"//span[@class='el-radio__input is-checked']//span[@class='el-radio__inner']"
		# 终端生产企业
		self.terminal_manufacturer = By.XPATH,"//i[@class='el-input__icon el-icon-search']"
		# 单位名称
		self.unit_name = By.XPATH,"//div[@class='el-input el-input--small el-input--suffix']//input[@class='el-input__inner']"
		# 单位查询
		self.inquiry_unit = By.XPATH,"//div[@class='el-col el-col-20']//button[@class='el-button el-button--primary el-button--small']"
		# 选择单位
		self.select_unit = By.XPATH,"//div[@class='cell']//span[@class='el-radio__inner']"
		# 确定
		self.determine = By.XPATH,"//button[@class='el-button el-button--primary el-button--mini']//span"
		# 终端检测报告扫描件
		self.scan_of_sport = By.XPATH,"//div[@class='el-form-item is-required el-form-item--mini']//div[@class='el-form-item__content']//div//div//div[@class='el-upload el-upload--picture-card']"

	# 查找新增
	def find_add_car_model(self):
		return self.get_element(self.add_car_model)
	
	# 查找终端型号
	def find_car_model(self):
		return self.get_element(self.car_model)
	
	# 查找终端种类
	def find_terminal_category(self):
		return self.get_element(self.terminal_category)
	
	# 查找支持加密芯片
	def find_support_encryption_chip(self):
		return self.get_element(self.support_encryption_chip)
	
	# 查找终端生产企业
	def find_terminal_manufacturer(self):
		return self.get_element(self.terminal_manufacturer)
	
	# 查找单位名称
	def find_unit_name(self):
		return self.get_element(self.unit_name)
	
	# 单位查询
	def find_inquiry_unit(self):
		return self.get_element(self.inquiry_unit)
	
	# 选择单位
	def find_select_unit(self):
		return self.get_element(self.select_unit)
	
	# 确定
	def find_determine(self):
		return self.get_element(self.determine)
	
	# 终端检测报告扫描件
	def find_scan_of_sport(self):
		return self.get_element(self.scan_of_sport)