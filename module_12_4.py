import logging
from runner_12_4 import Runner
import unittest

logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='runner_tests.log',
                    encoding='UTF-8',
                    format='%(asctime)s, %(levelname)s, %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            var1 = Runner("Alex", -5)
            for i in range(10):
                var1.walk()
            self.assertEqual(var1.distance,50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            var2 = Runner('Bob'-5, 5)
            for i in range(10):
                var2.run()
            self.assertEqual(var2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        var1 = Runner("Alex", 2)
        var2 = Runner("Bob", 5)
        for i in range(10):
            var1.walk()
            var2.run()
        self.assertNotEqual(var1.distance, var2.distance)

if __name__ == "__main__":
    unittest.main