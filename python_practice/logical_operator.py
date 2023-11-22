# And operator 🔻

# num1 = 1110;
# num2 = 440;
# num3 = 30;
#
# if num1 > num2 and num1 > num3:
#     print(num1);
# elif num2 > num1 and num2 > num3:
#     print(num2);
# else:
#     print(num3);

# Or operator 🔻

# vowel = str(input("Enter a Vowel : "));
# if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or  vowel == 'U':
#     print("Vowel = {}".format(vowel));
# else:
#     print("It is not Vowel");

mark = 4;
if 80 <= mark <= 100:
    print("A+");
elif 70 <= mark <= 79:
    print("A");
elif 60 <= mark <= 69:
    print("B");
elif 50 <= mark <= 59:
    print("C");
elif 40 <= mark <= 49:
    print("D");
else:
    print("F")