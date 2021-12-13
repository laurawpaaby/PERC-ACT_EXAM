### IMPORTING NECESSARY PACKAGES:
from psychopy import visual, core, event, gui, data   
import pandas as pd 
import glob 
import random 

#Initialize dialogue box
Dialoguebox = gui.Dlg(title = "Participant Information")
Dialoguebox.addField("Participant ID:")
Dialoguebox.addField("Age:")
Dialoguebox.addField("Gender:", choices = ["Female","Male","Other"])
Dialoguebox.addField("Condition:(Researcher chooses)", choices = ["0","1","2"])
Dialoguebox.addField("I have received written information about the study and consent to participate.", choices = ["Yes","No"])
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
columns = ["Timestamp","ID","Age","Gender","Condition","ReactionTime", "Colourtask", "Colourrating", "Stimulus"]
DATA = pd.DataFrame(columns = columns)


#VARIABLER
#defining stop watch
stopwatch = core.Clock()
#ad a certain point we would like to reset - in the beginning of a new stimuli eg.
stopwatch.reset()

#### --- MAKING TEXTS USED IN THE EXPERIMENT: ---#####
txt_introduction_taste = '''
Welcome to our experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles.\n\n
The grid will contain either a yellow or red circle.
In each trial you have to investigate the grid and answer if it contains a red circle or a yellow circle. \n
You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n\n
Press space when you are ready to continue. '''

txt_instruction = '''
Before you start the experiment, we will give you a piece of candy.\n
We will ask you to close your eyes as we put the candy into your mouth.\n
You will have to keep the candy in your mouth and suck on it continuingly throughout the experiment - pay attention to its taste!\n
Remember that for each trial you have to answer if the grid contains a red circle (r) OR a yellow circle (y).\n
Should you have any questions, please ask the researchers. \n\n
Otherwise, please let the researchers know that you are now ready to receive the candy. 
'''


txt_introduction_control =  ''' 
Welcome to our experiment!\n\n
In a moment, you will see a grid of 8 x 6 coloured circles .\n\n
The grid will contain either a yellow or red circle.
In every trial you have to answer if the grid contains a red circle (r)or a yellow circle (y). You submit your response by pressing either r (for red) or y (for yellow) on the keyboard.\n\n
Press any key when you are ready to continue.
'''


txt_finish_colour = '''You are now done with the first part of the experiment. \n
You now have to indicate the colour you believe matches the taste of the candy the best: \n
A color spectrum and a scale will be shown to you shortly. \n
Click on the scale to submit your answer.  \n \n
Press space to continue.'''


texts = []
texts.append(txt_introduction_taste)
texts.append(txt_introduction_control)


###defining the image:
stimuli = glob.glob("/Users/emmaolsen/PERC-ACT_EXAM/stimuli/*.png")
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

for i in texts:
    if Condition == "0":
        msg_func(texts[1])
    else:
        msg_func(texts[0])


msg_func(txt_instruction)

### ADD COUNTDOWN (10 SECONDS)
for x in (10,9,8,7,6,5,4,3,2,1):
    count_stuff(x)


#################### NEW LOOP ####################
for stimulus in stimuli:
    cross = visual.ShapeStim(win, vertices=((0,-50),(0,50),(0,0),(-50,0),(50,0)), lineWidth = 2, closeShape = False, lineColor = "White")
    cross.draw()
    win.flip()
    core.wait(1)
    img = visual.ImageStim(win, image = stimulus)
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
        "Stimulus": stimulus,
        "ReactionTime": reaction_time}, ignore_index = True)

msg_func(txt_finish_colour)


### ----- COLOUR RATING ----- ####
# making window:
win_color = visual.Window(color = "black", fullscr = True)
#Defining stimulus image
color_stimuli= visual.ImageStim(win_color,image="/Users/emmaolsen/PERC-ACT_EXAM/colour_spectrum.jpg",pos = [0,0.3],size=(1.2,2))

#Defining scale function
ratingScale = visual.RatingScale(win_color, 
scale = None,          #This makes sure there's no subdivision on the scale.
low = 1,               #This is the minimum value I want the scale to have.
high = 100,             #This is the maximum value of the scale.
singleClick = True,    #This allows the user to submit a rating by one click.
showAccept = False,    #This shows the user's chosen value in a window below the scale.
markerStart = 50,       #This sets the rating scale to have its marker start on 5.
#labels = ['Negative Emotion', 'Positive Emotion'], #This creates the labels.
pos = [0, -0.6],
size = 2)      #This sets the scale's position.


while ratingScale.noResponse:
    color_stimuli.draw()
    ratingScale.draw() 
    win_color.flip()
    rating = ratingScale.getRating()
    print(rating)

win_color.close()
win.close()


DATA = DATA.append({
  "Timestamp":date,
    "ID": ID,
    "Age":Age,
    "Gender": Gender,
    "Condition": Condition,
    "Colourrating": rating
    }, ignore_index = True)


win_bye = visual.Window(fullscr = True, units = "pix", color = "Black")

message = visual.TextStim(win_bye, text = "The experiment is done. Thank you for your participation! :-)<3")
message.draw()
win_bye.flip()
core.wait(1)
event.waitKeys()



## saving data
#make logfile name
logfilename = "/Users/emmaolsen/PERC-ACT_EXAM/logfiles/logfile_{}_{}_{}.csv".format(ID, date, Condition)
DATA.to_csv(logfilename)
