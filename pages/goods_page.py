

from selenium.webdriver.common.by import By

# 商品详情页面
class GoodPage():

	# 点击商品
	good_detail = (By.CLASS_NAME,'floor-goods-item')
	# 点击添加购物车
	add_cart = (By.ID,'join_cart')
	# 点击关闭对话框
	close_cart = (By.CLASS_NAME,"layui-layer-ico")
	# 点击我的购物车
	my_cart = (By.CSS_SELECTOR,'i.share-shopcar-index')

