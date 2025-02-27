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
colours = ['light_grey', 'light_red', 'light_green',
           'light_blue', 'light_magenta', 'light_cyan', 'light_yellow']

# story text in json file
with open('dialog-reactions.json', 'r') as file:
    data = json.load(file)

# emoji variables
thumbs_up = emoji.emojize(':thumbs_up:')
crying_face = emoji.emojize(":crying_face:")
flexed_biceps = emoji.emojize(":flexed_biceps:")
raising_hands = emoji.emojize(":raising_hands:")


# Colour functions
def print_colour(text, color):
    """
    Prints text in a specific colour
    """
    return cprint(text, color, attrs=['bold'])


def print_inputs_coloured(text, colour):
    """
    This function allows text to be added
    to be printed and specified colour for the text

    Args:
        text: any text to be printd
        colour: chosen from the colours list
    """
    return colored(text, colour)


# ^ CLASSES for Student and Choices
# * Student Class
class Student:
    """
    Student class
    Creates a student with a name,
    about the student's character's strengths and flaws
    """

    def __init__(self, gender):
        self.gender = gender
        self.name = self.get_student_name()
        self.about, self.style = self.get_student_traits()

    def get_student_name(self):
        if self.gender == "female":
            return student_name("female", 4)
        else:
            return student_name("male", 5)

    def get_student_traits(self):
        if self.gender == "female":
            return students_character_traits("female-students", self.name, 4)
        else:
            return students_character_traits("male-students", self.name, 5)

# ~ Choices Class


class Choices:
    """
    This class will provide the blue print
    for the choices the player needs to make
    Each choice will have the id of: A, B, C
    reaction: The reaction of the character
    and the impact: impact of the choice.
    """

    def __init__(self, id, reaction, impact):
        self.id = id
        self.reaction = reaction
        self.impact = impact

    def impact_reveal(self):
        """
      this function will be used
      to display the impact only
        """
        print(self.impact)


# check_errors functions
def check_errors_input(input_text, value_text, error_text):
    """
    Checks for the text added to an input
    Sends an error if the text is incorrect
    Also clears the terminal once enter is pressed
    """
    while True:
        try:
            next_display = input(
                colored(f"{input_text}\n", "light_grey",
                        attrs=["bold"])).lower()
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
    Sends error message to the user
    if input value is not in the list
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


# ~ list to store players story
players_choices = []


# ^ DICTIONARIES for the story
story_dialogue = {
    "assembly":  data['story-1'][0]['derek-speech-1'],
    "audition":  data['story-1'][0]['audition'],
    "announcement":  data['story-1'][0]['roles-announced']

}

thoughts_of_student = {
    "assembly_thought": data['decision-1'][0]['thought-1'],
    "student-role":  data['story-1'][0]['character-role']
}

# intro to game story function


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
        " one of the dance student character.\n"
        "You will be in control of"
        " his or her future through your choices!\n"
        "You decide if they go for options:", colours[6])
    print_colour("Option A", colours[2])
    print_colour("Option B", colours[3])
    print_colour("Option C\n", colours[1])
    print_colour("\nHow does a dancer know"
                 " when to start dancing a rountine to the music?\n"
                 "It would be the teacher who"
                 " shouts out 4 numbers"
                 " to the beat of the music.\n"
                 "Those numbers are:", colours[3])
    print_colour("5,6,7,8", colours[6])

    check_errors_input("To begin type: 5,6,7,8", "5,6,7,8",
                       "Did you type:  5,6,7,8 ?")

    next_clear()


# gender of character function
def chose_gender():
    """
   Gives the player a choice of gender for their character
   The player is asked a yes or no queston so they can change
   the gender if they wish.
    """
    global thumbs_up
    male_female = ["male", "female"]
    yes_no = ["y", "n"]
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
        else:
            female = select_gender
            print_colour(f"You chose {female} {thumbs_up}", colours[4])

        agree_disagree = check_errors_list_inputs(
            f"Is {select_gender} correct?\n"
            "Type Y for Yes or N for No:", yes_no, "Did you type Y or N")

        if agree_disagree == "y":
            confirmed = True
            next_clear()
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
        name = input(print_inputs_coloured(
            "Type a first name only (max characters 10): ", colour))
        if len(name) > 10:
            print(
                colored("Name is longer than 10 characters, try again!",
                        "light_yellow"))
            continue
        agree = check_errors_list_inputs(
            f"Are you happy with {name}? Y for Yes and N for No: ", yes_no,
            "Please type Y or N")
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

    chosen = check_errors_list_inputs(
        "Type your chosen name: ", names, "Please type a name from the list")
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
    print_colour(
        f"You can create a name for your {gender} student", colours[num])
    print_colour("Or select one from suggested names.", colours[2])
    response = check_errors_list_inputs(
        "Would you like to create a name? Y for Yes N for No: ",
        yes_no,
        "Please type Y or N")

    if response == "y":
        name_created = create_custom_name(colours[6])
        print_colour(
            f"Your character's name is {name_created.capitalize()}",
            colours[num])
        next_clear(2)
        return name_created
    else:
        name_created = choose_name_from_list(
            gender, m_names, f_names, colours[num])
        print_colour(
            f"Your character's name is {name_created.capitalize()}",
            colours[num])
        next_clear(2)
        return name_created


# Choosing a charcter's traits functions
def students_character_traits(people, name, num):
    """
    This function allows the user to chose
    their character's traits
    """
    choice = ["a", "b", "c"]
    print_colour(doom_font.renderText("Character Build"), colours[5])
    print_colour(doom_font.renderText("Characteristics"), colours[5])
    print_colour(
        f"You will be shown three characteristics to choose for "
        f"{name.capitalize()}",
        colours[2])
    print_colour("Each one will consist of strengths and flaws:", colours[6])
    check_errors_input("Are you ready to view them? Type: OK", "ok",
                       "Did you type:  Ok ?")
    next_clear()

    for student in data[people]:
        print(colored(
            f"Background:\n {student['background']}\n",
            "light_cyan",
            attrs=['bold']),)

    chosen_person = check_errors_list_inputs(
        "What character traits would you like to chose from: A, B or C ",
        choice, "Did you type A, B or C?")

    next_clear()

    if chosen_person == "a":
        characteristics_text = data[people][0]['characteristics']
        character_style = data[people][0]['style']
        print_colour(
            f"Meet Your Character:\n{name.capitalize()} "
            f"{characteristics_text}", colours[num])
        check_errors_input("Once you have finished reading type: OK", "ok",
                           "Did you type:  Ok ?")

    elif chosen_person == "b":
        characteristics_text = data[people][1]['characteristics']
        character_style = data[people][1]['style']
        print_colour(
            f"Meet Your Character:\n{name.capitalize()} "
            f"{characteristics_text}", colours[num])
        check_errors_input("Once you have finished reading type: OK", "ok",
                           "Did you type:  Ok ?")

    elif chosen_person == "c":
        characteristics_text = data[people][2]['characteristics']
        character_style = data[people][2]['style']
        print_colour(
            f"Meet Your Character:\n{name.capitalize()} "
            f"{characteristics_text}", colours[num])
        check_errors_input("Once you have finished reading type: OK", "ok",
                           "Did you type:  Ok ?")

    return characteristics_text, character_style


def student_thoughts(name, thought, num):
    print_colour(
        f"{name.capitalize()} {thought}",
        colours[num])


def choices(name, style, decision):
    global players_choices

    if style == "lyrical":
        data_style = 1
    elif style == "commercial":
        data_style = 2
    elif style == "contemporary":
        data_style = 3

    print_colour(f"Choose where {name.capitalize()}'s thought go:",
                 colours[0])

    choice_1 = Choices(
        "Option A", data[decision][data_style]['choice-1'],
        data[decision][data_style]['impact-1'])
    choice_2 = Choices(
        "Option B", data[decision][data_style]['choice-2'],
        data[decision][data_style]['impact-2'])
    choice_3 = Choices(
        "Option C", data[decision][data_style]['choice-3'],
        data[decision][data_style]['impact-3'])

    print_colour(
        f"Option A:\n {choice_1.reaction} {flexed_biceps}", colours[2])
    print_colour(f"Option B:\n{choice_2.reaction} {raising_hands}", colours[3])
    print_colour(f"Option C:\n{choice_3.reaction} {crying_face}", colours[1])

    options = ["a", "b", "c"]

    chose_option = check_errors_list_inputs(
        f"Which thoughts will you pick for {name.capitalize()}?:\n"
        "Type A, B or C: ",
        options, "Did you type A, B or C?")

    if chose_option == "a":
        print_colour(f"{name.capitalize()}:", colours[0])
        print_colour(f"{choice_1.impact}", colours[6])
    elif chose_option == "b":
        print_colour(f"{name.capitalize()}:", colours[0])
        print_colour(f"{choice_2.impact}", colours[6])
    elif chose_option == "c":
        choice_3.impact
        print_colour(f"{name.capitalize()}:", colours[0])
        print_colour(f"{choice_3.impact}", colours[6])

    players_choices.append(chose_option)

    next_clear()


def actions_of_characters(name, style):
    global players_choices

    audition_map = {
        "a": "audition-1",
        "b": "audition-2",
        "c": "audition-3"
    }

    if style == "lyrical":
        data_style = 0
    elif style == "commercial":
        data_style = 1
    elif style == "contemporary":
        data_style = 2

    student_style = style

    if style == student_style:
        choice = players_choices[0]
        if choice in audition_map:
            action = data['character-actions'][data_style][audition_map
                                                           [choice]]
            colour_index = {"a": 2, "b": 3, "c": 1}[choice]
            print_colour(f"{name.capitalize()} {action}",
                         colours[colour_index])
    if players_choices[0] == "c":
        print_colour(
            f"After the auditions Derek calls over {name.capitalize()}"
            " and says:\n"
            f"I can see you have lost your confidence {name.capitalize()}\n"
            "You are one of the best dancers to grace our studios.\n"
            "But I could tell you that till I am blue in the face.\n"
            f"It's up to you to believe in yourself {name.capitalize()},\n"
            "no one can do that for you but you.\n"
            "See you in rehearsals.", colours[6])

    check_errors_input("When you are ready type: OK", "ok",
                       "Did you type:  Ok ?")
    next_clear()


def dance_role_revealed(name, style, gender):
    global players_choices

    roles_map = {
        "a": f"Lead in {style} jazz!",
        "b": "Main lead!!",
        "c": f"Understudy lead {style}",
    }

    selected_data = next(
        (item for item in data['decision-2'] if item['id'] == style), None)

    if selected_data:
        reaction_map = {
            "a": selected_data['reaction-1'],
            "b": selected_data['reaction-2'],
            "c": selected_data['reaction-3']
        }
    else:
        reaction_map = {}

    if gender == "female":
        num = 4
    else:
        num = 5

    student_style = style
    if style == student_style:
        role = players_choices[0]
        if role in roles_map:
            print_colour(
                f"Under {name.capitalize()}'s name was the role: "
                f"{roles_map[role]}",
                colours[num])

        if role in reaction_map:
            print_colour(
                f"{name.capitalize()} {reaction_map[role]}",
                colours[num])

    check_errors_input("When you are ready type: OK", "ok",
                       "Did you type:  Ok ?")
    next_clear()


def story_paths(title, story, num):
    print_colour(doom_font.renderText(f"{title}"), colours[5])
    print_colour(f"{story}", colours[num])


def end_of_story(name, style):
    global players_choices
    print_colour(doom_font.renderText("Show Time"), colours[5])
    print_colour("It was the evening of the third years\n"
                 "showcase at En Pointe Dance Academy!\n", colours[4])

    if "c" in players_choices:
        print_colour(f"Derek got to watch {name.capitalize()}\n"
                     f"in the lead role of the {style} dance\n"
                     "due to the lead coming down with flu.\n"
                     f"{name.capitalize()}'s performance surpassed"
                     "everyone's expectations\n"
                     f"Derek was very proud of {name.capitalize()}\n"
                     f"and wished {name.capitalize()} all the success\n"
                     "for their career."
                     "And so another school year was over\n"
                     "soon new freshed face first years would\n"
                     "be walking through the doors of\n"
                     "En Pointe Dance Academy", colours[4])
    else:
        print_colour(f"{name.capitalize()}'s performance surpassed"
                     " everyone's expectations\n"
                     f"Derek was very proud of {name.capitalize()}\n"
                     f"and wished {name.capitalize()} all the success\n"
                     "for their career."
                     "And so another school year was over\n"
                     "soon new freshed face first years would\n"
                     "be walking through the doors of\n"
                     "En Pointe Dance Academy", colours[4])

    print_colour(doom_font.renderText("The End"), colours[5])


def story_adventure_game():
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
    next_clear()
    about_game()
    gender = chose_gender()
    student = Student(gender)
    story_paths("Assembly", story_dialogue['assembly'], 6)
    student_thoughts(student.name, thoughts_of_student['assembly_thought'], 3)
    choices(student.name, student.style, "decision-1")
    story_paths("Audition", story_dialogue['audition'], 6)
    actions_of_characters(student.name, student.style)
    story_paths("Role Goes To", story_dialogue['announcement'], 6)
    student_thoughts(student.name, thoughts_of_student['student-role'], 3)
    dance_role_revealed(student.name, student.style, student.gender)
    end_of_story(student.name, student.style)


if __name__ == "__main__":
    story_adventure_game()
