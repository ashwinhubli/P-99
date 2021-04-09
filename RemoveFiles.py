import os
import shutil
import time

c_time = time.time()
days = 0
path = input('Enter The Name Of Directory:')
seconds  = time.time() - (days*24*60*60)

if(os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown = True):
        for name in files:
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime
            if seconds >= ctime:
                os.remove(path)
                print("Deleted The Path Successfully!")
        for name in dirs:
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime
            if seconds >= ctime:
                shutil.rmtree(path)
                print("Deleted The Path Successfully!")     

else:
    print("Path Not Found!")
