


from selenium.webdriver.common.by import By

# 我的订单页面
class OrderPage():

	# 鼠标悬浮我的商城
	my_shop = (By.LINK_TEXT,'我的商城')
	# 点击我的订单
	my_order = (By.LINK_TEXT,'我的订单')
	# 订单编号
	order_id = (By.CSS_SELECTOR,'span.time-num')	# 返回列表取第2个
	# 商品名称
	shop_name = (By.CSS_SELECTOR,'div.shop_name')	# 返回列表取第一个
	# 商品价格
	shop_price = (By.CSS_SELECTOR,'div.pric_rhz')	# 返回列表取取第2个
	# 商品数量
	shop_num = (By.CSS_SELECTOR,'td.sx3')		# 返回列表取第二个
	# 商品状态
	shop_status = (By.CSS_SELECTOR,'div.detail_or')	# 返回列表取第1个