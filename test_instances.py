import novaclient
import os
import unittest
import logging

from Infrastructure import disclaimer
from Infrastructure import instances
from Infrastructure import logger

class Test(unittest.TestCase):
	
    def setUp(self):
        #self.credentials = {'username': 'pknouff', 'apikey': '817cd8d95aeb4185ac85ebe72dbd6c49', 
        #                    'projectid': '666780', 
        #                    'url': 'https://auth.api.rackspacecloud.com/v2.0/tokens', 'region': 'DFW', 
        #                    'version': '2'} 
        self.oh = instances.manage_instances()
        
       
  #  def test_login(self):
   #     self.assertTrue(self.oh.login(), True)


    def test_search_instances(self):
       #instances = nt.list()
       listofinstances = self.oh.list_instances()
       element = self.oh.select_random_instance(listofinstances)
       self.assertTrue(element in listofinstances)


    def test_display_instances_found(self):
		#can_search_instances(self)
        self.assertRaises(None, self.oh.display_instances())

    def test_delete_instance(self):
        
        def fake_delete(server, fake_list):
            fake_list.remove(server)
            return fake_list

        server = "Demo"
        fake_servers = ['elem1', 'elem2', server]
        fake_servers2 = fake_delete(server, fake_servers)    
        self.assertTrue(server not in fake_servers2)

if __name__ == '__main__':
    unittest.main()


