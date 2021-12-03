### IMPORTING NECESSARY PACKAGES:
from psychopy import visual, core, event, gui, data, sound   
import pandas as pd 
import glob 
import random 
import numpy as np

#win = visual.Window(color = 'black',fullscr = True) #SETTING WINDOW
#path = "/Users/laura/Google Drev/UNI 3.0/Perception and Action/EXAM" #SETTING PATH

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
columns = ["Timestamp","ID","Age","Gender","Condition","ReactionTime"]
DATA = pd.DataFrame(columns = columns)


#### --- MAKING TEXTS USED IN THE EXPERIMENT: ---#####
txt_introduction_taste = '''
Welcome to this experiment, thank you for participating ..... a sweet drop will be given to you .... waiting time ..... 
press space to continue 
'''

txt_introduction_control = ''' welcome, thanks for participating .... waiting time ....  (if you want new line /n
this gives new line ;) press space to continue 
'''

# potential middle pause new taste text:
txt_break = ''' new taste will be given to you '''

txt_bye = ''' thank you for participating ... ''' 

texts = []
texts.append("testing text one, control")
texts.append("testing text one, taste")

###defining the image:
image = glob.glob("/stimuli/stimulus*.jpg")

##FUNCTION TEXT
## function for showing text and waiting for key press
def msg_func(txt):
    message = visual.TextStim(win, text = txt, height = 0.05)
    message.draw()
    win.flip()
    event.waitKeys(keyList=["space"])


### FUNCTION SHOW STIMULI 



#### ---- RUNNING THE EXPERIMENT ---- #####
#Initialize window 
#win = visual.Window(fullscr = True, units = "pix", color = "Black")


### SHOW INTRODUCTION 
for i in texts:
    if Condition == "0":
        msg_func(﻿i[0])
    else:
        msg_func(i[1])



### TASK START 

msg_func(txt_bye)



