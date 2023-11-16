# if Statement 🔽

# shirt_price = 500;
# if shirt_price == 500:
#     print("I will buy this shirt.");

# if else statement 🔽

# pant_price = 800;
# if pant_price == 600:
#     print("I will buy this pant");
# else:
#     print("I will return form home");

# if else, else if statement 🔽

# total_marks = 33;
#
# if total_marks >= 80:
#     print("A+");
# elif total_marks >= 60 and total_marks < 80:
#     print("B")
# elif total_marks >= 40 and total_marks < 60:
#     print("C");
# else:
#     print("F");

# apple_price = 270;
#
# if apple_price >= 300:
#     print("I will Buy");
# elif apple_price >= 250 and apple_price < 280:
#     print("I will think this buy");
# else:
#     print("I will return form My Sweet Home");

# user_area = "Mirpur";
# total_price = 100;
#
# if user_area in ["Mirpur", "Dhaka", "Gulsan"]:
#     if total_price >= 600:
#         print("Shipping Cost Free");
#     elif  total_price >= 300  and total_price < 600:
#         print("Shipping Cost 60")
#     else:
#         print("Shipping cost 150");
# elif user_area in ["Chittagong", "Noakhali"]:
#     if total_price >= 400:
#         print("Shipping Cost Free");
#     elif total_price >= 200 and total_price < 400:
#         print("Shipping Cost 40");
#     else:
#         print("Shipping Cost 120");
#
# else:
#     print("Shipping Not Available");

# short hand if 🔽

# y = 10;
# if y == 10 : z = 30;
# print(z)

# short hand if else 🔽

# a = 15;
# a = 30;
# b = 10 if a == 15 else 100;
# print(b);

# for loop 🔽

# fruits_list = ["Banana", "Orange", "Apple", "Papaya"];
# for fruit in fruits_list:
#     print(fruit);

# numbers = [1, 3, 10, 29, 33, 99];
# for all_num in numbers:
#     print(all_num);

# break continue 🔽

# for i in range(0, 10):
#     print(i);

# for i in range(1, 11):
#     if i == 6:
#         break;
#     print(i)
# print("Stop");

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
# print("Stop")

# for i in range(1, 12):
#     if i == 7:
#         continue
#     print(i)
# print("i love bangladesh ")

# item_price = [10, 20, 100, 500, 600];
# total_buget = 1000;
#
# total_count = 0;
#
# for current_item_price in item_price:
#     total_buget -= current_item_price
#     if total_buget < 0:
#         break
#     total_count += 1;
#
# print(total_count)

# total_item_price = [10, 30, 50, 400, 500, 600];
# total_budget = 1000;
#
# total_count = 0;
#
# for current_item_price in total_item_price:
#     total_budget -= current_item_price
#     if total_budget > 0:
#         total_count += 1
# print(total_count)

# while loop 🔽

# i = 1;
# while i <= 10:
#     print(i);
#     i += 1;
# print("Hello python");

# while break continue statement 🔽

# i = 1;
# while i <= 10:
#     if i == 6:
#         break
#     print(i);
#     i += 1;

# i = 1;
# while i <= 10:
#     if i > 5 and i < 8:
#         i += 1
#         continue
#     print(i);
#     i += 1;

#inline loop syntax 🔽

# my_list = [];
# for i in range(1, 101):
#     my_list.append(i)
# print(my_list)
#
# my_list = [i for i in range(1, 101)]
# print(my_list);

# numbers = [1, 2, 3, 10, 12, 22, 44, 98, 100]
# even_number = [number for number in numbers if number % 2 == 0]
# print(even_number);

# numbers = [1, 3, 10, 22, 11, 15, 17, 91, 81, 71];
# odd_number = [number for number in numbers if number % 2 == 1]
# print(odd_number)

#nested loop 🔽

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print("-----------")
