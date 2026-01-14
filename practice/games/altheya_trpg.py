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
    valid_input_list = []
    for i in range(len(option_list)):
        valid_input_list.append(str(i+1))
        print_with_pause(f"Enter {str(i+1)} - {option_list[i]}")

    input_message = f"Please enter {print_list_with_extra_word(valid_input_list, 'or')}: "
    response = validated_input(input_message, valid_input_list)

    print_with_pause(f'You chose {response} - {option_list[int(response)-1]}')
    return response


def role_dice(sides, goal):
    role = random.randint(1,sides)
    return role >= goal


### Story branch functions
def dead_end():
    print_with_pause("YOU ARE DEAD.")


def choice_1_fight():
    if 'your axe' in inventory:
        print_with_pause("With your axe in hand you approach the source of the noise.")
        print_with_pause("It looks to be a lone scout.")

        if role_dice(20, 10):
            print_with_pause("You dispatch of them quickly and move on.")
        else:
            print_with_pause("You dispatch of them quickly, but in the process your axe handle is broken.")
            print_with_pause("You pack up the broken axe just in case and move on.")
            inventory.remove('your axe')
            inventory.extend('broken axe')
        
        print_with_pause("You dispatch of them quickly, but in the process your axe handle is broken.")
        
    else:
        print_with_pause("You have no weapon, but still choose to fight.")
        print_with_pause("It looks to be a lone scout.")
        print_with_pause("You fight bravely, but they get the better of you.")
        dead_end()


def choice_1_sneak():
    if role_dice(20, 5):
        print_with_pause("You successfully sneak past the vault spawn and move on.")
    else:
        print_with_pause("You have no weapon, but still choose to fight.")
        print_with_pause("It looks to be a lone scout.")
        print_with_pause("You fight bravely, but they get the better of you.")
        dead_end()


def choice_1_walk():
    print_with_pause("You chat with the ork.")
    ork_lines = [
        'Im gonna kill ya!',
        'You\'s a punk!',
        'Just leave me alone!',
        'Getting tired?'
    ]
    ork_says = random.choice(ork_lines)
    print_with_pause(ork_says)


def start_of_adventure():
    print_with_pause("Hello and welcome to this mystical world!")
    print_with_pause("You are from a small logging village of Colvel.")
    print_with_pause("Recently a vault has opened near your village.")
    print_with_pause("Bringing with it dangerous vault spawn.")
    print_with_pause("You volunteered to go the Duke and tell them of your plight.")
    print_with_pause("You gather what you need for the journey.")
    inventory.extend(['some rope', 'your axe'])
    print_with_pause(f"Including {print_list_with_extra_word(inventory, 'and')}")
    print_with_pause("You set out on your journey!")

    print_with_pause('-'*30)

    print_with_pause("You walk through the woods.")
    print_with_pause("You hear a noise up ahead.")
    print_with_pause("It must be vault spawn.")
    print_with_pause("What do you do?")

    print_with_pause('-'*30)
    choice_1 = make_a_choice(['Fight!', 'Sneak around', 'Take longer path'])

    if choice_1 == '1':
        choice_1_fight()
    elif choice_1 == '2':
        choice_1_sneak()
    elif choice_1 == '3':
        choice_1_walk()
    else:
        print('Something broke!')


def main():
    while True:
        print_with_pause('-'*30)
        start_of_adventure()

        print_with_pause('-'*30)
        print_with_pause('Would you like to go again?')
        restart_choice = validated_input('Enter "yes" or "no": ', ['yes', 'no', ''])
        if restart_choice != 'yes':
            break


main()
