class Station:
    def __init__(self, stationinfo, finalS ):
        self.stationID = stationinfo[0]
        self.stationC = stationinfo[1]
        self.pvsid = stationinfo[6]
        self.line = stationinfo[2]
        self.stationN = stationinfo[3]
        self.distance = stationinfo[4]
        self.direction = stationinfo[7]
        self.finalS = finalS


    def print(self):
        print("""Current Station Name {} \t\t\tStationID {} \t\t pvsid {} \t\t TrainLine  {} \t\t Next Station  {} 
               Distnace {} \t\t Direction \t\t {} Final Stop {} \n""".format( self.stationC , self.stationID , self.pvsid, self.line ,
                                                                        self.stationN, self.distance, self.direction, self.finalS) )

