import unittest

from hall_crowd import hourly_flight_counts, hourly_forecast, morning_crowd


def flight(number, title, scheduled):
    return {
        'flight_number': number,
        'flight_title': title,
        'scheduled_time': scheduled,
        'board': 'today',
    }


class MorningCrowdTest(unittest.TestCase):
    def test_holiday_morning_is_busier_than_the_same_flights_later(self):
        morning = [
            flight('BT 362', 'Riia', '05:40'),
            flight('XQ 499', 'Antalya', '06:45'),
            flight('HN 3453', 'Sharm El Sheikh', '07:30'),
        ]
        afternoon = [
            flight('BT 362', 'Riia', '15:40'),
            flight('XQ 499', 'Antalya', '16:45'),
            flight('HN 3453', 'Sharm El Sheikh', '17:30'),
        ]
        self.assertGreater(morning_crowd(morning), morning_crowd(afternoon))
        self.assertEqual(morning_crowd(afternoon), 0.0)

    def test_london_airport_is_not_a_holiday_charter(self):
        gatwick = morning_crowd([flight('FR 1', 'London (Gatwick)', '06:00')])
        antalya = morning_crowd([flight('FR 1', 'Antalya', '06:00')])
        self.assertGreater(antalya, gatwick)

    def test_missing_schedule_is_skipped(self):
        self.assertIsNone(morning_crowd([flight('BT 1', 'Riia', 'N/A')]))

    def test_hourly_forecast_peaks_before_a_morning_departure(self):
        hours = {
            hour: (loads, word, reason)
            for hour, loads, word, reason in hourly_forecast([
                flight('XQ 499', 'Antalya', '06:45'),
                flight('HN 3453', 'Sharm El Sheikh', '07:30'),
            ])
        }
        self.assertGreater(hours['05:00'][0], hours['12:00'][0])
        self.assertEqual(hours['12:00'][1], 'quiet')
        self.assertEqual(hours['12:00'][2], 'no flights')
        self.assertIn('2 charters', hours['05:00'][2])
        self.assertIn('Antalya', hours['05:00'][2])

    def test_flight_is_counted_in_the_two_hours_before_departure(self):
        counts = dict(hourly_flight_counts([flight('BT 1', 'Riia', '12:00')]))
        self.assertEqual(counts['10:00'], 1)
        self.assertEqual(counts['11:00'], 1)
        self.assertEqual(counts['12:00'], 0)
        self.assertEqual(counts['09:00'], 0)

    def test_tomorrow_board_is_not_counted_twice(self):
        rows = [flight('XQ 499', 'Antalya', '06:45')]
        rows[0]['board'] = 'tomorrow'
        self.assertIsNone(morning_crowd(rows))


if __name__ == '__main__':
    unittest.main()
