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
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28", "2024-08-29", "2024-08-30", "2024-08-31", "2024-09-01", "2024-09-02"]
    y-axis "# departures" 0 --> 64
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55, 47, 56, 56, 52, 42, 55, 54, 46, 55, 56, 53, 44, 54, 58, 49, 55, 55, 52, 45, 54, 55]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29, 21, 25, 28, 24, 21, 26, 30, 21, 25, 28, 25, 22, 25, 30, 21, 24, 28, 24, 22, 26, 29]
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
Tallinn,Amsterdam,32
Tallinn,Antalya,50
Tallinn,Ateena,5
Tallinn,Barcelona,10
Tallinn,Berliin,37
Tallinn,Billund,19
Tallinn,Brussel,19
Tallinn,Burgas,14
Tallinn,Dublin,10
Tallinn,Dubrovnik,9
Tallinn,Frankfurt,88
Tallinn,Goteborg,1
Tallinn,Helsingi,310
Tallinn,Heraklion,18
Tallinn,Istanbul,30
Tallinn,Kerkira,4
Tallinn,Kopenhaagen,36
Tallinn,Kuressaare,55
Tallinn,Kardla,55
Tallinn,London,65
Tallinn,Malaga,13
Tallinn,Malta,5
Tallinn,Milano,37
Tallinn,Munchen,46
Tallinn,Nice,9
Tallinn,Oslo,36
Tallinn,Palma De Mallorca,5
Tallinn,Paphos,9
Tallinn,Pariis,33
Tallinn,Praha,18
Tallinn,Rhodos,10
Tallinn,Riia,129
Tallinn,Rooma,15
Tallinn,Split,10
Tallinn,Stockholm,207
Tallinn,Tampere,4
Tallinn,Tirana,4
Tallinn,Tivat,14
Tallinn,Varssavi,105
Tallinn,Veneetsia-Treviso,9
Tallinn,Viin,14
Tallinn,Vilnius,36
Tallinn,Zurich,27


```
