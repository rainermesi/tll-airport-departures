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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22]
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
Tallinn,Amsterdam,23
Tallinn,Antalya,37
Tallinn,Ateena,4
Tallinn,Barcelona,7
Tallinn,Berliin,26
Tallinn,Billund,13
Tallinn,Brussel,13
Tallinn,Burgas,11
Tallinn,Dublin,7
Tallinn,Dubrovnik,7
Tallinn,Frankfurt,63
Tallinn,Goteborg,1
Tallinn,Helsingi,222
Tallinn,Heraklion,13
Tallinn,Istanbul,22
Tallinn,Kerkira,3
Tallinn,Kopenhaagen,25
Tallinn,Kuressaare,40
Tallinn,Kardla,40
Tallinn,London,46
Tallinn,Malaga,10
Tallinn,Malta,4
Tallinn,Milano,26
Tallinn,Munchen,34
Tallinn,Nice,6
Tallinn,Oslo,23
Tallinn,Palma De Mallorca,3
Tallinn,Paphos,6
Tallinn,Pariis,23
Tallinn,Praha,12
Tallinn,Rhodos,7
Tallinn,Riia,93
Tallinn,Rooma,10
Tallinn,Split,7
Tallinn,Stockholm,145
Tallinn,Tampere,3
Tallinn,Tirana,3
Tallinn,Tivat,9
Tallinn,Varssavi,75
Tallinn,Veneetsia-Treviso,7
Tallinn,Viin,11
Tallinn,Vilnius,26
Tallinn,Zurich,19


```
