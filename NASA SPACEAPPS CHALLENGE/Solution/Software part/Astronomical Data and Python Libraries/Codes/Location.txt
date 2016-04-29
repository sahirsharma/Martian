import ephem
import time
planet = int(raw_input("Choose planet-\n1>Mercury\n2>Venus\n4>Mars\n5>Jupiter\n6>Saturn\n7>Uranus\n8>Neptune\n"))
date = raw_input("date on which you need the planets position (yyyy/mm/dd)-")
if(planet == 1):
  x = ephem.Mercury()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))
elif(planet == 2):

  x = ephem.Venus()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

elif(planet == 4):

  x = ephem.Mars()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

elif(planet == 5):

  x = ephem.Jupiter()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

elif(planet == 6):

  x = ephem.Saturn()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

elif(planet == 7):

  x = ephem.Uranus()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

elif(planet == 8):

  x = ephem.Neptune()  
  x.compute("%s"%date)
  print ("Right Ascension - %s\nDeclination - %s\n" % (x.ra,x.dec))

time.sleep(100)