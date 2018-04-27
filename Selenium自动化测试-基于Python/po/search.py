#encoding: utf-8
from base import BasePage
from base import InvalidPageException
import time

class SearchRegion(BasePage):
	_search_box_locator = '//*[@id=\"warp-box\"]/div[1]/div/form/input[1]'

	def __init__(self, driver):
		super(SearchRegion, self).__init__(driver)

	def searchFor(self, keyword):
		self.searchKeyword = self.driver.find_element_by_xpath(self._search_box_locator)
		self.searchKeyword.clear()
		self.searchKeyword.send_keys(keyword)
		self.searchButton = self.driver.find_element_by_id("searchBtn")
		self.searchButton.click()
		return SearchResults(self.driver)

class SearchResults(BasePage):

	locator = "cutstr"
	title = "title"
	resultKey = ""
	

	def __init__(self, driver):
		super(SearchResults, self).__init__(driver)
		time.sleep(2)
		results = self.driver.find_element_by_class_name(self.locator)
		resultsCheck = results.get_attribute(self.title)
		self.resultKey = resultsCheck




	def _validate_page(self, driver):
		pass
		# if "fuck" not in driver.title:
		# 	raise InvalidPageException('results not loaded!')








