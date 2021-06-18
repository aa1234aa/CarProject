from base.base_page import BasePage
import random
import string
from selenium.webdriver.common.by import By


# sim卡界面层
class SimCardPage(BasePage):
	def __init__(self):
		super().__init__()
		self.operators = By.XPATH,"//input[@placeholder='请选择...']"  # 运营商
		self.iccid = By.XPATH,"//div[@class='el-form-item is-required el-form-item--small']//div[@class='el-input el-input--small']//input[@class='el-input__inner']"
		self.msisdn = By.XPATH,"//div[@class='main']//div[3]//div[1]//div[1]//div[1]//input[1]"
		self.imsi = By.XPATH,"//div[4]//div[1]//div[1]//div[1]//input[1]"
		# 保存
		self.save_sim_card= By.XPATH,"//button[@class='el-button el-button--primary el-button--small']"
	
	# 查找运营商
	def find_operators(self):
		return self.get_element(self.operators)
	
	# 查找iccid
	def find_iccid(self):
		return self.get_element(self.iccid)
	
	# 查找MSISDN
	def find_msisdn(self):
		return self.get_element(self.msisdn)
	
	# 查找imsi
	def find_imsi(self):
		return self.get_element(self.imsi)
	
	# 查找保存按钮
	def find_sava_sim_card(self):
		return self.get_element(self.save_sim_card)