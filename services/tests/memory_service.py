import unittest
import psutil
import time

class TestSystemInfo(unittest.TestCase):
    
    def test_swap_usage(self):
        swap = psutil.swap_memory()
        self.assertIsNotNone(swap)
        self.assertIsInstance(swap.total, int)
        self.assertIsInstance(swap.used, int)
        self.assertIsInstance(swap.free, int)
        self.assertIsInstance(swap.percent, float)
        time.sleep(1)

    def test_ram_usage(self):
        ram = psutil.virtual_memory()
        self.assertIsNotNone(ram)
        self.assertIsInstance(ram.total, int)
        self.assertIsInstance(ram.available, int)
        self.assertIsInstance(ram.used, int)
        self.assertIsInstance(ram.free, int)
        self.assertIsInstance(ram.percent, float)
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()

