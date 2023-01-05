import os
import threading
from time import perf_counter
import multiprocessing as mp


class FileSearcher:
    def __init__(self):
        self.s=""
        pass

    def task2(self, drive, s):
        try:
            c = 0
            for root, dir, files in os.walk(drive):
                for name in files:
                    filepath = os.path.join(root, name)
                    if s in name:
                        c = c + 1
                        print(filepath)
            if c == 0:
                print("file not found")
            else:
                print(f"{c}files.")

        except:
            pass
    def run(self):
        pass


if __name__ =='__main__':
    obj=FileSearcher()
    driv,file_nam=input("drive name"), input("file search")
    start_time = perf_counter()
    obj.run()
    t2 = threading.Thread(target=obj.task2, args=(driv, file_nam))
    t2.start()
    t2.join()
    end_time = perf_counter()

    print(f'{end_time - start_time} seconds')


    # p2 = mp.Process(target=obj.task2, args = (drive, file_name))
    # start_time = perf_counter()
    # p2.start()
    # p2.join()
    # end_time = perf_counter()
    # print(f'{end_time - start_time} seconds')
