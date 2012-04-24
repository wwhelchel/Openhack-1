import novaclient
import os
import unittest
import logging

#from Infrastructure import disclaimer
from Infrastructure import instances
from Infrastructure import logger

class Test(unittest.TestCase):
	
    def setUp(self):
        self.credentials = {'username': 'ruse1', 'apikey': '0a2bb2bddd3337ed02dd27f042ea73a3', 
                            'projectid': 'ruse1-project', 'apikey': '0a2bb2bddd3337ed02dd27f042ea73a3', 
                            'url': 'http://alpha.auth.api.rackspacecloud.com:5000/v2.0/', 'region': 'ORD', 
                            'version': '1.1'} 
        self.oh = manage_instances()

    def test_login(self):
        self.assertTrue(manage_instances.login(self.oh, self.credentials), True)


    def test_search_instances(self):
        #instances = nt.list()
        instances = manage_instances.search_for_instances(self.oh)
        element = manage_instances.select_random_instance(self.oh)
        self.assertTrue(element in instances)


    def test_display_instances_found(self):
		#can_search_instances(self)
        self.assertRaises(None, manage_instances.display_instances(self.oh))
		
#class LoggingTestCase(unittest.TestCase):
#    """OpenHack logging tests"""
#    def setup(self):
#        indemn = disclaimer.indemnify()
#        manage = instances.manage_instances()
#        log = logger.logger()
#
#    def test_log_disclaimer_accepted(self):
#       
#        def fake_disclaimer_response(*args, **kwargs):
#            return True
#        
#        logfiles = os.listdir('openhack/logs')
#        indemn.disclaimer_response = fake_disclaimer_response
#        self.AssertTrue('disclaimer_response.log' in logfiles)
#
#    def test_open_log_with_invalid_path(self):
#        
#        def fake_open_log(*args, **kwargs):
#            return 'File Not Found'
#        invalid_file = open_log('dog/dj/mom.log')
#        log.open_log = fake_open_log
#        self.AssertEqual(invalid_file, 'File Not Found')
#
#
#class DeleteInstancesTestCase(unittest.TestCase):
#    """Tests for deleting an instance"""
#    def test_delete_instance(self):
#        server = "Demo"
#        def fake_list(*args, **kwargs):
#            fake_servers = ['elem1', 'elem2', server]
#            return fake_servers
#        
#        manage.search_for_instances = fake_list
#        terminate_instance(server)
#        self.assertNotIn(server,fake_servers)
#
#    def test_output_success(self):
#        def fake_delete(*args, **kwargs):
#            deleted = True
#            return deleted 
#
#        manage.terminate_instance = fake_delete
#        self.assertTrue(deleted)
#
#    def test_output_failure(self):
#        def fake_delete(*args, **kwargs):
#            deleted = False
#            return deleted 
#
#        terminate_instance = fake_delete
#        self.assertNotTrue(deleted)
