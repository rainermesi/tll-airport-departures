import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

import scrape_schedule

TALLINN = ZoneInfo('Europe/Tallinn')


def at(hour, minute):
    return datetime(2026, 10, 27, hour, minute, tzinfo=TALLINN)


class ScrapeWindowTests(unittest.TestCase):
    def test_target_hours_are_open(self):
        for hour in (6, 14, 22):
            self.assertTrue(scrape_schedule.scrape_window_open(at(hour, 0)))

    def test_delayed_night_run_stays_open(self):
        # 22:00 Europe/Tallinn on 26 Oct, started by Actions at 01:27 on 27 Oct.
        started = datetime(2026, 10, 27, 1, 27, tzinfo=TALLINN)
        self.assertTrue(scrape_schedule.scrape_window_open(started))

    def test_window_closes_after_five_hours(self):
        self.assertTrue(scrape_schedule.scrape_window_open(at(2, 59)))
        self.assertFalse(scrape_schedule.scrape_window_open(at(3, 0)))
        self.assertTrue(scrape_schedule.scrape_window_open(at(10, 59)))
        self.assertFalse(scrape_schedule.scrape_window_open(at(11, 0)))
        self.assertFalse(scrape_schedule.scrape_window_open(at(5, 33)))

    def test_summer_time_twin_hour_still_scrapes(self):
        # 04:00 UTC is 07:00 during summer time, one hour after the 06:00 run.
        self.assertTrue(scrape_schedule.scrape_window_open(at(7, 0)))


if __name__ == '__main__':
    unittest.main()
