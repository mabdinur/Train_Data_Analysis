class TrackDataReader:
    dict_track_data = dict()
    def __init__(self , path = "NTAS CSS//TrackCircuitMap.csv" ):
        for dataline in open(path, 'r'):
            data = dataline.split(',')
            trackdata1 = TrackData(data)
            self.__ifIsStation(trackdata1)


    def __ifIsStation(self, trackdata):
        if (trackdata.distance == "0"):
            trackID = trackdata.trackID
            self.dict_track_data[trackID] = trackdata

class TrackData:
    def __init__(self, info):
        self.trackID = info[0]
        self.stationID = info[5]   #FinCH ---> Downsview (is 2)       #Kennedy ---> Kipling (is 2)
        self.line = info[11]
        self.distance = info[6]

    def tprint(self):
        return "ID {}  Station {} Distance {}".format(self.trackID, self.stationID, self.distance )



def destination_dict(path = "NTAS CSS//Destinations.csv"):
    dict_dest = dict()
    for dataline in open(path, 'r'):
        data = dataline.split(',')
        dest_ascii = data[0]
        stationID = data[2]
        dict_dest[dest_ascii] = stationID
    return dict_dest

moon = TrackDataReader()
