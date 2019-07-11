import threading
import time
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

            test = self.queue.get()     # Получение теста из очереди
            if test is None:
                break                   # Прерывает выполнение потока, если получен нул
            self.execute_test(test)     # Запуск теста
            self.queue.task_done()      # Сигнал о завершении теста

    def execute_test(self, test):
        try:
            test()                                  # Вызов тестового метода
            results.append("{} passed!"
                           .format(test.__name__))  # Запись успешно прошедшего теста
        except AssertionError:
            results.append("{} failed!"
                           .format(test.__name__))  # Запись проваленого теста
            pass


def main(test_methods, threads_qtt):

    queue = Queue()                     # Создание очереди
    threads = []                        # Массив потоков
    for i in range(threads_qtt):        # Цикл запуска регулируемого количества потоков
        t = TestRunner(queue)           # Создание потока со списком
        t.start()                       # Запуск очереди
        threads.append(t)               # Добавление запущеного потока в массив

    for test in test_methods:           #
        queue.put(test)                 # Заполнение очереди тестовыми методами

    queue.join()                        # Ожидание очереди выполнения задач

    for i in range(threads_qtt):
        queue.put(None)                 # Заполнение очереди Нулами для остановки потоков
    for thread in threads:
        thread.join()                   # Ожидание каждого потока выполнения в нем задач (закрытие потока)
    print(results)


if __name__ == "__main__":
    tests_to_run = Collection().methods # Создание списка всех методов
    start = time.time()
    main(test_methods=tests_to_run, threads_qtt=2)
    print(time.time() - start)
