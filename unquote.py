def rmquote(inp):
    '''
    '''
    out = inp.split('-')
    return(out[0]+'-'+out[1]+'-'+out[2])
xx = rmquote('2022-03-05T23:45:00.000Z')
print(xx)
