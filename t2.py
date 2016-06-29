import unittest
import logging
import sys
import argparse

# setup run options
optparser = argparse.ArgumentParser()
optparser.add_argument('--log', '-l',
        dest = 'loglevel',
        default = 'WARNING',
        type = str,
        choices = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
        help = 'any single verbosity log level from the list')

args = optparser.parse_args()

# setup logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d][THREAD:%(thread)d]# %(levelname)-8s [%(asctime)s] [%(funcName)s]: %(message)s')
logger = logging.getLogger()
logger.setLevel(args.loglevel)

logging.info("Arguments: %s" % args)

class TestUM(unittest.TestCase):
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)
    runner = unittest.TextTestRunner(verbosity = 0)
    result = runner.run(suite)

