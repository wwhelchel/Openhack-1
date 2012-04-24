import novaclient
import os
import unittest
import time
import logging
import getpass

from Infrastructure import disclaimer
from Infrastructure import instances
from Infrastructure import logger



class Test(unittest.TestCase):
    def setUp(self):
        self.insts = instances.manage_instances()
        self.log = logger.logger()
        self.log.open_file() 
#    def test_metadata(self):
#        metaKeyTrue = 'test'
#        instances = self.insts.list_instances()
#        instances = self.insts.get_instances_with_tag(instances, 
#                                                      metaKeyTrue)
#        for i in range(len(instances)):
#            self.assertFalse(insts._instance_has_tag(instances[i], 
#                                                metaKeyTrue))

    def test_select_num_of_instances(self):
        for i in range(int(1)):
            self.assertRaises(self.insts.delete_random_instance(None), None)

    def test_wait_period(self):
        self.assertRaises(time.sleep(float(1)), None)
        
    def test_search_instances(self):
       #instances = nt.list()
       listofinstances = self.insts.list_instances()
       element = self.insts.select_random_instance(listofinstances)
       self.assertTrue(element in listofinstances)


    def test_display_instances_found(self):
		#can_search_instances(self)
        self.assertRaises(None, self.insts.display_instances())

    def test_delete_instance(self):
        
        def fake_delete(server, fake_list):
            fake_list.remove(server)
            return fake_list

        server = "Demo"
        fake_servers = ['elem1', 'elem2', server]
        fake_servers2 = fake_delete(server, fake_servers)    
        self.assertTrue(server not in fake_servers2)

    def test_log_disclaimer_accepted(self):
        
        self.log.log_disclaimer(True)
        username = getpass.getuser()
        path = '/home/%s/openhack/' % username
        logfiles = os.listdir(path)
        self.assertTrue('openhack.log' in logfiles)



if __name__ == '__main__':
    unittest.main()
