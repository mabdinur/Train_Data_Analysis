import TrackData
from datetime import datetime

class CSSData:

    def __init__(self, li_train_data , x , destinationID, TrackInfo):
        self.trainNum= int(li_train_data[x + 1])
        self.line= chr(int(li_train_data[x + 2]))
        self.destinCode= destinationID
        self.trainClass= chr(int(li_train_data[x + 4]))
        self.eventType= li_train_data[x + 5]
        self.trackCircuit= li_train_data[ x + 6]
        self.stationID = TrackInfo.stationID    #Station + Direction of the line
        self.datetime= self.setdate(li_train_data[x + 7] + ":" + li_train_data[x + 8])
        self.distance = TrackInfo.distance

    def setdate(self, date):
        return datetime.strptime(date, "%m/%d/%Y:%H:%M:%S")

    def toString(self):
        string = str(self.trainNum) + str(self.line) + str(self.destinCode) + str(self.trainClass) + str(self.eventType)\
                 + str(self.trackCircuit) + str(self.datetime) + self.stationID
        return string

