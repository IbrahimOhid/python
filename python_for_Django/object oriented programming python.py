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

class parent:
    def __init__(self, f_name, m_name):
        self.father_name = f_name
        self.mother_name = m_name

    def parent_info(self):
        print(f"Father Name: {self.father_name}, Mother Name: {self.mother_name}");


# p1 = parent("Mohammad Hanif", "Mostora Begum");
# p1.parent_info()


class Child(parent):
    def __init__(self, f_name, m_name, c_name, edu):
        super().__init__(f_name, m_name)
        self.child_name = c_name;
        self.education = edu;

    def child_info(self):
        print(
            f'My Father Name is : {self.father_name}, My Mother Name is : {self.mother_name}, Child Name: {self.child_name},Child Education Level: {self.education}');


child1 = Child('Mohammad  Hanif', 'Mostora Begum', 'Ibrahim', 'Diploma in Mechanical Engineering');
child2 = Child('Mohammad  Hanif', 'Mostora Begum', 'Ebnol', 'HSC');
child1.child_info();
child2.child_info();
