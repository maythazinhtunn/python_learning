# class Car:
#     def __init__(self):
#         self.name="Lamboghini";
#         self.wheels=4;
#     def drive(self):
#         print(f"{self.name} is driving");

# Lambo=Car();
# print(Lambo.name);
# print(Lambo.wheels);
# Lambo.drive();

class Car:
    def __init__(self,carname,carwheels):
        self.carname=carname;
        self.carwheel=carwheels;
    def drive(self):
        print(f'{self.carname} is driving with {self.carwheel} wheels');
lam=Car('Lamboghini',4);
lam.drive();
mar=Car('Marcedes',4);
mar.drive();
