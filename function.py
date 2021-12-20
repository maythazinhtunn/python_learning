def greet():
    print("Hello, good morning");
greet();

def greet1(name):
    print(f'Good morning,{name}');
greet1("Mg Mg");

def greet2(name,time):
    print(f'good {time},{name}');
greet2("Aung Aung","Afernoon");

def greet3(name="May",time="evening"):
    print(f'good {time} , {name} !');
greet3();
greet3("Thazin","Night");
greet3("Htun");