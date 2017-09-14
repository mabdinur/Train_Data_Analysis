import MySQLdb #you have to install this find an exacutable
import numpy as np
import matplotlib.pyploy as plt

db = MySQLdb.connect( "local host" , "testuser" , "password" , "dbName" )
cursor = db.cursor()
cursor.exacute("SELECT * FROM table_name")

dict_of_message_lengths = dict()

for row in cursor.fetchall():
    length_of_message = len(row[0]) #insert the row that you want to

    if length_of_message in dict_of_message_lengths.keys():
         occurance = dict_of_message_lengths.get(length_of_message) + 1
         dict_of_message_lengths[length_of_message] = occurance
    else:
        dict_of_message_lengths[length_of_message] = 1

x, y = zip(*dict_of_message_lengths)
plt.plot(x, y)
plt.show()
#NOW PLOT OCCURANCE vs.
