# tuple statement 🔽

#fruits = ("Mango", "Orange", "Banana", "Grape", 1, 2, 3, 4, [2.3, 4.33, 2, 1]);
#fruits = "Banana", "Orange", "Grape", 1, 2, 3, 6;
# print(fruits);
# print(type(fruits));

# numbers = 1, 3, 4, 5, 6;
# print(numbers);
# print(type(numbers));

# fruits = ("Mango", "Orange", "Banana", "Grape");
# print(fruits[3]);

# fruit = ("Mango", "Banana", "Orange");
# fruit = list(fruit);
# fruit[1] = "Apple";
# fruit.append(1);
# fruit.append(2);
# fruit.append(3);
# fruit = tuple(fruit);
# print(fruit);
#
# fruit = list(fruit);
# fruit.remove(2);
# fruit = tuple(fruit);
# print(fruit);

# tuple looping statement 🔽

# fruits = ("Mango", "Orange", "Kiwi", "Banana", "Orange");
#
# for fruit in fruits:
#     print(fruit);
# print("__________")
#
# for i in range(0, len(fruits)):
#     print(fruits[i]);

# tuple joining statement 🔽

# odd_num = (1, 3, 5, 7, 9);
# even_num = (2, 4, 6, 8, 10);
# user_name = ("Mohammad", "Ibrahim");
# numbers = odd_num + even_num + user_name;
# print(numbers);

# set declaration 🔽

# fruit = {"Mango", "Orange", "banana", "Grape", "Mango", "Orange"};
# print(fruit);
# print(type(fruit));

#fruit = set(("orange", "mango", "Apple"));
# fruit = set(["orange", "mango", "Apple", "mango"]);
# print(fruit);
# print(type(fruit));

# fruit = {"Orange", "Mango", "Banana"};
# print("kiwi" in fruit);

# set add 🔽

# user = {"Mohammad", "Ibrahim"};
# print(user);
# user.add("Ohid");
# print(user);
# user.add((1, 3, 4));
# print(user);

# set remove 🔽

# user = {"mohammad", "ibrahim", "ohid"};
# print(user);
# # user.remove("ibrahim");
# # print(user);
# user.discard("ohid");
# user.discard("ebnol");
# print(user);

# set looping 🔽

# user = {"Mohammad", "Jishan", "faruk", "touhid"};
# for user_name in user:
#     print(user_name);

# dictionary declaration 🔽

# student = {
#     'name': 'Mohammad Ibrahim',
#     'skills': ['HTML5', 'CSS', 'Javascript'],
#     'exp': '2 years'
# }
# print(student['name']);
# print(student['exp']);

# print(student.get('name'));
# print(student.get('exps', "Not found!!!"))

# print(student);
# student['name'] = 'ohid';
# print(student);
# student["exp"] = '8';
# print(student);

# student.update({
#     'name': "Ibrahim bhai",
#     'exp': 8,
#     'skills': ['javascript', 'python'],
#     'id': 22
# })
# print(student)

# student = {
#     'name': 'Mohammad Ibrahim',
#     'skills': ['HTML5', 'CSS', 'Javascript'],
#     'exp': '2 years',
#     'company': 'loga ase dot com',
#     'address': 'home'
# }

# del student['name'];
# print(student);

# print(student.keys());
# print(student.values());
# print(student.items());

# for current_key in student.keys():
#     print(current_key);
# print('____________')
#
# for current_key in student.keys():
#     print(current_key, student[current_key]);
# print('____________')
#
# for key, value in student.items():
#     print(key, value);

# student = {'name':'ibrahim', 'age': 25};
# student_details = student.copy();
# print(student_details);

# nested dictionary declaration 🔽

courses = {
    1: {
        'name': 'Javascript',
        'duration': 3
    },
    2: {
        'name': 'python',
        'duration': 4
    }
}

# print(courses[1]);
# print(courses[1]['duration']);
# print(courses[2]['name']);
courses[2]['finished'] = '3 month';
print(courses[2])

