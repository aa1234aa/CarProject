import pytest
import random
import string
from utils.UtilsDriver import is_exist
from utils.UtilsDriver import UtilsDriver
from proxy.basic_data_proxy import BasicDataProxy
from proxy.simcard_proxy import SimCardProxy
from proxy.car_terminal_model_proxy import CarTerminalModelProxy
import logging
import allure


@pytest.mark.run(order=3)
class TestAuditArticle:
	# 定义类级别的fixture初始化操作
	def setup_class(self):
		self.basic_data_proxy = BasicDataProxy()
		self.sim_card_proxy = SimCardProxy()
		self.car_terminal_model_proxy = CarTerminalModelProxy()
	def teardown_class(self):
		pass
	
	@pytest.mark.skip(reason="一直获取不到上过线")
	# sim卡添加
	def test_sim_card(self):
		# SIM卡管理新增
		'''
			string.ascii_letters:生成大小写字母（type:字符串）
			string.digits:生成数字（type:字符串）
		'''
		logging.info("用户名1111")
		iccid = "bitnei" + ''.join(random.sample(string.digits + string.ascii_letters, 14))
		msisdn = ''.join(random.sample(string.digits + string.ascii_letters, 10))
		imsi = random.randint(0000000000000000, 999999999999999)
		self.basic_data_proxy.get_find_sim_card_mange()
		self.sim_card_proxy.add_simcard('移动', iccid, msisdn, imsi)
		assert is_exist(UtilsDriver.get_driver(), "新增成功")
		
		# 车辆型号新增
	@allure.severity(allure.severity_level.BLOCKER)
	def test_car_terminal_model(self):
		logging.info("用户名1111")
		car_model = "bitnei" + ''.join(random.sample(string.digits + string.ascii_letters, 5))
		category = "车机"
		unit_name = "潍柴动力股份有限公司"
		image="d://time.img"
		self.basic_data_proxy.get_find_car_terminal_model()
		self.car_terminal_model_proxy.add_car_terminal_model(car_model,category,unit_name,image)
		allure.attach(UtilsDriver.get_driver().get_screenshot_as_png(), "车辆型号新增", allure.attachment_type.PNG)