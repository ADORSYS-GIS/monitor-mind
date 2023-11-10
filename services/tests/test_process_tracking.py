import unittest
import mock
from process_tracking import track_processes

class TrackProcessesTest(unittest.TestCase):

    mock_stdout = mock.Mock()

    @mock.patch('psutil.process_iter')
    def test_track_processes(self, mock_process_iter):
        # Mock the output of psutil.process_iter() to return a list of two processes.
        mock_process_iter.return_value = [mock.Mock(info={'pid': 1, 'name': 'Process 1'}), mock.Mock(info={'pid': 2, 'name': 'Process 2'})]

        # Call the track_processes() function.
        track_processes()

        # Assert that the track_processes() function printed the expected output to the stdout stream.
        expected_output = """Running Processes:
PID: 1, Name: Process 1
--------------------------------------------
PID: 2, Name: Process 2
--------------------------------------------
"""

        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

        # Assert that the track_processes() function called the psutil.process_iter() function.
        mock_process_iter.assert_called_once()

        # Assert that the track_processes() function printed the expected number of lines to the console.
        self.assertEqual(self.mock_stdout.call_count, len(expected_output.splitlines()))

if __name__ == '__main__':
    unittest.main()

