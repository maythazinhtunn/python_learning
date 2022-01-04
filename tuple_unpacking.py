def devision(num,divisior):
    if divisior==0:
        return "Division by zero",0
    else:
        return None,num/divisior
print("Division",devision(3,2))
err,result = devision(3,2)
if (not err):
    print("Result is",result)
else:
    print("Error",err)