#encoding: utf-8

from abc import abstractmethod

class BasePage(object):
	""" all page objects inherit from this"""

	def __init__(self, driver):
		self._validate_page(driver)
		self.driver = driver



	@abstractmethod
	def _validate_page(self, driver):
		pass

	""" regions define functionality available through all page objects"""
	@property
	def search(self):
		from search import SearchRegion
		return SearchRegion.searchFor(self.driver)


class InvalidPageException(Exception):
	""" throw this exception when you don't find the correct page """
	pass
