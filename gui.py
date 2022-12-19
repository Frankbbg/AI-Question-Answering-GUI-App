####################################################################################################################################################
# Name: Inquisitor: The AI Question Answering App                                                                                                  #
# Description: This module is a helper module that contains all the customtkinter functions and customized functions I have defined.               #
# Author: Braden Shrum                                                                                                                             #
# Date: 12/18/2022                                                                                                                                 #
####################################################################################################################################################

from customtkinter import *

#---------------------------------------------------------------------------------------------------------------------------
# Visuals

def window(master, title="", size="600x500"):
    '''
    :param: Title - The name of the window
    :param: Size - The size of the window in pixels, Example: '500x500'
    '''
    newWindow = CTkToplevel(master) # Create a new window

    # Title the window and define it's size
    newWindow.title(title)
    newWindow.geometry(size)

    return newWindow # return the object for later use

def label(screen, text, x, y, size, fontFamily='Arial', positionType = 'place'):
    '''
    Create display text on the screen

    :param: text - The text to display
    :param: x - The horizontal position of the text in pixels
    :param: y - the vertical position of the text in pixels
    :param: size - The size of the label
    :param: fontFamily - the font of the text
    :param: positionType - the method that the text is positioned on the screen
    '''
    #create a label object
    userLabel = CTkLabel(screen, text=text)

    #check which position type the user is using. Default to 'place'
    if positionType == 'place':
        userLabel.place(x=x, y=y) # place the object at specific x, y coordinates
    elif positionType == 'grid':
        userLabel.grid(column=x, row=y) # snap the object to a pre-defined grid
    elif positionType == 'pack':
        userLabel.pack() # let customtkinter place the object automatically

    textSize(userLabel, size, fontFamily) # set the text size

    return userLabel # return the label object for later use

def button(screen, x, y, width, height, text="", image=None, command=None):
    '''
    Creates a GUI button on the screen for the user to interact with.

    :param: text - The button display text
    :param: x - The horizontal position of the button
    :param: y - The vertical position of the button
    :param: width - how wide the button is
    :param: height - how tall the button is
    :param: command - What function to run when the button is clicked (optional)
    '''
    if image == None: # check if the button does not contain an image
        # create the button object without an image and place it on the screen at specific coordinates
        userButton = CTkButton(screen, text=text, width=width, height=height, command=command)
        userButton.place(x=x, y=y)
    else:
        # create a button object with an image and without text and place it at specific coordinates
        userButton = CTkButton(screen, text=text, image=image, width=width, height=height, command=command)
        userButton.place(x=x, y=y)

    return userButton # return the button object for later use

def textArea(x, y, width, height):
    '''
    Creates a text area for the user to type in

    :param: x - The horizontal position of the text area
    :param: y - The vertical position of the text area
    :param: width - The width of the text area
    :param: height - The height of the text area
    '''
    # create a textbox object and place it at specific coordinates
    textBox = CTkTextbox(width=width, height=height)
    textBox.place(x=x, y=y)

    return textBox # return the textbox object for later use

def slidebar(screen, x, y, highValue, variable, lowValue=0, step=0.0, default_value=0.0, command=None):
    '''
    :param: screen - the window to place the object onto
    :param: x - the horizontal position of the slider
    :param: y - the vertical position of the slider
    :param: highValue - the highest value on the slider
    :param: variable - the variable to assign the slider value to. NOTE: has to be a DoubleVar() type.
    :param: lowValue - the lowest value on the slider. Default 0
    :param: step - the amount of steps it takes to go from lowValue to highValue. Default 0.0
    :param: default_value - the value the slider is at when the program runs. Default 0.0
    :param: command - the command that's run when you change the slider. Default None
    '''
    userSlideBar = CTkSlider(screen, from_=lowValue, to=highValue, number_of_steps=step, command=command, variable=variable) # initialize the slider object
    userSlideBar.set(default_value) # set the default value
    userSlideBar.place(x=x, y=y) # place the object at specific coordinates

    return userSlideBar # return the slider object for later use

#---------------------------------------------------------------------------------------------------------------------------
# Colors and Sizes

def background(screen, color):
    '''
    Changes the background color of the window

    :param: screen - The window to change the color of
    :param: color - The new window color
    '''
    screen['bg'] = f'#{color}' # change the 'bg' attribute of the background to a specific color

def fill(object, color):
    '''
    Changes the color of a given label

    :param: object - The label or button to change the color of
    :param: color - the new color of the label
    '''
    if isinstance(object, CTkLabel): # if the object is a label
        object.configure(fg=f'#{color}') # change the color of the label
    elif isinstance(object, CTkButton): # if the object is a button
        object.configure(bg_color=f'#{color}') # change the color of the button

def textSize(label, size, fontFamily='Arial'):
    '''
    Changes the size of the given label text

    :param: label - The label to change the size of
    :param: size - The new size of the label
    '''
    label.configure(font=(fontFamily, size)) # configure the label to a different size and font