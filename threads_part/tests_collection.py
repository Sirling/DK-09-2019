import random
import inspect


class Collection:

    def __init__(self):
        self.methods = []
        methods_list = inspect.getmembers(self, predicate=inspect.ismethod)
        for method in methods_list:
            self.methods.append(method[1])

    bool_list = (0, 1)

    def test_1(self):

        assert 0 == random.choice(self.bool_list)

    def test_2(self):

        assert 0 == random.choice(self.bool_list)

    def test_3(self):

        assert 0 == random.choice(self.bool_list)

    def test_4(self):

        assert 0 == random.choice(self.bool_list)

    def test_5(self):

        assert 0 == random.choice(self.bool_list)

    def test_6(self):

        assert 0 == random.choice(self.bool_list)

    def test_7(self):

        assert 0 == random.choice(self.bool_list)

    def test_8(self):

        assert 0 == random.choice(self.bool_list)

    def test_9(self):

        assert 0 == random.choice(self.bool_list)

    def test_10(self):

        assert 0 == random.choice(self.bool_list)


