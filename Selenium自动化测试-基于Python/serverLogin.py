#coding: utf-8
import unittest
import time
from selenium import webdriver
import sys
# import io
reload(sys)
sys.setdefaultencoding("utf-8")

class LoginTest(unittest.TestCase):
	# def setUp(self):
	# 	self.driver = webdriver.Chrome()
	# 	self.driver.implicitly_wait(30)
	# 	self.driver.maximize_window()
	# 	self.driver.get("http://172.18.84.226:93")

	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['platform'] = 'WINDOWS'
		desired_caps['browserName'] = 'Chrome'
		cls.driver = webdriver.Remote('http://172.18.84.7:5566/wd/hub', desired_caps)
		cls.driver.implicitly_wait(30)
		cls.driver.maximize_window()
		cls.driver.get("http://172.18.84.226")

	def test_login_by_workno(self):
		workNo = self.driver.find_element_by_id("username")
		workNo.send_keys("")
		workPwd = self.driver.find_element_by_id("password")
		workPwd.send_keys("")
		vCode = self.driver.find_element_by_id("code")
		vCode.send_keys("")
		loginButton = self.driver.find_element_by_id("signin")
		loginButton.click()
		time.sleep(1.5)
		# print self.driver.title
		userNo = self.driver.find_element_by_id("workno")
		self.assertEqual("", userNo.text)


	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)


