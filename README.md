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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10", "2024-09-11", "2024-09-12"]
    y-axis "# departures" 0 --> 65
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55, 47, 57, 56, 52, 45, 58, 55, 46, 58, 59]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29, 20, 25, 28, 25, 23, 30, 29, 19, 26, 27]
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
Tallinn,Amsterdam,42
Tallinn,Antalya,70
Tallinn,Ateena,8
Tallinn,Barcelona,13
Tallinn,Berliin,48
Tallinn,Billund,24
Tallinn,Bodrum,1
Tallinn,Brussel,24
Tallinn,Burgas,18
Tallinn,Catania,1
Tallinn,Dublin,12
Tallinn,Dubrovnik,12
Tallinn,Frankfurt,116
Tallinn,Goteborg,1
Tallinn,Helsingi,407
Tallinn,Heraklion,24
Tallinn,Istanbul,40
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,47
Tallinn,Košice,1
Tallinn,Kuressaare,73
Tallinn,Kardla,73
Tallinn,Lamezia,1
Tallinn,London,82
Tallinn,Malaga,18
Tallinn,Malta,6
Tallinn,Milano,49
Tallinn,Munchen,61
Tallinn,Nice,12
Tallinn,Oslo,48
Tallinn,Palma De Mallorca,7
Tallinn,Paphos,12
Tallinn,Pariis,42
Tallinn,Praha,24
Tallinn,Rhodos,13
Tallinn,Riia,169
Tallinn,Rooma,18
Tallinn,Split,12
Tallinn,Stockholm,280
Tallinn,Tampere,7
Tallinn,Tirana,6
Tallinn,Tivat,18
Tallinn,Varssavi,137
Tallinn,Veneetsia-Treviso,12
Tallinn,Viin,19
Tallinn,Vilnius,49
Tallinn,Zurich,34


```
