# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Flights in the terminal

| Hour | 4 Nov | Flights | | 5 Nov | Flights |
| --- | --- | ---: | --- | --- | ---: |
| 04:00 | 4 Nov | 0 | | 5 Nov | 5 |
| 05:00 | 4 Nov | 0 | | 5 Nov | 11 |
| 06:00 | 4 Nov | 0 | | 5 Nov | 9 |
| 07:00 | 4 Nov | 0 | | 5 Nov | 6 |
| 08:00 | 4 Nov | 1 | | 5 Nov | 3 |
| 09:00 | 4 Nov | 2 | | 5 Nov | 5 |
| 10:00 | 4 Nov | 2 | | 5 Nov | 5 |
| 11:00 | 4 Nov | 1 | | 5 Nov | 5 |
| 12:00 | 4 Nov | 3 | | 5 Nov | 4 |
| 13:00 | 4 Nov | 5 | | 5 Nov | 6 |
| 14:00 | 4 Nov | 7 | | 5 Nov | 5 |
| 15:00 | 4 Nov | 7 | | 5 Nov | 6 |
| 16:00 | 4 Nov | 8 | | 5 Nov | 7 |
| 17:00 | 4 Nov | 5 | | 5 Nov | 5 |
| 18:00 | 4 Nov | 4 | | 5 Nov | 3 |
| 19:00 | 4 Nov | 4 | | 5 Nov | 4 |
| 20:00 | 4 Nov | 5 | | 5 Nov | 5 |
| 21:00 | 4 Nov | 4 | | 5 Nov | 4 |
| 22:00 | 4 Nov | 1 | | 5 Nov | 1 |

Each flight is counted in the two hours before it leaves.

## When the terminal is busiest

Averages from 1 Aug 2024 through 4 Nov 2026, 761 days. Weekday and month numbers are the average of that day’s busiest hour.

05:00 is the busiest hour (10.2 flights). 22:00 is the quietest (1.9).
Friday is the busiest weekday (13.2). Saturday is the quietest (10.2).
September is the busiest month (12.7). January is the quietest (10.8).

| Hour | Avg flights | | Weekday | Avg peak | | Month | Avg peak |
| --- | ---: | --- | --- | ---: | --- | --- | ---: |
| 04:00 | 5.7 | | Monday | 12.4 | | January | 10.8 |
| 05:00 | 10.2 | | Tuesday | 12.0 | | February | 11.1 |
| 06:00 | 9.2 | | Wednesday | 11.5 | | March | 11.5 |
| 07:00 | 7.7 | | Thursday | 11.8 | | April | 11.6 |
| 08:00 | 5.2 | | Friday | 13.2 | | May | 11.9 |
| 09:00 | 5.6 | | Saturday | 10.2 | | June | 12.1 |
| 10:00 | 6.0 | | Sunday | 11.5 | | July | 12.1 |
| 11:00 | 5.3 | |  |  | | August | 12.5 |
| 12:00 | 7.4 | |  |  | | September | 12.7 |
| 13:00 | 8.2 | |  |  | | October | 12.1 |
| 14:00 | 8.9 | |  |  | | November | 11.2 |
| 15:00 | 8.8 | |  |  | | December | 11.1 |
| 16:00 | 9.3 | |  |  | |  |  |
| 17:00 | 7.0 | |  |  | |  |  |
| 18:00 | 6.2 | |  |  | |  |  |
| 19:00 | 5.1 | |  |  | |  |  |
| 20:00 | 5.0 | |  |  | |  |  |
| 21:00 | 4.3 | |  |  | |  |  |
| 22:00 | 1.9 | |  |  | |  |  |

## Trend of Daily Departures

Last 90 days. One bar per day.

```mermaid
---
xyChart:
    xAxis:
      labelFontSize: 8
---
xychart-beta
    title "Departures by day"
    x-axis ["05.08", " ", " ", " ", " ", " ", " ", "12.08", " ", " ", " ", " ", " ", " ", "19.08", " ", " ", " ", " ", " ", " ", "26.08", " ", " ", " ", " ", " ", " ", "02.09", " ", " ", " ", " ", " ", " ", "09.09", " ", " ", " ", " ", " ", " ", "16.09", " ", " ", " ", " ", " ", " ", "23.09", " ", " ", " ", " ", " ", " ", "30.09", " ", " ", " ", " ", " ", " ", "07.10", " ", " ", " ", " ", " ", " ", "14.10", " ", " ", " ", " ", " ", " ", "21.10", " ", " ", " ", " ", " ", " ", "29.10", " ", " ", " ", " ", "04.11"]
    y-axis "# departures" 0 --> 69
    bar [50, 51, 62, 45, 57, 58, 43, 53, 54, 61, 48, 57, 60, 46, 54, 55, 60, 43, 58, 58, 48, 54, 33, 32, 34, 52, 54, 45, 54, 49, 62, 42, 56, 57, 48, 53, 52, 61, 44, 54, 56, 47, 51, 52, 59, 43, 52, 55, 46, 51, 53, 57, 40, 48, 54, 42, 46, 52, 54, 40, 48, 50, 36, 45, 46, 53, 35, 49, 50, 34, 46, 52, 58, 44, 55, 56, 46, 48, 52, 57, 46, 50, 46, 51, 27, 49, 49, 50, 44, 20]
```

## Departures by quarter

Full history. Bars are the average departures per day. The line is the average number of destinations per day.

```mermaid
---
config:
  xyChart:
    showDataLabel: true
    xAxis:
      labelFontSize: 12
---
xychart-beta
    title "Departures by quarter"
    x-axis ["2024 Q3", "2024 Q4", "2025 Q1", "2025 Q2", "2025 Q3", "2025 Q4", "2026 Q1", "2026 Q2", "2026 Q3", "2026 Q4"]
    y-axis "per day" 0 --> 58
    bar [51.9, 43.6, 40.5, 49.4, 48.6, 46.7, 44.3, 50.0, 51.4, 46.6]
    line [26.6, 22.5, 21.3, 23.1, 23.1, 22.1, 20.9, 23.4, 24.5, 23.4]
```

## Unique destinations and departures

Departures to each city since 1 Aug 2024. Airports in the same city are counted together. A multi-stop flight is counted once for each city on the title. The rates are averages over that whole span, and a longer bar means more departures.

```
Helsingi                         6867   8.3/day   58.3/wk   253.4/mo  3040.2/yr  ████████████████████████
Stockholm                        3257   3.9/day   27.6/wk   120.2/mo  1442.0/yr  ███████████
Riia                             3125   3.8/day   26.5/wk   115.3/mo  1383.5/yr  ███████████
Varssavi                         2546   3.1/day   21.6/wk    93.9/mo  1127.2/yr  █████████
Frankfurt                        1952   2.4/day   16.6/wk    72.0/mo   864.2/yr  ███████
Kopenhaagen                      1681   2.0/day   14.3/wk    62.0/mo   744.2/yr  ██████
Amsterdam                        1337   1.6/day   11.3/wk    49.3/mo   591.9/yr  █████
Kardla                           1302   1.6/day   11.0/wk    48.0/mo   576.4/yr  █████
London                           1291   1.6/day   11.0/wk    47.6/mo   571.6/yr  █████
Kuressaare                       1276   1.5/day   10.8/wk    47.1/mo   564.9/yr  ████
Vilnius                          1162   1.4/day    9.9/wk    42.9/mo   514.4/yr  ████
Istanbul                          945   1.1/day    8.0/wk    34.9/mo   418.4/yr  ███
Antalya                           800   1.0/day    6.8/wk    29.5/mo   354.2/yr  ███
Munchen                           660   0.8/day    5.6/wk    24.4/mo   292.2/yr  ██
Berliin                           658   0.8/day    5.6/wk    24.3/mo   291.3/yr  ██
Oslo                              610   0.7/day    5.2/wk    22.5/mo   270.1/yr  ██
Pariis                            580   0.7/day    4.9/wk    21.4/mo   256.8/yr  ██
Zurich                            495   0.6/day    4.2/wk    18.3/mo   219.2/yr  ██
Brussel                           458   0.6/day    3.9/wk    16.9/mo   202.8/yr  ██
Milano                            387   0.5/day    3.3/wk    14.3/mo   171.3/yr  █
Barcelona                         383   0.5/day    3.2/wk    14.1/mo   169.6/yr  █
Malaga                            279   0.3/day    2.4/wk    10.3/mo   123.5/yr  █
Sharm El Sheikh                   269   0.3/day    2.3/wk     9.9/mo   119.1/yr  █
Heraklion                         246   0.3/day    2.1/wk     9.1/mo   108.9/yr  █
Dublin                            222   0.3/day    1.9/wk     8.2/mo    98.3/yr  █
Krakow                            209   0.3/day    1.8/wk     7.7/mo    92.5/yr  █
Viin                              195   0.2/day    1.7/wk     7.2/mo    86.3/yr  █
Budapest                          180   0.2/day    1.5/wk     6.6/mo    79.7/yr  █
Hurghada                          179   0.2/day    1.5/wk     6.6/mo    79.2/yr  █
Rooma                             172   0.2/day    1.5/wk     6.3/mo    76.1/yr  █
Praha                             155   0.2/day    1.3/wk     5.7/mo    68.6/yr  █
Nice                              154   0.2/day    1.3/wk     5.7/mo    68.2/yr  █
Tenerife                          132   0.2/day    1.1/wk     4.9/mo    58.4/yr  █
Gdansk                            127   0.2/day    1.1/wk     4.7/mo    56.2/yr  █
Tirana                            119   0.1/day    1.0/wk     4.4/mo    52.7/yr  █
Rhodos                            119   0.1/day    1.0/wk     4.4/mo    52.7/yr  █
Tivat                             115   0.1/day    1.0/wk     4.2/mo    50.9/yr  █
Billund                           114   0.1/day    1.0/wk     4.2/mo    50.5/yr  █
Burgas                            104   0.1/day    0.9/wk     3.8/mo    46.0/yr  █
Split                              98   0.1/day    0.8/wk     3.6/mo    43.4/yr  █
Veneetsia                          94   0.1/day    0.8/wk     3.5/mo    41.6/yr  █
Malta                              78   0.1/day    0.7/wk     2.9/mo    34.5/yr  █
Veneetsia-Treviso                  67   0.1/day    0.6/wk     2.5/mo    29.7/yr  █
Paphos                             66   0.1/day    0.6/wk     2.4/mo    29.2/yr  █
Palma De Mallorca                  65   0.1/day    0.6/wk     2.4/mo    28.8/yr  █
Gran Canaria                       60   0.1/day    0.5/wk     2.2/mo    26.6/yr  █
Dusseldorf                         54   0.1/day    0.5/wk     2.0/mo    23.9/yr  █
Hamburg                            47   0.1/day    0.4/wk     1.7/mo    20.8/yr  █
Tampere                            38   0.0/day    0.3/wk     1.4/mo    16.8/yr  █
Funchal                            36   0.0/day    0.3/wk     1.3/mo    15.9/yr  █
Enfidha                            35   0.0/day    0.3/wk     1.3/mo    15.5/yr  █
Salzburg                           27   0.0/day    0.2/wk     1.0/mo    12.0/yr  █
Genf                               26   0.0/day    0.2/wk     1.0/mo    11.5/yr  █
Dubrovnik                          21   0.0/day    0.2/wk     0.8/mo     9.3/yr  █
Kittila                            21   0.0/day    0.2/wk     0.8/mo     9.3/yr  █
Reykjavik                          20   0.0/day    0.2/wk     0.7/mo     8.9/yr  █
Bodrum                             16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Larnaca                            16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Ateena                             16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Lamezia                            14   0.0/day    0.1/wk     0.5/mo     6.2/yr  █
Manchester                         11   0.0/day    0.1/wk     0.4/mo     4.9/yr  █
Madriid                            10   0.0/day    0.1/wk     0.4/mo     4.4/yr  █
Edinburgh                           8   0.0/day    0.1/wk     0.3/mo     3.5/yr  █
Birmingham                          8   0.0/day    0.1/wk     0.3/mo     3.5/yr  █
Catania                             5   0.0/day    0.0/wk     0.2/mo     2.2/yr  █
Faro                                5   0.0/day    0.0/wk     0.2/mo     2.2/yr  █
Kerkira                             4   0.0/day    0.0/wk     0.1/mo     1.8/yr  █
Visby                               4   0.0/day    0.0/wk     0.1/mo     1.8/yr  █
Goteborg                            3   0.0/day    0.0/wk     0.1/mo     1.3/yr  █
Cagliari                            2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Leon                                2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Tel Aviv                            2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Bratislava                          2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Istres Le Tube Istres Air Base      2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Linz                                2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Trieste                             2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Tromso                              2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Debrecen                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pisa                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Hambantota                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bahrain                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pamplona                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Szczecin-Goleniow Solidarnosc       1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Luxembourg                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Kosice                              1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Liverpool                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bucharest                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Farnborough                         1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Malmo                               1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
RzeszowJasionka                     1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Craiova                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
RAF Brize Norton                    1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Kalamata                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bern                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Akureyri                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Katowice                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Fort Worth                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Brno                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Tbilisi                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Verona                              1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pardubice                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
La Rioja                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Trondheim                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
```
