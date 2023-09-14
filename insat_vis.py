from PIL import Image
im = Image.open("3Dasiasec_vis.jpg")
cropped = im.crop((113,235,1120,1115))
#cropped.save('out.jpg')
w,h = cropped.size
new = Image.new('RGB',(w,h))
for i in range(w):
 for j in range(h):
  k = cropped.getpixel((i,j))
  if k[0] == k[1] and k[1] == k[2]:
   new.putpixel((i,j),k)
  else:
   new.putpixel((i,j),(0,0,0))
new.save('out.jpg')

