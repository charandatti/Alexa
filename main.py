import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    song = command.replace('play','')
    if 'play' in command:
        talk('playing  ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is' , '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,i have an headache')
    elif 'are you single'  in command:
        talk('i am in relationship with this code developer')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
         talk('please say the command again')





while True:
    run_alexa()


