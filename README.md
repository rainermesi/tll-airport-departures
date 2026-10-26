# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

I created this repo to:
- Test how to use Mermaid charting functions for basic reporting
- Test how to use Github Actions for scheudling basic data pipelines and transformations
- Find out where we can fly to from Tallinn

## Trend of Daily Departures

Last 90 days. Bars for total number of departures. Line for unique destinations.

```mermaid
---
xyChart:
    xAxis:
      labelFontSize: 8
---
xychart-beta
    title "Departures by day"
    x-axis ["28.07", " ", " ", " ", " ", " ", " ", "04.08", " ", " ", " ", " ", " ", " ", "11.08", " ", " ", " ", " ", " ", " ", "18.08", " ", " ", " ", " ", " ", " ", "25.08", " ", " ", " ", " ", " ", " ", "01.09", " ", " ", " ", " ", " ", " ", "08.09", " ", " ", " ", " ", " ", " ", "15.09", " ", " ", " ", " ", " ", " ", "22.09", " ", " ", " ", " ", " ", " ", "29.09", " ", " ", " ", " ", " ", " ", "06.10", " ", " ", " ", " ", " ", " ", "13.10", " ", " ", " ", " ", " ", " ", "20.10", " ", " ", " ", " ", "25.10"]
    y-axis "# departures" 0 --> 69
    bar [45, 53, 57, 60, 42, 56, 55, 44, 50, 51, 62, 45, 57, 58, 43, 53, 54, 61, 48, 57, 60, 46, 54, 55, 60, 43, 58, 58, 48, 54, 33, 32, 34, 52, 54, 45, 54, 49, 62, 42, 56, 57, 48, 53, 52, 61, 44, 54, 56, 47, 51, 52, 59, 43, 52, 55, 46, 51, 53, 57, 40, 48, 54, 42, 46, 52, 54, 40, 48, 50, 36, 45, 46, 53, 35, 49, 50, 34, 46, 52, 58, 44, 55, 56, 46, 48, 52, 57, 46, 50]
    line [21, 25, 26, 30, 21, 29, 27, 20, 26, 23, 31, 23, 30, 27, 20, 24, 22, 29, 23, 28, 28, 20, 24, 23, 30, 22, 29, 27, 20, 24, 17, 18, 18, 26, 26, 20, 24, 22, 29, 20, 26, 26, 20, 23, 22, 29, 21, 26, 27, 21, 23, 24, 28, 21, 27, 27, 21, 21, 23, 29, 20, 26, 28, 20, 22, 25, 29, 19, 28, 27, 17, 21, 22, 27, 19, 27, 27, 18, 20, 23, 29, 21, 27, 27, 22, 21, 23, 29, 22, 25]
```

## Departures by quarter

Full history. Bars are the average departures per day. The line is the average number of destinations per day.

```mermaid
---
xyChart:
    xAxis:
      labelFontSize: 12
---
xychart-beta
    title "Departures by quarter"
    x-axis ["2024 Q3", "2024 Q4", "2025 Q1", "2025 Q2", "2025 Q3", "2025 Q4", "2026 Q1", "2026 Q2", "2026 Q3", "2026 Q4"]
    y-axis "per day" 0 --> 58
    bar [51.9, 43.6, 40.5, 49.4, 48.6, 46.7, 44.3, 50.0, 51.4, 48.1]
    line [26.6, 22.5, 21.3, 23.1, 23.1, 22.1, 20.9, 23.4, 24.5, 23.8]
```

## Passengers in the terminal

Hour-by-hour forecast. Quiet, steady, busy, or crowded. Each flight is spread across the two hours before departure, and holiday flights count for more.

**2026-10-25**

| Hour | Terminal |
| --- | --- |
| 04:00 | busy |
| 05:00 | busy |
| 06:00 | steady |
| 07:00 | quiet |
| 08:00 | quiet |
| 09:00 | quiet |
| 10:00 | quiet |
| 11:00 | steady |
| 12:00 | steady |
| 13:00 | steady |
| 14:00 | steady |
| 15:00 | steady |
| 16:00 | steady |
| 17:00 | quiet |
| 18:00 | quiet |
| 19:00 | quiet |
| 20:00 | quiet |
| 21:00 | quiet |
| 22:00 | quiet |

## Unique destinations and departures

All destinations flown to from Tallinn. More departures = bigger node.

```mermaid
---
config:
  sankey:
    showValues: false
    width: 800
    height: 1000
---
sankey-beta
%% source,target,value
Tallinn,Akureyri,1
Tallinn,Amsterdam,1326
Tallinn,Antalya,781
Tallinn,Ateena,16
Tallinn,Bahrain Hambantota,1
Tallinn,Barcelona,377
Tallinn,Berliin,654
Tallinn,Bern,1
Tallinn,Billund,113
Tallinn,Billund Pariis (Charles De Gaulle),1
Tallinn,Birmingham,8
Tallinn,Bodrum,16
Tallinn,Bratislava,2
Tallinn,Brno,1
Tallinn,Brussel,454
Tallinn,Bucharest,1
Tallinn,Budapest,175
Tallinn,Burgas,104
Tallinn,Cagliari,2
Tallinn,Catania,2
Tallinn,Craiova,1
Tallinn,Debrecen,1
Tallinn,Dublin,219
Tallinn,Dubrovnik,21
Tallinn,Dusseldorf,51
Tallinn,Edinburgh,8
Tallinn,Enfidha,35
Tallinn,Farnborough,1
Tallinn,Faro,4
Tallinn,Faro Faro,1
Tallinn,Fort Worth,1
Tallinn,Frankfurt,1935
Tallinn,Funchal,35
Tallinn,Gdansk,123
Tallinn,Genf,26
Tallinn,Gran Canaria,60
Tallinn,Goteborg,3
Tallinn,Hamburg,47
Tallinn,Helsingi,6803
Tallinn,Heraklion,246
Tallinn,Hurghada,176
Tallinn,Istanbul,934
Tallinn,Istres Le Tube Istres Air Base,2
Tallinn,Kalamata,1
Tallinn,Katowice,1
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,1665
Tallinn,Kosice,1
Tallinn,Krakow,202
Tallinn,Kuressaare,1261
Tallinn,Kardla,1287
Tallinn,Kardla Kuressaare,3
Tallinn,La Rioja,1
Tallinn,Lamezia,11
Tallinn,Lamezia Catania,3
Tallinn,Larnaca,15
Tallinn,Leon,2
Tallinn,Linz,2
Tallinn,Liverpool,1
Tallinn,London (Gatwick),331
Tallinn,London (Luton),409
Tallinn,London (Stansted),542
Tallinn,Luxembourg,1
Tallinn,Madriid,10
Tallinn,Malaga,276
Tallinn,Malmo,1
Tallinn,Malta,76
Tallinn,Manchester,11
Tallinn,Milano (Bergamo),132
Tallinn,Milano (Malpensa),251
Tallinn,Munchen,656
Tallinn,Nice,150
Tallinn,Oslo,605
Tallinn,Palma De Mallorca,65
Tallinn,Pamplona,1
Tallinn,Paphos,66
Tallinn,Pardubice,1
Tallinn,Pariis (Charles De Gaulle),499
Tallinn,Pariis (Orly),72
Tallinn,Pisa,1
Tallinn,Praha,155
Tallinn,RAF Brize Norton,1
Tallinn,Reykjavik,20
Tallinn,Rhodos,119
Tallinn,Riia,3103
Tallinn,Riia Barcelona,1
Tallinn,Rooma (Ciampino),80
Tallinn,Rooma (Fiumicino),88
Tallinn,RzeszowJasionka,1
Tallinn,Salzburg,27
Tallinn,Sharm El Sheikh,264
Tallinn,Split,98
Tallinn,Stockholm (Arlanda),3228
Tallinn,Stockholm (Arlanda) Pariis (Charles De Gaulle),2
Tallinn,Stockholm (Bromma),1
Tallinn,Szczecin-Goleniow Solidarnosc,1
Tallinn,Tallinn,4
Tallinn,Tampere,17
Tallinn,Tampere Kittila,21
Tallinn,Tbilisi,1
Tallinn,Tel Aviv,2
Tallinn,Tenerife (South),129
Tallinn,Tirana,119
Tallinn,Tivat,115
Tallinn,Trieste,1
Tallinn,Trieste Rooma (Fiumicino),1
Tallinn,Tromso,2
Tallinn,Trondheim,1
Tallinn,Varssavi,2522
Tallinn,Veneetsia,93
Tallinn,Veneetsia-Treviso,67
Tallinn,Verona,1
Tallinn,Viin,193
Tallinn,Vilnius,1150
Tallinn,Visby,4
Tallinn,Zurich,495


```
