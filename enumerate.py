my_list=[10,20,30,40]

for index,value in enumerate(my_list):
    print(my_list[index]);
    my_list[index]*=2
    print(my_list[index]);
    
print(my_list);