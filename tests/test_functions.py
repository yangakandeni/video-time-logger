import unittest

from functions import get_total_vidoes, record_running_times, log_running_times,  display_running_times, calc_total_duration


class FunctionsTestCase(unittest.TestCase):

    def setUp(self):
    #     # get total videos
        # self.total_videos = get_total_vidoes()
    #     # self.records = record_running_times(3)
    #     # self.logs = log_running_times(self.records)
        return super().setUp()

    # def test_can_total_videos_returns_integer(self):
    #     # enter 3 for test to pass
    #     videos = get_total_vidoes()

    #     self.assertIsInstance(videos, int)
    #     self.assertEqual(videos, 3)

    # def test_display_error_on_invalid_input(self):
    #     videos = get_total_vidoes()
    #     self.assertEqual(videos, f"\nPlease enter a valid number\n")

    # def test_record_running_times_function(self):
    #     # enter 3 for tests to pass
    #     videos = get_total_vidoes()
    #     records = record_running_times(videos)
    #     self.assertEqual(len(records), 3)

    def test_log_running_times_function(self):
        videos = get_total_vidoes()
        records = record_running_times(3)
        pickled_data = log_running_times(records)

        self.assertDictEqual(records, pickled_data)

    def test_calc_total_duration_function(self):
        videos = get_total_vidoes()
        records = record_running_times(videos)
        result = calc_total_duration(records)
        self.assertTrue(isinstance(result, int))

    # def test_display_running_times(self):

