# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08"]
    y-axis "# departures" 0 --> 60
    bar [16, 51, 46, 50, 54, 46, 51, 52]
    line [12, 25, 21, 26, 30, 21, 26, 28]
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
Tallinn,Amsterdam,7
Tallinn,Antalya,11
Tallinn,Ateena,2
Tallinn,Barcelona,3
Tallinn,Berliin,8
Tallinn,Billund,4
Tallinn,Brussel,4
Tallinn,Burgas,3
Tallinn,Dublin,2
Tallinn,Dubrovnik,2
Tallinn,Frankfurt,20
Tallinn,Goteborg,1
Tallinn,Helsingi,71
Tallinn,Heraklion,4
Tallinn,Istanbul,7
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,7
Tallinn,Kuressaare,13
Tallinn,Kardla,13
Tallinn,London,14
Tallinn,Malaga,3
Tallinn,Malta,1
Tallinn,Milano,8
Tallinn,Munchen,11
Tallinn,Nice,2
Tallinn,Oslo,6
Tallinn,Palma De Mallorca,1
Tallinn,Paphos,2
Tallinn,Pariis,8
Tallinn,Praha,4
Tallinn,Rhodos,2
Tallinn,Riia,29
Tallinn,Rooma,3
Tallinn,Split,2
Tallinn,Stockholm,39
Tallinn,Tampere,1
Tallinn,Tirana,1
Tallinn,Tivat,3
Tallinn,Varssavi,22
Tallinn,Veneetsia-Treviso,2
Tallinn,Viin,4
Tallinn,Vilnius,9
Tallinn,Zurich,6


```
