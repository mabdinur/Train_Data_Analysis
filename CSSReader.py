from datetime import datetime
import csv


class CSSData:
    def __init__(self, liTraindata , x , trainNumPrev = "000", linePrev = "N/A", destCodePrev = "N/A"):
        self.trainNum= int(liTraindata[x + 1])
        self.line= chr(int(liTraindata[x + 2]))
        self.destinCode=  chr(int(liTraindata[x + 3]))
        self.trainClass= chr(int(liTraindata[x + 4]))
        self.eventType= liTraindata[x + 5]
        self.trackCircuit= liTraindata[ x + 6]

        self.datetime= self.setdate(liTraindata[x + 7] + ":" + liTraindata[x + 8])
        self.trainNumPrev= int(trainNumPrev)
        self.linePrev= linePrev
        self.destCodePrev = destCodePrev

    def setdate(self, date):
        return datetime.strptime(date, "%m/%d/%Y:%H:%M:%S")

    def toString(self):
        string = str(self.trainNum) + str(self.line) + str(self.destinCode) + str(self.trainClass) + str(self.eventType)\
                 + str(self.trackCircuit) + str(self.datetime)
        return string

    def updatetoString(self):
        string = self.toString() + str(self.trainNumPrev) + str(self.linePrev) + str(self.destCodePrev)
        return string


class CSSReader:
    "Reads CSS and Store KEY data into this class"
    TrainData = list()

    def __init__(self, path = "D:\\NTAS CSS\\ntas.css.log.08122017"):

        cssData = self.__opencsv(path)
        self.TrainData = self.__storeCSS(cssData, self.TrainData)

    def __storeCSS(self, cssData, TrainData):
        for x in range( len(cssData) ):
            if ("cooking data" in cssData[x] ) and ( self.isRevenue( cssData[x + 4] , cssData[x + 5]) ):
                if "update" in cssData[ x + 5]:
                    CSSDataInfo = CSSData(cssData, x, cssData[x + 9], cssData[x + 10], cssData[x + 11])
                    TrainData.append(CSSDataInfo)
                else:
                    CSSDataInfo = CSSData(cssData, x)
                    TrainData.append(CSSDataInfo)
        return sorted(TrainData , key =lambda CSSData: CSSData.trainNum)

    def __opencsv(self, path):
        cssData = [dataline.rstrip().rstrip('\.') for dataline in open(path, 'r')]
        return cssData

    #Deprecated, List is way too large to be stored in 1 string
    def trainDatatoString(self):
        foo = 'start'
        for i in self.TrainData:
           foo =  foo + i.updatetoString() + '\n'
        return foo

    def trainDataPrint(self):
        for i in self.TrainData:
           print(i.updatetoString())

    def isRevenue(self, trainClass, eventType):

        try:
         trainClass = int(trainClass)
        except:
            return False

        if "remove" in eventType:
            return False
        elif  ( trainClass == ord("X") ) or ( trainClass == ord("S") ) or ( trainClass == ord("R") ) :
            return True
        else:
            return False


file = open("D:\\NTAS CSS\\data.csv", 'w' , newline= '')
writer = csv.writer(file)
writer.writerow(["Train Number", "Line", "Destination Code", "Train Class", "Event Type", "Track Circuit",
                 "Date-time", "Previous Train Number", "Previous Line" , "Previous Destination Code"])
moonTEST1 = CSSReader()
moonTEST2 = CSSReader("D:\\NTAS CSS\\ntas.css.log.08132017")

for train in moonTEST1.TrainData:
    writer.writerow([train.trainNum, train.line, train.destinCode, train.trainClass, train.eventType,
                     train.trackCircuit, train.datetime, train.trainNumPrev, train.linePrev, train.destCodePrev] )

for train in moonTEST2.TrainData:
    writer.writerow([train.trainNum, train.line, train.destinCode, train.trainClass, train.eventType,
                     train.trackCircuit, train.datetime, train.trainNumPrev, train.linePrev, train.destCodePrev] )

