import random

def build_new_character(ctx):
    if ctx == "first_build":
        print("Welcome. What are you?")
        species = gather_species_input()
        print(species + ", huh? Well, not everyone gets the privilege of choosing how they're born. Still, I hope you chose right. Don't worry, sooner or later you will die and have an opportunity again. It's fine")
        generate_user_information()
    elif ctx == "random_mode":
        print("So you died. It won't the first time. But look at you, not faint of heart! You've chosen random mode.")
        options = ["human", "ethereal", "sojourner", "apsonid"]
        random_index = random.randint(0, 3)
        random_species = options[random_index]
        print("Welcome back to the world, " + random_species + ". Good luck.")

def gather_species_input():
    species = input(
        "CHOOSE A SPECIES:\nA. Human \nB. Ethereal\nC. Sojourner\nD. Apsonid\nOR type the name of the species for more information: ")
    selection = species.lower()
    if selection == "a" or species == "a.":
        return "human"
    elif species == "b" or species == "b.":
        return "ethereal"
    elif species == "c" or species == "c.":
        return "sojourner"
    elif species == "d" or species == "d.":
        return "apsonid"
    else:
        render_species_information(species)
        return gather_species_input()

def render_species_information(species_name):
    standardized_species_name = species_name.lower()
    if standardized_species_name == "human":
        print("Humans are the race of endurance and adaptation. Rare is the situation a human cannot get out of. That said, space is not their home and they have a lot of adapting left to do.")
    elif standardized_species_name == "ethereal":
        print("Contrary to all previous conceptions of life, ethereals have no body whatsoever and are pure energy. They are a peaceful species, though not well-regarded by many for mistakes made in their history.")
    elif standardized_species_name == "sojourner":
        print("They used to be human, though their own people barely recognize them now. They are ready for everything space can throw at them, even though politics aren't usually for them.")
    elif standardized_species_name == "apsonid":
        print("Every universe needs muscle. Apsonids are affable creatures, if not the most intelligent. All over the universe they're used for free labor, though in some sectors rumors grow that they won't be kept down much longer.")
    else:
        print("I applaud your creativity, but please choose an actual species: ")

def generate_user_information():
    return 'aye aye'

build_new_character("random_mode")