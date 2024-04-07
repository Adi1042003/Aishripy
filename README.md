# AISHRIPY - README

## Introduction
AISHRIPY is a voice-controlled assistant created by Aditya Puri. This Python-based assistant is designed to perform various tasks and provide information through voice commands. It integrates several libraries and APIs to offer features like sending WhatsApp messages, searching the web, providing weather updates, translating languages, and more.

## Installation
To run AISHRIPY, you need to install the required Python libraries. You can use pip to install these dependencies:

```bash
pip install pyttsx3 speech_recognition datetime wikipedia webbrowser os smtplib pyautogui Pdata_elements time winotify pillow translate geopy
```

You may also need to create your own ```Pdata_elements.py ``` file with your specific details.

## Usage
- Voice Commands: AISHRIPY can understand and execute commands given through voice. Simply say "AI SHRI" followed by your command.

- Web Search: You can ask AI SHRI to search for information on the web using the "Open search" command.

- Open Websites: Use commands like "Open YouTube," "Open Google," or "Open StackOverflow" to open specific websites in your default web browser.

- Play Music: Ask AISHRIPY to play music, and it will open a predefined URL for music streaming.

- Send WhatsApp Messages: AISHRIPY can send WhatsApp messages to your contacts. It will prompt you to select a contact and then ask for the message content.

- Volume Control: You can control your system's volume by saying "Volume up" or "Volume down."

- Distance Calculation: Ask AISHRIPY to calculate the distance between two places by specifying the place names.

- Email: You can ask AISHRIPY to send an email. Make sure to set up your email details in the Pdata_elements.py file.

- Date and Time: AISHRIPY can tell you today's date and the current time.

- Website: You can open your own website using the "Open my website" command.

- Take Screenshot: Ask AISHRIPY to take a screenshot.

- Shutdown: AISHRIPY can shut down your computer.

- Language Translation: Translate text from one language to another using the "Translate" command.

- Personal Interactions: AISHRIPY can answer questions like "What is your name?" and "What is your age?"

- Greetings: You can greet AISHRIPY, and it will respond with a fun interaction.

- Exit: To exit the program, you can say "Stop this program" or "Stay down."

## Configuration

Before using AISHRIPY, make sure to configure the following:

- Set your icon image location in the iconimg variable.
- Create a ``` Pdata_elements.py ``` file with your email and WhatsApp contact details.
- Customize the assistant's name by changing the Bot_Name variable.
- Support and Issues
- If you encounter any issues or have suggestions for improvements, please feel free to reach out to Me, the creator of AI SHRI.

# Note: This code and AISHRIPY are provided as-is, and the functionality may be affected by changes in external libraries or services.

Happy commanding! 🗣🤖
