import novaclient
import os
import unittest
from Infrastructure import instances
import time

class Test(unittest.TestCase):
    def setUp(self):
       self.insts = instances.manage_instances()

    def test_metadata(self):
        metaKeyTrue = 'test'
        instances = self.insts.list_instances()
        instances = self.insts.get_instances_with_tag(instances, 
                                                      metaKeyTrue)
        for i in range(len(instances)):
            self.assertFalse(insts._instance_has_tag(instances[i], 
                                                metaKeyTrue))

    def test_select_num_of_instances(self):
        for i in range(int(1)):
            self.assertRaises(self.insts.delete_random_instance(None), None)

    def test_wait_period(self):
        self.assertRaises(time.sleep(float(1)), None)
        

if __name__ == '__main__':
    unittest.main()
