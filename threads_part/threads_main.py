import threading
from queue import Queue
from threads_part.tests_collection import Collection
from threads_part.test_results import results


class TestRunner(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Запуск потока
        :return:
        """
        while True:
            # Получение теста из очереди
            test = self.queue.get()
            # Запуск теста
            self.execute(test)
            # Сигнал о завершении теста
            self.queue.task_done()

    def execute(self, test):
        self.test_results = []
        try:
            test()
            results.append("Test {} passed!")
            self.test_results.append("Test {} passed!")
        except AssertionError:
            self.test_results.append("Test {} failed!")
            results.append("Test {} failed!")
            self.queue.task_done()


def main(test_methods, threads_qtt):

    queue = Queue()

    for i in range(threads_qtt):

        tr = TestRunner(queue)
        tr.setDaemon(True)
        tr.start()

    for test in test_methods:
        queue.put(test)

    queue.join()
    print()

if __name__ == "__main__":
    test_methods = Collection().methods
    main(test_methods=test_methods, threads_qtt=4)
