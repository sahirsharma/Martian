What Is This?
-------------

This is library is intended to provides basic astronomical computations for the Python programming language. The name ephem is short for the word ephemeris, which is the traditional term for a table giving the position of a planet, asteroid, or comet for a series of dates.



Features provided by PyEphem include :-
---------------------------------------


->Find where a planet, comet, or asteroid is in the sky.
	->High-precision orbital routines are provdied for the Moon, Sun, planets, and the major planet moons.
	->The user can supply the orbital elements of a comet, asteroid, or Earth-orbiting satellite, and have its location computed.
	->The positions of 94 bright stars come built-in, and the user can create further fixed objects as needed for their calculations.

->Determine where in the sky an object appears for a particular observer.
	->The user can supply the longitude, latitude, and altitude of the location from which they will be observing.
	->For convenience, a small database of longitudes and latitudes for 122 world cities is included.
	->For specified weather conditions (temperature and pressure), PyEphem will compensate for atmospheric refraction by adjusting the positions of bodies near the           horizon.

->Compute when a body will rise, transit overhead, and set from a particular location.

->Determine the dates of the equinoxes and solstices.

->Compute the dates of the various phases of the Moon.

->Convert from the Greenwich Time (more precisely, Ephemeris Time) which PyEphem uses to the local time of   the user.

->Convert positions between the equatorial, ecliptic, and galactic coordinate systems.

->Determine on which page of the Uranometria or the Millennium Star Atlas a particular star should appear.

->Return the Julian Date corresponding to any calendar date.


How To Install The Library
--------------------------

1. If you have a C comiler and the pip Python installer tool on your system, then installing PyEhem should be as easy as:
               pip install ephem  

2. If you don't have a pip python installer , you could install the library from the setup.py file present inside pyephem-3.7.6.0 folder.   

