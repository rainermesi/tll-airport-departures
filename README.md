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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28"]
    y-axis "# departures" 0 --> 64
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24]
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
Tallinn,Amsterdam,27
Tallinn,Antalya,43
Tallinn,Ateena,5
Tallinn,Barcelona,8
Tallinn,Berliin,31
Tallinn,Billund,15
Tallinn,Brussel,16
Tallinn,Burgas,12
Tallinn,Dublin,8
Tallinn,Dubrovnik,8
Tallinn,Frankfurt,75
Tallinn,Goteborg,1
Tallinn,Helsingi,262
Tallinn,Heraklion,16
Tallinn,Istanbul,26
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,30
Tallinn,Kuressaare,47
Tallinn,Kardla,47
Tallinn,London,55
Tallinn,Malaga,11
Tallinn,Malta,4
Tallinn,Milano,31
Tallinn,Munchen,39
Tallinn,Nice,8
Tallinn,Oslo,28
Tallinn,Palma De Mallorca,4
Tallinn,Paphos,7
Tallinn,Pariis,28
Tallinn,Praha,15
Tallinn,Rhodos,8
Tallinn,Riia,109
Tallinn,Rooma,12
Tallinn,Split,8
Tallinn,Stockholm,174
Tallinn,Tampere,3
Tallinn,Tirana,3
Tallinn,Tivat,11
Tallinn,Varssavi,88
Tallinn,Veneetsia-Treviso,8
Tallinn,Viin,12
Tallinn,Vilnius,31
Tallinn,Zurich,23


```
