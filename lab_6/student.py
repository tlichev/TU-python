from person import Person
class Student(Person):
    def __init__(self,name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.__university = university
        self.__yearofstudy = yearofstudy

    def get_university(self):
        return self.__university

    def set_university(self, university):
        self.__university = university

    def get_yearofstudy(self):
        return self.__yearofstudy

    def set_yearofstudy(self, yearofstudy):
        self.__yearofstudy = yearofstudy

    def print_info(self):
        print(f"{self.__university}, {self.__yearofstudy}")


student1 = Student("Pencho", "Georgiev", 23, "BG", "TU", "2020")
student1.print_info()