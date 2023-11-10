import unittest
from unittest import mock
from services.cpu_service import calculate_cpu_usage, get_cpu_usage_array, _collect_cpu_usage,fake_mem


class CPUMonitorTestCase(unittest.TestCase):
    @mock.patch('cpu_monitor.ts.get_history_time')
    @mock.patch('cpu_monitor.psutil.cpu_percent')
    def test_calculate_cpu_usage(self, mock_cpu_percent, mock_get_history_time):
        mock_cpu_percent.return_value = 50.0
        mock_get_history_time.return_value = 1234567890

        calculate_cpu_usage()

        self.assertEqual(len(fake_mem), 1)
        self.assertEqual(fake_mem[1234567890], 50.0)

    def test_get_cpu_usage_array(self):
        fake_mem[1234567890] = 50.0
        fake_mem[1234567891] = 60.0

        timestamps, cpu_usages = get_cpu_usage_array()

        self.assertEqual(timestamps, [1234567890, 1234567891])
        self.assertEqual(cpu_usages, [50.0, 60.0])

    @mock.patch('cpu_monitor.ts.get_history_time')
    @mock.patch('cpu_monitor.psutil.cpu_percent')
    def test_collect_cpu_usage(self, mock_cpu_percent, mock_get_history_time):
        mock_cpu_percent.return_value = 50.0
        mock_get_history_time.return_value = 1234567890

        timestamp, cpu_usage = _collect_cpu_usage()

        self.assertEqual(timestamp, 1234567890)
        self.assertEqual(cpu_usage, 50.0)


if __name__ == '__main__':
    unittest.main()