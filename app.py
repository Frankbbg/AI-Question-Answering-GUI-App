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

def generateResponse(screen, prompt, questionBox, maxTokens=256, temperature=0.8, frequency_penalty=0.0, presence_penalty=0.0):
    '''
    Creates a respsonse using the OpenAI API and displays it to the console

    :prompt: The text to begin with
    :maxTokens: How long the AI generation will be
    :temperature: How random the AI generation will be
    :frequency_penalty: How often the AI repeats itself
    :presence_penalty: How much the AI moves to different topics
    '''
    questionLabel = gui.label(screen, "", 12, 3, 20)
    responseLabel = gui.label(screen, "", 12, 4, 15)
    responseLabel.configure(wraplength=500)
    gui.fill(questionLabel, "111")

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
    settingsIconPath = "C:\\Users\\frank\\OneDrive\\Documents\\School Documents\\Fall 2022\\Second 8 Weeks\\Intro to Sofware Development\\Final Project\\Inquisitor\\AI-Question-Answering-GUI-App\\images\\Settings_Icon.png"
    img = ImageTk.PhotoImage(Image.open(settingsIconPath))

    gui.background(screen, "d32")
    titleLabel = gui.label(screen, "Inquisitor: The AI Question Answering App", 12, 1, 20, "Times New Roman")
    questionBox = gui.textArea(12, 2, 500, 100)
    responseButton = gui.button(screen, 12, 5, 100, 50, "Get a Response", command=lambda: generateResponse(screen, f"{fewShotExample}{questionBox.textbox.get(1.0, 10.0)}\n\nA:\n", questionBox)) #<----- get prompt from textbox
    settingsButton = gui.button(screen, 12, 6, 50, 50, image=img, command=settingsDisplay)
    gui.fill(titleLabel, "342")
    gui.fill(responseButton, "e32")

def settingsDisplay():
    '''
    Displays the settings window for generation
    '''
    warningText = "Change the way the AI outputs text. Warning: This may cause the AI to write incorrect answers to your questions. Read the questions carefully"

    settingsWindow = gui.window(mainWindow, "AI Settings", "500x500")

    titleLabel = gui.label(settingsWindow, "AI Settings", 12, 1, 20)
    warningLabel = gui.label(settingsWindow, warningText, 12, 2, 10)

    warningLabel.configure(wraplength=400)


def main():
    mainDisplay(mainWindow)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()