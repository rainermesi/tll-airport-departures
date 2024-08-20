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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21]
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
Tallinn,Amsterdam,19
Tallinn,Antalya,31
Tallinn,Ateena,3
Tallinn,Barcelona,6
Tallinn,Berliin,21
Tallinn,Billund,11
Tallinn,Brussel,11
Tallinn,Burgas,8
Tallinn,Dublin,6
Tallinn,Dubrovnik,6
Tallinn,Frankfurt,53
Tallinn,Goteborg,1
Tallinn,Helsingi,184
Tallinn,Heraklion,11
Tallinn,Istanbul,18
Tallinn,Kerkira,2
Tallinn,Kopenhaagen,21
Tallinn,Kuressaare,33
Tallinn,Kardla,33
Tallinn,London,38
Tallinn,Malaga,8
Tallinn,Malta,3
Tallinn,Milano,21
Tallinn,Munchen,28
Tallinn,Nice,5
Tallinn,Oslo,18
Tallinn,Palma De Mallorca,3
Tallinn,Paphos,5
Tallinn,Pariis,20
Tallinn,Praha,10
Tallinn,Rhodos,6
Tallinn,Riia,77
Tallinn,Rooma,9
Tallinn,Split,6
Tallinn,Stockholm,116
Tallinn,Tampere,2
Tallinn,Tirana,2
Tallinn,Tivat,8
Tallinn,Varssavi,62
Tallinn,Veneetsia-Treviso,6
Tallinn,Viin,9
Tallinn,Vilnius,21
Tallinn,Zurich,16


```
