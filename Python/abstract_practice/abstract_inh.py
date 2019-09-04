from abc import ABC, abstractmethod


class InhABC(ABC):

    value = 5

    def output_base(self):
        print("Heresy")

    @classmethod
    @abstractmethod
    def abstract_output(cls):
        print("This is abstract method. You won't see it")

    @property
    @abstractmethod
    def abstract_property(self):
        pass

    @abstract_property.setter
    @abstractmethod
    def abstract_property(self, param):
        self.value = param

    @abstract_property.getter
    @abstractmethod
    def abstract_property(self):
        return self.value


class MyABC(InhABC):

    def __init__(self):
        super(MyABC, self).__init__()

    def abstract_output(self):
        print("Output of class My_ABC")

    @property
    def abstract_property(self):
        return self.value

    @abstract_property.setter
    def abstract_property(self, param):
        self.value = param


MyABC().abstract_output()
print(type(MyABC().abstract_property))
