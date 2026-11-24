"""Sample data; edit these values to test other courier scenarios."""
DEPOT = "DEPOT"
VEHICLE_CAPACITY = 15
PARCELS = [
 {"id":"P1","destination":"A","weight":4,"deadline":2,"priority":8},
 {"id":"P2","destination":"B","weight":6,"deadline":1,"priority":10},
 {"id":"P3","destination":"C","weight":3,"deadline":3,"priority":6},
 {"id":"P4","destination":"D","weight":5,"deadline":2,"priority":9},
 {"id":"P5","destination":"E","weight":2,"deadline":1,"priority":4},
 {"id":"P6","destination":"F","weight":7,"deadline":4,"priority":7},
]
EDGES = [
 ("DEPOT","A",4),("DEPOT","B",7),("DEPOT","C",9),("A","B",3),
 ("A","D",6),("B","C",2),("B","D",4),("B","E",7),("C","E",3),
 ("C","F",8),("D","E",2),("D","F",5),("E","F",3)
]
