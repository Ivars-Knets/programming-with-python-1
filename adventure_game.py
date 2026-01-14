import time
import random


enemies = ['troll', 'hag', 'bandit', 'gorgon', 'dragon', 'imp']
modifier = ['brutish', 'wicked', 'crazed', 'ruthless', 'demonic']
default_weapon = 'old dagger'


# Functional functions
def slow_print(message, pause_time=1):
    print(message)
    time.sleep(pause_time)


def print_list_plus(list, word):
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
        slow_print(f"Enter {str(i+1)} - {option_list[i]}", 0)

    input_message = f"Please enter {print_list_plus(valid_input_list, 'or')}: "
    response = validated_input(input_message, valid_input_list)
    choice = option_list[int(response)-1]

    return choice


def role_dice(sides, dc):
    role = random.randint(1, sides)
    return role >= dc


# Story branch functions

def dead_end():
    slow_print("...")
    slow_print("YOU HAVE DIED")
    slow_print('GAME OVER', 0)


def good_end():
    slow_print("...")
    slow_print("You are victorious!")
    slow_print('WELL DONE')
    slow_print('GAME OVER', 0)


def faceoff(game_data):
    weapon = game_data['weapon']
    enemy = game_data['enemy']
    enemy_desc = game_data['enemy_desc']

    slow_print(f"The {enemy} attacks you!")
    if weapon == "old dagger":
        slow_print(f"You feel a bit under-prepared for this,")
        slow_print(f" what with only having a {game_data['weapon']}.")

    slow_print("")
    fight_choice = make_a_choice(['Fight!', 'Run away!'])
    slow_print("")

    if fight_choice == 'Fight!':
        if weapon == "old dagger":
            slow_print("You do your best...", 1)
            slow_print(f" but your {game_data['weapon']}")
            slow_print(f" is no match for the {enemy_desc}.")
            dead_end()
        elif weapon == "family sword":
            slow_print(f"As the {enemy_desc} moves to attack,")
            slow_print(" you unsheathe your family sword.")
            slow_print("The Sword of Family Oregan shines brightly")
            slow_print(" as you take a combat stance.", 2)
            slow_print(f"The {enemy} puts up a though fight!")
            slow_print("But you managed to subdue them")
            slow_print(" and give them a choice - flee or die.")
            slow_print("")

            enemy_fights = role_dice(20, 12)
            if enemy_fights is True:
                slow_print(f"The {enemy} is not scared of you.")
                slow_print("So you are forced to end them. For good.")
            else:
                slow_print(f"The {enemy} surrenders and promises to leave.")

            slow_print("", 1)
            slow_print(f"You have rid the lands of the {enemy_desc}.")
            good_end()

    elif fight_choice == 'Run away!':
        slow_print("You run back to the garden.")
        slow_print(f"Luckily, the {enemy} chose not to follow.")
        where_to(game_data)


def house(game_data):
    if game_data['house_visited'] is True:
        slow_print(f"You feel ready to face the {game_data['enemy_desc']}.")
        slow_print("You approach the door of the house.")
        slow_print(f"The {game_data['enemy']} steps out yet again.")
    elif game_data['house_visited'] is False:
        slow_print("You approach the door of the house.")
        slow_print("You go to knock on the door...")
        slow_print(" but the door opens first")
        slow_print(f" and out steps the {game_data['enemy_desc']}.")
        slow_print("So the rumors where true,")
        slow_print(f" the {game_data['enemy']} is here!")
        game_data['house_visited'] = True
    faceoff(game_data)


def cave(game_data):
    slow_print("You peer cautiously into the cave.")
    if game_data['cave_visited'] is True:
        slow_print("You've been here before,")
        slow_print(" and gotten all the good stuff.")
        slow_print("It's just an empty cave now.")
    elif game_data['cave_visited'] is False:
        slow_print("It turns out to be only a very small cave.")
        slow_print("Your eye catches a glint of metal behind a rock.")
        slow_print("You have found the magical Sword of Family Oregan!")
        slow_print("You take up the family sword,")
        slow_print(f" and discard the {game_data['weapon']}.")
        game_data['weapon'] = "family sword"
        game_data['cave_visited'] = True
    slow_print("You walk out of the cave, and back to the garden.")
    where_to(game_data)


def where_to(game_data):
    slow_print("")
    slow_print("What would you like to do?", 0)
    choice = make_a_choice(['Knock on the house door', 'Peer into the cave'])
    slow_print("", 0)

    if choice == 'Knock on the house door':
        house(game_data)
    elif choice == 'Peer into the cave':
        cave(game_data)


def start_adventure(game_data):
    slow_print("Finally!")
    slow_print("You find yourself in front of the gate.")
    slow_print("This land used to belong to the Oregan family.")
    slow_print("Your family.")
    slow_print("", 1)

    slow_print("Behind the gate there is a lovely garden,")
    slow_print(" an once-great-now-imposing house")
    slow_print(" and a side path that goes somewhere that you can't see.")
    slow_print("", 1)

    slow_print(f"Rumor has it that a {game_data['enemy_desc']} took over,")
    slow_print(" and has been attacking the people nearby.")
    slow_print("", 1)

    slow_print(f"With your {game_data['weapon']} in hand you go in.")
    slow_print("You walk into the garden and stand before the house.")
    slow_print("You notice that the side path leads to a nearby cave.")

    where_to(game_data)


def main():
    while True:
        rand_enemy = random.choice(enemies)
        game_data = {
            'enemy': rand_enemy,
            'enemy_desc': random.choice(modifier) + ' ' + rand_enemy,
            'weapon': default_weapon,
            'cave_visited': False,
            'house_visited': False
        }
        start_adventure(game_data)

        slow_print('-'*30)
        slow_print('Would you like to go again?', 0)
        answers = ['yes', 'no', '']
        restart_choice = validated_input('Enter "yes" or "no": ', answers)
        if restart_choice != 'yes':
            break
        else:
            print("\n\n" + '-' * 30 + "\n\n")


main()
