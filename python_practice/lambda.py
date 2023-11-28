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

num = [1, 2, 3, 4, 5];
result = list(filter(lambda x: x%2==0, num))
print(result)
