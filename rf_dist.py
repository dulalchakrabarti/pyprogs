import tabula
# convert PDF into CSV file
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv", pages='all')
