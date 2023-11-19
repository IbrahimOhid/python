# file = open("../text.txt",  "r");
# print(file.read());

# file = open("../text.txt", "r");
# print(file.readline());
# print(file.readline());
# print(file.readline());

# while True:
#     line = file.readline()
#     if not line:
#         break;
#     print(line);

# print(file.readlines());

# with open("../text.txt", "r") as file:
#  print(file.read());

# with open("../text.txt", "w") as file:
#     file.write("I love Bangladesh");

# with open("../text.txt", "a") as file:
#  file.write(" Hello World!");

# with open("../text.txt", "w") as file:
#     file.write("I love pakistan\n")
#     my_list = ["I learn python\n" "I love javascript\n" "HTML\n"];
#     file.writelines(my_list);

# with open("text2.txt", "w") as file:
#     file.write("Hello bhai")

import  os

path = 'text2.txt'
os.remove(path);
