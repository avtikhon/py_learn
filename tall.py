#!/usr/bin/python3.4

import unittest
import logging
import sys
import os
import re
import argparse
sys.path.append(os.getcwd())
import tc1
import tc2

# setup run options
optparser = argparse.ArgumentParser()

optparser.add_argument('--log', '-l',
        dest = 'loglevel',
        default = 'WARNING',
        type = str,
        choices = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
        help = 'any single verbosity log level from the list')

optparser.add_argument('--tests', '-t',
        dest = 'testlist',
        default = '1,2',
        type = str,
        help = 'test list to run, like 1,2')

args = optparser.parse_args()

# setup logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d][THREAD:%(thread)d]# %(levelname)-8s [%(asctime)s] [%(funcName)s]: %(message)s')
logger = logging.getLogger()
logger.setLevel(args.loglevel)

# print run arguments
logging.info("Arguments: %s" % args)

# setup tests names
tests = re.split('[| :;,]', args.testlist)

# main routine
if __name__ == '__main__':
    suite = unittest.TestSuite()
    for test in tests:
        if test == '1':
            suite.addTests(unittest.TestLoader().loadTestsFromModule(tc1))
        elif test == '2':
            suite.addTests(unittest.TestLoader().loadTestsFromModule(tc2))

    runner = unittest.TextTestRunner(verbosity = 2)
    result = runner.run(suite)

