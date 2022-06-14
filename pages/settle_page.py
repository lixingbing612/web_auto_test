

from selenium.webdriver.common.by import By

# 结算页面
class SettlePage():

	# 输入数量
	amount = (By.CSS_SELECTOR,'input.wi43')
	# 点击去结算
	settle = (By.LINK_TEXT,'去结算')
	# 点击提交订单
	sumbit_order = (By.CSS_SELECTOR,"a[onclick='submit_order();']")
	# 选择付款方式为货到付款
	pay_way = (By.CSS_SELECTOR,"input[value='pay_code=cod']")
	# 点击确认支付
	confirm_pay = (By.LINK_TEXT,'确认支付方式')

