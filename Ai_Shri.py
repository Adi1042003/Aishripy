# code by Aditya puri
import random                               # use pip install random or Random
import pyttsx3                              # use pip install pyttsx3
import speech_recognition as sr             # use pip install SpeechRecognition
import datetime                             # use pip install datetime
import wikipedia                            # use pip install wikipedia
import webbrowser                           # use pip install webbrowser
import os                                   # use pip install os
import smtplib                              # use pip install smtplib
import pyautogui as auto                    # use pip install pyautogui
import Pdata_elements as PD                 # creat ur own file with ur own details
import time                                 # use pip install time
from winotify import Notification, audio    # use pip install winotify and pip install pillow
from translate import Translator            # use pip install Translate
from geopy.geocoders import Nominatim       # use pip install gocoder
from geopy import distance                  # use pip install geopy

iconimg = "C:\\Users\\adity\\OneDrive\\Pictures\\aishrilogo.jpg"
# enter ur icon img location from your pc and add extra \ as one \ python will consider it as escape character

Bot_Name = "SHRI"

def notify(messagetoD, mtitle='AI SHRI IS LIVE'):
    shri = Notification(app_id='AI Assistant', title=mtitle, msg=messagetoD,
                        duration='short', icon=iconimg)
    shri.set_audio(audio.Mail, loop=False)
    shri.add_actions(label='click me!',
                     launch='https://adi1042003.github.io/mywebpage/sap.html')
    shri.show()

messagetoD = f'{Bot_Name} is now able to help you'
notify(messagetoD)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# def takeCommand():
#     r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def volumeup():
    for i in range(0, 5):
        auto.press('volumeup')

def volumedown():
    for i in range(0, 5):
        auto.press('volumedown')


def erroroc():
    speak("I am sorry, I did not get that. Please try again")


def sendWhatmsg():
    try:
        speak("ok ")
        speak('I will provide the names from my contact list u can choose one from them')
        print(PD.user_list.keys())
        time.sleep(4)
        speak('now whom should i send message')
        name = takeCommand().upper()
        time.sleep(2)
        print(name)
        if name in PD.user_list:
            speak('what should i message')
            time.sleep(1)
            takecmd = takeCommand()
            if takecmd == 'None':
                speak('I didn\'t recived any input from u please say it again')
                sendWhatmsg()
            else:
                msgToSend = takecmd.replace(' ', '%20')
                print(msgToSend)
                webbrowser.open('https://web.whatsapp.com/send?phone=' +
                                PD.user_list.get(name)+'&text='+msgToSend)
                speak('wait for 10 seconds while whatsapp is loading')
                time.sleep(10)
                auto.hotkey('f11')
                auto.hotkey('enter')
                time.sleep(1)
                speak('message sent sucessfully')
        else:
            speak('there is no person named' +
                  name + 'in contact list')
            speak('I will terminate this command')
            speak('u can try once again')
    except:
        erroroc()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(f"I am {Bot_Name} . Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(PD.send_from, PD.Apass_key)
    server.sendmail(PD.send_to, to, content)
    server.close()


def todaydate():
    today = datetime.datetime.today()
    print(f"Today\'s date is {today:%B %d, %Y}")
    speak(f"Today\'s date is {today:%B %d, %Y}")


def distancecalc(location1, location2):
    geocoders = Nominatim(user_agent='aishri')
    try:
        coordinates1 = geocoders.geocode(location1)
        coordinates2 = geocoders.geocode(location2)
        lat1, longi1 = (coordinates1.latitude), (coordinates1.longitude)
        lat2, longi2 = (coordinates2.latitude), (coordinates2.longitude)
        place1 = (lat1, longi1)
        place2 = (lat2, longi2)
        print(
            f'The distance between {location1} and {location2 } is {(distance.distance(place1,place2))}')
        speak(
            f' the distance between {location1} and {location2 } is {distance.distance(place1,place2)}')
    except:
        print('error: The place does not exist')


def translation(msg, language='spanish'):
    translator = Translator(to_lang=language)
    translation = translator.translate(msg)
    return translation


def schedule():
    # get the current date
    now = datetime.datetime.now()

    # check if today is April 10th
    if now.month == 4 and now.day == 10:
        speak(" it\'s 10 april today ,So i wish you a happiest birthday Aditya ! Wishing you all the best on your special day!")
        print("happiest birthday Aditya ! Wishing you all the best on your special day!💜")


# main output
if __name__ == "__main__":
    wishMe()
    schedule()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open search' in query:
            speak('Searching Wikipedia...')
            content = takeCommand()
            if 'who built you' in content:
                speak(f"I am {Bot_Name} . And i was built by aditya puri")
                print(f"I am {Bot_Name} . And i was built by aditya puri")
            elif 'who is Aditya Puri' in content:
                adidetails = 'Aditya Puri (born 10 April 2003) is an E and C enengineering student who is currently studying at the GOGTE INSTITUTE OF TECHNOLOGY, BELGAUM'
                print(adidetails)
                speak(adidetails)
            else:
                try:
                    results = wikipedia.summary(content, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak("  Your are offline")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            webbrowser.open(
                "https://open.spotify.com/track/2e8zEzmedii6VKaV2852rl?")
            time.sleep(6)
            auto.hotkey('space')

        elif 'volume up' in query:
            try:
                volumeup()
            except:
                erroroc()

        elif 'distance calculation' in query:
            try:
                speak(' what\'s the first place name?')
                frplce = takeCommand().lower()
                speak(' what\'s the second place name?')
                sdplce = takeCommand().lower()
                distancecalc(frplce, sdplce)
            except:
                erroroc()

        elif 'send a message'  in query:
            try:
                sendWhatmsg()
            except:
                erroroc()

        elif 'volume down' in query:
            try:
                volumedown()
            except:
                erroroc()

        elif 'stop music' in query:
            try:
                os.system('TASKKILL /F /IM msedge.exe')
            except:
                erroroc()

        elif 'what is today\'s date' in query:
            todaydate()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f", the time is {strTime}")

        elif 'open my website' in query:
            webbrowser.open('https://adi1042003.github.io/mywebpage/sap.html')

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = PD.send_to
                sendEmail(to, content)
                messagetoD = 'email sent sucessfully'
                speak(messagetoD)
                notify(messagetoD)
                print(messagetoD)
            except Exception as e:
                print(e)
                messagetoD = 'Sorry my friend Aditya . I am not able to send this email'
                speak(messagetoD)
                notify(messagetoD)

        elif 'what is my name' in query:
            try:
                speak("your name is aditya")
            except:
                speak("sorry an error ocurred")
            finally:
                speak("is there any thing else i can help you with")

        elif 'take screenshot' in query:
            try:
                speak("ok  as u say")
                auto.press('printscreen')
            except:
                erroroc()

        elif 'what is your name' in query:
            try:
                speak(f"my name is {Bot_Name}")
            except:
                erroroc()
            finally:
                speak("is there any thing else i can help you with")

        elif 'stay down' in query:
            try:
                messagetoD = 'bye ,  u can call me back when u are in need'

                speak(messagetoD)
                notify(messagetoD, mtitle=f'AI {Bot_Name} IS DOWN')
                time.sleep(1)
                os.system('TASKKILL /F /IM pycharm64.exe')
                os.system('TASKKILL /F /IM Code.exe')
            except:
                erroroc()
            finally:
                speak("bye ")
                speak(" u can call me back when u are in need")

        elif 'stop this program' in query:
            try:
                speak("ok  as u say")
                time.sleep(1)
                auto.hotkey('shift', 'f5')
                time.sleep(1)
                auto.hotkey('ctrl', 'f2')
            except:
                erroroc()
            finally:
                speak("bye ")

        elif 'close microsoft edge' in query:
            try:
                speak("ok  as u say")
                time.sleep(1)
                os.system('TASKKILL /F /IM msedge.exe')
            except:
                erroroc()

        elif 'close chrome' in query:
            try:
                speak("ok  as u say")
                time.sleep(1)
                os.system('TASKKILL /F /IM chrome.exe')
            except:
                erroroc()

        elif 'shutdown' in query:
            try:
                speak("ok  as u say")
                os.system('TASKKILL /F /IM msedge.exe')
                os.system('TASKKILL /F /IM chrome.exe')
                time.sleep(2)
                os.system('shutdown /p /f')
            except:
                erroroc()
            finally:
                speak("byeeee")

        elif 'hello' in query:
            try:
                speak("well it is a complex question")
                speak('So to make it more simple let\'s make a toss')
                speak('if it\'s an head then i am yours and if it\'s tail you are mine')
                speak('so choose your option head or tail')
                option = takeCommand().lower()
                head = 1
                results = random.randint(1, 2)
                print('your choice is ' + option)
                if results == head:
                    speak('it\'s an head so i am yours')
                    speak('ma ka tugila var mogaa assa')
                else:
                    speak('it\'s a tail so now you are mine')
                    speak('ma ka tugila var mogaa assa')
            except:
                erroroc()
            finally:
                speak('let\'s meet soon')

        elif 'what is your age' in query:
            try:
                speak(
                    "Age is simply the number of years the world has been enjoying you!")
            except:
                erroroc()
            finally:
                speak("Any how i don/'t get older!")

        elif 'hi shri' in query:
            try:
                speak("hello  , how can i help you")
            except:
                erroroc()

        elif 'translate' in query:
            try:
                speak(
                    ' in which language you want to translate in default is set to spanish\n')
                language = takeCommand()
                if language == 'None':
                    language = 'spanish'
                speak(f' what should i translate into {language}\n')
                msg = takeCommand()
                speak(translation(msg, language))
                print(translation(msg, language))
                speak(f'I have translated and displayed it in {language}\n')
            except:
                erroroc()
        else:
            print("No query matched")
            # speak("No query matched, Please search from the defined query")
