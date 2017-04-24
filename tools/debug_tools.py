import logging
import time

import django.conf


class TimeIt(object):
    def __init__(self, ident):
        """
        Track the time (in seconds) it takes to execute a block of code.

        :param str ident: String to identify the block of code.
        """
        self.ident = ident

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        elapsed = round(time.time() - self.start, 2)
        message = '{0}: {1}s'.format(self.ident, elapsed)
        logging.getLogger('debug_tools.timer').info(message)
        if django.conf.settings.DEBUG or django.conf.settings.TESTING:
            print(message)

