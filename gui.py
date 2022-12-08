from customtkinter import *

is_on = False

#---------------------------------------------------------------------------------------------------------------------------
# Visuals

def window(master, title="", size="600x500"):
    '''
    :param: Title - The name of the window
    :param: Size - The size of the window in pixels, Example: '500x500'
    '''
    newWindow = CTkToplevel(master)

    newWindow.title(title)
    newWindow.geometry(size)

    return newWindow

def label(screen, text, x, y, size, fontFamily='Arial'):
    '''
    Create display text on the screen

    :param: text - The text to display
    :param: x - The x position of the text in pixels
    :param: y - the y position of the text in pixels
    :param: size - The size of the label
    '''
    userLabel = CTkLabel(screen, text=text)
    # userLabel.place(x=x, y=y)
    userLabel.grid(column=x, row=y)
    # userLabel.pack()

    textSize(userLabel, size, fontFamily)

    return userLabel

def button(screen, x, y, width, height, text="", image=None, command=None):
    '''
    Creates a GUI button on the screen for the user to interact with.

    :param: text - The button display text
    :param: x - The x position of the button
    :param: y - The y position of the button
    :param: width - how wide the button is
    :param: height - how tall the button is
    :param: command - What function to run when the button is clicked (optional)
    '''
    if image == None:
        userButton = CTkButton(screen, text=text, width=width, height=height, command=command)
        # userButton.place(x=x, y=y)
        userButton.grid(column=x, row=y)
        # userButton.pack()
    else:
        userButton = CTkButton(screen, text=text, image=image, width=width, height=height, command=command)
        # userButton.place(x=x, y=y)
        userButton.grid(column=x, row=y)
        # userButton.pack()

    return userButton

def textArea(x, y, width, height):
    '''
    Creates a text area for the user to type in

    :param: x - The x position of the text area
    :param: y - The y position of the text area
    :param: width - The width of the text area
    :param: height - The height of the text area
    '''
    textBox = CTkTextbox(width=width, height=height)
    # textBox.place(x=x, y=y)
    textBox.grid(column=x, row=y)
    # textBox.pack()

    return textBox

#---------------------------------------------------------------------------------------------------------------------------
# Colors and Sizes

def background(screen, color):
    '''
    Changes the background color of the window

    :param: screen - The window to change the color of
    :param: color - The new window color
    '''
    screen['bg'] = f'#{color}'

def fill(object, color):
    '''
    Changes the color of a given label

    :param: object - The label or button to change the color of
    :param: color - the new color of the label
    '''
    if isinstance(object, CTkLabel):
        object.configure(fg=f'#{color}')
    elif isinstance(object, CTkButton):
        object.configure(bg_color=f'#{color}')

def textSize(label, size, fontFamily='Arial'):
    '''
    Changes the size of the given label text

    :param: label - The label to change the size of
    :param: size - The new size of the label
    '''
    label.configure(font=(fontFamily, size))

#---------------------------------------------------------------------------------------------------------------------------
# Utilities

