class Car:
    sterring_wheel=1;
    def __init__(self,name,wheel):
        self.name=name;
        self.wheel=wheel;
    def drive(self):
        print(f'{self.name} is driving with {self.wheel} wheels');
    
    @classmethod
    def common(cls):
        print(f'all car have only {cls.sterring_wheel} sterring wheel ');

# print(Car.sterring_wheel);
# Car.common();


# Lam=Car("Lamboghini",4);
# Lam.drive();
# Lam.common()