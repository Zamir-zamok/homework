import unittest
import suite_12_3

testik = unittest.TestSuite()
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testik)