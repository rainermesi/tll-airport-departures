"""Whether a scheduled scrape should run.

GitHub Actions often starts a cron job after the clock has moved on. Requiring
the local hour to be exactly 06, 14, or 22 skipped those late starts, so no
flight log was written. A run stays inside the window from each of those hours
until five hours later. The 22:00 window crosses midnight.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

TALLINN = ZoneInfo('Europe/Tallinn')
SCRAPE_HOURS = (6, 14, 22)
GRACE_MINUTES = 5 * 60


def scrape_window_open(now):
    local = now.astimezone(TALLINN)
    minutes = local.hour * 60 + local.minute
    day = 24 * 60
    for hour in SCRAPE_HOURS:
        start = hour * 60
        end = start + GRACE_MINUTES
        if end <= day:
            if start <= minutes < end:
                return True
        elif minutes >= start or minutes < (end % day):
            return True
    return False


def main():
    now = datetime.now(TALLINN)
    if scrape_window_open(now):
        print(f'Scrape window is open ({now:%Y-%m-%d %H:%M} Europe/Tallinn)')
        return 0
    print(f'Skipping scrape at {now:%Y-%m-%d %H:%M} Europe/Tallinn')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
