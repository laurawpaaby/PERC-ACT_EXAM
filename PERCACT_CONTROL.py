### IMPORTING NECESSARY PACKAGES:
from psychopy import visual, core, event, gui, data, sound   
import pandas as pd 
import glob 
import random 

#Initialize dialogue box
Dialoguebox = gui.Dlg(title = "funky problem spice(ALSO CALLLED BEST GRP EVERZZZ)")
Dialoguebox.addField("Participant ID (just make up one):")
Dialoguebox.addField("Age:")
Dialoguebox.addField("Gender:", choices = ["Female","Male","Other"])
Dialoguebox.addField("Condition:(Researcher chooses)", choices = ["0","1"])
Dialoguebox.show()

#Save data from dialoguebox
if Dialoguebox.OK:
    ID = Dialoguebox.data[0]
    Age = Dialoguebox.data[1]
    Gender = Dialoguebox.data[2]
    Condition = Dialoguebox.data[3]
elif Dialoguebox.Cancel:
    core.quit()


#getting the date and timestamp to make an unique logfile name we will remember
date = data.getDateStr()

#setting the variables of the data 
columns = ["Timestamp","ID","Age","Gender","Condition","ReactionTime", "Colourtask", "Stimulus"]
DATA = pd.DataFrame(columns = columns)


#VARIABLER
#defining stop watch
stopwatch = core.Clock()
#ad a certain point we would like to reset - in the beginning of a new stimuli eg.
stopwatch.reset()

#### --- MAKING TEXTS USED IN THE EXPERIMENT: ---#####
txt_introduction_control =  ''' 
Welcome to our experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles .\n\n
The grid will contain either a yellow or red circle.
In every trial you have to answer if the grid contains a red circle (r)or a yellow circle (y). You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press any key when you are ready to continue.
'''

txt_introduction_taste = '''
not used here :) '''

txt_bye = '''
The experiment is done. Thank you for your participation'''

texts = []
texts.append(txt_introduction_taste)
texts.append(txt_introduction_control)


###defining the image:
stimuli = glob.glob("/Users/laura/Google Drev/UNI 3.0/Perception and Action/EXAM/stimuli/stimulus*.jpg")

##FUNCTION TEXT
## function for showing text and waiting for key press
def msg_func(txt):
    message = visual.TextStim(win, text = txt, height = 0.05)
    message.draw()
    win.flip()
    event.waitKeys(keyList=["space"])

#Initialize window 
win = visual.Window(fullscr = True, units = "pix", color = "Black")
### SHOW INTRODUCTION 

#msg_func(txt_introduction_control)

for i in texts:
    if Condition == "1":
        msg_func(texts[1])
    else:
        msg_func(texts[0])


### show and press yellow or red and save time
suc_count = 0
while suc_count < 5:
    #Cross
    cross = visual.ShapeStim(win, vertices=((0,-50),(0,50),(0,0),(-50,0),(50,0)), lineWidth = 2, closeShape = False, lineColor = "White")
    cross.draw()
    win.flip()
    core.wait(1)
    image = stimuli[random.randint(0,4)]
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
        "Colourtask": key,
        "Stimulus": img,
        "ReactionTime": reaction_time}, ignore_index = True)


msg_func(txt_bye)


## saving data
#make logfile name
logfilename = "/Users/laura/Desktop/GitHub PercAct/logfiles_control/logfile_{}_{}_{}.csv".format(ID, date, Condition)
DATA.to_csv(logfilename)