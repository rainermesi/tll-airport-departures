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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06", "2024-09-07", "2024-09-08"]
    y-axis "# departures" 0 --> 64
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55, 47, 57, 56, 52, 45, 58]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29, 20, 25, 28, 25, 23, 30]
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
Tallinn,Amsterdam,38
Tallinn,Antalya,61
Tallinn,Ateena,7
Tallinn,Barcelona,11
Tallinn,Berliin,44
Tallinn,Billund,22
Tallinn,Bodrum,1
Tallinn,Brussel,22
Tallinn,Burgas,17
Tallinn,Dublin,11
Tallinn,Dubrovnik,11
Tallinn,Frankfurt,104
Tallinn,Goteborg,1
Tallinn,Helsingi,367
Tallinn,Heraklion,22
Tallinn,Istanbul,36
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,43
Tallinn,Košice,1
Tallinn,Kuressaare,65
Tallinn,Kardla,65
Tallinn,Lamezia,1
Tallinn,London,76
Tallinn,Malaga,16
Tallinn,Malta,6
Tallinn,Milano,43
Tallinn,Munchen,55
Tallinn,Nice,11
Tallinn,Oslo,44
Tallinn,Palma De Mallorca,6
Tallinn,Paphos,10
Tallinn,Pariis,39
Tallinn,Praha,21
Tallinn,Rhodos,12
Tallinn,Riia,153
Tallinn,Rooma,17
Tallinn,Split,11
Tallinn,Stockholm,249
Tallinn,Tampere,6
Tallinn,Tirana,5
Tallinn,Tivat,16
Tallinn,Varssavi,125
Tallinn,Veneetsia-Treviso,11
Tallinn,Viin,17
Tallinn,Vilnius,43
Tallinn,Zurich,31


```
