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
