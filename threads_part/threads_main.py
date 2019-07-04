import threading
from threads_part.collection import Collection
import inspect

def collect_test_methods():

    result_list = []
    parser = Collection()
    methods_list = inspect.getmembers(parser, predicate=inspect.ismethod)
    for element in methods_list:
        result_list.append(element[0])
    print(result_list)

collect_test_methods()
