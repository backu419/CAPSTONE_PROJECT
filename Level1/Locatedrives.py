
# import os
# print(os.popen("fsutil fsinfo drives").read())
# print(os.system('cmd /c "wmic logicaldisk list brief"'))

import psutil,os

class SystemDriveFinder:

    def __init__(self):
        pass

    def find_drives(self):
        print("This is the find drivers method of System Drive Finder Class")

        drives=[]
        for x in range(65, 91):
            if os.path.exists(chr(x) + ":"):
                drives.append(chr(x))
        return drives

    def drives_info(self):
        print(os.popen("fsutil fsinfo drives").read())

if __name__ == '__main__':
    obj = SystemDriveFinder()
    print(obj.find_drives())

