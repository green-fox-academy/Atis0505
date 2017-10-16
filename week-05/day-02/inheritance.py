class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class LazyStudent(Person):
    def __init__(self, name, age, neptun_handle):
        super().__init__(name, age)
        self.neptun_handle = neptun_handle


class LazyStudenWithGlasses(LazyStudent):
    def __init__(self, name, age, neptun_handle, color_of_glasses):
        super().__init__(name, age, neptun_handle)
        self.color_of_glasses = color_of_glasses