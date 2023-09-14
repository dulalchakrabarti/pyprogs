count = 0
grid = []
gfl = open('grid_file.csv','w')
gfl.write('sn'+','+'lat'+','+'lon'+'\n')
for i in range(61,100):
 for j in range(1,40):
  count+=1
  lat = j
  lon = i
  grid.append([lat,lon])
  gfl.write(str(count)+','+str(lat)+','+str(lon)+'\n')
#print(grid)
print(count)
