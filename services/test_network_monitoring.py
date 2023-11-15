from network_service import get_network_usage as gnu
import unittest

class NetworkMonitoringTest(unittest.TestCase):

    def test_network_monitoring(self):
        result = gnu()
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()