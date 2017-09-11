import os
import io
from stationinfo import Station

def ttc_Station_Reader():
    LiStation = list()
    path = "D:\\NTAS CSS\\StationMap.csv"

    stationSpecs = [dataline.strip().split(',') for dataline in open(path, 'r')]

    for line in stationSpecs:
        isLastStation  = True if line[8] == 0 else False
        NewStation = Station(line, isLastStation )
        LiStation.append(NewStation)

    return LiStation       #liCurrentStation

def reader_test():
   for x in ttc_Station_Reader():
       x.print()

reader_test()
