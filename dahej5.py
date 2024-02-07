import getgfs
f=getgfs.Forecast("0p25")
res=f.get(["gustsfc"],":", 21.67,72.51)
print(res.variables["gustsfc"].data)
