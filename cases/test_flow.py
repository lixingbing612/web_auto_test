import unittest
from time import sleep
from selenium import webdriver
from logic.buy_flow import BuyFlowLogic


class TestFlow(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.bf = BuyFlowLogic()

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("http://localhost")
		self.driver.maximize_window()

	def tearDown(self) -> None:
		pass

	# 测试购买流程
	def test_buy_flow(self):
		self.bf.login(self.driver, '13112345678', '123456', '8888')
		sleep(5)
		self.bf.buy(self.driver, '1')
		sleep(3)
		self.shop_name, self.order_id, self.shop_num, self.shop_price, self.shop_status = self.bf.order_info(self.driver)


if __name__ == '__main__':
	unittest.main()
