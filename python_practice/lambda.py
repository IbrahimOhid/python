# a = (lambda a, b : a * a + 2 * a * b + b * b)(2, 3);
# print(a)

# b = (lambda x, y : x + y -x)(10, 5);
# print(b)

# z = (lambda y: y * y * y)(3);
# print(z)

# map

# def square(x):
#     return x * x;
# num = [1, 2, 3, 4, 5];
#
# result = list(map(square,num));
# print(result)

# num = [1, 2, 3, 4, 5];
# result = list(filter(lambda x: x%2==0, num))
# print(result)

# Zip function

# id = [101, 102, 103, 104, 105, 106];
# name = ["Ibrahim", "ohid", "mohammad", "ebna", "osman", "ebnol"];
# print(list(zip(id, name)))

# Recursion

# def num(n):
#     if n == 1:
#         return 1
#     else:
#         return  n * num(n-1)
# print(num(4))

# file

# file = open("text.txt", "r");
# text = file.read();
# print(text)

# file = open("text.txt", "a");
# file.write("Ibrahim");
# print(file)

file = open('text.txt', 'w');
file.write("Hello World")
