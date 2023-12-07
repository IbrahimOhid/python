# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def hello(self):
#         print("Hello Bangladesh")
#
#
# class B(A):
#     pass
# obj = B("Ibrahim");
# obj.hello()

# class A:
#     def __init__(self, name):
#         self.name = name
#     def hello(self):
#         print('Hello Bangladesh')
#
# class B(A):
#     def __init__(self, name, job):
#         super().__init__(name)
#         self.job = job
#     def hello(self):
#         print(f"{self.name} is a {self.job}")
#
# obj = B("Ibrahim", "Mentor")
# obj.hello();

# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# class B:
#     def __init__(self, job):
#         self.job = job
#
#
# class C(A, B):
#     def __init__(self, name, job):
#         A.__init__(self, name)
#         B.__init__(self, job)
#
#     def title(self):
#         print(f"{self.name} is {self.job}")
#
#
# obj = C('Ibrahim', 'Developer')
# obj.title()


# class Person:
#     def __init__(self, name, sex, profession, study):
#         self.name = name;
#         self.sex = sex;
#         self.profession = profession;
#         self.study = study;
#
#     def state(self):
#         print(f"Name: {self.name}, Sex: {self.sex}, Profession: {self.profession}")
#
#     def behavior(self):
#         print(f"{self.name} working as a {self.profession} and She studies {self.study} a day")
#
#
# people1 = Person("Mohammad", "Male", "Software Developer", "2 Hours");
# people1.state()
# people1.behavior()
#
# people1 = Person("Ebnol", "Male", "Doctor", "5 Hours");
# people1.state()
# people1.behavior()

class student:
    school_name = 'ACD School';

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        print(f'Name: {self.name} Age: {self.age} School: {student.school_name}')




student1 = student('Mohammad', 15)
student1.student_info()

