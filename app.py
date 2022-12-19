##################################################################################################################################################
# Name: Inquisitor: The AI Question Answering App                                                                                                #
# Description: This program will take user input for a number greater than 1, and will find all the prime numbers up to or including that number #
# Author: Braden Shrum                                                                                                                           #
# Date: 11/18/2022                                                                                                                               #
##################################################################################################################################################

import gui
import openai
import time
from PIL import ImageTk, Image

openai.api_key = "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"

mainWindow = gui.CTk()
mainWindow.geometry("500x500")

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
    if prompt != "":
        responseLabel.configure(text="AI is typing...")
        questionLabel.configure(text=questionBox.textbox.get(1.0, 10.0))
        print(questionBox.textbox.get(1.0, 10.0))

        time.sleep(0.5)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=maxTokens,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=["\n"]
        ).choices[0].text
    else:
        response = "Ask me any question!"

    responseLabel.configure(text=response)

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

    completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=maxTokens,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=["\n"]
    ).choices[0].text

    response = ''

    for char in completion:
        if char != '?':
            response += char
        else:
            response += '?'

    if questionBox.textbox.get(1.0, 10.0) == "":
        questionBox.textbox.insert(0.0, response)
    else:
        questionBox.textbox.delete(0.0, 10.0)
        questionBox.textbox.insert(0.0, response)

def mainDisplay(screen):

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

    surpriseMePrompt = 'Ask me a unique, logical question about the anything\n\n'

    settingsIconPath = "C:\\Users\\frank\\OneDrive\\Documents\\School Documents\\Fall 2022\\Second 8 Weeks\\Intro to Sofware Development\\Final Project\\Inquisitor\\AI-Question-Answering-GUI-App\\images\\Settings_Icon.png"
    img = ImageTk.PhotoImage(Image.open(settingsIconPath))

    gui.background(screen, "d32")
    
    titleLabel = gui.label(screen, "Inquisitor: The AI Question Answering App", 20, 0, 20, "Times New Roman")
    questionLabel = gui.label(screen, "", 0, 250, 20)
    responseLabel = gui.label(screen, "", 0, 350, 15)
    
    questionBox = gui.textArea(0, 100, 500, 100)
    
    responseButton = gui.button(screen, 100, 200, 100, 50, "Get a Response", command=lambda: generateResponse(f"{fewShotExample}{questionBox.textbox.get(1.0, 10.0)}\n\nA:\n", questionLabel, responseLabel, questionBox, temperature=temperature.get(), frequency_penalty=frequency_penalty.get(), presence_penalty=presence_penalty.get())) #<----- get prompt from textbox
    surpriseMeButton = gui.button(screen, 300, 200, 100, 50, "Surprise Me!", command=lambda: generateQuestion(f"{surpriseMePrompt}", questionBox, temperature=temperature.get(), frequency_penalty=frequency_penalty.get(), presence_penalty=presence_penalty.get()))
    settingsButton = gui.button(screen, 450, 30, 50, 50, image=img, command=settingsDisplay)
    
    gui.fill(questionLabel, "111")
    gui.fill(titleLabel, "342")
    gui.fill(responseButton, "e32")

    responseLabel.configure(wraplength=625)
    questionLabel.configure(wraplength=625)

def settingsDisplay():
    '''
    Displays the settings window for generation
    '''
    global temperature, frequency_penalty, presence_penalty
        

    warningText = "Change the way the AI outputs text. Warning: This may cause the AI to write incorrect answers to your questions. Read the questions carefully"

    settingsWindow = gui.window(mainWindow, "AI Settings", "500x500")

    titleLabel = gui.label(settingsWindow, "AI Settings", 200, 0, 20)
    warningLabel = gui.label(settingsWindow, warningText, 30, 50, 10)

    warningLabel.configure(wraplength=600)

    temperatureLabel = gui.label(settingsWindow, "Temperature", 0, 100, 25)
    frequencyPenaltyLabel = gui.label(settingsWindow, "Frequency Penalty", 0, 200, 25)
    presencePenaltyLabel = gui.label(settingsWindow, "Presence Penalty", 0, 300, 25)

    tempuratureScrollBar = gui.slidebar(settingsWindow, 0, 150, 1, step=10, default_value=0.8, variable=temperature)
    frequencyPenaltyScrollBar = gui.slidebar(settingsWindow, 0, 250, 2, step=20, default_value=0.0, variable=frequency_penalty)
    presencePenaltyScrollBar = gui.slidebar(settingsWindow, 0, 350, 2, step=20, default_value=0.0, variable=presence_penalty)

    temperatureNumber = gui.label(settingsWindow, tempuratureScrollBar.get(), 0, 175, 10)
    frequencyPenaltyNumber = gui.label(settingsWindow, frequencyPenaltyScrollBar.get(), 0, 275, 10)
    presencePenaltyNumber = gui.label(settingsWindow, presencePenaltyScrollBar.get(), 0, 375, 10)


    def changeTemperature(event):
        temperatureNumber.configure(text="{: .1f}".format(temperature.get()))

    def changeFrequencyPenalty(event):
        frequencyPenaltyNumber.configure(text="{: .1f}".format(frequency_penalty.get()))

    def changePresencePenalty(event):
        presencePenaltyNumber.configure(text="{: .1f}".format(presence_penalty.get()))


    tempuratureScrollBar.configure(command=changeTemperature)
    frequencyPenaltyScrollBar.configure(command=changeFrequencyPenalty)
    presencePenaltyScrollBar.configure(command=changePresencePenalty)

def main():
    mainDisplay(mainWindow)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()