# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07"]
    y-axis "# departures" 0 --> 60
    bar [16, 51, 46, 50, 54, 46, 51]
    line [12, 27, 22, 29, 32, 21, 28]
```


## Unique destinations and departures

All destinations flown to from Tallinn. More departures = bigger node.
Note that multiple airports in same city are counted separately (to be aggregated)
Also, umlauts don't seem to be supported in Mermaid Sankey Diagrams (experimental diagram)

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
Tallinn,Amsterdam (Schiphol),6
Tallinn,Antalya,10
Tallinn,Ateena,2
Tallinn,Barcelona,2
Tallinn,Berliin,7
Tallinn,Billund,3
Tallinn,Brussel,4
Tallinn,Burgas,3
Tallinn,Dublin,2
Tallinn,Dubrovnik,2
Tallinn,Frankfurt,18
Tallinn,Goteborg (Landvetter),1
Tallinn,Helsingi,61
Tallinn,Heraklion,4
Tallinn,Istanbul,6
Tallinn,Kerkira,1
Tallinn,Kopenhaagen,6
Tallinn,Kuressaare,11
Tallinn,Kardla,11
Tallinn,London (Gatwick),4
Tallinn,London (Luton),4
Tallinn,London (Stansted),5
Tallinn,Malaga,2
Tallinn,Malta,1
Tallinn,Milano (Bergamo),3
Tallinn,Milano (Malpensa),4
Tallinn,Munchen,9
Tallinn,Nice,2
Tallinn,Oslo,5
Tallinn,Palma De Mallorca,1
Tallinn,Paphos,1
Tallinn,Pariis (Charles De Gaulle),5
Tallinn,Pariis (Orly),2
Tallinn,Praha,3
Tallinn,Rhodos,2
Tallinn,Riia,25
Tallinn,Rooma (Ciampino),3
Tallinn,Split,2
Tallinn,Stockholm (Arlanda),33
Tallinn,Tivat,2
Tallinn,Varssavi (Chopin),19
Tallinn,Veneetsia-Treviso,2
Tallinn,Viin,3
Tallinn,Vilnius,7
Tallinn,Zurich,5


```
