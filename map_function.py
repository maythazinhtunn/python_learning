nums=[1,2,3,4,5,6,7,8,9,10];
def mapFunction(num):
    return num*2;

print("Map function", map(mapFunction,nums));

nums=list(map(mapFunction,nums));
print(nums);