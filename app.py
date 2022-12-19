####################################################################################################################################################
# Name: Inquisitor: The AI Question Answering App                                                                                                  #
# Description: This program will ask a question through user input through a GUI textbox, and the program will generate a response to the question #
#              using OpenAI's API once the user has pressed the appropriate button. A second button also exists: A button that generates a         #
#              question for the user automatically also using OpenAI's API. The third and last button opens the settings window, which allows the  #
#              user to change three different sliders that change how the AI outputs answers.                                                      #
# Author: Braden Shrum                                                                                                                             #
# Date: 12/18/2022                                                                                                                                 #
####################################################################################################################################################

import gui
import openai
import time
from PIL import ImageTk, Image

openai.api_key = "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" #OpenAI API Key to generate text

# initialize the main window and set the size
mainWindow = gui.CTk()
mainWindow.geometry("500x500")

# set the settings as global variables
temperature = gui.DoubleVar(value=0.8)
frequency_penalty = gui.DoubleVar(value=0.0)
presence_penalty = gui.DoubleVar(value=0.0)

def generateResponse(prompt, questionLabel, responseLabel, questionBox, maxTokens=256, temperature=0.8, frequency_penalty=0.0, presence_penalty=0.0):
    '''
    Creates a respsonse using the OpenAI API and displays it to the console

    :param: screen - the screen object to display to
    :param: prompt - The text to begin with
    :param: questionBox - The textbox to take the question from
    :param: maxTokens - How long the AI generation will be
    :param: temperature - How random the AI generation will be
    :param: frequency_penalty - How often the AI repeats itself
    :param: presence_penalty - How much the AI moves to different topics
    '''
    if prompt != "": # if the user typed something into the textbox
        responseLabel.configure(text="AI is typing...") # set the output text to "AI is Typing"
        questionLabel.configure(text=questionBox.textbox.get(1.0, 10.0)) # get the text from the textbox and set it as the question header

        time.sleep(0.5)

        # get a response to the question from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=maxTokens,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=["\n"]
        ).choices[0].text
    else: # if the user didn't type anything into the textbox
        response = "Ask me any question!" # set the response to a predefined text

    responseLabel.configure(text=response) # render the response onto the screen

def generateQuestion(prompt, questionBox, maxTokens=256, temperature=0.8, frequency_penalty=0.0, presence_penalty=0.0):
    '''
    Creates a question and puts it in the textbox

    :param: screen - the screen object to display to
    :param: prompt - The text to begin with
    :param: questionBox - The textbox to put the question into
    :param: maxTokens - How long the AI generation will be
    :param: temperature - How random the AI generation will be
    :param: frequency_penalty - How often the AI repeats itself
    :param: presence_penalty - How much the AI moves to different topics
    '''

    # get a question from OpenAI
    completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=maxTokens,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=["\n"]
    ).choices[0].text

    response = '' # set the final question variable

    # loop over every character in the question
    for char in completion:
        if char != '?': # if the character is not a question mark
            response += char # add the character to the final response
        else: # if the character is a question mark
            response += '?' # add the final question mark and stop looking for text
            break

    if questionBox.textbox.get(1.0, 10.0) == "": # if the textbox contains no text
        questionBox.textbox.insert(0.0, response) # add the final question to the textbox
    else: # if the textbox does contain text
        questionBox.textbox.delete(0.0, 10.0) # delete the text in the textbox
        questionBox.textbox.insert(0.0, response) # add the final question to the textbox

def mainDisplay(screen):

    # the prompt text to make the AI output factual answers
    fewShotExample = """I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown" then proceed to explain why I cannot give an answer to the question.

                Q: 
                What is human life expectancy in the United States?

                A: 
                Human life expectancy in the United States is 78 years. Although in future years this could increase.


                Q: 
                Who was president of the United States in 1955?

                A: 
                Dwight D. Eisenhower was president of the United States in 1955.


                Q: 
                Which party did he belong to?

                A: 
                He belonged to the Republican Party.


                Q: 
                What is the square root of banana?

                A: 
                Unknown | A banana is an object, not a number. You can only take the square root of numbers, therefore the square root of banana will not work


                Q: 
                How does a telescope work?

                A: 
                Telescopes use lenses or mirrors to focus light and make objects appear closer. These methods were used a long time ago by ancient astronomers to observe the stars. They have found and named the constilations we know today.


                Q: 
                Where were the 1992 Olympics held?

                A: 
                The 1992 Olympics were held in Barcelona, Spain.


                Q: 
                How many squigs are in a bonk?

                A: 
                Unknown | squigs to bonks is not a valid unit conversion since neither squigs nor bonks are units. They are simply nonsense words.


                Q:"""

    # the prompt to get the AI to generate a question
    surpriseMePrompt = 'Ask me a unique, logical question about the anything\n\n'

    # the path to the settings icon
    settingsIconPath = "C:\\Users\\frank\\OneDrive\\Documents\\School Documents\\Fall 2022\\Second 8 Weeks\\Intro to Sofware Development\\Final Project\\Inquisitor\\AI-Question-Answering-GUI-App\\images\\Settings_Icon.png"
    img = ImageTk.PhotoImage(Image.open(settingsIconPath)) # make the image a PhotoImage object

    gui.background(screen, "d32") # change the background color to red
    
    titleLabel = gui.label(screen, "Inquisitor: The AI Question Answering App", 20, 0, 20, "Times New Roman") # the title screen label
    questionLabel = gui.label(screen, "", 0, 250, 20) # the label that renders the questions
    responseLabel = gui.label(screen, "", 0, 350, 15) # the label that renders the responses
    
    questionBox = gui.textArea(0, 100, 500, 100) # the textbox to enter questions into
    
    # the button that triggers a response from OpenAI
    responseButton = gui.button(screen, 100, 200, 100, 50, "Get a Response", command=lambda: generateResponse(f"{fewShotExample}{questionBox.textbox.get(1.0, 10.0)}\n\nA:\n", questionLabel, responseLabel, questionBox, temperature=temperature.get(), frequency_penalty=frequency_penalty.get(), presence_penalty=presence_penalty.get())) #<----- get prompt from textbox
    # the button that triggers a question from OpenAI
    surpriseMeButton = gui.button(screen, 300, 200, 100, 50, "Surprise Me!", command=lambda: generateQuestion(f"{surpriseMePrompt}", questionBox, temperature=temperature.get(), frequency_penalty=frequency_penalty.get(), presence_penalty=presence_penalty.get()))
    # the button that opens the settings window
    settingsButton = gui.button(screen, 450, 30, 50, 50, image=img, command=settingsDisplay)
    
    # the coloring for all the labels
    gui.fill(questionLabel, "111")
    gui.fill(titleLabel, "342")
    gui.fill(responseButton, "e32")

    # the wraplength of the two display labels
    responseLabel.configure(wraplength=625)
    questionLabel.configure(wraplength=625)

def settingsDisplay():
    '''
    Displays the settings window for generation
    '''
    global temperature, frequency_penalty, presence_penalty #get the three settings variables from the global scope
        
    # the warning text for the settings window
    warningText = "Change the way the AI outputs text. Warning: This may cause the AI to write incorrect answers to your questions. Read the questions carefully"

    # the settings window creation
    settingsWindow = gui.window(mainWindow, "AI Settings", "500x500")

    # the display labels for the title and the warning
    titleLabel = gui.label(settingsWindow, "AI Settings", 200, 0, 20)
    warningLabel = gui.label(settingsWindow, warningText, 30, 50, 10)

    # configure the warning label wraplength
    warningLabel.configure(wraplength=600)

    # display the title labels for the settings sliders
    temperatureLabel = gui.label(settingsWindow, "Temperature", 0, 100, 25)
    frequencyPenaltyLabel = gui.label(settingsWindow, "Frequency Penalty", 0, 200, 25)
    presencePenaltyLabel = gui.label(settingsWindow, "Presence Penalty", 0, 300, 25)

    # display the settings sliders
    tempuratureslidebar = gui.slidebar(settingsWindow, 0, 150, 1, step=10, default_value=0.8, variable=temperature)
    frequencyPenaltyslidebar = gui.slidebar(settingsWindow, 0, 250, 2, step=20, default_value=0.0, variable=frequency_penalty)
    presencePenaltyslidebar = gui.slidebar(settingsWindow, 0, 350, 2, step=20, default_value=0.0, variable=presence_penalty)

    # display the number that the sliders are at
    temperatureNumber = gui.label(settingsWindow, tempuratureslidebar.get(), 0, 175, 10)
    frequencyPenaltyNumber = gui.label(settingsWindow, frequencyPenaltyslidebar.get(), 0, 275, 10)
    presencePenaltyNumber = gui.label(settingsWindow, presencePenaltyslidebar.get(), 0, 375, 10)


    def changeTemperature(event):
        '''
        sets the label that defines the temperature slider position
        :param: event - a customtkinter event
        '''
        temperatureNumber.configure(text="{: .1f}".format(temperature.get()))

    def changeFrequencyPenalty(event):
        '''
        sets the label that defines the frequency_penalty slider position
        :param: event - a customtkinter event
        '''
        frequencyPenaltyNumber.configure(text="{: .1f}".format(frequency_penalty.get()))

    def changePresencePenalty(event):
        '''
        sets the label that defines the presence_penalty slider position
        :param: event - a customtkinter event
        '''
        presencePenaltyNumber.configure(text="{: .1f}".format(presence_penalty.get()))

    # set the command of the sliders
    tempuratureslidebar.configure(command=changeTemperature)
    frequencyPenaltyslidebar.configure(command=changeFrequencyPenalty)
    presencePenaltyslidebar.configure(command=changePresencePenalty)

def main():
    mainDisplay(mainWindow)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()