stud={'Name:' : 'Ravi','Age:' : 21,'Class:':'S1'}
print(stud['Name:'])
print(stud.get('Age:'))
print(stud.pop('Class:')) # removes Class key and its value

for key in stud.keys():
    print(key)
for value in stud.values():
    print(value)
for key in stud:
    print(key,stud[key])