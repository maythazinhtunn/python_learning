age=int(input("age :"))

if age<18:
    print("you are young");
elif age>18 and age<30:
    print("you are normal age");
else:
    print("you are old");

tired=input("are you tired? 'y/n' ")
if tired =='y':
    print('rest well')
elif tired =='n':
    print('go back to work')
else :
    print('please enter y / n')