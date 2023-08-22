from enum import Enum
from helper import *


cars = []

class Actions(Enum):
    Add = 1
    Search_by_brand = 2
    Delete_by_brand = 3
    Update_by_brand = 4
    Print = 5
    Exit = -1


#prints all actions to get wanted action from user
def actions_display(): #display options
    for x in Actions: print(COLOR_RESET+f'{x.name} = {x.value}')
    print('')
    return Actions(int(input('select an action: ')))

#navigates between all option according to user selection
def car_menu(): #actions navigator
    while(True):
        slc = actions_display() # selection from user
        if slc == Actions.Add: add_car(cars)
        if slc == Actions.Search_by_brand: search_car(cars)
        if slc == Actions.Delete_by_brand: delete_car(cars)
        if slc == Actions.Update_by_brand: update_data(cars)
        if slc == Actions.Print: print_all(cars)
        if slc == Actions.Exit: return

#main
if __name__ == '__main__': 
    clear_screen()
    cars = load_data("cars.csv") #when start - load from CSV file
    car_menu() 
    clear_screen()
    save_data(cars,"cars.csv") #when end - save to CSV file