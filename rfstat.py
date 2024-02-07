import pandas as pd
#read lat long file & store in adictionary
df = pd.read_csv('asos.csv')
df1 = df.loc[df['valid'] == "2023-12-27 03:00"]
df1.to_csv('vis.csv')

'''
for num in range(len(lst)):
 txt = lst[num]
 line = txt[0].split()
 if len(line) == 10:
   print(line[1],line[2],line[-2],line[-1])
   gl.write(line[1]+','+line[2]+','+line[-2]+','+line[-1]+'\n')
 elif len(line) == 11:
  print(line[1],line[2],line[3],line[-2],line[-1])
  gl.write(line[1]+line[2]+','+line[3]+','+line[-2]+','+line[-1]+'\n')
 elif len(line) == 12:
  print(line[1],line[2],line[3],line[4],line[-2],line[-1])
  gl.write(line[1]+line[2]+line[3]+','+line[4]+','+line[-2]+','+line[-1]+'\n')
 elif len(line) == 13:
  print(line[1],line[2],line[3],line[4],line[5],line[-2],line[-1])
  gl.write(line[1]+line[2]+line[3]+line[4]+','+line[5]+','+line[-2]+','+line[-1]+'\n')
 else:
  print(line[1],line[2],line[-2],line[-1])
  gl.write(line[1]+','+line[2]+','+line[-2]+','+line[-1]+'\n')
'''
