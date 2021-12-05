# Loading modules
from psychopy import visual, core, event, data, gui
import glob # module for getting filenames
import random # module for randomization
import pandas as pd # module for creating data frame and saving log file

# Defining dialogue box (important that this happens before you define window)
box = gui.Dlg(title = "Paaby and Emmo hitting percact<333")
box.addField("Participant ID: ") 
box.addField("Age: ")
box.addField("Gender: ", choices=["Female", "Male", "Other" ])
box.addField("Condition: ", choices=["0","1" ])
box.show()

if box.OK: # To retrieve data from popup window
    ID = box.data[0]
    AGE = box.data[1]
    GENDER = box.data[2]
    CONDITION = box.data[3]
elif box.Cancel: # To cancel the experiment if popup is closed
    core.quit()

# define window
win = visual.Window(fullscr = True, color = "black")

# define stop watch
stopwatch = core.Clock()

# get date for unique logfile name
date = data.getDateStr()

# get image file names that end with .png
stimuli = glob.glob("stimuli/*.png")

# randomize order of images (not sure about this one)
random.shuffle(stimuli)

# Define logfile 
# Prepare pandas data frame for recorded data
columns = ['timestamp','id', 'age', 'aender', 'stimulus', 'accuracy', 'reaction_time']
logfile = pd.DataFrame(columns=columns)

############## text ###################

# instructions
instruction = '''
Welcome to our taste experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles .\n\n
The grid will contain either a yellow or red circle.
In every trial you have to answer if the grid contains a red circle (r)or a yellow circle (y). You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press any key when you are ready to continue.
'''

candytime = '''
Before you start the experiment, we will ask to give you a piece of hard candy.\n\n
We will ask you to close your eyes as we put the candy into your mouth.\n\n
You will have to keep the candy in your mouth and suck on it continuingly throughout the experiment.\n\n
Remember that for each trial you have to answer if the grid contains a red circle (r)or a yellow circle (y).\n\n\n
Press any key when you are ready to start the experiment.
'''

goodbye = '''
The experiment is done. Thank you for your participation'''

texts = []
texts.append(instruction)
texts.append(candytime)
texts.append(goodbye)


## FUNCTION TEXT
## Function for showing text and waiting for key press
def msg_func(txt):
    message = visual.TextStim(win, text = txt, height = 0.05)
    message.draw()
    win.flip()
    event.waitKeys(keyList=["space"])

# Initialize window 
win = visual.Window(fullscr = True, units = "pix", color = "Black")


### SHOW INTRODUCTION 
msg_func(instruction)

#### press next via space 
for i in stimuli:
    cross = visual.ShapeStim(win, vertices=((0,-50),(0,50),(0,0),(-50,0),(50,0)), lineWidth = 2, closeShape = False, lineColor = "White")
    cross.draw()
    win.flip()
    core.wait(1)
    img = visual.ImageStim(win, image = i)
    img.draw()
    #stopwatch.reset()
    win.flip()
    event.waitKeys(keyList = ["r", "y"])
    #reaction_time = stopwatch.getTime()


### show and press yellow or red and save time
suc_count = 0
while suc_count < 5:
    #Cross
    cross = visual.ShapeStim(win, vertices=((0,-50),(0,50),(0,0),(-50,0),(50,0)), lineWidth = 2, closeShape = False, lineColor = "White")
    cross.draw()
    win.flip()
    core.wait(1)
    image = stimuli[random.randint(0,6)]
    img = visual.ImageStim(win, image = image)
    img.draw()
    stopwatch.reset()
    win.flip()
    key = event.waitKeys(keyList = ["y","r","escape"])
    reaction_time = stopwatch.getTime()
    if image[-5] == "y" and key[0] == "y" or image[-5] == "r" and key[0] == "r":
        suc_count = suc_count + 1 
    elif key[0] == "escape":
        core.quit()
        win.close()
    else:
        suc_count = 0
    DATA = DATA.append({
        "Timestamp":date,
        "ID": ID,
        "Age":Age,
        "Gender": Gender,
        "Condition": Condition,
        "ReactionTime": reaction_time}, ignore_index = True)


msg_func(txt_bye)


## saving data
#make logfile name
logfilename = "/Users/emmaolsen/OneDrive - Aarhus Universitet/UNI/P&A/Exam/logfiles/logfile_{}_{}_{}.csv".format(ID, date, Condition)
DATA.to_csv(logfilename)


