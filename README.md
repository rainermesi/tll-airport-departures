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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15"]
    y-axis "# departures" 0 --> 62
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28]
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
Tallinn,Amsterdam,14
Tallinn,Antalya,22
Tallinn,Ateena,3
Tallinn,Barcelona,5
Tallinn,Berliin,16
Tallinn,Billund,8
Tallinn,Brussel,8
Tallinn,Burgas,6
Tallinn,Dublin,4
Tallinn,Dubrovnik,4
Tallinn,Frankfurt,39
Tallinn,Goteborg,1
Tallinn,Helsingi,138
Tallinn,Heraklion,8
Tallinn,Istanbul,13
Tallinn,Kerkira,2
Tallinn,Kopenhaagen,15
Tallinn,Kuressaare,25
Tallinn,Kardla,25
Tallinn,London,28
Tallinn,Malaga,6
Tallinn,Malta,2
Tallinn,Milano,16
Tallinn,Munchen,21
Tallinn,Nice,4
Tallinn,Oslo,13
Tallinn,Palma De Mallorca,2
Tallinn,Paphos,4
Tallinn,Pariis,15
Tallinn,Praha,8
Tallinn,Rhodos,4
Tallinn,Riia,57
Tallinn,Rooma,6
Tallinn,Split,4
Tallinn,Stockholm,87
Tallinn,Tampere,2
Tallinn,Tirana,2
Tallinn,Tivat,6
Tallinn,Varssavi,45
Tallinn,Veneetsia-Treviso,4
Tallinn,Viin,7
Tallinn,Vilnius,17
Tallinn,Zurich,12


```
