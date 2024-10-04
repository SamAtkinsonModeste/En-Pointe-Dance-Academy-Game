# importing emoji library and coloured, cprint from termcolor
import emoji
import os
from termcolor import colored, cprint
from pyfiglet import Figlet
georgia11_font = Figlet(font="georgia11")
doom_font = Figlet(font="doom")
bolger_font = Figlet(font="bolger")
male_female = ["male", "female"]

# colours for the print colour function
colours = ["light_grey", "light_red", "light_green",
           "light_blue", "light_magenta", "light_cyan", "light_yellow"]


# Colour Function
def print_colour(text, color):
    """
    Prints text in colours
    """
    return cprint(text, color, attrs=["bold"])


class Student:
    """
    Student class
    """

    def __init__(self, name, about, secret):
        self.name = name
        self.about = about
        self.secret = secret

    def description(self):
        """
        Describes the student
        """
        return f"{self.name}\n{self.about}\n{self.secret}"


# Dance Student Characters
zoe = Student('Zoe', emoji.emojize(
    "A rebellious triple-threat dancer.:fire:"),
    'Torn between jazz and ballet,\n'
    'hiding her true dream\n'
    'to be a principal ballerina.\n')

sara = Student('Sara', emoji.emojize(
    "A determined ballet dancer,:flexed_biceps:"),
    'struggling with technique and self-confidence,\n'
    'trying to reconnect with the passion\n'
    'for dance she has lost with her confidence.\n')

lily = Student('Lily', emoji.emojize(
    "A technically perfect ballerina, :ballet_shoes:"),
    'facing intense pressure from her overbearing mother\n'
    'to be a principle ballerina, when,'
    'secretly dreaming of a career in singing.\n')


class Reactions:
    """
    Character reactions which the player chooses.
    """

    def __init__(self, positive, neutral, negative):
        self.positive = positive
        self.neutral = neutral
        self.negative = negative

    def reaction_positive(self):
        return f'{self.positive}'

    def reaction_neutral(self):
        return f'{self.neutral}'

    def reaction_negative(self):
        return f'{self.negative}'


def chose_gender():
    """
    User chooses between male or female
    character with raise ValueError
    and a confirmation yes or no
    to give them the option to change their minds
    """
    while True:
        try:
            which_gender = input(
                colored("Type Male or Female:\n",
                        "light_grey", attrs=["bold"])).lower()
            genders = ["male", "female"]

            if which_gender not in genders:
                raise ValueError("Did you type Male or Female?")

            proceed_to_next = True

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])
            proceed_to_next = False

        if which_gender == "male":
            print_colour(f"You chose {which_gender.capitalize()}", colours[5])
        else:
            print_colour(f"You chose {which_gender.capitalize()}", colours[4])

        if proceed_to_next:
            try:
                happy_choice = input(
                    colored("If you are happy with your choice type Y:\n"
                            "Or if you want to change type N:\n",
                            "light_grey", attrs=["bold"])).lower()
                choices = ["y", "n"]
                yes_no = happy_choice

                if yes_no not in choices:
                    raise ValueError("Did you type Y or N?")

                if happy_choice == "y":
                    next_clear()

                break

            except ValueError as e:
                print_colour(e, colours[1])
                print_colour("Try again", colours[2])
                proceed_to_next = False

            if not proceed_to_next:
                continue


def check_errors_inputs(input_text, value_text, error_text):
    """
    Cheaks for errors in inputs and sends error meesages to the user
    also clears the terminal once enter is hit
    """
    while True:
        try:
            next_display = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            if next_display != f"{value_text}":
                print(type(next_display))
                print(value_text)
                raise ValueError(f"{error_text}")

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

        else:
            next_clear()
            return value_text


def check_errors_list_inputs(input_text, options, error_text):
    """
    Cheaks for errors in inputs and checks if 
    input value is in a list. Sends error message to the user
    also clears the terminal once enter is hit
    """
    while True:
        try:
            next_display = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            value_text = next_display
            if value_text not in options:
                print(type(value_text))
                print(value_text)
                raise ValueError(f"{error_text}")

            break

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])


def next_clear():
    """
    Clears the terminal as if turning the pages of a book
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def game_play():
    """
    Main game play function
    """
    print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Academy"), colours[5])
    print_colour('Step into the world of dance\n'
                 'and follow the journeys of three unique dancers\n'
                 'in their final year at the prestigious\n'
                 'En Pointe Dance Academy!', colours[4])
    check_errors_inputs("To continue type: Next",
                        "next", "Did you type: Next?")


def about_game():
    """
    Tells the player what is expected of them and how to play
    """
    print_colour(doom_font.renderText("How To Play"), colours[5])
    print_colour(
        "This is a story driven adventure,"
        "where every choice matters!\n"
        "You can choose to follow"
        " one of the three"
        " character dance students.\n"
        "You will be in control of"
        " their future through your choices!\n"
        "You decide if their thougts or answers are:", colours[4])
    print(colored("Positive,", "light_green", attrs=["bold"]),
          colored("Neutral,", "light_blue", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Negative\n", "light_red", attrs=["bold"]))
    print_colour("When does a dancer know"
                 " when to start dancing a rountine?\n"
                 "It would be the teacher who"
                 " shouts out 4 numbers"
                 " to the beat of the music.\n"
                 "Those numbers are:", colours[3])
    print_colour("5,6,7,8", colours[6])

    check_errors_inputs("To begin type: 5,6,7,8", "5,6,7,8",
                        "Did you type:  5,6,7,8 ?")


def create_character_gender():
    """
   The player can create their character.
   They can choose male or female and create a name.
They will have a choice of three background and personalities
for their character as well as a choice of secret talents. 
   .
    """
    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour("You can create your own character.\n"
                 "Let's start by choosing:", colours[5])
    print(colored("Male", "light_cyan", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Female", "light_magenta", attrs=["bold"]))
    chose_gender()


if __name__ == "__main__":
    game_play()
    about_game()
    create_character_gender()
