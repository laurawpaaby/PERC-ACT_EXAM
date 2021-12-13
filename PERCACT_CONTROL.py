### IMPORTING NECESSARY PACKAGES:
from psychopy import visual, core, event, gui, data, sound   
import pandas as pd 
import glob 
import random 

#Initialize dialogue box
Dialoguebox = gui.Dlg(title = "Participant Information")
Dialoguebox.addField("Participant ID:")
Dialoguebox.addField("Age:")
Dialoguebox.addField("Gender:", choices = ["Female","Male","Other"])
Dialoguebox.addField("Choose 0", choices = ["0","1", "2"])
Dialoguebox.addField("I have received written information about\n the study and consent to participate:", choices = ["Yes", "No"])
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
In a moment, you will see a grid of 8 x 6 coloured circles.\n\n
The grid will contain either a yellow or red circle.
In each trial you have to investigate the grid and answer if it contains a red circle or a yellow circle. \n
You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press space when you are ready to continue. '''

txt_introduction_taste = '''
not used here :) '''

txt_bye = '''
The experiment is done. Thank you for your participation! '''

texts = []
texts.append(txt_introduction_taste)
texts.append(txt_introduction_control)


###defining the image:
stimuli = glob.glob("/Users/laura/Desktop/GitHub PercAct/stimuli/*.png")
random.shuffle(stimuli)

##FUNCTION TEXT
## function for showing text and waiting for key press
def msg_func(txt):
    message = visual.TextStim(win, text = txt)
    message.draw()
    win.flip()
    event.waitKeys(keyList=["space"])

## for the count down
def count_stuff(n):
    message = visual.TextStim(win, text = n, units = "pix", height = 90)
    message.draw()
    win.flip()
    core.wait(1)

#Initialize window 
win = visual.Window(fullscr = True, units = "pix", color = "Black")
### SHOW INTRODUCTION 

#msg_func(txt_introduction_control)

for i in texts:
    if Condition == "0":
        msg_func(texts[1])
    else:
        msg_func(texts[0])

### ADD COUNTDOWN (10 SECONDS)
for x in (10,9,8,7,6,5,4,3,2,1):
    count_stuff(x)


### show and press yellow or red and save time
for i in stimuli:
    cross = visual.ShapeStim(win, vertices=((0,-50),(0,50),(0,0),(-50,0),(50,0)), lineWidth = 2, closeShape = False, lineColor = "White")
    cross.draw()
    win.flip()
    core.wait(1)
    img = visual.ImageStim(win, image = i)
    img.draw()
    stopwatch.reset()
    win.flip()
    key = event.waitKeys(keyList = ["y","r","escape"])
    reaction_time = stopwatch.getTime()
    DATA = DATA.append({
        "Timestamp":date,
        "ID": ID,
        "Age":Age,
        "Gender": Gender,
        "Condition": Condition,
        "Colourtask": key,
        "Stimulus": i,
        "ReactionTime": reaction_time}, ignore_index = True)



msg_func(txt_bye)


## saving data
#make logfile name
logfilename = "/Users/laura/Desktop/GitHub PercAct/logfiles_control/logfile_control_{}_{}_{}.csv".format(ID, date, Condition)
DATA.to_csv(logfilename)