import csv


class Stop:
    dict_of_stoplists = dict()

    def __init__(self, stopInfo, nextstopInfo, distance, train_num):
        self.arrival_time = nextstopInfo.datetime
        self.arrival_station = nextstopInfo
        self.previous_station = stopInfo
        self.distance = float(distance)
        self.travel_time = self.calc_travel_time(stopInfo, nextstopInfo)
        self.departure = stopInfo.datetime
        self.speed = ( (self.distance/self.travel_time.total_seconds() ) * 3.6 )
        self.train_num = train_num
        self.__create_dict_of_stoplists()

    def __create_dict_of_stoplists(self):
        if self.arrival_station.stationID in self.dict_of_stoplists:
            self.dict_of_stoplists[self.arrival_station.stationID].append(self)
        else:
            self.dict_of_stoplists[self.arrival_station.stationID] = [self]


    #DOESNT WORK
    @staticmethod
    def remove_duplicates():
        new_dict_of_stoplists = dict()
        for key in Stop.dict_of_stoplists.keys():
                for list_item in Stop.dict_of_stoplists.get(key) :
                    default = True
                    if (new_dict_of_stoplists.get(key, default)) or (list_item in Stop.__new_dict(key) ):
                        if key in new_dict_of_stoplists:
                            new_dict_of_stoplists[key].append(list_item)
                        else:
                            new_dict_of_stoplists[key] = [list_item]
        i = 0
        for list in new_dict_of_stoplists.values():
            i += len(list)
        print(i)
        Stop.dict_of_stoplists = new_dict_of_stoplists

    def __new_dict(key):
        if ( Stop.new_dict_of_stoplists.get(key).arrival_time in Stop.dict_of_stoplists.get(key) ):
            return False


    @staticmethod
    def print_all_stop_data():
        file = open("NTAS CSS\\travelTimes.csv", 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ARRIVED AT", "DateTIME Arrival", "Departure", "Travel TIME", "speed (km//s)", "distance", "train"])

        for key in Stop.dict_of_stoplists.keys():
         #   print(key, "  --------------------------------")
            for each_stop in Stop.dict_of_stoplists[key]:
                writer.writerow([each_stop.arrival_station.stationID, each_stop.arrival_time, each_stop.departure, each_stop.travel_time, each_stop.speed, each_stop.distance, each_stop.train_num])
          #      print(each_stop.arrival_station.stationID , each_stop.arrival_time, each_stop.travel_time)
           # print("------------------------------------")
        file.close()



    def calc_travel_time(self, stopInfo, nextstopInfo):
        return (nextstopInfo.datetime - stopInfo.datetime)


class StationStops:
    pass

