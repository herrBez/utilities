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


import sys
import os



input_length = len(sys.argv)

if input_length < 3:
    print ("Usage: %s input_file (input_file | epsilon)* output" % (sys.argv[0]))
    exit(1)
output=sys.argv[input_length-1]
inputs=sys.argv[1:input_length-1]


lines=[]

for i in range(len(inputs)):
    f = open(inputs[i], "r")
    
    lines.append([x.strip() for x in f.readlines()])
    
    f.close()


with open(output, "w") as out:
    
    finished=False
    row_number=0
    
    while not finished:
        finished=True
        for i in range(len(lines)):
            if row_number < len(lines[i]):
                out.write(lines[i][row_number])
                finished=False
            if i != len(lines)-1:
                out.write(",")
        
            
        row_number = row_number + 1
        out.write("\n")

