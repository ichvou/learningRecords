import unittest
from selenium import webdriver
# from basepage import BasePage
from page import LoginPage

class test_login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("http://172.18.84.226")

	def test_login_system(self):
		# login_page = LoginPage(self.driver)
		login_page = LoginPage(self.driver)
		login_page.set_username("35771")
		login_page.set_password("9876501")
		login_page.set_vcode("2024")
		login_page.click_login("signin")



	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main(verbosity=2)