fl = open ('vill.csv','w')
lines = [line.rstrip('\n') for line in open('IN.txt')]
for line in lines:
 line = line.strip().split('	')
 #if line[3][:1] == 'W':
 fl.write(line[1]+','+line[2]+','+line[3]+','+line[5]+','+line[7]+','+line[9]+','+line[10]+'\n')
