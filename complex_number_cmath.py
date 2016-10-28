#!/usr/bin/python

import math
import cmath
import re

complex_number=raw_input("")
postive_img=re.compile('[0-9]*\+[0-9]*j')
negtive_img=re.compile('[0-9]*-[0-9]*j')
negtive_rel=re.compile('-[0-9]*\+[0-9]*j')
negtive_both=re.compile('-[0-9]*-[0-9]*j')

if re.match(postive_img, complex_number):
	real,img=complex_number.split("+")
elif re.match(negtive_img, complex_number):
	real,img=complex_number.split("-")
elif re.match(negtive_rel, complex_number):
	real,img=complex_number.split("+")
elif re.match(negtive_both, complex_number):
	occurance=[m.start for m in re.finder(negtive_both, complex_number)]
	real=str[:occurance[1]]
	img=str[occurance[1]+1:]

#real,img=complex_number.split("+")
#img_1=[int(s) in img.split() if s.isdigit()]
img_1,dummy =img.split("j")

#print "real part:%d" %int(real)
#print "img   part:%d" %int(img_1)
print abs(complex(int(real),int(img_1)))
print cmath.phase(complex(int(real),int(img_1)))
