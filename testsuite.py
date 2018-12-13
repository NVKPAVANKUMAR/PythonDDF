import unittest
from scenarios.scenario_a import TestSceanarioA

scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestSceanarioA)
test_suite = unittest.TestSuite([scenario_a])
logFile = open("logfile.txt", "a")
unittest.TextTestRunner(verbosity=2, stream=logFile).run(test_suite)

# # initialize the test suite
# loader = unittest.TestLoader()
# suite = unittest.TestSuite()
#
# # add tests to the test suite
# suite.addTests(loader.loadTestsFromTestCase(TestSceanarioA))
#
# # initialize a runner, pass it your suite and run it
# runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=2, report_title="Regression Suite")
# runner.run(suite)

# suite = unittest.TestSuite()
# suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestSceanarioA)])
# runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=3, report_title="Regression Suite")
# runner.run(suite)
# logger = logging.getLogger()
# with open('report.html', 'a') as report_file:
#     runner = HtmlTestRunner.HTMLTestRunner(output=report_file, verbosity=2, report_title="Regression Suite")
#
#     scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestSceanarioA)
#     test_suite = unittest.TestSuite([scenario_a])
#
#     result = runner.run(test_suite)
#     print(result)
