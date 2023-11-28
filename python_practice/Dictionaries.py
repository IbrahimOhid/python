# studentId = {
#     101: "Mohammad",
#     102: "Ibrahim",
#     103: "Ohid",
#     104: "Jisan"
# }
# # print(studentId[104]);
# print(studentId.get(105, 'Not a Valid Key'));

# name = ("Mohammad", "ibrahim", "Ohid");
# print(name[0:2]);
# # print(name[2])

# set

# num = {1, 2, 3, 4, 4};
# print(num)

# numbers = [4, 5, 6, 7, 7];
# numbers = set(numbers)
# numbers.add(8)
# numbers.remove(6)

#print(8 in numbers)
# print(4 in numbers)

num1 = {1, 2, 3, 4, 5, 4, 7};
num2 = set([6, 7, 8, 9, 4, 10]);
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)