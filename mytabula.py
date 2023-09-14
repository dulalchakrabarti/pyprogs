import tabula
df = tabula.read_pdf("rf.pdf", pages="all")
print len(df)
