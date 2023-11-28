# def add(a, b):
#     sum = a + b;
#     print(sum)
#     sum = a - b;
#     print(sum)
# add(20, 10)

# def muli(x, y):
#     result = x * y;
#     return result;
#
# result = muli(10, 2);
# print(result)

# def large(c, d):
#     if c > d:
#         return c
#     else:
#         return d
# print(large(60, 40))

# def information(*details):
#     print(details)
# information("101", "Mohammad");
# information("103", "Ibrahim", 3.05);

# def add(*num):
#     sum = 0;
#     for x in num:
#         sum = sum + x;
#     print(sum);
#
# add(10, 20);
# add(10, 20, 30);
# add(10, 20, 30, 60);

def student_info(**details):
    print(details["gpa"]);
student_info(id = 101, name = "Ibrahim", gpa=3.05);
student_info(id=103, name="ohid", gpa=3.05);
