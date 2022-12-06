##################################################################################################################################################
# Name: Inquisitor: The AI Question Answering App                                                                                                #
# Description: This program will take user input for a number greater than 1, and will find all the prime numbers up to or including that number #
# Author: Braden Shrum                                                                                                                           #
# Date: 11/18/2022                                                                                                                               #
##################################################################################################################################################

import gui
import openai

openai.api_key = "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"

screen = gui.CTk()

def generateResponse(prompt, displayLabel, maxTokens=256, temperature=0.8, frequency_penalty=0.0, presence_penalty=0.0):
    '''
    Creates a respsonse using the OpenAI API and displays it to the console

    :prompt: The text to begin with
    :maxTokens: How long the AI generation will be
    :temperature: How random the AI generation will be
    :frequency_penalty: How often the AI repeats itself
    :presence_penalty: How much the AI moves to different topics
    '''
    if prompt != "":
        displayLabel.configure(text="AI is typing...")

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

    displayLabel.configure(text=response)

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

    gui.background(screen, "d32")
    testLabel = gui.label(screen, "This is a label", 200, 200, 10)
    entryBox = gui.textArea(100, 200, 500, 100)
    responseLabel = gui.label(screen, "", 100, 350, 100)
    responseLabel.configure(wraplength=500)
    button1 = gui.button(screen, "Generate", 50, 50, 100, 50, lambda: generateResponse(f"{fewShotExample}{entryBox.textbox.get(1.0, 10.0)}\n\nA:\n", responseLabel)) #<----- get prompt from textbox
    gui.fill(testLabel, "342")
    gui.fill(button1, "e32")

def main():
    mainDisplay(screen)
    screen.mainloop()

if __name__ == "__main__":
    main()