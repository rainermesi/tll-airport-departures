from destinations import normalize_destination

# One plane-load is 150 departing passengers. The chart unit is this size.
PLANE_LOAD = 150
LOAD_FACTOR = 0.85
CHARTER_WEIGHT = 1.5
BIN_MINUTES = 15
# Passengers are spread from 3 hours before departure until 1 hour before.
LEAD_MINUTES = 180
SPREAD_MINUTES = 120
MORNING_START = 3 * 60
MORNING_END = 8 * 60

SEATS_BY_PREFIX = {
    'AY': 100,
    'BT': 145,
    'FR': 189,
    'LH': 180,
    'LO': 112,
    'LX': 180,
    'OJ': 70,
    'SK': 180,
    'TK': 180,
    'W4': 180,
    'W6': 230,
    'W9': 180,
}
DEFAULT_SEATS = 160
CHARTER_PREFIXES = {
    'ENT',
    'GW',
    'HN',
    'HOT',
    'QU',
    'STM',
    'XQ',
}
CHARTER_DESTINATIONS = {
    'antalya',
    'bodrum',
    'burgas',
    'enfidha',
    'funchal',
    'gran canaria',
    'heraklion',
    'hurghada',
    'kerkira',
    'larnaca',
    'palma de mallorca',
    'paphos',
    'rhodos',
    'sharm el sheikh',
    'tenerife',
    'tenerife (south)',
}


def flight_prefix(flight_number):
    parts = str(flight_number or '').split()
    return parts[0] if parts else ''


def is_charter(flight_number, flight_title):
    if flight_prefix(flight_number) in CHARTER_PREFIXES:
        return True
    title = normalize_destination(flight_title).casefold()
    return title in CHARTER_DESTINATIONS


def passengers(row):
    seats = SEATS_BY_PREFIX.get(flight_prefix(row.get('flight_number')), DEFAULT_SEATS)
    weight = CHARTER_WEIGHT if is_charter(row.get('flight_number'), row.get('flight_title')) else 1
    return seats * LOAD_FACTOR * weight


def clock_minutes(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text or text == 'N/A' or ':' not in text:
        return None
    hour, minute = text.split(':', 1)
    try:
        return int(hour) * 60 + int(minute)
    except ValueError:
        return None


def crowd_bins(rows, skip_tomorrow=True):
    bins = {}
    saw_time = False
    for row in rows:
        if skip_tomorrow and str(row.get('board') or 'today') == 'tomorrow':
            continue
        depart = clock_minutes(row.get('scheduled_time'))
        if depart is None:
            continue
        saw_time = True
        start = depart - LEAD_MINUTES
        end = start + SPREAD_MINUTES
        slot = (start // BIN_MINUTES) * BIN_MINUTES
        slots = []
        while slot < end:
            slots.append(slot)
            slot += BIN_MINUTES
        if not slots:
            continue
        share = passengers(row) / len(slots)
        for minute in slots:
            bins[minute] = bins.get(minute, 0) + share
    return bins, saw_time


def crowd_label(plane_loads):
    if plane_loads < 0.7:
        return 'quiet'
    if plane_loads < 1.1:
        return 'steady'
    if plane_loads < 1.5:
        return 'busy'
    return 'crowded'


def morning_crowd(rows):
    """Peak plane-loads of departing passengers in the terminal from 03:00 to 08:00.

    Returns None when no row has a scheduled time. Returns 0 when flights are
    scheduled only outside the morning.
    """
    bins, saw_time = crowd_bins(rows, skip_tomorrow=True)
    if not saw_time:
        return None
    morning = [load for minute, load in bins.items() if MORNING_START <= minute < MORNING_END]
    if not morning:
        return 0.0
    return max(morning) / PLANE_LOAD


def hourly_forecast(rows):
    """Peak plane-loads during each hour from 04:00 through 22:00."""
    bins, saw_time = crowd_bins(rows, skip_tomorrow=False)
    if not saw_time:
        return []
    hours = []
    for hour in range(4, 23):
        window = [bins.get(minute, 0) for minute in range(hour * 60, (hour + 1) * 60, BIN_MINUTES)]
        peak = (max(window) / PLANE_LOAD) if window else 0.0
        hours.append((f'{hour:02d}:00', round(peak, 1), crowd_label(peak)))
    return hours
