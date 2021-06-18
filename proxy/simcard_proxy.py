from handle.simcard_handle import SimCardHandle

class SimCardProxy:
	def __init__(self):
		self.sim_card_handle = SimCardHandle()
	
	# 新增
	def add_simcard(self,operator,iccid,msisdn,imsi):
		self.sim_card_handle.select_operators(operator)
		self.sim_card_handle.send_iccid(iccid)
		self.sim_card_handle.send_msisdn(msisdn)
		self.sim_card_handle.send_imsi(imsi)
		self.sim_card_handle.click_sava_sim_card()

