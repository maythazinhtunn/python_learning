with open("./about.txt",'w') as file:
    file.write('I am May Thazin Htun.');
    file.write('\nI am 29 years old.');
# other work
with open("./about.txt",'a') as file:# a means amend
    file.write('\nI used to work in Customs');
lists=["I am Tar Yar Linn Latt","\n I work in Frontiir"];
with open('./about.txt','a') as file:
    file.writelines(lists);