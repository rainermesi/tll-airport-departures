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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21]
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
Tallinn,Amsterdam,16
Tallinn,Antalya,25
Tallinn,Ateena,3
Tallinn,Barcelona,5
Tallinn,Berliin,18
Tallinn,Billund,9
Tallinn,Brussel,9
Tallinn,Burgas,8
Tallinn,Dublin,5
Tallinn,Dubrovnik,5
Tallinn,Frankfurt,44
Tallinn,Goteborg,1
Tallinn,Helsingi,156
Tallinn,Heraklion,9
Tallinn,Istanbul,15
Tallinn,Kerkira,2
Tallinn,Kopenhaagen,17
Tallinn,Kuressaare,28
Tallinn,Kardla,28
Tallinn,London,32
Tallinn,Malaga,7
Tallinn,Malta,3
Tallinn,Milano,18
Tallinn,Munchen,24
Tallinn,Nice,4
Tallinn,Oslo,14
Tallinn,Palma De Mallorca,2
Tallinn,Paphos,4
Tallinn,Pariis,16
Tallinn,Praha,8
Tallinn,Rhodos,5
Tallinn,Riia,65
Tallinn,Rooma,7
Tallinn,Split,5
Tallinn,Stockholm,99
Tallinn,Tampere,2
Tallinn,Tirana,2
Tallinn,Tivat,6
Tallinn,Varssavi,52
Tallinn,Veneetsia-Treviso,5
Tallinn,Viin,8
Tallinn,Vilnius,18
Tallinn,Zurich,13


```
