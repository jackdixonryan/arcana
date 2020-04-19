
# load file creates the open world through a mapping system
# locations are loaded based on character load
# map is only figured out by various location interactions via the gateway system

from locations import anaxios_bar
from characters import character_list

def main():
    print(character_list.anaxio.skills)
    bar = anaxios_bar.anaxios_bar
    bar.enter_character(character_list.anaxio, 10, 10)
    bar.room_map()
    exited = False
    while not exited:
        user_command = input('').lower()
        if user_command == 'exit':
            exited = True
        # movement commands
        elif user_command == 'a':
            bar.move_character('west')
        elif user_command == "d":
            bar.move_character('east')
        elif user_command == 'w':
            bar.move_character('north')
        elif user_command == 's':
            bar.move_character('south')
        elif user_command == 'i':
            bar.trigger_interact()
        elif user_command == 'c':
            bar.current_character.inventory_readout()
        elif user_command == 'skill':
            bar.current_character.show_skill_xp_quantities()
        else:
            print("Do you need a refresher on the controls?")
        bar.room_map()


main()