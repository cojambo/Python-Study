#import os for clear the terminal
import os

#create a list of cars to add the cars of the system
cars = ['camaro','honda']

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
5 - Turn of car
6 - Car list
7 - Exit
''')
    opt = input('Type a option: ')
    return int(opt)


#funcions 1 New Car
def newC():
    os.system('cls' or None)
    n = input('car name')
    p = input('car power')
    newcar = car(n, p)
    cars.append(newcar)        
    print('New car created')
    os.system('pause' or None)

#Funcition 2 Car information
def carinfo():
    os.system('cls' or None)
    n = input('Car number: ')
    try:
        cars[int(n)].Info()
    except:
        print('Unknow car')
    os.system('pause' or None)

#Function 3 delete a car
def deletecar():
    os.system('cls' or None)
    n = input('Car number: ')
    try:
        del cars[int(n)]
    except:
        print('Unknow car')
    os.system('pause' or None)


#function 4 Turn on car
def caron():
    os.system('cls' or None)
    n = input('car number: ')
    try:
        cars[n].Turnoon()
    except:
        print('Unknow car')

#function 5 Turn off car
def caroff():
    os.system('cls' or None)
    n = input('car number: ')
    try:
        cars[n].Turnoff()
    except:
        print('Unknow car')


#function 6 Car list
def list():
    carnum = 1
    for i in cars:
        print(f'{str(carnum)} - {i}')
        carnum += 1

opt = menu()
match opt:
    case 1:
        newC()


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