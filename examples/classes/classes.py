#!/usr/bin/env python3


class A:
    def __init__(self):
        self.variable = 1
        self._protected_variable = 2
        self.__private_variable = 3

    def say_hi(self):
        print("Hi ConSolis!",\
               self.variable,\
               self._protected_variable,\
               self.__private_variable)


class B(A):
    def __init__(self):
        super().__init__()
        self.variable = 42


a = A()
print(a.variable)
a.say_hi()

b = B()
b.say_hi()
print(b.variable)
print(b._protected_variable)

# Raises because of private access
try:
    print(b.__private_variable)
except AttributeError as e:
    print("Exception:", e)
