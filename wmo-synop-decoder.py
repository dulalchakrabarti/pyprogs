from pymetdecoder import synop as s

synop = "AAXX 01004 88889 12782 61506 10094 20047 30111 40197 53007 60001 81541 333 81656 86070"
output = s.SYNOP().decode(synop)
print(output)
