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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29"]
    y-axis "# departures" 0 --> 64
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28]
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
Tallinn,Amsterdam,28
Tallinn,Antalya,44
Tallinn,Ateena,5
Tallinn,Barcelona,9
Tallinn,Berliin,32
Tallinn,Billund,16
Tallinn,Brussel,16
Tallinn,Burgas,12
Tallinn,Dublin,8
Tallinn,Dubrovnik,8
Tallinn,Frankfurt,77
Tallinn,Goteborg,1
Tallinn,Helsingi,272
Tallinn,Heraklion,16
Tallinn,Istanbul,27
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,31
Tallinn,Kuressaare,49
Tallinn,Kardla,49
Tallinn,London,56
Tallinn,Malaga,12
Tallinn,Malta,4
Tallinn,Milano,32
Tallinn,Munchen,41
Tallinn,Nice,8
Tallinn,Oslo,30
Tallinn,Palma De Mallorca,4
Tallinn,Paphos,8
Tallinn,Pariis,29
Tallinn,Praha,16
Tallinn,Rhodos,8
Tallinn,Riia,113
Tallinn,Rooma,12
Tallinn,Split,8
Tallinn,Stockholm,182
Tallinn,Tampere,4
Tallinn,Tirana,4
Tallinn,Tivat,12
Tallinn,Varssavi,91
Tallinn,Veneetsia-Treviso,8
Tallinn,Viin,13
Tallinn,Vilnius,33
Tallinn,Zurich,24


```
