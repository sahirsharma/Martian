import openpyxl
from openpyxl import Workbook
import ephem
import time
print "The following code will store the location of mars for a period of 1 month from a used defined year and month"
yearx = int(raw_input("Year - "))
monthx = int(raw_input("Month - "))
wb = Workbook()
data = wb.active
data["A1"] = "Date"
data["B1"] = "Right Ascension"
data["C1"] = "Declination"
c = 1 
for c in range(1,30):
    x = ephem.Mars()
    x.compute("%s/%s/%s"%(yearx,monthx,c))
    data["A%s"%(c+1)] = "%s/%s/%s"%(yearx,monthx,c)
    data["B%s"%(c+1)] = x.ra
    data["C%s"%(c+1)] = x.dec


wb.save("data.xlsx")
time.sleep(10)



