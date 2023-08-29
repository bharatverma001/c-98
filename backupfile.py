import os
import shutil
source=input("enter source folder name")
destination=input("enter destiation folder name")
source=source+"/"
destination=destination+"/"
list_of_files=os.listdir(source)
for x in list_of_files:
    shutil.copy(source+x,destination)
 