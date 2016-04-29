What Is This?
-------------

Astropy is a package intended to contain core functionality and some common tools needed for performing astronomy and astrophysics research with Python. It also provides an index for other astronomy packages and tools for managing them.


Features provided by Astropy include :-
---------------------------------------

->Constants :- astropy.constants contains a number of physical constants useful in Astronomy. Constants are Quantity objects with additional meta-data describing their                provenance and uncertainties.

->Time and Dates :- The astropy.time package provides functionality for manipulating times and dates.Specific emphasis is placed on supporting time scales (e.g. UTC,                     TAI, UT1, TDB) and time representations (e.g. JD, MJD, ISO 8601) that are used in astronomy and required to calculate, e.g., sidereal times and                     barycentric corrections.

->World Coordinate System :- astropy.wcs contains utilities for managing World Coordinate System (WCS) transformations in FITS files. These transformations map the                              pixel locations in an image to their real-world units, such as their position on the sky sphere. These transformations can work both                              forward (from pixel to sky) and backward (from sky to pixel).

->Astronomical Coordinate Systems :- The coordinates package provides classes for representing a variety of celestial/spatial coordinates, as well as tools for                                      converting between common coordinate systems in a uniform way.

How To Install The Library
--------------------------

1. If you have a C comiler and the pip Python installer tool on your system, then installing PyEhem should be as easy as:
               pip install --no-deps astropy  

2. If you don't have a pip python installer , you could install the library from the setup.py file present inside astropy-1.1.2 folder.   

