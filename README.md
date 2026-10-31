# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Flights in the terminal

| Hour | 31 Oct | Flights | | 1 Nov | Flights |
| --- | --- | ---: | --- | --- | ---: |
| 04:00 | 31 Oct | 8 | | 1 Nov | 7 |
| 05:00 | 31 Oct | 15 | | 1 Nov | 10 |
| 06:00 | 31 Oct | 15 | | 1 Nov | 9 |
| 07:00 | 31 Oct | 13 | | 1 Nov | 7 |
| 08:00 | 31 Oct | 9 | | 1 Nov | 10 |
| 09:00 | 31 Oct | 9 | | 1 Nov | 9 |
| 10:00 | 31 Oct | 7 | | 1 Nov | 7 |
| 11:00 | 31 Oct | 8 | | 1 Nov | 3 |
| 12:00 | 31 Oct | 8 | | 1 Nov | 5 |
| 13:00 | 31 Oct | 12 | | 1 Nov | 9 |
| 14:00 | 31 Oct | 10 | | 1 Nov | 10 |
| 15:00 | 31 Oct | 9 | | 1 Nov | 8 |
| 16:00 | 31 Oct | 9 | | 1 Nov | 6 |
| 17:00 | 31 Oct | 6 | | 1 Nov | 4 |
| 18:00 | 31 Oct | 5 | | 1 Nov | 2 |
| 19:00 | 31 Oct | 5 | | 1 Nov | 1 |
| 20:00 | 31 Oct | 6 | | 1 Nov | 3 |
| 21:00 | 31 Oct | 5 | | 1 Nov | 3 |
| 22:00 | 31 Oct | 2 | | 1 Nov | 2 |

Each flight is counted in the two hours before it leaves.

## When the terminal is busiest

Averages from 1 Aug 2024 through 31 Oct 2026, 758 days. Weekday and month numbers are the average of that day’s busiest hour.

05:00 is the busiest hour (10.3 flights). 22:00 is the quietest (1.9).
Friday is the busiest weekday (13.2). Saturday is the quietest (10.2).
September is the busiest month (12.7). January is the quietest (10.8).

| Hour | Avg flights | | Weekday | Avg peak | | Month | Avg peak |
| --- | ---: | --- | --- | ---: | --- | --- | ---: |
| 04:00 | 5.7 | | Monday | 12.4 | | January | 10.8 |
| 05:00 | 10.3 | | Tuesday | 12.0 | | February | 11.1 |
| 06:00 | 9.2 | | Wednesday | 11.5 | | March | 11.5 |
| 07:00 | 7.8 | | Thursday | 11.9 | | April | 11.6 |
| 08:00 | 5.2 | | Friday | 13.2 | | May | 11.9 |
| 09:00 | 5.6 | | Saturday | 10.2 | | June | 12.1 |
| 10:00 | 6.0 | | Sunday | 11.4 | | July | 12.1 |
| 11:00 | 5.4 | |  |  | | August | 12.5 |
| 12:00 | 7.5 | |  |  | | September | 12.7 |
| 13:00 | 8.2 | |  |  | | October | 12.2 |
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
    x-axis ["02.08", " ", " ", " ", " ", " ", " ", "09.08", " ", " ", " ", " ", " ", " ", "16.08", " ", " ", " ", " ", " ", " ", "23.08", " ", " ", " ", " ", " ", " ", "30.08", " ", " ", " ", " ", " ", " ", "06.09", " ", " ", " ", " ", " ", " ", "13.09", " ", " ", " ", " ", " ", " ", "20.09", " ", " ", " ", " ", " ", " ", "27.09", " ", " ", " ", " ", " ", " ", "04.10", " ", " ", " ", " ", " ", " ", "11.10", " ", " ", " ", " ", " ", " ", "18.10", " ", " ", " ", " ", " ", " ", "25.10", " ", " ", " ", " ", "31.10"]
    y-axis "# departures" 0 --> 69
    bar [56, 55, 44, 50, 51, 62, 45, 57, 58, 43, 53, 54, 61, 48, 57, 60, 46, 54, 55, 60, 43, 58, 58, 48, 54, 33, 32, 34, 52, 54, 45, 54, 49, 62, 42, 56, 57, 48, 53, 52, 61, 44, 54, 56, 47, 51, 52, 59, 43, 52, 55, 46, 51, 53, 57, 40, 48, 54, 42, 46, 52, 54, 40, 48, 50, 36, 45, 46, 53, 35, 49, 50, 34, 46, 52, 58, 44, 55, 56, 46, 48, 52, 57, 46, 50, 46, 51, 27, 49, 25]
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
    bar [51.9, 43.6, 40.5, 49.4, 48.6, 46.7, 44.3, 50.0, 51.4, 46.7]
    line [26.6, 22.5, 21.3, 23.1, 23.1, 22.1, 20.9, 23.4, 24.5, 23.4]
```

## Unique destinations and departures

Departures to each city since 1 Aug 2024. Airports in the same city are counted together. A multi-stop flight is counted once for each city on the title. The rates are averages over that whole span, and a longer bar means more departures.

```
Helsingi                         6840   8.3/day   58.3/wk   253.6/mo  3043.0/yr  ████████████████████████
Stockholm                        3247   4.0/day   27.7/wk   120.4/mo  1444.5/yr  ███████████
Riia                             3117   3.8/day   26.6/wk   115.6/mo  1386.7/yr  ███████████
Varssavi                         2536   3.1/day   21.6/wk    94.0/mo  1128.2/yr  █████████
Frankfurt                        1945   2.4/day   16.6/wk    72.1/mo   865.3/yr  ███████
Kopenhaagen                      1674   2.0/day   14.3/wk    62.1/mo   744.7/yr  ██████
Amsterdam                        1334   1.6/day   11.4/wk    49.5/mo   593.5/yr  █████
Kardla                           1298   1.6/day   11.1/wk    48.1/mo   577.5/yr  █████
London                           1288   1.6/day   11.0/wk    47.8/mo   573.0/yr  █████
Kuressaare                       1272   1.5/day   10.8/wk    47.2/mo   565.9/yr  ████
Vilnius                          1157   1.4/day    9.9/wk    42.9/mo   514.7/yr  ████
Istanbul                          940   1.1/day    8.0/wk    34.8/mo   418.2/yr  ███
Antalya                           794   1.0/day    6.8/wk    29.4/mo   353.2/yr  ███
Berliin                           658   0.8/day    5.6/wk    24.4/mo   292.7/yr  ██
Munchen                           657   0.8/day    5.6/wk    24.4/mo   292.3/yr  ██
Oslo                              608   0.7/day    5.2/wk    22.5/mo   270.5/yr  ██
Pariis                            578   0.7/day    4.9/wk    21.4/mo   257.1/yr  ██
Zurich                            495   0.6/day    4.2/wk    18.4/mo   220.2/yr  ██
Brussel                           456   0.6/day    3.9/wk    16.9/mo   202.9/yr  ██
Milano                            385   0.5/day    3.3/wk    14.3/mo   171.3/yr  █
Barcelona                         380   0.5/day    3.2/wk    14.1/mo   169.1/yr  █
Malaga                            277   0.3/day    2.4/wk    10.3/mo   123.2/yr  █
Sharm El Sheikh                   265   0.3/day    2.3/wk     9.8/mo   117.9/yr  █
Heraklion                         246   0.3/day    2.1/wk     9.1/mo   109.4/yr  █
Dublin                            220   0.3/day    1.9/wk     8.2/mo    97.9/yr  █
Krakow                            205   0.2/day    1.7/wk     7.6/mo    91.2/yr  █
Viin                              194   0.2/day    1.7/wk     7.2/mo    86.3/yr  █
Hurghada                          179   0.2/day    1.5/wk     6.6/mo    79.6/yr  █
Budapest                          178   0.2/day    1.5/wk     6.6/mo    79.2/yr  █
Rooma                             171   0.2/day    1.5/wk     6.3/mo    76.1/yr  █
Praha                             155   0.2/day    1.3/wk     5.7/mo    69.0/yr  █
Nice                              152   0.2/day    1.3/wk     5.6/mo    67.6/yr  █
Tenerife                          132   0.2/day    1.1/wk     4.9/mo    58.7/yr  █
Gdansk                            125   0.2/day    1.1/wk     4.6/mo    55.6/yr  █
Tirana                            119   0.1/day    1.0/wk     4.4/mo    52.9/yr  █
Rhodos                            119   0.1/day    1.0/wk     4.4/mo    52.9/yr  █
Tivat                             115   0.1/day    1.0/wk     4.3/mo    51.2/yr  █
Billund                           114   0.1/day    1.0/wk     4.2/mo    50.7/yr  █
Burgas                            104   0.1/day    0.9/wk     3.9/mo    46.3/yr  █
Split                              98   0.1/day    0.8/wk     3.6/mo    43.6/yr  █
Veneetsia                          93   0.1/day    0.8/wk     3.4/mo    41.4/yr  █
Malta                              76   0.1/day    0.6/wk     2.8/mo    33.8/yr  █
Veneetsia-Treviso                  67   0.1/day    0.6/wk     2.5/mo    29.8/yr  █
Paphos                             66   0.1/day    0.6/wk     2.4/mo    29.4/yr  █
Palma De Mallorca                  65   0.1/day    0.6/wk     2.4/mo    28.9/yr  █
Gran Canaria                       60   0.1/day    0.5/wk     2.2/mo    26.7/yr  █
Dusseldorf                         53   0.1/day    0.5/wk     2.0/mo    23.6/yr  █
Hamburg                            47   0.1/day    0.4/wk     1.7/mo    20.9/yr  █
Tampere                            38   0.0/day    0.3/wk     1.4/mo    16.9/yr  █
Enfidha                            35   0.0/day    0.3/wk     1.3/mo    15.6/yr  █
Funchal                            35   0.0/day    0.3/wk     1.3/mo    15.6/yr  █
Salzburg                           27   0.0/day    0.2/wk     1.0/mo    12.0/yr  █
Genf                               26   0.0/day    0.2/wk     1.0/mo    11.6/yr  █
Dubrovnik                          21   0.0/day    0.2/wk     0.8/mo     9.3/yr  █
Kittila                            21   0.0/day    0.2/wk     0.8/mo     9.3/yr  █
Reykjavik                          20   0.0/day    0.2/wk     0.7/mo     8.9/yr  █
Bodrum                             16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Larnaca                            16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Ateena                             16   0.0/day    0.1/wk     0.6/mo     7.1/yr  █
Lamezia                            14   0.0/day    0.1/wk     0.5/mo     6.2/yr  █
Manchester                         11   0.0/day    0.1/wk     0.4/mo     4.9/yr  █
Madriid                            10   0.0/day    0.1/wk     0.4/mo     4.4/yr  █
Edinburgh                           8   0.0/day    0.1/wk     0.3/mo     3.6/yr  █
Birmingham                          8   0.0/day    0.1/wk     0.3/mo     3.6/yr  █
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
