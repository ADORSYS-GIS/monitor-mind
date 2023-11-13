
import unittest
from io import StringIO
from unittest.mock import patch

import cpu_service
import memory_service
import disk_service

class ServiceTests(unittest.TestCase):

    def test_cpu_usage(self):
        print('CPU usage:')
        cpu_usage = cpu_service._collect_cpu_usage()
        print(cpu_usage)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            cpu_service._collect_cpu_usage()
            output = fake_output.getvalue().strip()

        self.assertFalse("CPU usage is above threshold" in output)

    def test_memory_usage(self):
        print('Memory usage:')
        memory_usage = memory_service.get_memory_usage()
        print(memory_usage)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            memory_service.get_memory_usage()
            output = fake_output.getvalue().strip()

        self.assertTrue("The memory usage is stable" in output)

    def test_disk_usage(self):
        print('Disk usage:')
        disk_usage = disk_service.get_disk_usage()
        print(disk_usage)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            disk_service.get_disk_usage()
            output = fake_output.getvalue().strip()

        self.assertTrue("The disk usage is stable" in output)

if __name__ == '__main__':
    unittest.main()






