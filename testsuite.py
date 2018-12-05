import unittest
import HtmlTestRunner
from scenarios.scenario_a import TestSceanarioA

scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestSceanarioA)
test_suite = unittest.TestSuite([scenario_a])
# initialize a runner, pass it your suite and run it
runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=2)
runner.run(test_suite)
