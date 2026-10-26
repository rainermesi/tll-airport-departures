# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

I created this repo to:
- Test how to use Mermaid charting functions for basic reporting
- Test how to use Github Actions for scheudling basic data pipelines and transformations
- Find out where we can fly to from Tallinn

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
---
xyChart:
    xAxis:
      labelFontSize: 8
---
xychart-beta
    title "Departures by day"
    x-axis ["2026-07-28", "2026-07-29", "2026-07-30", "2026-07-31", "2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04", "2026-08-05", "2026-08-06", "2026-08-07", "2026-08-08", "2026-08-09", "2026-08-10", "2026-08-11", "2026-08-12", "2026-08-13", "2026-08-14", "2026-08-15", "2026-08-16", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20", "2026-08-21", "2026-08-22", "2026-08-23", "2026-08-24", "2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28", "2026-08-29", "2026-08-30", "2026-08-31", "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05", "2026-09-06", "2026-09-07", "2026-09-08", "2026-09-09", "2026-09-10", "2026-09-11", "2026-09-12", "2026-09-13", "2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20", "2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25", "2026-09-26", "2026-09-27", "2026-09-28", "2026-09-29", "2026-09-30", "2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04", "2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15", "2026-10-16", "2026-10-17", "2026-10-18", "2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25"]
    y-axis "# departures" 0 --> 69
    bar [45, 53, 57, 60, 42, 56, 55, 44, 50, 51, 62, 45, 57, 58, 43, 53, 54, 61, 48, 57, 60, 46, 54, 55, 60, 43, 58, 58, 48, 54, 33, 32, 34, 52, 54, 45, 54, 49, 62, 42, 56, 57, 48, 53, 52, 61, 44, 54, 56, 47, 51, 52, 59, 43, 52, 55, 46, 51, 53, 57, 40, 48, 54, 42, 46, 52, 54, 40, 48, 50, 36, 45, 46, 53, 35, 49, 50, 34, 46, 52, 58, 44, 55, 56, 46, 48, 52, 57, 46, 50]
    line [21, 25, 26, 30, 21, 29, 27, 20, 26, 23, 31, 23, 30, 27, 20, 24, 22, 29, 23, 28, 28, 20, 24, 23, 30, 22, 29, 27, 20, 24, 17, 18, 18, 26, 26, 20, 24, 22, 29, 20, 26, 26, 20, 23, 22, 29, 21, 26, 27, 21, 23, 24, 28, 21, 27, 27, 21, 21, 23, 29, 20, 26, 28, 20, 22, 25, 29, 19, 28, 27, 17, 21, 22, 27, 19, 27, 27, 18, 20, 23, 29, 21, 27, 27, 22, 21, 23, 29, 22, 25]
```


## Unique destinations and departures

All destinations flown to from Tallinn. More departures = bigger node.
Note that umlauts don't seem to be supported in Mermaid Sankey Diagrams (experimental diagram).

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
Tallinn,"Bahrain,Hambantota",1
Tallinn,Barcelona,377
Tallinn,Berliin,654
Tallinn,Bern,1
Tallinn,Billund,113
Tallinn,"Billund,Pariis (Charles De Gaulle)",1
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
Tallinn,"Faro,Faro",1
Tallinn,Fort Worth,1
Tallinn,Frankfurt,1935
Tallinn,Funchal,35
Tallinn,Gdańsk,123
Tallinn,Genf,26
Tallinn,Gran Canaria,60
Tallinn,Goteborg,3
Tallinn,Hamburg,47
Tallinn,Helsingi,6803
Tallinn,Heraklion,246
Tallinn,Hurghada,176
Tallinn,Istanbul,934
Tallinn,Istres Le TubeIstres Air Base,2
Tallinn,Kalamata,1
Tallinn,Katowice,1
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,1665
Tallinn,Kosice,1
Tallinn,Kraków,202
Tallinn,Kuressaare,1261
Tallinn,Kardla,1287
Tallinn,"Kardla,Kuressaare",3
Tallinn,La Rioja,1
Tallinn,Lamezia,11
Tallinn,"Lamezia,Catania",3
Tallinn,Larnaca,15
Tallinn,León,2
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
Tallinn,"Riia,Barcelona",1
Tallinn,Rooma (Ciampino),80
Tallinn,Rooma (Fiumicino),88
Tallinn,Rzeszów–Jasionka,1
Tallinn,Salzburg,27
Tallinn,Sharm El Sheikh,264
Tallinn,Split,98
Tallinn,Stockholm (Arlanda),3228
Tallinn,"Stockholm (Arlanda),Pariis (Charles De Gaulle)",2
Tallinn,Stockholm (Bromma),1
Tallinn,"Szczecin-Goleniów ""Solidarność",1
Tallinn,Tallinn,4
Tallinn,Tampere,17
Tallinn,"Tampere,Kittila",21
Tallinn,Tbilisi,1
Tallinn,Tel Aviv,2
Tallinn,Tenerife (South),129
Tallinn,Tirana,119
Tallinn,Tivat,115
Tallinn,Trieste,1
Tallinn,"Trieste,Rooma (Fiumicino)",1
Tallinn,Tromsø,2
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
