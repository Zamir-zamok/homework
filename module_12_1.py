import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        q = runner.Runner('JOil')
        for i in range(10):
            q.walk()
        self.assertEqual(q.distance, 50)

    def test_run(self):
        w = runner.Runner('Max')
        for i in range(10):
            w.run()
        self.assertEqual(w.distance, 100)

    def test_challenge(self):
        q = runner.Runner('JOil')
        w = runner.Runner('Max')
        for i in range(10):
            q.run()
            w.walk()
        self.assertNotEqual(q.distance, w.distance)
