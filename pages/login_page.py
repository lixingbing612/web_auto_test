



from selenium.webdriver.common.by import By

# 登录页面
class LoginPage():

	# 点击登录
	login_link_elem = (By.LINK_TEXT, "登录")
	# 输入用户
	username_elem = (By.ID, "username")
	# 输入密码
	password_elem = (By.ID, "password")
	# 输入验证码
	verify_elem = (By.ID, "verify_code")
	# 点击登录
	login_button_elem = (By.NAME, "sbtbutton")
	# 验证成功消息
	login_success_msg = (By.LINK_TEXT, "13112345678")
	# 验证失败消息
	login_error_msg = (By.CLASS_NAME, "layui-layer-content")
	# 点击商城首页
	front_page = (By.CSS_SELECTOR,'a.home')
