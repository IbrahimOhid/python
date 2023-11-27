# subject = ["html", "css", "bootstrap", "tailwind css", "javascript"];
# print(subject[3])
#print("html" in subject)
# print("python" not in subject)
# subject = subject + ["python"]
# print(subject)
# print(subject[-1])

# subject = ["html", "css", "bootstrap", "tailwind css", "javascript"];
# subject.append("java")
# subject.append(["python", "c++"]);
# subject.insert(1, "java")
# subject.remove("bootstrap")
# subject.sort();
# subject.reverse()
# subject.pop()
# subject = subject.index("css")
# print(subject)

# num = [1, 2, 3, 5, 3, 4, 3, 4];
# print(num.count(3))

# n = input("Enter a Number: ");
# sum = 0;
# list = n.split();
#
# for x in list:
#     sum = sum + int(x);
# print(sum)

numberOfWord = 0;
numberOfLetter = 0;
numberOfDigit = 0;

n = input("Enter a Text: ");

for x in n:
    x = x.lower();
    if x >= 'a' and x <= 'z':
        numberOfLetter = numberOfLetter + 1;
    elif x >= '0' and x <= '9':
        numberOfDigit = numberOfDigit + 1;
    elif x == ' ':
        numberOfWord = numberOfWord + 1;

print("Number of Letter", numberOfLetter);
print("Number of Digit", numberOfDigit);
print("Number of Word", numberOfWord + 1);

