# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Flights in the terminal

| Hour | 16 Nov | Flights | | 17 Nov | Flights |
| --- | --- | ---: | --- | --- | ---: |
| 04:00 | 16 Nov | 5 | | 17 Nov | 7 |
| 05:00 | 16 Nov | 8 | | 17 Nov | 12 |
| 06:00 | 16 Nov | 7 | | 17 Nov | 11 |
| 07:00 | 16 Nov | 6 | | 17 Nov | 10 |
| 08:00 | 16 Nov | 7 | | 17 Nov | 8 |
| 09:00 | 16 Nov | 11 | | 17 Nov | 9 |
| 10:00 | 16 Nov | 10 | | 17 Nov | 7 |
| 11:00 | 16 Nov | 10 | | 17 Nov | 7 |
| 12:00 | 16 Nov | 8 | | 17 Nov | 8 |
| 13:00 | 16 Nov | 10 | | 17 Nov | 9 |
| 14:00 | 16 Nov | 8 | | 17 Nov | 8 |
| 15:00 | 16 Nov | 10 | | 17 Nov | 8 |
| 16:00 | 16 Nov | 13 | | 17 Nov | 10 |
| 17:00 | 16 Nov | 9 | | 17 Nov | 7 |
| 18:00 | 16 Nov | 6 | | 17 Nov | 5 |
| 19:00 | 16 Nov | 4 | | 17 Nov | 4 |
| 20:00 | 16 Nov | 6 | | 17 Nov | 5 |
| 21:00 | 16 Nov | 7 | | 17 Nov | 6 |
| 22:00 | 16 Nov | 4 | | 17 Nov | 3 |

Each flight is counted in the two hours before it leaves.

## When the terminal is busiest

Averages from 1 Aug 2024 through 16 Nov 2026, 771 days. Weekday and month numbers are the average of that day’s busiest hour.

05:00 is the busiest hour (10.1 flights). 22:00 is the quietest (1.9).
Friday is the busiest weekday (13.2). Saturday is the quietest (10.2).
September is the busiest month (12.7). January is the quietest (10.8).

| Hour | Avg flights | | Weekday | Avg peak | | Month | Avg peak |
| --- | ---: | --- | --- | ---: | --- | --- | ---: |
| 04:00 | 5.6 | | Monday | 12.4 | | January | 10.8 |
| 05:00 | 10.1 | | Tuesday | 12.0 | | February | 11.1 |
| 06:00 | 9.1 | | Wednesday | 11.5 | | March | 11.5 |
| 07:00 | 7.7 | | Thursday | 11.8 | | April | 11.6 |
| 08:00 | 5.2 | | Friday | 13.2 | | May | 11.9 |
| 09:00 | 5.6 | | Saturday | 10.2 | | June | 12.1 |
| 10:00 | 5.9 | | Sunday | 11.4 | | July | 12.1 |
| 11:00 | 5.3 | |  |  | | August | 12.5 |
| 12:00 | 7.4 | |  |  | | September | 12.7 |
| 13:00 | 8.2 | |  |  | | October | 12.1 |
| 14:00 | 8.9 | |  |  | | November | 11.2 |
| 15:00 | 8.8 | |  |  | | December | 11.1 |
| 16:00 | 9.3 | |  |  | |  |  |
| 17:00 | 7.0 | |  |  | |  |  |
| 18:00 | 6.1 | |  |  | |  |  |
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
    x-axis ["15.08", " ", " ", " ", " ", " ", " ", "22.08", " ", " ", " ", " ", " ", " ", "29.08", " ", " ", " ", " ", " ", " ", "05.09", " ", " ", " ", " ", " ", " ", "12.09", " ", " ", " ", " ", " ", " ", "19.09", " ", " ", " ", " ", " ", " ", "26.09", " ", " ", " ", " ", " ", " ", "03.10", " ", " ", " ", " ", " ", " ", "10.10", " ", " ", " ", " ", " ", " ", "17.10", " ", " ", " ", " ", " ", " ", "24.10", " ", " ", " ", " ", " ", " ", "01.11", " ", " ", " ", " ", " ", " ", "09.11", " ", " ", " ", " ", "16.11"]
    y-axis "# departures" 0 --> 69
    bar [48, 57, 60, 46, 54, 55, 60, 43, 58, 58, 48, 54, 33, 32, 34, 52, 54, 45, 54, 49, 62, 42, 56, 57, 48, 53, 52, 61, 44, 54, 56, 47, 51, 52, 59, 43, 52, 55, 46, 51, 53, 57, 40, 48, 54, 42, 46, 52, 54, 40, 48, 50, 36, 45, 46, 53, 35, 49, 50, 34, 46, 52, 58, 44, 55, 56, 46, 48, 52, 57, 46, 50, 46, 51, 27, 49, 49, 50, 44, 20, 43, 24, 45, 47, 38, 20, 23, 41, 22, 37]
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
    bar [51.9, 43.6, 40.5, 49.4, 48.6, 46.7, 44.3, 50.0, 51.4, 43.7]
    line [26.6, 22.5, 21.3, 23.1, 23.1, 22.1, 20.9, 23.4, 24.5, 22.4]
```

## Unique destinations and departures

Departures to each city since 1 Aug 2024. Airports in the same city are counted together. A multi-stop flight is counted once for each city on the title. The rates are averages over that whole span, and a longer bar means more departures.

```
Helsingi                         6937   8.3/day   58.0/wk   252.3/mo  3027.2/yr  ████████████████████████
Stockholm                        3283   3.9/day   27.5/wk   119.4/mo  1432.6/yr  ███████████
Riia                             3149   3.8/day   26.3/wk   114.5/mo  1374.2/yr  ███████████
Varssavi                         2578   3.1/day   21.6/wk    93.7/mo  1125.0/yr  █████████
Frankfurt                        1969   2.4/day   16.5/wk    71.6/mo   859.2/yr  ███████
Kopenhaagen                      1697   2.0/day   14.2/wk    61.7/mo   740.5/yr  ██████
Amsterdam                        1347   1.6/day   11.3/wk    49.0/mo   587.8/yr  █████
Kardla                           1313   1.6/day   11.0/wk    47.7/mo   573.0/yr  █████
London                           1303   1.6/day   10.9/wk    47.4/mo   568.6/yr  █████
Kuressaare                       1287   1.5/day   10.8/wk    46.8/mo   561.6/yr  ████
Vilnius                          1175   1.4/day    9.8/wk    42.7/mo   512.7/yr  ████
Istanbul                          956   1.1/day    8.0/wk    34.8/mo   417.2/yr  ███
Antalya                           812   1.0/day    6.8/wk    29.5/mo   354.3/yr  ███
Munchen                           662   0.8/day    5.5/wk    24.1/mo   288.9/yr  ██
Berliin                           658   0.8/day    5.5/wk    23.9/mo   287.1/yr  ██
Oslo                              614   0.7/day    5.1/wk    22.3/mo   267.9/yr  ██
Pariis                            584   0.7/day    4.9/wk    21.2/mo   254.8/yr  ██
Zurich                            498   0.6/day    4.2/wk    18.1/mo   217.3/yr  ██
Brussel                           464   0.6/day    3.9/wk    16.9/mo   202.5/yr  ██
Milano                            391   0.5/day    3.3/wk    14.2/mo   170.6/yr  █
Barcelona                         386   0.5/day    3.2/wk    14.0/mo   168.4/yr  █
Malaga                            283   0.3/day    2.4/wk    10.3/mo   123.5/yr  █
Sharm El Sheikh                   274   0.3/day    2.3/wk    10.0/mo   119.6/yr  █
Heraklion                         246   0.3/day    2.1/wk     8.9/mo   107.3/yr  █
Dublin                            228   0.3/day    1.9/wk     8.3/mo    99.5/yr  █
Krakow                            219   0.3/day    1.8/wk     8.0/mo    95.6/yr  █
Viin                              196   0.2/day    1.6/wk     7.1/mo    85.5/yr  █
Budapest                          186   0.2/day    1.6/wk     6.8/mo    81.2/yr  █
Hurghada                          184   0.2/day    1.5/wk     6.7/mo    80.3/yr  █
Rooma                             174   0.2/day    1.5/wk     6.3/mo    75.9/yr  █
Praha                             155   0.2/day    1.3/wk     5.6/mo    67.6/yr  █
Nice                              154   0.2/day    1.3/wk     5.6/mo    67.2/yr  █
Tenerife                          133   0.2/day    1.1/wk     4.8/mo    58.0/yr  █
Gdansk                            130   0.2/day    1.1/wk     4.7/mo    56.7/yr  █
Tirana                            119   0.1/day    1.0/wk     4.3/mo    51.9/yr  █
Rhodos                            119   0.1/day    1.0/wk     4.3/mo    51.9/yr  █
Tivat                             115   0.1/day    1.0/wk     4.2/mo    50.2/yr  █
Billund                           114   0.1/day    1.0/wk     4.1/mo    49.7/yr  █
Burgas                            104   0.1/day    0.9/wk     3.8/mo    45.4/yr  █
Split                              98   0.1/day    0.8/wk     3.6/mo    42.8/yr  █
Veneetsia                          96   0.1/day    0.8/wk     3.5/mo    41.9/yr  █
Malta                              78   0.1/day    0.7/wk     2.8/mo    34.0/yr  █
Veneetsia-Treviso                  67   0.1/day    0.6/wk     2.4/mo    29.2/yr  █
Paphos                             66   0.1/day    0.6/wk     2.4/mo    28.8/yr  █
Palma De Mallorca                  65   0.1/day    0.5/wk     2.4/mo    28.4/yr  █
Gran Canaria                       60   0.1/day    0.5/wk     2.2/mo    26.2/yr  █
Dusseldorf                         56   0.1/day    0.5/wk     2.0/mo    24.4/yr  █
Hamburg                            47   0.1/day    0.4/wk     1.7/mo    20.5/yr  █
Tampere                            38   0.0/day    0.3/wk     1.4/mo    16.6/yr  █
Funchal                            37   0.0/day    0.3/wk     1.3/mo    16.1/yr  █
Enfidha                            35   0.0/day    0.3/wk     1.3/mo    15.3/yr  █
Salzburg                           27   0.0/day    0.2/wk     1.0/mo    11.8/yr  █
Genf                               26   0.0/day    0.2/wk     0.9/mo    11.3/yr  █
Kittila                            21   0.0/day    0.2/wk     0.8/mo     9.2/yr  █
Dubrovnik                          21   0.0/day    0.2/wk     0.8/mo     9.2/yr  █
Reykjavik                          20   0.0/day    0.2/wk     0.7/mo     8.7/yr  █
Larnaca                            16   0.0/day    0.1/wk     0.6/mo     7.0/yr  █
Bodrum                             16   0.0/day    0.1/wk     0.6/mo     7.0/yr  █
Ateena                             16   0.0/day    0.1/wk     0.6/mo     7.0/yr  █
Lamezia                            14   0.0/day    0.1/wk     0.5/mo     6.1/yr  █
Manchester                         11   0.0/day    0.1/wk     0.4/mo     4.8/yr  █
Madriid                            10   0.0/day    0.1/wk     0.4/mo     4.4/yr  █
Birmingham                          8   0.0/day    0.1/wk     0.3/mo     3.5/yr  █
Edinburgh                           8   0.0/day    0.1/wk     0.3/mo     3.5/yr  █
Faro                                5   0.0/day    0.0/wk     0.2/mo     2.2/yr  █
Catania                             5   0.0/day    0.0/wk     0.2/mo     2.2/yr  █
Visby                               4   0.0/day    0.0/wk     0.1/mo     1.7/yr  █
Kerkira                             4   0.0/day    0.0/wk     0.1/mo     1.7/yr  █
Goteborg                            3   0.0/day    0.0/wk     0.1/mo     1.3/yr  █
Cagliari                            2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Linz                                2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Istres Le Tube Istres Air Base      2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Tel Aviv                            2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Leon                                2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Bratislava                          2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Trieste                             2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Tromso                              2   0.0/day    0.0/wk     0.1/mo     0.9/yr  █
Trondheim                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Szczecin-Goleniow Solidarnosc       1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bern                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Verona                              1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Fort Worth                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pardubice                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
RzeszowJasionka                     1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Kosice                              1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Hambantota                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bahrain                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Liverpool                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Sofia                               1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pisa                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
La Rioja                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Bucharest                           1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Farnborough                         1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Pamplona                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Brno                                1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Tbilisi                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Kalamata                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Akureyri                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Luxembourg                          1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Katowice                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Malmo                               1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Craiova                             1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
Debrecen                            1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
RAF Brize Norton                    1   0.0/day    0.0/wk     0.0/mo     0.4/yr  █
```
