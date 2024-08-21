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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25]
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
Tallinn,Amsterdam,20
Tallinn,Antalya,31
Tallinn,Ateena,4
Tallinn,Barcelona,6
Tallinn,Berliin,23
Tallinn,Billund,11
Tallinn,Brussel,12
Tallinn,Burgas,9
Tallinn,Dublin,6
Tallinn,Dubrovnik,6
Tallinn,Frankfurt,56
Tallinn,Goteborg,1
Tallinn,Helsingi,193
Tallinn,Heraklion,12
Tallinn,Istanbul,19
Tallinn,Kerkira,3
Tallinn,Kopenhaagen,22
Tallinn,Kuressaare,35
Tallinn,Kardla,35
Tallinn,London,41
Tallinn,Malaga,8
Tallinn,Malta,3
Tallinn,Milano,23
Tallinn,Munchen,29
Tallinn,Nice,6
Tallinn,Oslo,19
Tallinn,Palma De Mallorca,3
Tallinn,Paphos,5
Tallinn,Pariis,21
Tallinn,Praha,11
Tallinn,Rhodos,6
Tallinn,Riia,81
Tallinn,Rooma,9
Tallinn,Split,6
Tallinn,Stockholm,125
Tallinn,Tampere,2
Tallinn,Tirana,2
Tallinn,Tivat,8
Tallinn,Varssavi,65
Tallinn,Veneetsia-Treviso,6
Tallinn,Viin,9
Tallinn,Vilnius,23
Tallinn,Zurich,17


```
