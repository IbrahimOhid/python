# class declare 🔽

# class student:
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
# student_one = student("Ibrahim", "Javascript");
# student_Two = student("Ohid", "Python");
#
# print(student_one.name);
# print(student_one.course);
# print(student_Two.name);
# print(student_Two.course);

# class student:
#     training_center = "Ibrahim IT";
#     def __init__(self, name, id):
#         self.name = name;
#         self.id = id;
#
#
# student_one = student("Ibrahim", "101")
# student_two = student("Ohid", "1029")
# print(student_two.id);
# print(student_one.training_center);
# print(student_two.training_center)

# class Time_Manager:
#
#     @staticmethod
#     def get_Current_time():
#         return "2023-07-02"
#
# print(Time_Manager.get_Current_time())

# import datetime
# class real_Time:
#     @staticmethod
#     def current_time():
#         return datetime.datetime.now()
#
# print(real_Time.current_time());

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def details(self):
#         return "My name is {}".format(self.name)
#
#
# class Student(person):
#     def __init__(self, name, age, course):
#         self.course = course
#         person.__init__(self, name, age)
#
#
# student_one = Student("Ibrahim", 26, "python")
# print(student_one.details());

class A:
    def __init__(self):
        print("From A")

class B(A):
    def __init__(self):
        print("From B")
        A.__init__(self)

class C(B):
    def __init__(self):
        print("From C")
        B.__init__(self)


c = C();