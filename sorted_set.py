# nums=[2,3,4,5,3,2,6,7,3,1];
# print(sorted(nums));

# names=["Mg Mg","ma ma","Ko Aung","gi gi","Su SU"];
# print(names);

# nums=[3,4,5,6,5,4,3,2,1,9,3,5,4];
# for num in set(nums):
#     print(num);

# ages=[40,30,20,45,32];
# for age in set(ages):
#     print(age);

person={};

while True:
    name=input("Enter Name: ");
    age=input("Enter your age: ");
    person[name]=age;

    another=input('another y / n :');
    if another=='y':
        continue;
    else:
        break;
ages=list(person.values());
names=list(person.keys());
for age in set(ages):
    count=ages.count(age);
    print(f'{count}');
    print(f'{age} years old -{count}');

