import threading
from queue import Queue
from threads_part.tests_collection import Collection


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

        test()


def main(test_methods, threads_qtt):

    queue = Queue()

    for i in range(threads_qtt):

        tr = TestRunner(queue)
        tr.setDaemon(True)
        tr.start()

    for test in test_methods:
        queue.put(test)

    queue.join()

if __name__ == "__main__":
    test_methods = Collection().govnokod_1
    main(test_methods=test_methods, threads_qtt=4)
