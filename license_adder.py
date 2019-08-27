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

#
# This script adds the content of a given input file (e.g., a license) 
# at the beggining of each file matching a given file extension (e.g., .java).
# It start from the specified root directory (e.g., '.') and performs this 
# recursively
#

import sys
import os

if len(sys.argv) < 2:
	print ("Usage: %s license_file [root_dir] [file_extension]" % sys.argv[0])
	sys.exit(1)

file_a = sys.argv[1]
rootdir='.'
file_extension = '.java'

if len(sys.argv) > 2:
	rootdir = sys.argv[2]
if len(sys.argv) > 3:
	file_extension = sys.argv[3]

with open (file_a, "r") as a:
	lines_a = a.readlines()
	string_a = ''.join(lines_a)
	a.close()
	for root, subdirs, files in os.walk(rootdir):
		for f in files:
			if f.endswith(file_extension):
				file_path = os.path.join(root, f)
				print( file_path )
				with open(file_path, "r") as b:
					lines_b = b.readlines()
					string_b = ''.join(lines_b)
					b.close()
				with open(file_path, "w") as out:
					out.write(string_a + "\n" + string_b)
					out.close()
