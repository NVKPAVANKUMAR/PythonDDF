import unittest
from scenarios.scenario_a import TestSceanarioA

scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestSceanarioA)
test_suite = unittest.TestSuite([scenario_a])
unittest.TextTestRunner(verbosity=2).run(test_suite)
