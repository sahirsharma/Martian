import ephem
import time
print "The following code will let you find the apperent position of mars from your current position"
curlat = int(raw_input("Your current lattitude-"))
curlon = int(raw_input("Your current longitude-"))
curele = int(raw_input("Your current elevation-"))
curdate = (raw_input("Your current date (yyyy/mm/dd)-"))
you = ephem.Observer()
you.lat = "%s"%curlat
you.lon = "%s"%curlon
you.elevation = curele
you.date = "%s"%curdate
m = ephem.Mars(you)
print "Azimuth east of north - %s\nAltitude above horizon - %s"%(m.alt,m.az)
time.sleep(10)