# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12"]
    y-axis "# departures" 0 --> 61
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54, 55]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26, 29]
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
Tallinn,Amsterdam,11
Tallinn,Antalya,17
Tallinn,Ateena,2
Tallinn,Barcelona,4
Tallinn,Berliin,13
Tallinn,Billund,7
Tallinn,Brussel,7
Tallinn,Burgas,5
Tallinn,Dublin,4
Tallinn,Dubrovnik,3
Tallinn,Frankfurt,31
Tallinn,Goteborg,1
Tallinn,Helsingi,108
Tallinn,Heraklion,6
Tallinn,Istanbul,11
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,12
Tallinn,Kuressaare,19
Tallinn,Kardla,19
Tallinn,London,23
Tallinn,Malaga,4
Tallinn,Malta,2
Tallinn,Milano,13
Tallinn,Munchen,16
Tallinn,Nice,3
Tallinn,Oslo,10
Tallinn,Palma De Mallorca,2
Tallinn,Paphos,3
Tallinn,Pariis,12
Tallinn,Praha,6
Tallinn,Rhodos,4
Tallinn,Riia,45
Tallinn,Rooma,6
Tallinn,Split,4
Tallinn,Stockholm,63
Tallinn,Tampere,1
Tallinn,Tirana,1
Tallinn,Tivat,5
Tallinn,Varssavi,36
Tallinn,Veneetsia-Treviso,3
Tallinn,Viin,5
Tallinn,Vilnius,12
Tallinn,Zurich,9


```
