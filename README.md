# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10"]
    y-axis "# departures" 0 --> 60
    bar [16, 51, 46, 50, 54, 46, 51, 52, 50, 44]
    line [12, 25, 21, 26, 30, 21, 26, 28, 24, 21]
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
Tallinn,Amsterdam,9
Tallinn,Antalya,15
Tallinn,Ateena,2
Tallinn,Barcelona,3
Tallinn,Berliin,10
Tallinn,Billund,5
Tallinn,Brussel,5
Tallinn,Burgas,5
Tallinn,Dublin,3
Tallinn,Dubrovnik,3
Tallinn,Frankfurt,25
Tallinn,Goteborg,1
Tallinn,Helsingi,89
Tallinn,Heraklion,5
Tallinn,Istanbul,9
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,9
Tallinn,Kuressaare,16
Tallinn,Kardla,16
Tallinn,London,18
Tallinn,Malaga,4
Tallinn,Malta,2
Tallinn,Milano,10
Tallinn,Munchen,14
Tallinn,Nice,2
Tallinn,Oslo,7
Tallinn,Palma De Mallorca,1
Tallinn,Paphos,2
Tallinn,Pariis,9
Tallinn,Praha,4
Tallinn,Rhodos,3
Tallinn,Riia,37
Tallinn,Rooma,4
Tallinn,Split,3
Tallinn,Stockholm,50
Tallinn,Tampere,1
Tallinn,Tirana,1
Tallinn,Tivat,3
Tallinn,Varssavi,29
Tallinn,Veneetsia-Treviso,3
Tallinn,Viin,5
Tallinn,Vilnius,10
Tallinn,Zurich,7


```
