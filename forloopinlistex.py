num_of_sub= int(input("Enter number of Sub"));
marks=[]
pass_mark=40;
isPass=True

for i in range(num_of_sub):
    mark=float(input("Enter mark of Sub "+str(i)));
    isPass=isPass and mark>=40

if isPass==True:
    print("Pass the exam")
else:
    print("Fail the exam")