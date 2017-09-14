from CSSReader import CSSReader
import csv
from Trip import Stop

#Logfile_Aug8 = CSSReader()
Logfile_Aug9 = CSSReader("NTAS CSS\\ntas.css.log.08132017")
#Logfile_Aug8.identify_stops()
Logfile_Aug9.identify_stops()
#Stop.remove_duplicates()
Stop.print_all_stop_data()



