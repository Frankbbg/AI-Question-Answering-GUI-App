# AI-Question-Answering-GUI-App
 Allows the user to ask any question via the question box, and an AI will answer the question to the best of its ability. Fair Notice: The AI may not always output things that are true. Fact check or take every output with a grain of salt.

# Features
## Buttons
- **Ask**: Asks the question in the question box
- **Surprise Me**: Places a random question in the question box
- **Settings**: Opens the settings window

## Settings
- **Tempurature**: The higher the tempurature, the more random the output will be. The lower the tempurature, the more likely the output will be to make sense. The default tempurature is 0.7
- **Frequency Penalty**: The higher the frequency penalty, the more likely the output will be less repetitive. The lower the frequency penalty, the more likely the output will be more repetitive. The default frequency penalty is 0.0
- **Presence Penalty**: The higher the presence penalty, the more likely the output will move away from the original question. The lower the presence penalty, the more likely the output will be more similar to the original question. The default presence penalty is 0.6

## Validation Checks
The AI will not answer the question if:
- The question is empty
- The question contains random characters
- The question is vague
- The question contains words that don't make sense 
- The question contains words that are not in the dictionary

# How to Use
## Requirements
- Python 3.10 or higher
- Internet Connection
- OpenAI API Key (provided)
- customtkinter (pip install)

### Installing customtkinter
1. Open the terminal
2. Run the command `pip install customtkinter`

## Running the Program
1. Download the repository
2. Open the repository
3. Open the terminal
4. Run the command `python app.py`

# Other Information
## How to Get an OpenAI API Key
1. Go to https://beta.openai.com/
4. Click on the "Sign Up" button
5. Click on the "API Keys" button
6. Click on the "Create API Key" button
7. Copy the API Key

## How to Change the OpenAI API Key
1. Open the repository
2. Open the file `app.py`
3. Go to line 16
4. Replace the API Key with your own