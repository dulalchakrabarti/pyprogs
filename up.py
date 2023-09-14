lines = [line.rstrip('\n') for line in open('up.csv')]
txt = [line for line in lines if line != '']
txt_ = [line.split() for line in txt]
lst = [ line[2] for line in txt_ ]
print lst
