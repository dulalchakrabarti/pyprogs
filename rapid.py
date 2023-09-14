import os
lllo = 70
llla = 25
dlo = 0.16
dla = 0.06
urlo = 75
urla = 30

buf = 'curl '+'\'https://rapid.imd.gov.in/thredds/wms/testArchive/3RIMG_L1B_STD_4.h5?version=1.3.0&CRS=CRS:84&SRS=CRS:84&COLORSCALERANGE=339,954&ELEVATION=0&TIME=2020-12-21T11:15Z&styles=boxfill/greyscale&ABOVEMAXCOLOR=extend&BELOWMINCOLOR=extend&LAYERS=IMG_TIR1&TRANSPARENT=true&FORMAT=image%2Fpng&SERVICE=WMS&REQUEST=GetMap&BBOX='+str(lllo)+','+str(llla)+','+str(urlo)+','+str(urla)+'&WIDTH=256&HEIGHT=256\' -H \'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0\' -H \'Accept: image/webp,*/*\' -H \'Accept-Language: en-US,en;q=0.5\' --compressed -H \'DNT: 1\' -H \'Connection: keep-alive\' -H \'Referer: https://www.rapid.imd.gov.in/rapid/\' -H \'Cookie: _ga=GA1.3.1362926586.1582890005; _gid=GA1.3.1888641813.1608368179\' --output AHM.png'
result = os.system(buf)
if result == 0:
 print 'success'
else:
 result = os.system(buf)
 

'''
gdal_translate -of GTiff -gcp 0.0064 0.0064 70 30 -gcp 255.998 255.995 75 25 -gcp 0.0064 255.994 70 25 "/home/dulal/imgproc/AHM.png" "/tmp/AHM.png"
gdalwarp -r near -order 1 -co COMPRESS=NONE  -t_srs EPSG:4326 "/tmp/AHM.png" "/home/dulal/imgproc/AHM_modified.tif"
fl = open('rapid.sh','w')
lllo = 91.167517-.08
llla = 23.849616-.03
dlo = 0.16
dla = 0.06
urlo = lllo+dlo/2
urla = llla+dla/2
i = 482
j = 174
for i in range(482,491):
 for j in range(174,183):
  buf = 'curl '+'\'https://rapid.imd.gov.in/thredds/wms/testArchive/3RIMG_L1B_STD_4.h5?version=1.3.0&CRS=CRS:84&SRS=CRS:84&service=WMS&request=GetFeatureInfo&BBOX='+str(lllo)+','+str(llla)+','+str(urlo)+','+str(urla)+'&I='+str(i)+'&J='+str(j)+'&TIME=2020-12-08T13:45Z&ELEVATION=0&INFO_FORMAT=text/xml&QUERY_LAYERS=IMG_TIR1&WIDTH=961&HEIGHT=354&layerName=IMG_TIR1\' -H \'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0\' -H \'Accept: application/xml, text/xml, */*; q=0.01\' -H \'Accept-Language: en-US,en;q=0.5\' --compressed -H \'X-Requested-With: XMLHttpRequest\' -H \'DNT: 1\' -H \'Connection: keep-alive\' -H \'Referer: https://rapid.imd.gov.in/rapid/\' -H \'Cookie: JSESSIONID=444298C9558751F5F06A6AF3E95B868A; _ga=GA1.3.1362926586.1582890005\''
  fl.write(buf+'\n')
  fl.write('sleep 5'+'\n')
fl.close()
'''
