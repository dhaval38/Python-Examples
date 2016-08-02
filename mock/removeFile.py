import os
import os.path

class RemovalService(object):
    """ A service for removing objects from filesystem. """

    def rm(self, filename):
        if os.path.isfile(filename):
            print "%s : filename : %s" %(__file__, filename)
            os.remove(filename)

class UploadService(object):
    
    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        print "upload_complete : %s " %filename
        self.removal_service.rm(filename)

