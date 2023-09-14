import h5py
import glob
for name in glob.glob('3DIMG*.h5'):
 print '--------'+name+'-----------------'
 f = h5py.File(name, 'r+')
 f.keys()
 f.values()
 members = []
 f.visit(members.append)
 for i in range(len(members)):
    print members[i]
 print '-------------------------'

