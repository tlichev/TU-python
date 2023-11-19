from person import Person
class Lecturer(Person):
    def __init__(self,name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.__university = university
        self.__experience = experience

    def get_university(self):
        return self.__university

    def set_university(self, university):
        self.__university = university

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def print_info(self):
        print(f"{self.__university}, {self.__experience}")


lecturer1 = Lecturer("Pencho", "Georgiev", 23, "BG", "TU", "56")
lecturer1.print_info()