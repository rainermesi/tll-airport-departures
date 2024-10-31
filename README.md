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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10", "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14", "2024-09-15", "2024-09-16", "2024-09-17", "2024-09-18", "2024-09-19", "2024-09-20", "2024-09-21", "2024-09-22", "2024-09-23", "2024-09-24", "2024-09-25", "2024-09-26", "2024-09-27", "2024-09-28", "2024-09-29", "2024-09-30", "2024-10-01", "2024-10-02", "2024-10-03", "2024-10-04", "2024-10-05", "2024-10-06", "2024-10-07", "2024-10-08", "2024-10-09", "2024-10-10", "2024-10-11", "2024-10-12", "2024-10-13", "2024-10-14", "2024-10-15", "2024-10-16", "2024-10-17", "2024-10-18", "2024-10-19", "2024-10-20", "2024-10-21", "2024-10-22", "2024-10-23", "2024-10-24", "2024-10-25", "2024-10-26", "2024-10-27", "2024-10-28", "2024-10-29", "2024-10-30", "2024-10-31"]
    y-axis "# departures" 0 --> 66
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55, 47, 57, 56, 52, 45, 58, 55, 46, 58, 59, 54, 44, 60, 58, 49, 57, 59, 55, 45, 57, 57, 50, 57, 59, 53, 46, 58, 55, 49, 56, 60, 54, 45, 57, 58, 46, 56, 60, 54, 45, 56, 58, 47, 57, 60, 57, 42, 58, 58, 46, 56, 56, 54, 43, 47, 50, 45, 49, 45]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29, 20, 25, 28, 25, 23, 30, 29, 19, 26, 27, 25, 23, 29, 29, 20, 25, 28, 25, 23, 29, 30, 21, 25, 28, 24, 23, 29, 29, 22, 23, 28, 24, 22, 29, 31, 20, 24, 27, 24, 22, 28, 30, 20, 25, 27, 27, 20, 29, 30, 17, 24, 26, 26, 20, 24, 24, 18, 21, 20]
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
Tallinn,Amsterdam,93
Tallinn,Antalya,229
Tallinn,Ateena,16
Tallinn,"Bahrain,Hambantota",1
Tallinn,Barcelona,27
Tallinn,Berliin,100
Tallinn,Billund,49
Tallinn,Bodrum,11
Tallinn,Brussel,53
Tallinn,Burgas,21
Tallinn,Catania,2
Tallinn,Dublin,26
Tallinn,Dubrovnik,21
Tallinn,Enfidha,7
Tallinn,Faro,4
Tallinn,"Faro,Faro",1
Tallinn,Frankfurt,247
Tallinn,Funchal,2
Tallinn,Gran Canaria,2
Tallinn,Goteborg,1
Tallinn,Helsingi,874
Tallinn,Heraklion,46
Tallinn,Hurghada,4
Tallinn,Istanbul,96
Tallinn,Istres Le TubeIstres Air Base,2
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,101
Tallinn,Kosice,1
Tallinn,Kuressaare,157
Tallinn,Kardla,157
Tallinn,Lamezia,1
Tallinn,"Lamezia,Catania",3
Tallinn,Larnaca,4
Tallinn,London,167
Tallinn,Malaga,38
Tallinn,Malta,13
Tallinn,Milano,111
Tallinn,Munchen,123
Tallinn,Nice,25
Tallinn,Oslo,109
Tallinn,Palma De Mallorca,19
Tallinn,Paphos,25
Tallinn,Pariis,82
Tallinn,Praha,49
Tallinn,Rhodos,32
Tallinn,Riia,365
Tallinn,Rooma,39
Tallinn,Sharm El Sheikh,6
Tallinn,Split,25
Tallinn,Stockholm,614
Tallinn,Tampere,17
Tallinn,Tenerife,2
Tallinn,Tirana,8
Tallinn,Tivat,26
Tallinn,Varssavi,294
Tallinn,Veneetsia-Treviso,26
Tallinn,Viin,42
Tallinn,Vilnius,104
Tallinn,Zurich,68


```
