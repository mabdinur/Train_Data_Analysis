from datetime import datetime
import csv
import TrackData
from CSSData import CSSData
from TrackData import TrackDataReader
from Trip import Stop
import csv
from stationinfo import Station
from stationinfo import stationinfo_reader

class CSSReader:
    "Reads CSS and Store KEY data into this class"
    TrainData = list()

    def __init__(self, path = "NTAS CSS\\ntas.css.log.08122017"):
        cssData = self.__opencsv(path)
        trackdataR = TrackDataReader()
        trackinfo = trackdataR.dict_track_data
        self.TrainData = self.__storeRevenueTrains(cssData, self.TrainData, trackinfo)              #self.__storeCSS(cssData, self.TrainData)

    def __storeRevenueTrains(self, cssData, TrainData, dict_track_data):
        destionation_dict = self.destination_dict()
        for x in range( len(cssData) ):
            if ("cooking data" in cssData[x] ) and ( self.is_revenue( cssData[x + 4] , cssData[x + 5]) ):
                if ("arrival" in cssData[ x + 5]) and ( cssData[ x + 6] in dict_track_data ):
                    trackinfo = dict_track_data.get(cssData[ x + 6])
                    destCode = chr(int(cssData[x + 3]))
                    destinationID = (destionation_dict.get(destCode))
                    CSSDataInfo = CSSData(cssData, x, destinationID, trackinfo)
                    TrainData.append(CSSDataInfo)
        return sorted(TrainData , key =lambda CSSData: CSSData.trainNum)

    def __opencsv(self, path):
        cssData = [dataline.rstrip().rstrip('\.') for dataline in open(path, 'r')]
        return cssData

    def train_data_print(self):
        for i in self.TrainData:
           print(i.updatetoString())

    def is_revenue(self, train_class, eventType):

        try:
         train_class = int(train_class)
        except:
            return False

        if "remove" in eventType:
            return False
        elif (train_class == ord("X")) or (train_class == ord("S")) or (train_class == ord("R")) :
            return True
        else:
            return False

    def wrtie_cssdata_tocsv(self, writer):
        for train in self.TrainData:
            writer.writerow([train.trainNum, train.line, train.destinCode, train.train_class, train.eventType,
                             train.trackCircuit, train.datetime, train.trainNumPrev, train.linePrev,
                             train.destCodePrev, train.stationID])

    def destination_dict(self, path="NTAS CSS//Destinations.csv"):
        dict_dest = dict()
        for dataline in open(path, 'r'):
            data = dataline.split(',')
            dest_ascii = data[0]
            station_id = data[2]
            dict_dest[dest_ascii] = station_id
        return dict_dest

    def identify_stops(self):
        dict_stations = stationinfo_reader()

        for i in range(len(self.TrainData) - 1):
            currTrainNum = self.TrainData[i].trainNum
            station = self.TrainData[i].stationID
            nextTrainNum = self.TrainData[i + 1].trainNum
            nextstation_actual = self.TrainData[i + 1].stationID
            nextstation_route = dict_stations.get(station)

            if(currTrainNum == nextTrainNum)and(nextstation_actual == nextstation_route.stationNext):
                Stop(self.TrainData[i], self.TrainData[i + 1], nextstation_route.distance, currTrainNum )

    def ___next_station_on_map(self, dict_stations, station):
        if "BAY2" in station:
            return dict_stations.get("BAU2")
        else:
            return dict_stations.get(station)


        
def createDataCSV ():
    file = open("NTAS CSS\\data.csv", 'w' , newline= '')
    writer = csv.writer(file)
    writer.writerow(["Train Number", "Line", "Destination Code", "Train Class", "Event Type", "Track Circuit",
                     "Date-time", "Previous Train Number", "Previous Line", "Previous Destination Code", "StationID"])
    moonTEST1 = CSSReader()
    moonTEST2 = CSSReader("NTAS CSS\\ntas.css.log.08132017")

    moonTEST1.wrtie_cssdata_tocsv(writer)
    moonTEST2.wrtie_cssdata_tocsv(writer)


#createDataCSV()    #Create data file containtating extracted CSS information


