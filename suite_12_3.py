import runner
import unittest
import runner_and_tournament as rt

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        q = runner.Runner('JOil')
        for i in range(10):
            q.walk()
        self.assertEqual(q.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        w = runner.Runner('Max')
        for i in range(10):
            w.run()
        self.assertEqual(w.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        q = runner.Runner('JOil')
        w = runner.Runner('Max')
        for i in range(10):
            q.run()
            w.walk()
        self.assertNotEqual(q.distance, w.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = rt.Runner("Усэйн", 10)
        self.run2 = rt.Runner("Андрей", 9)
        self.run3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_1(self):
        run_1 = rt.Tournament(90, self.run1, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_2(self):
        run_1 = rt.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_3(self):
        run_1 = rt.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish
