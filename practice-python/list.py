# my_car = ["Bmw", "audi", "toyota"];
# print(my_car);

# countries = ["Bangladesh", "India", "Pakistan", "africa"];
#
# print(countries[3]);
# print(countries[-4]);

#MODIFY LIST

# countries = ["India", "pakistan", "africa", "jordan"];
# print(countries);
# countries[3] = "Bangladesh";
# print(countries);
#
# countries[-3] = "Norway";
# print(countries);

#REMOVE LIST

# countries = ["Bangladesh", "Pakistan", "Indonesia", "Afganistan", "Oman"];
# print(countries);
# del countries[2];
# print(countries);
# del countries[-1];
# print(countries);

# fruits = ["Banana", "Orange", "Apple", "Water Melon"];
# fruits.pop();
# # remove_item = fruits.pop();
# # print(remove_item);
# print(fruits);
# fruits.pop(2);
# print(fruits);

#REMOVE METHOD

# word = ["i", "c", "e", "w", "c", "x"];
# word.remove("c");
# print(word);

#SLICE METHOD

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
#print(numbers[1:6]);
#print(numbers[:7]);
# print(numbers[3:])
# print(numbers[-6:-2])

#SORT METHOD

# numbers = [3, 7, 1, 9, 11, 55, 2];
# numbers.sort(reverse=True);
# print(numbers);

# fruits = ["mango", "banana", "Orange", "Papaya", "Apple"];
# fruits.sort();
# print(fruits);

# numbers = [1, 33, 2, 5, 4, 55];
# sorted_num = sorted(numbers);
# sorted_num_rev = sorted(sorted_num, reverse=True)
# print(numbers);
# print(sorted_num);
# print(sorted_num_rev);

#COPY METHOD

# numbers = [30, 33, 55, 10, 5];
# print(numbers);
# print(numbers.copy());

#EXTENT METHOD

# numbers = [3, 4, 5, 7];
# numbers_one = [8, 9, 10, 11];
# numbers.extend(numbers_one);
# print(numbers);

#APEND METHOD

fruits = ["Banana", "orange", "Apple"];
# print(fruits);
# fruits.append("grape");
# print(fruits);
fruits.insert(1, "grape");
print(fruits);