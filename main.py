
import speech_recognition as sr
import pyttsx3
import json

import os
import datetime
import webbrowser
import random

from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai
openai.api_key = OPENAI_KEY

engine = pyttsx3.init()

# Change the location of the chrome execution
chrome_exe='C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_exe))

# Convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()
 
def basic_text():
    global myname, responseback
    with open('basicText.json', 'r+') as f:
        data = json.load(f)
        myname = data.get('name', "Sir")
        responseback = data.get('response', "Hi")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        SpeakText("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        SpeakText("Good Afternoon Sir !")   
  
    else:
        SpeakText("Good Evening Sir !")  
  
    assname =("THe name is Tom, Tom Hagen, your consigliere.")
    print("( ⚆ _ ⚆ )")
    SpeakText("I am your Assistant")
    SpeakText(assname)
     
 
def username():
    SpeakText("What should i call you sir")
    uname = record_text()
    SpeakText("Welcome Mister")
    SpeakText(uname)
    SpeakText("How can I help you, Sir?")
     
    SpeakText("How can i Help you, Sir")


# Initialize the recognizer
r = sr.Recognizer()

def record_text():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source, timeout=5)
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}\n")
            print("( ¬ _ ¬ )")
            return query.lower()
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("I could not get you, please speak again")
        return ""
    

def output_text(text):
    # Append to the output file
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return 

def get_rule_content(rule_number):
    with open('48-law.json') as f:
        data = json.load(f)
        for rule in data:
            if rule["rule"] == rule_number:
                return rule["content"]
    return None

messages = []


if __name__ == "__main__":
    
    basic_text()
    SpeakText("Welcome Mr.")
    SpeakText(myname)
    print("#####################")
    print("Welcome Mr.", myname)
    print("#####################")
    wishMe()
    
    while(1):
        text = record_text()

        if not text:
            continue
        
        if 'open admin' in text:
            username()
            
        elif 'intro' in text:
            wishMe()
        elif 'sports news' in text:
                SpeakText("SPORTS center!!!")
                sportsName = record_text()
                SpeakText(f"Preparing the latest news on {sportsName}")
                sports_urls = {
                    'basketball': 'https://www.espn.com/nba/scoreboard',
                    'hockey': 'https://www.espn.com/nhl/scoreboard',
                    'soccer': 'https://www.espn.com/soccer/',
                    'racing': 'https://www.espn.com/f1/',
                    'cfl': 'https://www.tsn.ca/cfl/scores/',
                    'tennis': 'https://www.atptour.com/'
                }
                url = sports_urls.get(sportsName, None)
                if url:
                    webbrowser.get('chrome').open_new_tab(url)
                else:
                    SpeakText(f"No specific source for {sportsName}. Please try another sport.")
        elif 'Local' in text:
            SpeakText('Local News')    
        elif '48 laws' in text:
            SpeakText('48 Laws of Power')
            rule_num = random.randrange(1,49)
            print("getting rule number str{rule_num}")
            SpeakText(get_rule_content(rule_num))
            
        elif 'stock updates' in text:
            SpeakText('Fetching stock updates...')
            webbrowser.get('chrome').open_new_tab('https://www.marketwatch.com/')
            
        elif 'open google' in text:
            SpeakText("Opening Google")
            webbrowser.get('chrome').open_new_tab('https://www.google.com/')
            
        elif 'open audacity' in text:
            SpeakText("Opening Audacity")
            os.system("start audacity")
            
        elif 'open chat' in text:
            SpeakText("Opening Chat")
            os.system("start slack")  
            
        elif 'open code' in text:
            SpeakText("Opening Visual Studio Code")
            os.system("code")
            
        elif 'the weather' in text:
            SpeakText("Fetching weather information")
            webbrowser.get('chrome').open_new_tab('https://www.weather.com/')
            
        elif 'close system' in text:
            SpeakText("Closing system")
            
        else:
            # SpeakText("I am at your service")
            continue
            
        messages.append({"content":text})
        SpeakText(text)