#!/usr/bin/env python
from logger import logger

class indemnify(object):
        def disclaimer_response(self):
            answer = raw_input("WARNING!!! OpenHack is going to break stuff.\n"
                   "Input 'D' to indemnify OpenHack and its\n"
                   "creators/contributors to your actions.\n"
                   "Anything else input will exit.\n")
            log = logger()
            log.open_file()
            response = False
            if answer == 'D':
                print 'Disclaimer Accepted.'
                response = True
            else:
                print 'Disclaimer Rejected. Terminating program.'
                response = False

            log.log_disclaimer(response)
           
            return response
