#test
import novaclient
import os
import unittest
import logging
import getpass

from Infrastructure import disclaimer
from Infrastructure import instances
from Infrastructure import logger




class Test(unittest.TestCase):
    def setUp(self):
#        self.indemn = disclaimer.indemnify()
#        self.manage = instances.manage_instances()
        self.log = logger.logger()

    def test_log_disclaimer_accepted(self):
       
        self.log.log_disclaimer(True)
        username = getpass.getuser()
        path = '/home/%s/openhack/' % username
        logfiles = os.listdir(path)
        self.assertTrue('openhack.log' in logfiles)

if __name__ == '__main__':
    unittest.main()
