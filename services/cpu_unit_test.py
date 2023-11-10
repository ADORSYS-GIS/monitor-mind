import unittest
from unittest.mock import patch
import cpu_service as cpu_service
import time


class CpuServicesTest(unittest.TestCase):
    def setUp(self):
        # Reset the fake_mem dictionary before each test
        cpu_service.fake_mem = {}

    @patch('cpu_service.psutil.cpu_percent')
    @patch('cpu_service.ts.get_history_time')
    def test_calculate_cpu_usage(self, mock_get_history_time, mock_cpu_percent):
        # Configure the mock return values
        mock_get_history_time.return_value = 123456789
        mock_cpu_percent.return_value = 50.0

        # Call the function under test
        result = cpu_service.calculate_cpu_usage()

        # Assert the mock function calls
        mock_get_history_time.assert_called_once()
        mock_cpu_percent.assert_called_once_with(interval=1)

        # Assert the result
        expected_result = (123456789, 50.0)
        self.assertEqual(result, expected_result)

        # Assert the fake_mem dictionary
        expected_fake_mem = {123456789: 50.0}
        self.assertEqual(cpu_service.fake_mem, expected_fake_mem)

    def test_get_cpu_usage_array(self):
        # Set up fake data in fake_mem dictionary
        cpu_usages = {123456789: 50.0, 987654321: 75.0}
        cpu_service.fake_mem = cpu_usages

        # Call the function under test
        result_keys, result_values = cpu_service.get_cpu_usage_array()

        # Assert the result
        expected_keys = [123456789, 987654321]
        expected_values = [50.0, 75.0]
        self.assertEqual(result_keys, expected_keys)
        self.assertEqual(result_values, expected_values)


if __name__ == '__main__':
    # Continuous test execution loop
    while True:
        # Create a test suite
        suite = unittest.TestSuite()

        # Add the test cases
        suite.addTest(unittest.makeSuite(CpuServicesTest))

        # Create a test runner
        runner = unittest.TextTestRunner()
        
        # Run the tests
        runner.run(suite)
        
        # Sleep for a few seconds before running the tests again
        time.sleep(5)