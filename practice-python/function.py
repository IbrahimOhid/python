# def welcome_msg():
#     print("Welcome to Python Courser !!!");
#
# def welcome_message():
#     print("Welcome to Javascript Course !");

# stu1 = "Mohammad";
# welcome_msg();
#
# stu2 = "Ibrahim";
# welcome_message();
#
# stu3 = "ohid";
# welcome_msg();

# def user_info(first_name, last_name):
#     print("User First Name is {}".format(first_name));
#     print("User last Name is {}".format(last_name));
#     print("User Full Name is {} {}".format(first_name, last_name))
#
# # user_info("Mohammad", "Ibrahim");
# #user_info(first_name="Mohammad", last_name="Ibrahim");
# user_info(last_name="Jisan", first_name="Mobarak");

# square = lambda a: a * 2;
# print(square(4));
#
# add = lambda a, b: a + b;
# print(add(50, 30));
#
# multiply = lambda z, y: z ** y;
# print(multiply(2, 6));
#
# vag = lambda  a, b: a / b;
# print(int(vag(10,2) + 3));

# time statement 🔽

#import time;

# print(time.time());
# print(time.ctime());
# print("I am Mohammad Ibrahim");
# time.sleep(3);
# print("I am learning python");
#print(time.localtime());

# import datetime;

# print(datetime.datetime.now());
# print(datetime.datetime.utcnow());
#print(datetime.date.today());

# current_time = datetime.datetime.now();
# time_struct = current_time.timetuple();
# print(time_struct[0]);
# print(time_struct[1]);
# print(time_struct[2]);
# print(time_struct[3]);
# print(time_struct[4]);
# print(time_struct[5]);
# print(time_struct[6]);
# print(time_struct[7]);
# print(time_struct[8]);

# from  datetime import datetime;
#
# current_time = datetime.now();
# print(current_time);
# print(datetime.strftime(current_time, "%d/%m/%Y %H:%M:%S"));

# from datetime import datetime;
#
# date_String = "07, May, 1997";
# date_formating = datetime.strptime(date_String, "%d, %B, %Y");
# print(date_formating);

