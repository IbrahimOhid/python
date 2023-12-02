# student_info = {'name': 'ibrahim', 'id': 103, 'gpa': 3.05, 'subject': 'mechanical'};
# print(student_info)

# student = {};
# student['name'] = 'ohid';
# student['id'] = 1033;
# print(student)

# myDic = dict();
# myDic['key'] = 'ohid';
# myDic['gpa'] = 3.05;
# del myDic['gpa']
# print(myDic)

# student_info = {'name': 'ibrahim', 'id': 103, 'gpa': 3.05, 'subject': 'mechanical'};
# del student_info['subject'];
# print(student_info)

# a = dict(name='ohid', gpa=3.05, subj='english');
# b = {'name': 'ibrahim', 'subj': 'mechanical', 'id': 303};
# c = dict(zip(['name', 'id', 'gpa'], ['ibrhaim', 101, 3.05]));
# d = dict([('name', 'ibrahim'), ('id', 3), ('gpa', 3.05)]);
# print(a)
# print(b)
# print(c)
# print(d)

# a = {'name': 'ibrahim', 'id': 1033, 'gpa': 3.05};
# print(a)
# b = dict({'name': 'ibrahim', 'id': 1033, 'gpa': 3.05});
# print(b)
# c = {'name': 'ohid', 'country': 'bangladesh', 'city' : 'cox Bazar'};
# print(c['city'])
# print(c['country'])
# print(c.get('name'))
# print(c.keys())
# print(c.values())
# print(c.items())

# person = {"name": "Jessa", "country": "USA", "telephone": 1178, 'id': 103};
# for key in person:
#     print(key, ':', person[key])

# print(len(person))
# person['weight'] = 70;
# person.update({'height': 30})
# print(person)
# person= person.setdefault('state', 'chittagong');
# print(person)
# person = person.popitem();
# print(person)
# print(person.pop('country'))
# del person['name'];
# print(person)

# dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
# dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}
# dict1.update(dict2);
# dict2.update(dict1)
# print(dict1)
# print(dict2)

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# key_value = dict(zip(keys, values));
# print(key_value)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2);
# print(dict1)
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"]);

# tuple1 = ('ibrahim', 'ohid');
# tuple2 = ('mohammad',);
# print(tuple1 + tuple2)

# country = ('Bangladesh', 'pakistan', 'afganistan');
# b, p, a = country;
# print(b, p, a);

# country = ['Bangladesh', 'pakistan', 'afganistan',  'indonesia'];
# *a, b, c = country;
print(a);
print(b);
print(c);

# a, b, c, (d, e, f) = country;
# print(a);
# print(b);
# print(c);
# print(d);
# print(e);
# print(f);