# tll-airport-departures

Tracking departures from Tallinn Airport. Data and graphs are updated daily.

## Trend of Daily Departures

Bars for total number of departures. Line for unique destinations.

```mermaid
xychart-beta
    title "Departures by day"
    x-axis ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06"]
    y-axis "# departures" 0 --> 60
    bar [16, 51, 46, 50, 54, 46]
    line [12, 27, 22, 29, 32, 21]
```


## Unique destinations and departures

All destinations flown to from Tallinn. More departures = bigger node.
Note that multiple airports in same city are counted separately (to be aggregated)
Also, umlauts don't seem to be supported in Mermaid Sankey Diagrams (experimental diagram)

```mermaid
sankey-beta
%% source,target,value
Tallinn,Amsterdam (Schiphol),5
Tallinn,Antalya,9
Tallinn,Ateena,1
Tallinn,Barcelona,2
Tallinn,Berliin,5
Tallinn,Billund,3
Tallinn,Brussel,3
Tallinn,Burgas,2
Tallinn,Dublin,2
Tallinn,Dubrovnik,2
Tallinn,Frankfurt,15
Tallinn,Goteborg (Landvetter),1
Tallinn,Helsingi,52
Tallinn,Heraklion,3
Tallinn,Istanbul,5
Tallinn,Kopenhaagen,5
Tallinn,Kuressaare,9
Tallinn,Kardla,9
Tallinn,London (Gatwick),4
Tallinn,London (Luton),3
Tallinn,London (Stansted),4
Tallinn,Malaga,2
Tallinn,Malta,1
Tallinn,Milano (Bergamo),2
Tallinn,Milano (Malpensa),3
Tallinn,Munchen,8
Tallinn,Nice,1
Tallinn,Oslo,4
Tallinn,Palma De Mallorca,1
Tallinn,Paphos,1
Tallinn,Pariis (Charles De Gaulle),4
Tallinn,Pariis (Orly),2
Tallinn,Praha,2
Tallinn,Rhodos,2
Tallinn,Riia,21
Tallinn,Rooma (Ciampino),3
Tallinn,Split,2
Tallinn,Stockholm (Arlanda),27
Tallinn,Tivat,2
Tallinn,Varssavi (Chopin),17
Tallinn,Veneetsia-Treviso,2
Tallinn,Viin,3
Tallinn,Vilnius,5
Tallinn,Zurich,4


```
