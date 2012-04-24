import argparse
import novaclient
import novaclient.v1_1.client
import os
from random import choice
from logger import logger

class manage_instances(object):
    def __init__(self):
        self.log = logger() 
        self.servers = []
        self.auth_data = { 'region_name':'DFW',
                           'service_name':'cloudServersOpenStack' }
        self.credentials = {'username': os.environ['NOVA_USERNAME'], 
                            'apikey': os.environ['NOVA_API_KEY'], 
                            'projectid': os.environ['NOVA_PROJECT_ID'] , 
                            'url': os.environ['NOVA_URL'], 
                            'version': 2,
                            }
       
        self.nt = novaclient.v1_1.client.Client(
                                self.credentials['username'], 
                                self.credentials['apikey'], 
                                self.credentials['projectid'], 
                                self.credentials['url'], 
                                insecure=True,
                               **self.auth_data)

    def list_instances(self):
        servers = self.nt.servers.list()
        if servers:
            return servers

    def display_instances(self):
        for server in self.servers:
            server = server.lstrip('<Server: ')
            server = server.rstrip('>')
            print server
    
    def terminate_instance(self, inst): 
        inst.delete()

    def select_random_instance(self, instances):
        inst = choice(instances)
        return inst
    
    def _has_tag(self, instance, tag):
        print instance
        if 'metadata' in instance:
            if 'tag' in instance['metadata']:
                if instance['metadata']['tag'] == tag:
                    return True
        else:
            return False

    def get_instances_with_tag(self, instance_list, tagname):
        instances = []
        for instance in instance_list:
            if self._has_tag(instance, tagname):
                instances.append(instance)
        return instances 

    def delete_random_instance(self, tag):
        self.log.open_file()
        instances = self.list_instances()

        if tag:
            instances = self.get_instances_with_tag(instances, tag)

        rmvabl=self.select_random_instance(instances)

        try:
            print "deleting instance %s" % (rmvabl)
            self.terminate_instance(rmvabl)
            self.log.log_termination_success(rmvabl)
            return True
        except Exception as e:
            print e
            print "There was a problem!"
            self.log.log_termination_failure(rmvabl)
            return False
