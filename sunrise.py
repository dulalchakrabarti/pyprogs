import tabula
import re
tabula.convert_into("Cochin.pdf", "sunrise.csv", output_format="csv",pages='all')
lines = [line.rstrip('\n') for line in open('sunrise.csv')]
for line in lines:
 line = line.split(',')
 print line[0],line[1],line[2],line[3],line[4]

