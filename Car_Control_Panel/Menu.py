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
        
pablo = car('pablo',10)



#test for all the functions
print('-------TEST-1-------')
pablo.Info()

print('-------TEST-2-------')
pablo.Turnon()
pablo.Turnon()
pablo.Info()

print('-------TEST-3-------')
pablo.Turnoff()
pablo.Turnoff()
pablo.Info()