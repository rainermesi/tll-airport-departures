import re

# Qualifiers that mark a different airport in the same city. Other
# parenthetical or " - " suffixes are the same destination written twice.
DISTINCT_AIRPORTS = {
    'gatwick',
    'luton',
    'stansted',
    'bergamo',
    'malpensa',
    'charles de gaulle',
    'orly',
    'ciampino',
    'fiumicino',
    'arlanda',
    'bromma',
    'south',
    'treviso',
}

# The live board uses Estonian city names. Map the English duplicate onto that.
ALIASES = {
    'geneva': 'Genf',
    'genf': 'Genf',
}


def normalize_destination(name):
    if name is None:
        return 'N/A'
    text = str(name).strip()
    if not text or text == 'N/A':
        return 'N/A'
    parts = [_normalize_segment(part) for part in text.split(',')]
    return ','.join(part for part in parts if part)


def _normalize_segment(segment):
    name = re.sub(r'\s+', ' ', segment).strip()
    if ' - ' in name:
        city, airport = name.split(' - ', 1)
        if airport.strip().casefold() not in DISTINCT_AIRPORTS:
            name = city.strip()
    match = re.fullmatch(r'(.*?)\s*\(([^)]+)\)', name)
    if match and match.group(2).strip().casefold() not in DISTINCT_AIRPORTS:
        name = match.group(1).strip()
    return ALIASES.get(name.casefold(), name)
