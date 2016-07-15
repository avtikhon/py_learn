import unittest
import logging

class TestCase2(unittest.TestCase):
    def setUp(self):
        logging.debug("")
        pass

    def tearDown(self):
        logging.debug("")
        pass

    # start testing with methods named by pattern test_*
    
    def test_2_1(self):
        logging.debug("3 * 4 = 12")
        self.assertEqual(3 * 4, 12)

    def test_2_2(self):
        logging.debug("'a' * 3 = 'aaa'")
        self.assertEqual('a' * 3, 'aaa')

    def test_2_3(self):
        logging.debug("'a' * 3 = 'aaa'")
        self.assertEqual('a' * 3, 'aaa')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    runner = unittest.TextTestRunner(verbosity = 0)
    result = runner.run(suite)

