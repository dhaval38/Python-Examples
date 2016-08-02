import unittest
import mock
from removeFile import RemovalService, UploadService

class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch("removeFile.os.path")
    @mock.patch("removeFile.os")
    def test_rm(self, mock_os, mock_path):

        reference = RemovalService()
        mock_path.isfile.return_value = False
        reference.rm("any path")
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present")

        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):
    
    
    @mock.patch.object(RemovalService, "rm")
    def test_upload_complete(self, mock_rm):
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        reference.upload_complete("my uploaded file")
        mock_rm.assert_called_with("my uploaded file")
        removal_service.rm.assert_called_with("my uploaded file")
    """
     
    def test_upload_complete(self, mock_rm):
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        reference.upload_complete("my uploaded file")
        mock_removal_service.rm.assert_called_with("my uploaded file")   
   """
 
if __name__ == "__main__":
    unittest.main()
