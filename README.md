# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11"]
    y-axis "# departures" 0 --> 60
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44, 54]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21, 26]
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
Tallinn,Amsterdam,10
Tallinn,Antalya,17
Tallinn,Ateena,2
Tallinn,Barcelona,3
Tallinn,Berliin,12
Tallinn,Billund,6
Tallinn,Brussel,6
Tallinn,Burgas,5
Tallinn,Dublin,3
Tallinn,Dubrovnik,3
Tallinn,Frankfurt,28
Tallinn,Goteborg,1
Tallinn,Helsingi,98
Tallinn,Heraklion,6
Tallinn,Istanbul,10
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,11
Tallinn,Kuressaare,17
Tallinn,Kardla,17
Tallinn,London,21
Tallinn,Malaga,4
Tallinn,Malta,2
Tallinn,Milano,11
Tallinn,Munchen,15
Tallinn,Nice,3
Tallinn,Oslo,9
Tallinn,Palma De Mallorca,1
Tallinn,Paphos,2
Tallinn,Pariis,11
Tallinn,Praha,5
Tallinn,Rhodos,3
Tallinn,Riia,41
Tallinn,Rooma,5
Tallinn,Split,3
Tallinn,Stockholm,56
Tallinn,Tampere,1
Tallinn,Tirana,1
Tallinn,Tivat,4
Tallinn,Varssavi,33
Tallinn,Veneetsia-Treviso,3
Tallinn,Viin,5
Tallinn,Vilnius,11
Tallinn,Zurich,8


```
