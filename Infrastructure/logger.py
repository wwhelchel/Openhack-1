import logging
import os
import getpass
from time import gmtime, strftime

class logger(object):
    def open_file(self):
        self.LOG = logging.getLogger(__name__)
        LOG_FILENAME = 'openhack.log'
        self.LOG.setLevel(logging.INFO)
        file_handler = logging.FileHandler(LOG_FILENAME)
        #console_handler = logging.StreamHandler()
        #self.LOG.addHandler(console_handler)
        self.LOG.addHandler(file_handler)

    def log_disclaimer(self, accepted):
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        username = getpass.getuser()
        uid = os.getuid()

        if accepted:
            logmessage = "DISCLAIMER log: User %s with UID %i ACCEPTED disclaimer at %s" % (username,uid,time)
            self.LOG.info(logmessage)
        if not accepted:
            logmessage = "DISCLAIMER log: User %s with UID %i DECLINED disclaimer at %s" % (username,uid,time)
            self.LOG.info(logmessage)
            

    def log_termination_success(self, instanceid):
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        username = getpass.getuser()
        uid = os.getuid()
        logmessage = ("INSTANCE log: User %s with UID %i TERMINATED instance"
                      " with instance ID %s at %s" % (username,uid,instanceid,time))
        self.LOG.info(logmessage)

 
    def log_termination_failure(self, instanceid):
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        username = getpass.getuser()
        uid = os.getuid()
        logmessage = ("INSTANCE log: User %s with UID %i FAILED TO TERMINATE instance"
                      " with instance ID %s at %s" % (username,uid,instanceid,time))
        self.LOG.info(logmessage)      
