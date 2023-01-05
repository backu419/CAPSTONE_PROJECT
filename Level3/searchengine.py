from exceptions import FileSearcher
from threading import Thread


class SearchManager:
    def _init_(self):
        pass

    def search(self, filename, drives):
        print("search method")
        searcher_threads = []
        file_searchers = []
        for drive in drives:
            print(drive)
            file_searcher = FileSearcher()
            file_searcher.task2(drives, filename)
            search_thread = Thread()
            search_thread.start()
            file_searchers.append(file_searcher)
            searcher_threads.append(search_thread)
        for searcher_thread in searcher_threads:
            searcher_thread.join()
        search_results = []
        for file_searcher in file_searchers:
            search_results.append(file_searcher.s)
        return search_results


if __name__ == '__main__':
    name = input("enter filename: ")
    dire = input("enter dire: ")
    obj = SearchManager()
    data = obj.search(name, dire)
    print(data)
