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

from  functools import reduce;

# num = [1, 2, 3, 4, 5, 6];
# new_num = reduce(lambda x,y: x*y, num);
# print(new_num)
