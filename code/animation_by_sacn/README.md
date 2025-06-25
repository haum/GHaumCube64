Animations controlled by sACN
=============================

What?
-----

Program that receives sACN data on universe 3 and use them to control
GHaumCube64 on universe 1&2

sACN universe 3 ===> [animation_by_sacn ] ===> sACN universe 1&2 ===> [GHaumCube64]

Data
----

Data on universe 3:

| Byte | Short name | Description             |
| ---- | ---------- | ----------------------- |
|    0 |         R1 | Color1, red component   |
|    1 |         G1 | Color1, green component |
|    2 |         B1 | Color1, blue component  |
|    3 |         R2 | Color2, red component   |
|    4 |         G2 | Color2, green component |
|    5 |         B2 | Color2, blue component  |
|    6 |         FX | Effect number           |
|    7 |         P  | Period                  |

If effect number is not supported, the cube is black.
0 is black, first effect is 1

Period is in arbitrary units for using the full range of the slider.
Lower is faster, 0 is a special value for "normal speed".

Programs
--------

./animation_by_sacn.py
Main program with integrated console

./console.py
Only the console which sends data on universe 3
