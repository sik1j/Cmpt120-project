import pygame
import draw

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

### Global Variables ###
gameState = {
    'TOTAL_CSV_LINES' : len(open('blackfoot.csv').readlines()),
    'learnCount' : 3
}
### Functions ###
# Validates input before returning it
def validatedInput(string, min, max):
    valid = False
    while not valid:
        try:
            # might need to validated that input isn't a float as well
            value = int(input(string))
            print(value)
            while value < min or value > max:
                print(f'Please choose a number from {min} to {max}')
                value = int(input(string))
            valid = True
        except:
            print(f'Please choose a number from {min} to {max}')
    return int(value)

def Menu():
    option = {'LEARN': 1, 'PLAY': 2, 'SETTINGS': 3, 'EXIT': 4}
    exitFlag = False
    while not exitFlag:
        print(
    """\nMAIN MENU
    1. Learn - Word Flashcards
    2. Play - Seek and Find Game
    3. Settings - Change Difficulty
    4. Exit"""
            )
        chosenOption = validatedInput('Choose an option: ', 1, 4)
        if chosenOption == option.get('LEARN'):
            learn()
        elif chosenOption == option.get('PLAY'):
            play()
        elif chosenOption == option.get('SETTINGS'):
            settings()
        else:
            exitFlag = exit()

# Learn
    # ouput message explaining what the option does
    # requires 2 options back and continue
    # display image and play sound
        # use drawItem with random location to print images
    # output text telling them to press enter to move on
        # n. Press enter to continue... (where n is the number of the picture)
    # when user presses enter move on to next image
    # default amount of images is 3 (first 3 item in .csv file) can change num of images in settings
    # output menu at the end
def learn():
    file = open('blackfoot.csv')
    print('LEARN')
    for index in range(1,gameState.get('learnCount')+1):
        item = file.readline().split()[0]
        image = draw.cmpt120image.getImage(f'images/{item}.png')
        playSound(item, ENV)
        canvas = draw.cmpt120image.getWhiteImage(400,300)
        draw.distributeItems(canvas, image, 1)
        draw.cmpt120image.showImage(canvas)
        input(f'{index}. Press Enter to continue... ')

# Play
    # ouput message explaining what the option does
    # requires 2 options back and continue
    # asks how many rounds to be played
    # display x images n times on screen with at least 1 of the right image (random colored too) and play sound
        # use distributeItems x times
    # "Listen to the word. How many of them can you find?" (accepts only int)
    # inform user if they are right or wrong (if wrong show the correct number of instences)
    # "Press enter to continue."
    # output menu at the end

# Settings
    # ouput message explaining what the option does
    # requires 2 options back and continue
    # "How many words would you like to lean?" (accept only int between 3 and max num of images/sounds)
        # reset to 3 if invalid
    # changes amount of images to be shown in the learn section
    # changes which images can be shown in the play section
    # output menu at the end
def settings():
    learnCount = gameState.get('learnCount')
    maxLines = gameState.get('TOTAL_CSV_LINES')
    print(f'You are currently learning {learnCount} words.')
    newLearnCount = validatedInput(f'How many would you like to learn? (3-{maxLines})', 3, maxLines)

    while newLearnCount < 3 or newLearnCount > maxLines:
        print(f'{newLearnCount} is not allowed. Please choose again.')
        newLearnCount = validatedInput(f'How many would you like to learn? (3-{maxLines})', 3, maxLines)
    gameState['learnCount'] = newLearnCount

# Exit?
    # ouput message explaining what the option does
    # asks for exit confirmation
        # need 2 options back and exit
    # exits program
def exit():
    print("Goodbye! ")
    return True

# ### Main ###
Menu()
# # greets user
# print("Welcome! Before we start...")
#
# # verifies user gives valid input
# valid_input = False
# while Valid_input = False:
#     # asks user for whch interface they are using
#     user_interface = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)?").lower()
#     # checks if user input is valid
#     if user_interface == "m" or user_interface == "r" or user_interface == "i":
#         valid_input = True
#         print("Great! Have fun!")
#     else:
#         print("Sorry, invalid input detected. Please try again.")
#
# ### Make this a function ###
# # outputs options for user to interact with
# print("""MAIN MENU
#       1. Learn - Word Flashcards
#       2. Play - Seek and Find Game
#       3. Settings - Change Difficulty
#       4. Exit""")
#
# # verifies user gives valid input
# valid_input = False
# while Valid_input = False:
#     # asks user what option they want to pick
#     menu_choice = int(input("Choose and option:"))
#     # verifies that the option entered is valid
#     if menu_choice <= 4 and menu_choice >= 0:
#         valid_input = True
#     else:
#         print("Sorry, invalid input detected. Please try again.")