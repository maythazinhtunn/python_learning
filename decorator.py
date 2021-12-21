def greet(fun):
    def wrapper(name):
        print('hello')
        #before
        fun(name);
        #after
        print('good morning')
    return wrapper
@greet #function name

def sayName(name):
    print(name);
sayName("Aung Aung");