import random

list_dinner = ['korean', 'japanese', 'thai', 'vietnamese']

def current_dinner_list():
    dinner_dinner_greeting = 'Dinner choices are '
    for option in list_dinner:
        dinner_dinner_greeting += option
        if option == list_dinner[-1]:
            dinner_dinner_greeting += '.  '
        else:
            dinner_dinner_greeting +=  ', '
    return dinner_dinner_greeting

print(list_dinner)
print(current_dinner_list())

while True:
    usr_input = input("Type other dinner options to add to list, 'c' to have another random choice, or 'q' to quit. ")
    if usr_input == 'q':
        break;
    elif usr_input == 'c':
        dinner = random.choice(list_dinner)
        print('Randomly picked dinner is ' + dinner)
    else:
        list_dinner.append(usr_input)
        print(current_dinner_list())
    continue;
