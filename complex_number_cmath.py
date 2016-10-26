#!/usr/bin/python

import math
import cmath
import re

complex_number=raw_input("")

real,img=complex_number.split("+")
#img_1=[int(s) in img.split() if s.isdigit()]
img_1,dummy =img.split("j")

#print "real part:%d" %int(real)
#print "img   part:%d" %int(img_1)
print abs(complex(int(real),int(img_1)))
print cmath.phase(complex(int(real),int(img_1)))
