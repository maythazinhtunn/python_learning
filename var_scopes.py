name="May Thazin Htun"; #global variable

def sayMyName():
    name = "Ko Ko"; #local var overwrite
    print(name);
sayMyName();
print(name);


name1="May Thazin Htun";

def sayMyName1():
    global name1;
    name1="TarYar LinnLatt";
    print(f"global name is{name1}");

sayMyName1();
print(name1);