import pytest
# from project.folder.subfolder.filename import functionname
# import requi9red module
import sys
sys.path.append("..")
from Level1.Locatedrives import SystemDriveFinder
from Level6.dbconnect import FileSearcher

# from Level1.Locatedrives import SystemDriveFinder
# from Level6.dbconnect import FileSearcher

class Test_Drive:
    def test_Drive(self):
        obj = SystemDriveFinder()
        self.expected=obj.find_drives()  #['C', 'D']
        print(self.expected)
        self.actual=['C']
        assert self.expected == self.actual

    def test_searchfile(self):
        obj = FileSearcher()
        d = obj.task2('C://','file.txt')
        print(d)
        self.expected=d
        self.actual_res = 'C://file.txt'
        assert self.expected == self.actual_res
