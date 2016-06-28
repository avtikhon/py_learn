import unittest
import logging
import sys
import argparse

optparser = argparse.ArgumentParser()
optparser.add_argument('--log', '-l', dest='loglevel', default = 'INFO', help = 'verbosity log level from the list: DEBUG, INFO, WARNING, ERROR, CRITICAL')
args = optparser.parse_args()
print("Arguments: %s" % args)

class TestUM(unittest.TestCase):
    def setUp(self):
        logging.debug("")
        pass

    def tearDown(self):
        logging.debug("")
        pass

    # start testing with methods named by pattern test_*
    
    def test_numbers_3_4(self):
        logging.debug("")
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        logging.debug("")
        self.assertEqual('a' * 3, 'aaa')

logger = logging.getLogger()
logger.setLevel(args.loglevel)
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d][THREAD:%(thread)d]# %(levelname)-8s [%(asctime)s] [%(funcName)s]: %(message)s')

### USE:
#if __name__ == '__main__':
#    unittest.main()
### EITHER with verbose range(2):
suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)
unittest.TextTestRunner(verbosity = 2).run(suite)

