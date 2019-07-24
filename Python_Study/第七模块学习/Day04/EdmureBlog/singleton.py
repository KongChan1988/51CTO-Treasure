__author__ = 'Administrator'

# class Foo(object):
#     instance = None
#
#     def __init__(self):
#         self.name = 'alex'
#     @classmethod
#     def get_instance(cls):
#         if Foo.instance:
#             return Foo.instance
#         else:
#             Foo.instance = Foo()
#             return Foo.instance
#
#     def process(self):
#         return '123'

# obj1 = Foo()
# obj2 = Foo()
# print(id(obj1),id(obj2))

# obj1 = Foo.get_instance()
# obj2 = Foo.get_instance()
# print(id(obj1),id(obj2))


class Foo(object):
    instance = None

    def __init__(self):
        self.name = 'alex'

    def __new__(cls, *args, **kwargs):
        if Foo.instance:
            return Foo.instance
        else:
             Foo.instance = object.__new__(cls, *args, **kwargs)
             return Foo.instance

# obj1 = Foo()
# obj2 = Foo()
# print(id(obj1),id(obj2))


