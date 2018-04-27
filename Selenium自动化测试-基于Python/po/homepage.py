from base import BasePage
from base import InvalidPageException
import time

class HomePage(BasePage):

	_home_page_slideshow_locator = "username"

	def __init__(self, driver):
		super(HomePage, self).__init__(driver)
		userno=""
		pwd = ""
		vode = ""
		workNo = self.driver.find_element_by_id("username")
		workNo.send_keys(userno)
		workPwd = self.driver.find_element_by_id("password")
		workPwd.send_keys(pwd)
		vCode = self.driver.find_element_by_id("code")
		vCode.send_keys(vode)
		loginButton = self.driver.find_element_by_id("signin")
		loginButton.click()
		time.sleep(1.5)

	def _validate_page(self, driver):
	 	pass
	# 	try:
	# 		driver.find_element_by_id(slef._home_page_slideshow_locator)
	# 	except:
	# 		raise InvalidPageException("Home Page not loaded")
    



