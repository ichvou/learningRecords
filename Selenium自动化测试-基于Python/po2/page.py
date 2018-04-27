#encoding: utf-8
from basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
	username = (By.ID,"username")
	password = (By.ID,"password")
	vcode = (By.ID,"code")
	loginbtn = (By.ID,"signin")


	def set_username(self, username):
		name = self.driver.find_element(*LoginPage.username)
		name.send_keys(username)

	def set_password(self, password):
		pwd = self.driver.find_element(*LoginPage.password)
		pwd.send_keys(password)

	def set_vcode(self, vcode):
		vc = self.driver.find_element(*LoginPage.vcode)
		vc.send_keys(vcode)

	def click_login(self, loginbtn):
		login = self.driver.find_element(*LoginPage.loginbtn)
		login.click()