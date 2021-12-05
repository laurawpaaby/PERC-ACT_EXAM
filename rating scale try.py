# load modules
from psychopy import visual

# define window
win = visual.Window()

#Defining stimulus image
color_stimuli= visual.ImageStim(win,image="/Users/laura/Desktop/GitHub PercAct/colour_spectrum.jpg",pos = [0,0.3],size=(1.2,2))



#Defining stimulus image


#Defining scale function
ratingScale = visual.RatingScale(win, 
scale = None,          #This makes sure there's no subdivision on the scale.
low = 1,               #This is the minimum value I want the scale to have.
high = 20,             #This is the maximum value of the scale.
singleClick = True,    #This allows the user to submit a rating by one click.
showAccept = False,    #This shows the user's chosen value in a window below the scale.
markerStart = 10,       #This sets the rating scale to have its marker start on 5.
#labels = ['Negative Emotion', 'Positive Emotion'], #This creates the labels.
pos = [0, -0.6],
size = 2)      #This sets the scale's position.



#Get question
#msg(random_con)

while ratingScale.noResponse:
    color_stimuli.draw()
    ratingScale.draw()
    win.flip()
    rating = ratingScale.getRating()
    print(rating)

win.close()