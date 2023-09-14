def deg2comp(deg):
    '''
    '''
    if deg == '--':
     out = '--'
    elif deg >= 0 and deg < 22.5:
     out = 'N'
    elif deg >= 22.5 and deg < 45:
     out = 'NNE'
    elif deg >= 45 and deg < 67.5:
     out = 'NE'
    elif deg >= 67.5 and deg < 90:
     out = 'ENE'
    elif deg >= 90 and deg < 112.5:
     out = 'E'
    elif deg >= 112.5 and deg < 135:
     out = 'ESE'
    elif deg >= 135 and deg < 157.5:
     out = 'SE'
    elif deg >= 157.5 and deg < 180:
     out = 'SSE'
    elif deg >= 180 and deg < 202.5:
     out = 'S'
    elif deg >= 202.5 and deg < 225:
     out = 'SSW'
    elif deg >= 225 and deg < 247.5:
     out = 'SW'
    elif deg >= 247.5 and deg < 270:
     out = 'WSW'
    elif deg >=270 and deg < 292.5:
     out = 'W'
    elif deg >= 292.5 and deg < 315:
     out = 'WNW'
    elif deg >= 315 and deg < 337.5:
     out = 'NW'
    elif deg >= 337.5 and deg < 360:
     out = 'NNW'
    return out
inp = range(360)
for i in inp:
 print deg2comp(i)
inp = '--'
print deg2comp(inp)
