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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13"]
    y-axis "# departures" 0 --> 61
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21]
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
Tallinn,Amsterdam,12
Tallinn,Antalya,19
Tallinn,Ateena,2
Tallinn,Barcelona,4
Tallinn,Berliin,13
Tallinn,Billund,7
Tallinn,Brussel,7
Tallinn,Burgas,5
Tallinn,Dublin,4
Tallinn,Dubrovnik,4
Tallinn,Frankfurt,34
Tallinn,Goteborg,1
Tallinn,Helsingi,118
Tallinn,Heraklion,7
Tallinn,Istanbul,12
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,13
Tallinn,Kuressaare,21
Tallinn,Kardla,21
Tallinn,London,24
Tallinn,Malaga,5
Tallinn,Malta,2
Tallinn,Milano,13
Tallinn,Munchen,18
Tallinn,Nice,3
Tallinn,Oslo,10
Tallinn,Palma De Mallorca,2
Tallinn,Paphos,3
Tallinn,Pariis,13
Tallinn,Praha,6
Tallinn,Rhodos,4
Tallinn,Riia,49
Tallinn,Rooma,6
Tallinn,Split,4
Tallinn,Stockholm,70
Tallinn,Tampere,1
Tallinn,Tirana,1
Tallinn,Tivat,5
Tallinn,Varssavi,39
Tallinn,Veneetsia-Treviso,4
Tallinn,Viin,6
Tallinn,Vilnius,13
Tallinn,Zurich,10


```
