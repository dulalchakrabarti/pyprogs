def clean(buff):
    '''
    input: raw strings with unprintable ascii
    output: printable ascii
    '''
    store = ''
    for idx in range(len(buff)):
     if ord(buff[idx]) <127:
      store = store + buff[idx]
    return store
# open csv output with ; as the separator because , is used inside the text by whatsapp senders
gl = open('mandi.csv','w')
buf = ''
# iterate over whatsapp text file named 'mandi.txt'
with open("mandi.txt") as fl:
 lines = [x.strip() for x in fl.readlines()]
 for line in lines:
# use '[' as message separator
  if '[' in line:
   if len(buf) > 0:
    tmp = clean(buf) #clean
    gl.write(tmp+';')# write with ';' as separator
   buf = ''
  else:
   buf = buf+'\n'+line
gl.close()

