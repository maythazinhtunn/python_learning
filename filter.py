nums=[1,2,3,4,5,6,7,8,9,10]

def even(num):
    return (num%2)==0;
print(filter(even,nums))
evenNum=list(filter(even,nums))
print(evenNum)

evenNum=[num for num in nums if (num%2)==0]
print(f"Comprehension ways:{evenNum}");

evenNum=[];
for num in nums:
    if num%2==0:
        evenNum.append(num);
print(f"For Loop {evenNum}");