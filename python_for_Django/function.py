# def name(fname, lastname):
#     print(f'Full Name: {fname} {lastname}');
#
# name('Mohammad','Ibrahim');

# def person(name, age):
#     print(f'Name: {name}, Age: {age}');
# person('Ibrahim', 27);

# def studentInfo(*details):
#     print(details);
# studentInfo("Mohammad", '27', "Bangladesh", 3.05, 5.11);

# def name(fname='Mohammad', lname='Ibrahim'):
#     print(f'Full Name: {fname} {lname}');
# name('Ohid');

# def student(**studentInfo):
#     print(studentInfo["fname"]);
# student(fname="Mohammad", lname= "Ibrahim", age= 25);

# def details(*student, **studentInfo):
#     print(student,studentInfo);
# details('Mohammad', 'Ibrahim', 'ohid', fname='Hosna', lname='Mobarak', age= 25);

# sum = lambda x, y: x + y;
# print(sum(10, 30));

# print((lambda a, b: a * b)(10, 10));

# def num(n):
#     return n*n;
#
# numbers = [3, 4, 8, 10];
# final_number = list(map(num,numbers));
# print(final_number)

# def num(n):
#     return n*n*n;
# number = [3, 2, 4];
# final = tuple(map(num, number));
# final = set(map(num, number));
# print(final);

# numbers = [1, 3, 4, 7, 9];
# new_num = list(map(lambda x: x*x, numbers));
# new_num = set(map(lambda a:a*a, numbers));
# print(new_num);

# num = ['Mohammad', 'Ibrahim', 'Ohid'];
# new_num = list(map(tuple, num));
# new_num = list(map(list, num));
# new_num = list(map(set, num));
# print(new_num);

# n = [1, 2, 4, 5, 7, 8, 10, 12];
# new_num = list(filter(lambda a: a%2==1,n));
# new_num = tuple(filter(lambda a: a%2==1,n));
# new_num = set(filter(lambda a: a % 2 == 0, n));
# print(new_num);

# from  functools import reduce;

# num = [1, 2, 3, 4, 5, 6];
# new_num = reduce(lambda x,y: x*y, num);
# print(new_num)


# def hof(fn):
#     print(fn.__name__)
#     fn()
# def name():
#     print("Mohamamd Ibrahim");
#
# def friend():
#     print("Jisna");
#
# hof(friend);

# def allName(n):
#     print(n.__name__)
#     n();
#
# def fname():
#     print("Ibrahim");
# def lname():
#     print("Ohid");
#
# allName(fname);
# allName(lname);

# def my():
#     def hello():
#         print("Hello World")
#     return hello()
# my();

# def para(p):
#     def text():
#         print("Bangladesh");
#         p()
#         print("Pakistan");
#
#     return text()
#
#
# def newText():
#     print("Canada")
#
#
# def fruit():
#     print("orange", "banana")
#
# para(fruit)

# def course_name(name, course):
#     print("Hello!", name, "Welcome to Python");
#     print("Your Course Name is", course);
# course_name("Mohammad", "Python");

# def calculate(a, b):
#     add = a + b;
#     return add
# res = calculate(10, 20);
# print(res)

# def calculate(x, y):
#     multi = x * y;
#     return multi
# result = calculate(10, 10);
# print(result)

# def even_num(n):
#     if n % 2 == 0:
#         print("Even Number");
#     else:
#         print("Odd Number");
# even_num(11);

# def  calculate(a, b):
#     return  a + b;
# result =  calculate(10, 20);
# print(result)

# def text(t):
#     """I love Python Language"""
#     return t;
# print(text.__doc__)

# def number(num1, num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multiply = num1 * num2
#     division = num1 / num2
#     return add, sub, multiply, division
#
#
# a,b,c,d = number(10, 5)
# print('Add', a);
# print('Sub', b);
# print('Multiply', c);
# print('Division', d);
