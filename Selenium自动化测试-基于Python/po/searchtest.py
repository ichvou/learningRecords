#encoding: utf-8

import unittest
from homepage import HomePage
from basetestcase import BaseTestCase
from search import SearchRegion

class SearchCaseTest(BaseTestCase):
	def testSearchCaseTest(self):
		keyword = u"大明宫中央广场"
		homepage = HomePage(self.driver)
		search_case = SearchRegion(self.driver)
		searchResults = search_case.searchFor(keyword)
		self.assertEqual(keyword, searchResults.resultKey)




if __name__ == '__main__':
	unittest.main(verbosity=2)