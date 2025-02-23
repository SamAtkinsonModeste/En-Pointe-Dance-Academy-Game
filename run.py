# importing json, emoji library ans coloured, cprint fro termcolor
import json
import emoji
import os
import time
from termcolor import colored, cprint
from pyfiglet import Figlet



# font variables
georgia11_font = Figlet(font='georgia11')
doom_font = Figlet(font='doom')
bolger_font = Figlet(font='bolger')

# colours for the print colour function
colours = ['light_grey', 'light_red', 'light_green', 'light_blue', 'light_magenta', 'light_cyan', 'light_yellow']

# story text in json file
with open('dialog-reactions.json', 'r') as file:
    data = json.load(file)

# emoji variables
thumbs_up = emoji.emojize(':thumbs_up:')
angry_face = emoji.emojize(':angry_face:')
big_laugh = emoji.emojize(':grinning_squinting_face:')


# Colour functions
def print_colour(text, color):
    """
    Prints text in a specific colour
    """
    return cprint(text, color, attrs=['bold'])

def print_inputs_coloured(text, colour):
    # return the colored string
    return colored(text, colour)



# Student class
class Student:
    """
    Student class
    Creates a student with a name, 
    about the student
    and their hidden secret talent
    """

    def __init__(self, name, about, secret):
        self.name = name
        self.about = about
        self.secret = secret



# check_errors functions
def check_errors_input(input_text, value_text, error_text):
    """
    Checks for the text added to an input 
    Sends an error if the text is incorrect
    Also clears the terminal once enter is pressed

    """
    while True:
        try:
            next_display = input(colored(f"{input_text}\n", "light_grey", attrs=["bold"])).lower()
            if next_display != f"{value_text}":
                raise ValueError(f"{error_text}")

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

        else:
            next_clear()
            return value_text


def check_errors_list_inputs(input_text, options, error_text):
    """
    Cheaks for errors in inputs
    checks if input value is in a list `options`.
    Sends error message to the user if input value is not in the list
    also clears the terminal once enter is hit
    """
    while True:
        try:
            value_text = input(colored(
                f"{input_text}\n", "light_grey", attrs=["bold"])).lower()

            if value_text not in options:
                raise ValueError(f"{error_text}")

        except ValueError as e:
            print_colour(e, colours[1])
            print_colour("Try again", colours[2])

        else:
            return value_text


# function for clearing the terminal

def next_clear(delay=0):
    """
    Clears the terminal as if turning the pages of a book
    """
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

# intro to game story
def intro_to_game_story():
    """
    Tells the player the games story
    And the possible charcters
    """
    print_colour(georgia11_font.renderText("En Pointe"), colours[5])
    print_colour(doom_font.renderText("Dance Academy"), colours[5])
    print_colour('Step into the world of dance\n'
                 'and follow the journey of one of three unique dancers\n'
                 'in their final year at the prestigious\n'
                 'En Pointe Dance Academy!', colours[4])
    check_errors_input("To continue type: Next",
                        "next", "Did you type: Next?")

# tells the player what kind of game it is
def about_game():
    """
    Tells the player what is expected of them and how to play
    """
    print_colour(doom_font.renderText("What To Expect"), colours[5])
    print_colour(
        "This is a story driven adventure,"
        "where every choice matters!\n"
        "You can choose to follow"
        " one of the three"
        " character dance students.\n"
        "You will be in control of"
        " their future through your choices!\n"
        "You decide if their thougts or answers are:", colours[6])
    print(colored("Positive,", "light_green", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Negative\n", "light_red", attrs=["bold"]))
    print_colour("How does a dancer know"
                 " when to start dancing a rountine to the music?\n"
                 "It would be the teacher who"
                 " shouts out 4 numbers"
                 " to the beat of the music.\n"
                 "Those numbers are:", colours[3])
    print_colour("5,6,7,8", colours[6])

    check_errors_input("To begin type: 5,6,7,8", "5,6,7,8",
                        "Did you type:  5,6,7,8 ?")



def chose_gender():
    """
   Gives the player a choice of gender for their character
   The player is asked a yes or no queston so they can change
   the gender if they wish.
    """
    global thumbs_up
    male_female = ["male", "female"]
    yes_no = ["y", "n"]
    agree = "y"
    confirmed = False

    print_colour(doom_font.renderText("Character Build"), colours[2])
    print_colour(doom_font.renderText("Gender"), colours[6])
    print_colour("You can create your own character.\n"
                 "Let's start by choosing:", colours[6])
    print(colored("Male", "light_cyan", attrs=["bold"]),
          colored("or", "light_grey", attrs=["bold"]),
          colored("Female", "light_magenta", attrs=["bold"]))

    while not confirmed:
        select_gender = check_errors_list_inputs(
            "Type Male or Female", male_female, "Did You type Male or Female?")

        if select_gender == "male":
            male = select_gender
            print_colour(f"You chose {male} {thumbs_up}", colours[5])
        else : 
            female = select_gender
            print_colour(f"You chose {female} {thumbs_up}", colours[4])


     

        agree_disagree = check_errors_list_inputs(
            f"Is {select_gender} correct?\n"
            "Type Y for Yes or N for No:", yes_no, "Did you type Y or N")



        if agree_disagree == "y":
            confirmed = True
            return select_gender
          
        else:
            print_colour("Please reselect:", colours[6])


# student name functions


def create_custom_name(colour):
    """
    This function gives the user
    the choice to create a name
    """
    yes_no = ["y", "n"]
    while True:
        name = input(print_inputs_coloured("Type a first name only (max characters 10):  ", colour))
        if len(name) > 10:
            print(colored("Name is longer than 10 characters, try again!", "light_yellow"))
            continue 
        agree = check_errors_list_inputs(f"Are you happy with {name}? Y for Yes and N for No: ", yes_no, "Please type Y or N")
        if agree == "y":
            return name
       



def choose_name_from_list(gender, m_names, f_names, colour):
    """
    this function allows the user
    to choose a name from a list
    """
    if gender.lower() == "female":
        names = f_names
    else:
        names = m_names
    print_colour(f"Choose from these names: {names}", colour)
 
    chosen = check_errors_list_inputs("Type your chosen name: ", names, "Please type a name from the list")
    return chosen



def student_name(gender, num, names=None):
    """
    The student name function
    controls which method of name creation
    the user either creates a name using the create_custom_name function
    or chosses from a list using the choose_name_from_list function
    """
    yes_no = ["y", "n"]
    m_names = ["liam", "jordan", "ethan"]
    f_names = ["zoe", "maya", "lily"]

    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour(doom_font.renderText("Name"), colours[5])
    print_colour(f"You can create a name for your {gender} student", colours[num])
    print_colour("Or select one from suggested names.", colours[2])
    response = check_errors_list_inputs("Would you like to create a name? (Y/N): ", yes_no, "Please type Y or N")
    
    if response == "y":
        name_created = create_custom_name(colours[6])
        print_colour(f"Your character's name is {name_created.capitalize()}", colours[num])
        next_clear(3)
        return name_created
    else:
        name_created = choose_name_from_list(gender, m_names, f_names, colours[num])
        print_colour(f"Your character's name is {name_created.capitalize()}", colours[num])
        next_clear(3)
        return name_created

                
           



                

            

  
  










if __name__ == "__main__":
    intro_to_game_story()
    about_game()
    gender = chose_gender()
    next_clear()
    if gender == "female":
        student_name("female", 4)
        
    else:
        student_name("male", 5)
      
    