import re
import csv
c = 0
outfile = open('outfile.txt', 'w')
csvfile = open('NER tagging dataset.csv', 'r')
for i in csvfile.readlines():   
    line = re.sub(r'\"\,\"\,Other\,', '', i)
    line = re.sub(r'\,\"\,\"\,other\,', ',', line)
    line = re.sub(r'(\,\,Other)*', '', line)
    if(line[-1]=='\n'):
        line = line[0:len(line)-1]
    if(line[-1]==','):
        line = line[0:len(line)-1]
    arr = line.split(',')
    for j in arr:
        if c == 1:
            c = 0
            outfile.write( j + '\n' )
        elif c == 0:
            c = 1    
            outfile.write( j + ',' )
            
