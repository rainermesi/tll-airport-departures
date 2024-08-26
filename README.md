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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26"]
    y-axis "# departures" 0 --> 64
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30]
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
Tallinn,Amsterdam,25
Tallinn,Antalya,39
Tallinn,Ateena,4
Tallinn,Barcelona,8
Tallinn,Berliin,29
Tallinn,Billund,15
Tallinn,Brussel,15
Tallinn,Burgas,11
Tallinn,Dublin,8
Tallinn,Dubrovnik,7
Tallinn,Frankfurt,69
Tallinn,Goteborg,1
Tallinn,Helsingi,242
Tallinn,Heraklion,14
Tallinn,Istanbul,25
Tallinn,Kerkira,3
Tallinn,Kopenhaagen,28
Tallinn,Kuressaare,43
Tallinn,Kardla,43
Tallinn,London,51
Tallinn,Malaga,10
Tallinn,Malta,4
Tallinn,Milano,29
Tallinn,Munchen,36
Tallinn,Nice,7
Tallinn,Oslo,27
Tallinn,Palma De Mallorca,4
Tallinn,Paphos,7
Tallinn,Pariis,26
Tallinn,Praha,14
Tallinn,Rhodos,8
Tallinn,Riia,101
Tallinn,Rooma,12
Tallinn,Split,8
Tallinn,Stockholm,158
Tallinn,Tampere,3
Tallinn,Tirana,3
Tallinn,Tivat,11
Tallinn,Varssavi,82
Tallinn,Veneetsia-Treviso,7
Tallinn,Viin,11
Tallinn,Vilnius,28
Tallinn,Zurich,21


```
