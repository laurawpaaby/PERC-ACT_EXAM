### IMPORTING NECESSARY PACKAGES:
from psychopy import visual, core, event, gui, data, sound   
import pandas as pd 
import glob 
import random 

#Initialize dialogue box
#Dialoguebox = gui.Dlg(title = "funky problem spice(ALSO CALLLED BEST GRP EVERZZZ)")
#Dialoguebox.addField("Participant ID (just make up one):")
#Dialoguebox.addField("Age:")
#Dialoguebox.addField("Gender:", choices = ["Female","Male","Other"])
#Dialoguebox.addField("Condition:(Researcher chooses)", choices = ["0","1"])
#Dialoguebox.show()

#Save data from dialoguebox
i#f Dialoguebox.OK:
#    ID = Dialoguebox.data[0]
#    Age = Dialoguebox.data[1]
#    Gender = Dialoguebox.data[2]
#    Condition = Dialoguebox.data[3]
#elif Dialoguebox.Cancel:
#    core.quit()


#getting the date and timestamp to make an unique logfile name we will remember
#date = data.getDateStr()

#setting the variables of the data 
#columns = ["Timestamp","ID","Age","Gender","Condition","ReactionTime", "Colourtask"]
#DATA = pd.DataFrame(columns = columns)


#VARIABLER
#defining stop watch
stopwatch = core.Clock()
#ad a certain point we would like to reset - in the beginning of a new stimuli eg.
stopwatch.reset()

#### --- MAKING TEXTS USED IN THE EXPERIMENT: ---#####
txt_introduction_taste = '''
Welcome to our experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles .\n\n
The grid will contain either a yellow or red circle.
In every trial you have to answer if the grid contains a red circle (r)or a yellow circle (y). You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press any key when you are ready to continue.

Before you start the experiment, we will ask to give you a piece of hard candy.\n\n
We will ask you to close your eyes as we put the candy into your mouth.\n\n
You will have to keep the candy in your mouth and suck on it continuingly throughout the experiment.\n\n
Remember that for each trial you have to answer if the grid contains a red circle (r)or a yellow circle (y).\n\n\n
Press any key when you are ready to start the experiment.
'''


txt_introduction_control =  ''' 
Welcome to our experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles .\n\n
The grid will contain either a yellow or red circle.
In every trial you have to answer if the grid contains a red circle (r)or a yellow circle (y). You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press any key when you are ready to continue.
'''

# potential middle pause new taste text:
txt_break = ''' new taste will be given to you '''

txt_bye = '''
The experiment is done. Thank you for your participation'''

txt_finish_colour = '''You are now done with the first part of the experiment. \n
You are now to rate the colour of the taste you were given: \n
A color spectrum and a scale will be shown to you shortly,  \n
press with the mouse which colour on the scale you found to be the best match to your taste.  \n \n
Press space to continue.'''


texts = []
texts.append(txt_introduction_taste)
texts.append(txt_introduction_control)




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


msg_func(txt_break)



#msg_func(txt_break)
stimuli_lol = glob.glob("/Users/laura/Desktop/GitHub PercAct/stimuli_lol/*.jpg")

for i in stimuli_lol:
    imgf = visual.ImageStim(win, image = i)
    imgf.draw() 
    stopwatch.reset()
    win.flip()
    key = event.waitKeys(keyList = ["y","r","escape"])
    reaction_time = stopwatch.getTime()
    if imgf[-5] == "y" and key[0] == "y" or imgf[-5] == "r" and key[0] == "r":
    elif key[0] == "escape":
        core.quit()
        win.close()
    print(reaction_time)



msg_func(txt_finish_colour)