import time
import random

inventory = []

### Functional functions
def print_with_pause(message, pause_time=1):
    print(message)
    time.sleep(pause_time)


def print_list_with_extra_word(list, word):
    response = ""
    for i in range(len(list)):
        if i == len(list)-1:
            response += f' {word} {list[i]}'
        elif i == 0:
            response += list[i]
        else:
            response += f', {list[i]}'
    return response


def validated_input(message, valid_list):
    response = input(message)
    while response not in valid_list:
        response = input(message)
    return response


def make_a_choice(option_list):
    print_with_pause('-'*30)
    valid_input_list = []
    for i in range(len(option_list)):
        valid_input_list.append(str(i+1))
        print_with_pause(f"Enter {str(i+1)} - {option_list[i]}")

    input_message = f"Please enter {print_list_with_extra_word(valid_input_list, 'or')}: "
    response = validated_input(input_message, valid_input_list)
    choice = option_list[int(response)-1]

    print_with_pause('-'*10)
    # print_with_pause(f'You chose {response} - {choice}')
    return choice


def role_dice(sides, goal):
    role = random.randint(1,sides)
    return role >= goal


### Story branch functions
def free_end():
    print_with_pause("...")
    print_with_pause("Majestic snow-capped mountain in the distance.")
    print_with_pause("Rolling fields of wild flowers.")
    print_with_pause("The occasional golden wheat farm or bountiful orchard.")
    print_with_pause("And a large road nearby.")
    print_with_pause("You are free to go where you please.")
    print_with_pause("THE END!")


def dead_end():
    print_with_pause("...")
    print_with_pause("YOU ARE DEAD.")


def forest_edge():
    print_with_pause("You reached the edge of the forest.")
    print_with_pause("Passing the last few trees the view opens up.")
    free_end()


def forest_humans(aggressive):
    humans_status = random.choice(['good', 'bad'])
    human_count = random.randint(2,6)
    print_with_pause(f"There is a camp of {human_count} people.")
    if humans_status == 'good':
        print_with_pause("Each one has an axe by their side.")


def forest_cave():
    print_with_pause('-'*30)
    print_with_pause("You enter the cave.")


def deeper_forest_path():
    print_with_pause('-'*30)
    print_with_pause("You are deep in the forest.")
    print_with_pause("The underbrush is clearing out.")
    print_with_pause("You hear people in the distance.")
    print_with_pause("They might be friendly! They could be dangerous.")
    print_with_pause("What do you do?")
    
    approach_humans_choice = make_a_choice(['Approach peacefully', 'Approach aggressively', 'Sneak past'])
    if approach_humans_choice == 'Approach peacefully':
        forest_humans(False)
    elif approach_humans_choice == 'Approach aggressively':
        forest_humans(True)
    elif approach_humans_choice == 'Sneak past':
        print_with_pause("You sneak past the humans.")
        forest_edge()
    else:
        print('Something broke!!')


def forest_path():
    print_with_pause('-'*30)
    print_with_pause("You walk down the forest path.")
    print_with_pause("The underbrush is getting thicker as you go.")

    forest_fork = ['Cave path', 'Forest path']

    if 'sword' in inventory:
        print_with_pause("You use your sword to cut the some of the bushes away to clear your path.")
        print_with_pause("You notice that the path forks.")
        print_with_pause("One path goes to a cave. The other further into a forest")
        print_with_pause("Where do you go?")
        forest_fork_choice = make_a_choice(forest_fork)
        if forest_fork_choice == 'Cave path':            
            forest_cave()
        elif forest_fork_choice == 'Forest path':
            deeper_forest_path()
        else:
            print('Something broke!!')
        
    else:
        print_with_pause("You walk through the thick underbrush.")
        random_path = random.choice(forest_fork)
        if random_path == 'Cave path':            
            print_with_pause("You see a cave entrance approaching")
            forest_cave()
        elif random_path == 'Forest path':
            print_with_pause("The forest path keeps going.")
            deeper_forest_path()
        else:
            print('Something broke!!!')


def river_bank():
    print_with_pause('-'*30)
    print_with_pause("You walk down the river bank.")
    


def start_of_adventure():
    print_with_pause('-'*30)

    print_with_pause("Hello and welcome to this mystical world!")
    print_with_pause("You awaken in a small forest clearing by a river.")    
    print_with_pause("There is a weapon near you.")
    print_with_pause("What is it?")

    weapon_choice = make_a_choice(['Sword', 'Bow', 'Axe', 'Pike'])
    inventory.append(weapon_choice.lower())    

    print_with_pause('-'*30)

    print_with_pause(f"You pick up the {weapon_choice.lower()}.")
    print_with_pause("You look around.")
    print_with_pause("There is a path through the forest.")
    print_with_pause("The river bank is good to walk down as well.")
    print_with_pause("Where do you go?")

    path_choice = make_a_choice(['Forest path', 'River bank'])

    if path_choice == 'Forest path':
        forest_path()
    elif path_choice == 'River bank':
        river_bank()
    else:
        print('Something broke!')


def main():
    while True:
        start_of_adventure()

        print_with_pause('-'*30)
        print_with_pause('Would you like to go again?')
        restart_choice = validated_input('Enter "yes" or "no": ', ['yes', 'no', ''])
        if restart_choice != 'yes':
            break
        else:
            inventory.clear()


main()
