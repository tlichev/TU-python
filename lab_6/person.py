class Person:
    def __init__(self, name, family, age, nationality):
        self.__name = name
        self.__family = family
        self.__age = age
        self.__nationality = nationality

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def get_family(self):
        return self.__family

    def set_family(self, family):
        self.__family = family


    def get_age(self):
        return self.age

    def set_age(self, age):
        self.__age = age



    def get_nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def print_info(self):
        print(f"{self.__name}, {self.__nationality}")



person1 = Person("Pesho", "Petrov", 23, "BG")
person1.print_info()




