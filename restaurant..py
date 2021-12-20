class RestaurantTable:
    menus={
        'pizza':5000,
        'cola':600,
        'apple juice':2000,
        'hamburger':3000,
        'fried potato':1500
    }
    def __init__(self) :
        self.total=0;
        self.orders=[];
    def addOrder(self,order):
        self.orders.append(order);
        self.total+=self.menus[order];


    def printBill(self):
        
        for order in self.orders:
            print (f'{order} : {self.menus[order]}');
        print(self.total);  

def StartProgram():
    table=RestaurantTable();
    while True:
        order=input('Order :');
        table.addOrder(order);
        
        another=input('Order again y/n');
        
        if another=='y':
            continue;
        else:
            table.printBill();
            break;

StartProgram();