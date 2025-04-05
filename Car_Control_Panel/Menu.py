#import os for clear the terminal
import os

#create a list of cars to add the cars of the system
cars = []

#def the car class to create all cars in the system with this main Class
class car:
    name=''
    power=0
    maxspd=0
#def the init function to the system    
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.maxspd = int(power)*2
        self.on = False
    
#Turnon is a function to turn the car to ON
    def Turnon(self):
        if self.on == False:
            self.on = True
            print('This car is now ON')
        else:
            print('This car is already ON')

#Turnoff is a function to turn the car to OFF    
    def Turnoff(self):
        if self.on == True:
            self.on = False
            print('This car is now OFF')
        else:
            print('This car is already OFF')
    
#create a function to show the informations about the select car:
    def Info(self):
        print(f'''Name....:{self.name}
Power...:{self.power}
MaxSpeed:{self.maxspd}
ON......:{'yes' if self.on == True else 'not'}              
              ''')
        
def menu():
    os.system('cls' or None) #cls to clear the terminal and 'Or None' for not windows system
    print('''1 - New Car
2 - Car informations
3 - Delete car
4 - Turn on car
5 - Turn off car
6 - Car list
7 - Exit
''')
    opt = input('Type a option: ')
    return opt


#funcions 1 New Car
def newC():
    os.system('cls' or None)
    n = input('car name: ')
    p = input('car power: ')
    newcar = car(n, p)
    cars.append(newcar)        
    print('New car created')
    os.system('pause' or None)

#Funcition 2 Car information
def carinfo():
    os.system('cls' or None)
    n = input('Car number to show info: ')
    try:
        cars[int(n)].Info()
    except:
        print('unknown car')
    os.system('pause' or None)

#Function 3 delete a car
def deletecar():
    os.system('cls' or None)
    n = input('Car number to delete: ')
    try:
        del cars[int(n)]
    except:
        print('unknown car')
    os.system('pause' or None)


#function 4 Turn on car
def caron():
    os.system('cls' or None)
    n = input('car number to turn on: ')
    try:
        cars[int(n)].Turnon()
    except:
        print('unknown car')
    os.system('pause' or None)

#function 5 Turn off car
def caroff():
    os.system('cls' or None)
    n = input('car number to turn off: ')
    try:
        cars[int(n)].Turnoff()
    except:
        print('unknown car')
    os.system('pause' or None)


#function 6 Car list
def list():
    os.system('cls' or None)
    carnum = 0
    for i in cars:
        print(f'{str(carnum)} - {i.name}')
        carnum += 1
    os.system('pause' or None)

while True:
    opt = menu()
    match opt:
        case '1':
            newC()
        
        case '2':
            carinfo()

        case '3':
            deletecar()

        case '4':
            caron()

        case '5':
            caroff()

        case '6':
            list()

        case '7':
            break

        case _:
            print('Unknown option, please try again!')
            os.system('pause' or None)





'''#test for all the functions
pablo = car('pablo',10)

print('-------TEST-1-------')
pablo.Info()

print('-------TEST-2-------')
pablo.Turnon()
pablo.Turnon()
pablo.Info()

print('-------TEST-3-------')
pablo.Turnoff()
pablo.Turnoff()
pablo.Info()'''