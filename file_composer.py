#!/usr/bin/python
#MIT License
#
#Copyright (c) 2017 Mirko Bez
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


#Description: this program takes two input text-files (A and B). 
#It creates a new file (out), by combining A and B, alternating stepA lines
#from A and stepB lines from B, until it reaches the end of A or B.

#Use Scenario: fill some missing data in a benchmark file

import sys
import os


if len(sys.argv) < 6:
	print "Usage: %s <srcA> <srcB> <stepA> <stepB> [out]" % (sys.argv[0])
	exit(1);
else:
	file_a = sys.argv[1]
	file_b = sys.argv[2]
	step_a = int(sys.argv[3])
	step_b = int(sys.argv[4])
	file_out = sys.argv[5]




with open (file_a, "r") as a, open(file_b, "r") as b, open(file_out, "w") as out:
	lines_a = a.readlines()
	ptr_a = 0
	n_a = len(lines_a)
	
	lines_b = b.readlines()
	ptr_b = 0
	n_b = len(lines_b)
	while(ptr_a < n_a and ptr_b < n_b):
		for i in range(ptr_a, ptr_a + step_a):
			out.write(lines_a[i])
		for i in range(ptr_b, ptr_b + step_b):
			out.write(lines_b[i])
		ptr_a += step_a
		ptr_b += step_b
	a.close()
	b.close()
	out.close()
