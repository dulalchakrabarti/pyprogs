import datetime

def date_time(hr):
    '''
    '''
    out = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out = out.split()
    out = out[0].split('-')
    out = int(out[-1])
    if hr == 0:
     out = str(out)+'/'+'0600'
    elif hr == 6:
     out = str(out)+'/'+'1200'
    elif hr == 12:
     out = str(out)+'/'+'1800'
    elif hr == 18:
     out = out + 1
     out = str(out)+'/'+'0000'
    elif hr == 24:
     out = out + 1
     out = str(out)+'/'+'0600'
    elif hr == 30:
     out = out + 1
     out = str(out)+'/'+'1200'
    elif hr == 36:
     out = out + 1
     out = str(out)+'/'+'1800'
    elif hr == 42:
     out = out + 2
     out = str(out)+'/'+'0000'
    elif hr == 48:
     out = out + 2
     out = str(out)+'/'+'0600'
    elif hr == 54:
     out = out + 2
     out = str(out)+'/'+'1200'
    elif hr == 60:
     out = out + 2
     out = str(out)+'/'+'1800'
    elif hr == 66:
     out = out + 3
     out = str(out)+'/'+'0000'
    elif hr == 72:
     out = out + 3
     out = str(out)+'/'+'0600'
    elif hr == 78:
     out = out + 3
     out = str(out)+'/'+'1200'
    elif hr == 84:
     out = out + 3
     out = str(out)+'/'+'1800'
    elif hr == 90:
     out = out + 4
     out = str(out)+'/'+'0000'
    elif hr == 96:
     out = out + 4
     out = str(out)+'/'+'0600'
    elif hr == 102:
     out = out + 4
     out = str(out)+'/'+'1200'
    elif hr == 108:
     out = out + 4
     out = str(out)+'/'+'1800'
    elif hr == 114:
     out = out + 5
     out = str(out)+'/'+'0000'
    return out
lst = range(0,120,6)
for i in lst:
 print date_time(i)

