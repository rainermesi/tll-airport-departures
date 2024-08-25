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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25]
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
Tallinn,Amsterdam,24
Tallinn,Antalya,37
Tallinn,Ateena,4
Tallinn,Barcelona,7
Tallinn,Berliin,28
Tallinn,Billund,14
Tallinn,Brussel,14
Tallinn,Burgas,11
Tallinn,Dublin,7
Tallinn,Dubrovnik,7
Tallinn,Frankfurt,66
Tallinn,Goteborg,1
Tallinn,Helsingi,232
Tallinn,Heraklion,14
Tallinn,Istanbul,23
Tallinn,Kerkira,3
Tallinn,Kopenhaagen,27
Tallinn,Kuressaare,41
Tallinn,Kardla,41
Tallinn,London,49
Tallinn,Malaga,10
Tallinn,Malta,4
Tallinn,Milano,27
Tallinn,Munchen,35
Tallinn,Nice,7
Tallinn,Oslo,26
Tallinn,Palma De Mallorca,3
Tallinn,Paphos,6
Tallinn,Pariis,25
Tallinn,Praha,13
Tallinn,Rhodos,7
Tallinn,Riia,97
Tallinn,Rooma,11
Tallinn,Split,7
Tallinn,Stockholm,151
Tallinn,Tampere,3
Tallinn,Tirana,3
Tallinn,Tivat,10
Tallinn,Varssavi,79
Tallinn,Veneetsia-Treviso,7
Tallinn,Viin,11
Tallinn,Vilnius,27
Tallinn,Zurich,20


```
