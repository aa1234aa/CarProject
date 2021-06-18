from base.base_handle import BaseHandle
from page.simcard_page import SimCardPage
from utils.UtilsDriver import UtilsDriver,choice_operator


# sim卡操作层
class SimCardHandle(BaseHandle):
	def __init__(self):
		self.simcardpage=SimCardPage()
		self.driver = UtilsDriver.get_driver()
		
	# 选择运营商
	def select_operators(self,operator):
		choice_operator(self.driver,self.simcardpage.find_operators(),operator)
	
	# 输入iccid
	def send_iccid(self,iccid):
		self.input_text(self.simcardpage.find_iccid(),iccid)
	
	# 输入msisdn
	def send_msisdn(self,msisdn):
		self.input_text(self.simcardpage.find_msisdn(),msisdn)
	
	# 输入imsi
	def send_imsi(self,imsi):
		self.input_text(self.simcardpage.find_imsi(),imsi)
	
	# 点击保存按钮
	def click_sava_sim_card(self):
		self.simcardpage.find_sava_sim_card().click()