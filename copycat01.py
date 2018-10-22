#!usr/bin/env python3
import shutil
import os

#setting home directory
os.chdir('/home/student/mycode/')

#making a copy of the file

shutil.copy('5G_research/sdn_network.txt', '5G_research/sdn_network.txt.copy')

#making a backup of the folder
shutil.copytree('5G_research/', '5G_research_backup/')


