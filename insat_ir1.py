from PIL import Image
col = {}
im = Image.open("3Dasiasec_ir1.jpg")
cropped = im.crop((8,91,1224,1308))
w,h = cropped.size
new = Image.new('RGB',(w,h))
for i in range(w):
 for j in range(h):
  k = cropped.getpixel((i,j))
  if col.has_key(k):
   col[k] = col[k]+1
  else:
   col[k] = 1
for i in range(w):
 for j in range(h):
  k = cropped.getpixel((i,j))
  if col[k] > 100 and k[0] > 100 and k[0] < 230:
   new.putpixel((i,j),col[k])
  else:
   new.putpixel((i,j),(0,0,0))
new.save('out.jpg')

