# num = [10, 20, 30, 40, 50];
# print(num);
#
# index = 0;
# n = len(num)
# while index <= n:
#     print(num[index])
#     index = index + 1;

# numbers = [10, 20, 30, 40, 50];
# sum = 0;
# for x in numbers:
#     print(x)

# for x in numbers:
#     sum = sum + x;
# print(sum)


# 1) 1 + 2 + 3 + …. + n

# n = int(input("Enter a Number : "));
# sum = 0
# for x in range(1, n+1, 1):
#     sum = sum + x;
# print(sum);

# 2) 2 + 4 + 6 + …. + n  (sum of even numbers from 1-n )

# n = int(input("Enter a Number : "));
# sum = 0;
# for x in range(2, n+1, 2):
#     sum = sum + x;
# print(sum);

# 3) 1 + 3 + 5 + …. + n  (sum of odd numbers from 1-n )

# n = int(input("Enter a Number: "));
# sum = 0;
# for x in range(1, n+1, 2):
#     sum = sum + x;
# print(sum);

# 4) 4 + 8 + 12 + … + n

# n = int(input("Enter a Number: "));
# sum = 0;
# for x in range(4, n+1, 4):
#     sum = sum + x;
# print(sum);

# 5) 1^2 + 2^2 + 3^2 + … + n^2

# n = int(input("Enter a Number: "));
# sum = 0;
# for x in range(1, n+1, 1):
#     sum = sum + x**x;
# print(sum);

# 6) 2^2 + 4^2 + 6^2 + … + n^2

# n = int(input("Enter a Number: "));
# sum = 0;
# for x in range(2, n+1, 2):
#     sum = sum + x**x;
# print(sum);

# 7) 1 + ½ + 1/3 + …. + 1/n

# n = int(input("Enter a Number : "));
# sum = 0;
# for x in range(1, n+1, 1):
#     sum += 1/x;
#
# print(sum);

# 8) 2 x 4 x 6 x …. x n  (sum of even numbers from 1-n )

# n = int(input("Enter a Number : "));
# sum = 0;
# for x in range(2, n+1, 2):
#     sum += x * x;
# print(sum);

# 9) 1 x 3 x 5 x …. x n  (sum of odd numbers from 1-n )
#
# n = int(input("Enter a Number : "))
# sum = 0;
# for x in range(1, n+1, 2):
#     sum += x * x;
# print(sum);

# 10) 4 x 8 x 12 x … x n

# n = int(input("Enter a Number : "));
# sum = 0;
# for x in range(4, n+1, 4):
#     sum += x * x;
# print(sum);

# file = open('../text.txt', 'r');
# # search_word = ["Python", "C", "OOP", "Hello", "Java]" 💓💓💓💓💓💓💓💓
# print(file.read())

"""
*
**
***

*
***
*****
"""
# n = 3;
# for i in range(n+1):
#     print(i * "*");

# n = 3;
# for i in range(n+1):
#     print((2*i-1)*"*");

# n = 6;
# for i in range(n+1):
#     print(i * "*");

# n = 5;
# for i in range(n+1):
#     print((2*i-1) * "*")

# from random import randint;

# guess_num = int(input("Enter a number : "));
# random_num = randint(1, 50);
#
# if guess_num == random_num:
#     print("You Win");
#     print("Random Number Was", random_num);
# else:
#     print("lost")

from random import randint;

for x in range(1, 6):
    low = 1;
    high = 50;

    guessNumber = int(input("Enter a Number 1 to 50: "));
    correct_answer = randint(low, high);
    if guessNumber < correct_answer:
        print("Correct answer is greater!");
        print("Guess Number Was", correct_answer)
    elif guessNumber > correct_answer:
        print("Correct answer is smaller!")
        print("Guess Number Was", correct_answer)
    elif guessNumber == correct_answer:
        print("You Win");
        print("Guess Number Was", correct_answer)
    else:
        print("You Lose!")
