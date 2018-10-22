#!usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode')

#move file command : file name --> directory
shutil.move('raynor.obj', 'ceph_storage/')

#input for renaming file
xname = input('What is the new name for the kerrigan.obj file?')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

