# person={}

# name=input('Input Name:');
# age=input('Age :');

# person[name]=age;

# print(person);

person={}
while True:
    name=input('Input Name:');
    age=input('Age :');
    person[name]=age;
    another=input('another y/n')
    if another=='y':
        continue;
    else:
        break;
print(person);  
for (key,val) in person.items():
    print(f'{key} is {val} years old.')