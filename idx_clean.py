lines = [line.rstrip('\n') for line in open('idx.csv')]
fl = open('idx1.csv','w+')
for line in lines:
 line_ = line.split(',')
 if line_[-1] != '':
  fl.write(line+'\n')
fl.close()
