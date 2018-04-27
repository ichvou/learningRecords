import unittest
from serverLogin import LoginTest
import HTMLTestRunner
import os

dir = os.getcwd()

hereTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

smokeTests = unittest.TestSuite([hereTest])

outfile = open(dir + "/smokeTestsReport.html", "w")

#unittest.TextTestRunner(verbosity=2).run(smokeTests)

runner = HTMLTestRunner.HTMLTestRunner(
	stream = outfile,
	title = 'Test Report',
	description = 'Smoke Tests'
	)
runner.run(smokeTests)


