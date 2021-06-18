from handle.car_terminal_model_handle import CarTerminalModelHandle
from utils.UtilsDriver import action_down

# 车辆型号
class CarTerminalModelProxy:
	def __init__(self):
		self.car_terminal_model_handle = CarTerminalModelHandle()
	
	# 添加型号
	def add_car_terminal_model(self,car_model,category,unit_name,image):
		self.car_terminal_model_handle.click_add_car_model()
		self.car_terminal_model_handle.input_car_model(car_model)
		self.car_terminal_model_handle.select_terminal_category(category)
		self.car_terminal_model_handle.click_support_encryption_chip()
		self.car_terminal_model_handle.click_terminal_manufacturer()
		self.car_terminal_model_handle.input_unit_name(unit_name)
		self.car_terminal_model_handle.click_inquiry_unit()
		self.car_terminal_model_handle.click_select_unit()
		self.car_terminal_model_handle.click_determine()
		action_down()
		self.car_terminal_model_handle.upload_scan_of_sport(image)