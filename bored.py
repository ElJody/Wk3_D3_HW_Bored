from dis import dis
import requests
import os
import colorout

class Bored:
    def __init__(self):
        self.activity=''
        self.type=''
        self.participants=''
        self.price=''
        self.min={}
        self.max=''
    
    def min_max(self):
        
        colorout.clear_screen()

#       I've tried so many different ways to take input return values or return false/true,
#       break, continue and the like... I've changed this so much but is stuck on this block
#       
        while True:
            try:
                budget = int(input(f'So You\'re Bored, huh? Please enter your budget range - Min/Max: {self.min} / {self.max}'))
#                return budget
#           return (self.min(budget) self.max(budget))
#                continue
                break
            except ValueError:
                colorout.clear_screen()
                print('\n'"Sorry, Please Enter a Valid Min/Max Dollar Amount!!!"'\n')
                continue 
            

    
    def get_activity(self):   
        response=requests.get(f'http://www.boredapi.com/api/activity?minprice={self.min}&maxprice={self.max}')
        if not response.ok:
            return False
        data = response.json()

        self.activity = data["activity"]
        self.type = data["type"]
        self.participants = data["participants"]
        self.price = data["price"]
        return data

    def display_activity(self):
        print(colorout.print_blue(f'Activity : (self.activity)'))
        print(colorout.print_red(f'Activity Type : (self.type)'))
        print(colorout.print_yellow(f'# of Participants : (self.participants)'))   
        print(colorout.print_green(f'Cost : (self.price)'))

        user_want = input(f'If you would like another activity Press Enter, or Type Quit to exit.)')
        if user_want.lower() != "quit":
            return True
        else:
            return False

eljody = Bored()
eljody.min_max()
