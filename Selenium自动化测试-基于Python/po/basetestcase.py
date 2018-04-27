import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(30)
		cls.driver.maximize_window()
		cls.driver.get("http://172.18.84.226")

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()