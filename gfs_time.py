from datetime import date, datetime, timedelta
#start = date(1-1-1 00:00:0.0)
def str2dec(strs):
    '''
    '1-1-1T00:00:00.000Z'
    '''
    stm = strs
    dt = datetime.strptime(stm, '%Y-%m-%dT%H:%M:%S.%fZ')
    tm = datetime.timestamp(dt)
    return(tm)
def dec2str(dec):
    '''
    '2022-03-22T21:30:00.000Z'
    '''
    timestamp = dec
    dt_object = datetime.fromtimestamp(timestamp)
    return(dt_object)
dt_tm = '2001-1-1T0:0:0.0Z'
print(str2dec(dt_tm))
