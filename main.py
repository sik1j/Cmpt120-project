import pygame
import draw
import random
import sys

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
            # print(value)
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

# creates the canvas for the user to view
def play_canvas(canvas, item):
    image_num = random.randint(1, 4)
    new_canvas = draw.distributeItems(canvas, item, image_num)
    return new_canvas, image_num
    # return new_canvas, item, image_num

# 
def play():
    file = open('blackfoot.csv')
    # outputs how the game works to the user
    print('PLAY')
    print('This is a seek and find game. You will hear a word. Count how many of that item you find!')
    
    # asks the user and ensures valid input for how many lines to play
    num_rounds = validatedInput('How many rounds would you like to play?', 0, sys.maxsize)
    
    # creates a list of all items availale
    all_items = []
    for line in file:
        all_items.append(line)
    
    # creates a list of items within the learning count
    items = []
    count = 0
    while count < gameState.get('learnCount'):
        randItemIndex = random.randint(0, gameState.get('learnCount')-1)
        if all_items[randItemIndex] not in items:
            items.append(all_items[randItemIndex])
            count += 1
    
    # plays the rounds
    for i in range(0,num_rounds):
        # creates a list of the items that will be shown in the round
        round_items = []
        count = 0
        while count < 3:
            randItemIndex = random.randint(0, gameState.get('learnCount')-1)
            if items[randItemIndex] not in round_items:
                round_items.append(items[randItemIndex])
                count += 1
                
        # picks a random item to be the english name of the answer image
        rand_num = random.randint(0, len(round_items)-1)
        answer_item = round_items[rand_num]
        
        # creates a list of the image data
        round_images = []
        for x in range(len(round_items)):
            item = round_items[x]
            image = draw.cmpt120image.getImage(f'images/{item}.png')
            
            true_false = [True, False]
            if random.choice(true_false) == True:
                # recolor
                rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                image = draw.recolorImage(image, rand_color)
            if random.choice(true_false) == True:
                #minify
                image = draw.minify(image)
            if random.choice(true_false) == True:
                #mirror
                image = draw.mirror(image)
            round_images.append(image)
            
        # # creates an associated array with the image name being the key for the pixel data
        # round_data = {}
        # for x in range(len(round_images)):
        #    # round_data.append(round_items[x]:round_image[x])
        #    round_data[round_items[x]] = round_image[x]
        
        # generates the canvas
        # creates an associated array of the pixel data being the key for the num of repeats
        canvas = draw.cmpt120image.getWhiteImage(400,300)
        answer_data = {}
        for x in range(len(round_images)):
            canvas, item, num_repeats = play_canvas(canvas, round_images[x])
            # answer_data.append(item:num_repeats)
            # answer_data[item] = num_repeats
            answer_data[round_items[x]] = num_repeats
        draw.cmpt120image.showImage(canvas)
        
        # grabs the answer
        #image_pixels = round_data[answer_item]
        answer = answer_data[answer_item]
        
        # plays the sound for the user
        playSound(answer_item, ENV)
        # takes user answer and compares it to the answer
        user_answer = input('Listen to the word. How many of them can you find?')
        if user_answer == answer:
            input("That's right! Press enter to continue.")
        else:
            input("That's wrong. The right answer is {}. Press enter to continue".format(answer))
        
        
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
