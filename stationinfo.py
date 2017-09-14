class Station:
    def __init__(self, stationinfo):
        self.stationID = stationinfo[0]
        if("BAY2" in stationinfo[3]):
            print(stationinfo[3])
        self.stationNext = stationinfo[3]
        self.distance = stationinfo[4]

    def toString(self):
        return ("Current Station {} \t\t Next Station  {} Distance {} ".
              format(self.stationID , self.stationNext, self.distance))

def stationinfo_reader():
    stations = dict()
    path = "NTAS CSS\\StationMap.csv"

    stationSpecs = [dataline.strip().split(',') for dataline in open(path, 'r')]

    for line in stationSpecs:
        NewStation = Station(line)
        stations[ line[0] ] = NewStation
        NewStation.toString()
   #     print(line[0])
   #     print(NewStation.toString())

    return stations       #liCurrentStation