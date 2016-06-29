import unittest
import logging
import sys
import argparse
import t1
import t2

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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(t1)
    suite.addTests(unittest.TestLoader().loadTestsFromModule(t2))

    runner = unittest.TextTestRunner(verbosity = 2)
    result = runner.run(suite)

