from time import sleep

from loguru import logger

from pages.login_page import LoginPage
from pages.goods_page import GoodPage
from pages.settle_page import SettlePage
from pages.order_page import OrderPage
from selenium.webdriver import ActionChains

# 购物流程类
class BuyFlowLogic():

	# 登录逻辑
	def login(self, driver, username, password, verify_code):

		# 点击登录按钮
		driver.find_element(*LoginPage.login_link_elem).click()
		# 输入用户名
		driver.find_element(*LoginPage.username_elem).send_keys(username)
		# 输入密码
		driver.find_element(*LoginPage.password_elem).send_keys(password)
		# 输入验证码
		driver.find_element(*LoginPage.verify_elem).send_keys(verify_code)
		# 点击登录
		driver.find_element(*LoginPage.login_button_elem).click()
		sleep(3)
		# 点击商城首页
		driver.find_element(*LoginPage.front_page).click()

	# 购买逻辑
	def buy(self,driver,num):

		# 点击商品
		driver.find_element(*GoodPage.good_detail).click()
		sleep(5)
		# 加入购物车
		driver.find_element(*GoodPage.add_cart).click()
		sleep(5)
		# 关闭对话框
		driver.find_element(*GoodPage.close_cart).click()
		sleep(10)
		# 点击我的购物车
		driver.find_element(*GoodPage.my_cart).click()
		sleep(5)
		# 输入数量
		driver.find_element(*SettlePage.amount).send_keys(num)
		sleep(5)
		# 点击去结算
		driver.find_element(*SettlePage.settle).click()
		sleep(10)
		# 点击提交订单
		driver.find_element(*SettlePage.sumbit_order).click()
		sleep(10)
		# 选择货到付款
		driver.find_element(*SettlePage.pay_way).click()
		sleep(10)
		# 确认付款方式
		driver.find_element(*SettlePage.confirm_pay).click()
		sleep(10)
		# 鼠标悬浮到我的商城链接上
		ActionChains(driver).move_to_element(driver.find_element(*OrderPage.my_shop)).perform()
		sleep(2)
		# 点击我的订单
		driver.find_element(*OrderPage.my_order).click()
		driver.implicitly_wait(5)

	# 跳转订单逻辑
	def order_info(self,driver):

		# 切换窗口
		driver.switch_to.window(driver.window_handles[-1])
		sleep(5)
		# 获取商品名称
		shop_name = driver.find_elements(*OrderPage.shop_name)[0].text
		logger.info('获取的商品名称：{}'.format(shop_name))
		# 获取订单编号
		order_id = driver.find_elements(*OrderPage.order_id)[1].text
		logger.info('获取的订单id：{}'.format(order_id))
		# 获取商品数量
		shop_num = driver.find_elements(*OrderPage.shop_num)[1].text
		logger.info('获取的商品数量：{}'.format(shop_num))
		# 获取商品价格
		shop_price = driver.find_elements(*OrderPage.shop_price)[1].text
		logger.info('获取的商品价格：{}'.format(shop_price))
		# 获取商品状态
		shop_status = driver.find_elements(*OrderPage.shop_status)[0].text
		logger.info('获取的商品状态：{}'.format(shop_status))

		return shop_name,order_id,shop_num,shop_price,shop_status
