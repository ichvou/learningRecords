#coding: utf-8

import time


def search_by_name(driver,xpath,keyword):
	driver = driver
	caseName = driver.find_element_by_xpath(xpath)
	caseName.clear()
	caseName.send_keys(keyword)
	return 0
