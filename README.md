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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06", "2024-09-07", "2024-09-08", "2024-09-09", "2024-09-10", "2024-09-11", "2024-09-12", "2024-09-13", "2024-09-14", "2024-09-15", "2024-09-16", "2024-09-17", "2024-09-18", "2024-09-19", "2024-09-20", "2024-09-21", "2024-09-22", "2024-09-23", "2024-09-24", "2024-09-25", "2024-09-26", "2024-09-27", "2024-09-28", "2024-09-29", "2024-09-30", "2024-10-01"]
    y-axis "# departures" 0 --> 66
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55, 47, 57, 56, 52, 45, 58, 55, 46, 58, 59, 54, 44, 60, 58, 49, 57, 59, 55, 45, 57, 57, 50, 57, 59, 53, 46, 58, 55, 49]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29, 20, 25, 28, 25, 23, 30, 29, 19, 26, 27, 25, 23, 29, 29, 20, 25, 28, 25, 23, 29, 30, 21, 25, 28, 24, 23, 29, 29, 22]
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
Tallinn,Amsterdam,61
Tallinn,Antalya,130
Tallinn,Ateena,10
Tallinn,Barcelona,18
Tallinn,Berliin,69
Tallinn,Billund,35
Tallinn,Bodrum,7
Tallinn,Brussel,35
Tallinn,Burgas,21
Tallinn,Catania,2
Tallinn,Dublin,18
Tallinn,Dubrovnik,18
Tallinn,Enfidha,3
Tallinn,Faro,2
Tallinn,"Faro,Faro",1
Tallinn,Frankfurt,166
Tallinn,Goteborg,1
Tallinn,Helsingi,589
Tallinn,Heraklion,35
Tallinn,Istanbul,63
Tallinn,Istres Le Tubé/Istres Air Base,1
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,69
Tallinn,Košice,1
Tallinn,Kuressaare,105
Tallinn,Kardla,105
Tallinn,Lamezia,1
Tallinn,"Lamezia,Catania",2
Tallinn,London,115
Tallinn,Malaga,26
Tallinn,Malta,9
Tallinn,Milano,72
Tallinn,Munchen,88
Tallinn,Nice,17
Tallinn,Oslo,72
Tallinn,Palma De Mallorca,12
Tallinn,Paphos,17
Tallinn,Pariis,58
Tallinn,Praha,34
Tallinn,Rhodos,22
Tallinn,Riia,245
Tallinn,Rooma,27
Tallinn,Split,18
Tallinn,Stockholm,410
Tallinn,Tampere,12
Tallinn,Tirana,8
Tallinn,Tivat,23
Tallinn,Varssavi,198
Tallinn,Veneetsia-Treviso,18
Tallinn,Viin,27
Tallinn,Vilnius,69
Tallinn,Zurich,48


```
