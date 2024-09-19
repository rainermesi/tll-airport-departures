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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10", "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14", "2024-09-15", "2024-09-16", "2024-09-17", "2024-09-18", "2024-09-19"]
    y-axis "# departures" 0 --> 66
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55, 47, 57, 56, 52, 45, 58, 55, 46, 58, 59, 54, 44, 60, 58, 49, 57, 59]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29, 20, 25, 28, 25, 23, 30, 29, 19, 26, 27, 25, 23, 29, 29, 20, 25, 28]
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
Tallinn,Amsterdam,49
Tallinn,Antalya,93
Tallinn,Ateena,9
Tallinn,Barcelona,15
Tallinn,Berliin,56
Tallinn,Billund,28
Tallinn,Bodrum,3
Tallinn,Brussel,28
Tallinn,Burgas,19
Tallinn,Catania,1
Tallinn,Dublin,14
Tallinn,Dubrovnik,14
Tallinn,Enfidha,1
Tallinn,"Faro,Faro",1
Tallinn,Frankfurt,135
Tallinn,Goteborg,1
Tallinn,Helsingi,475
Tallinn,Heraklion,28
Tallinn,Istanbul,49
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,55
Tallinn,Košice,1
Tallinn,Kuressaare,85
Tallinn,Kardla,85
Tallinn,Lamezia,1
Tallinn,"Lamezia,Catania",1
Tallinn,London,94
Tallinn,Malaga,21
Tallinn,Malta,7
Tallinn,Milano,58
Tallinn,Munchen,71
Tallinn,Nice,14
Tallinn,Oslo,57
Tallinn,Palma De Mallorca,9
Tallinn,Paphos,14
Tallinn,Pariis,48
Tallinn,Praha,28
Tallinn,Rhodos,16
Tallinn,Riia,197
Tallinn,Rooma,21
Tallinn,Split,14
Tallinn,Stockholm,329
Tallinn,Tampere,9
Tallinn,Tirana,7
Tallinn,Tivat,20
Tallinn,Varssavi,159
Tallinn,Veneetsia-Treviso,14
Tallinn,Viin,22
Tallinn,Vilnius,57
Tallinn,Zurich,39


```
