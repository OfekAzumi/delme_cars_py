import csv
import os

#colors
COLOR_RED = '\x1b[31m' #error
COLOR_GREEN = '\x1b[32m'#succes
COLOR_YELLOW = '\x1b[33m'#questions
COLOR_RESET = '\x1b[0m'  # Reset to default color

#clear termnial
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#gets data paramter and puts it into csv "file_name"
def save_data(data, file_name = "cars.csv"):
    with open(file_name, "w", newline='') as csvfile: #new line makes sure there are no spaces between rows
        writer = csv.writer(csvfile)
        # Write the data to the CSV file
        writer.writerows(data)

#loads data to tData from csv "file_name" and return it
def load_data(file_name = "cars.csv"):
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        tData = []
        for row in reader:
            tData.append(row)  
        return tData

#adds item to list according to csv model    
def add_car(list): #add action
    # cars.append({"brand": input('enter car brand: '),"model": input('enter car model: '),"color": input('enter car color: ')}) - JSON
    list.append([input(COLOR_YELLOW+'enter car brand: '),input('enter car model: '),input('enter car color: ')])

#gets car from search_action, delets it and print success
def delete_car(list): #delete action
    res = search_action(list)
    if(res != None): 
        list.remove(res)
        print(COLOR_GREEN+f'{res[2]} {res[0]}, year {res[1]} deleted succesfully')
    else: print(COLOR_RED+'no such car in database')

#get car from search_action, prints in a readable oreder. if not found print message
def search_car(list): #search + print action
    res = search_action(list)
    if(res != None): print(COLOR_GREEN+f'{res[2]} {res[0]}, year {res[1]}')
    else: print(COLOR_RED+'no such car in database')

#gets brand from user, searches in list. return car if found, else None
def search_action(list): #generic search function
    if(list):
        brd = input(COLOR_YELLOW+'enter car brand to search: ') # brand from user
        found = False
        for x in list:
            if x[0] == brd: 
                car=x
                found = True
        if found: return (car)
        return None        
    else: print(COLOR_RED+'no data at all')

#get car from search_action, updates according to user - brand.mode.car and prints success
def update_data(list): #update data
    res = search_action(list)
    if(res != None): 
        b = True
        while(b):
            print(COLOR_YELLOW+'What to update?')
            t = int(input(f'{res[0]} = 1 | {res[1]} = 2 | {res[2]} = 3 | if end enter 4 ?'))
            if t == 1: res[0] = input("Enter updated brand: ")
            if t == 2: res[1] = input("Enter updated model: ")
            if t == 3: res[2] = input("Enter updated color: ")
            if t == 4: return
            print(COLOR_GREEN+f'Updated to: {res[2]} {res[0]}, year {res[1]}')
    else: print(COLOR_RED+'no such car in database')

#prints all list with index/all cars
def print_all(list): #print all cars
    if(list):
        c = 1
        for x in list:
            print(COLOR_GREEN+f'{c}/{len(list)} : {x[2]} {x[0]}, year {x[1]}') # 'color' 'brand', year 'model' (black mazda, year 2015)
            c=c+1
    else: print(list)