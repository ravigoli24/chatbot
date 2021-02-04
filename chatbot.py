import pyttsx3
import webbrowser
import os
import datetime

print("")
print("      *******WELCOME*******      ")
print("")  
print("Hey Ravindra this is chatbot")
print("")

pyttsx3.speak("Hello , how can i help you ")
print("Hello , how may i help you ?")
pyttsx3.speak("please give your requirements :")
print("please give your requirements :")
p=input()

while "exit" not in p:
    if (("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p)) and ("chrome" in p):
             webbrowser.open('https://www.google.com')
             pyttsx3.speak("google chrome is launched tell me how can i help you")
             print("google chrome is launched")
             print("please tell me your next requirement :")
             p=input()
    elif ("current" in p) or ("date" in p) or ("time" in p):
             noww=datetime.datetime.now()
             print(noww)
             pyttsx3.speak("current date and time is launched tell me how can i help you")
             print("current date and time is launched")
             print("please tell me your next requirement :")
             p=input()
    elif (("run" in p) or ("open" in p) or ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ):
             os.system("notepad")
             pyttsx3.speak("notepad is launched tell me tell me how can i help you")
             print("Notepad is launched")
             print("please tell me your other requirement :")
             p=input()
    elif (("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p)) and (("gmail" in p) or ("mail" in p) or ("mailbox" in p)) :
             webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox')
             pyttsx3.speak("gmail is launched tell me tell me how can i help you")
             print("Gmail is launched")
             print("please tell me your next requirement :")
             p=input()
    elif (("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p)) and ("facebook" in p) :
             webbrowser.open("https://www.facebook.com/")
             pyttsx3.speak("facebook is launched tell me how can i help you")
             print("Facebook is launched")
             print("please tell me your next requirement :")
             p=input()
    elif (("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p)) and ("linkedin" in p) :
             webbrowser.open("https://www.linkedin.com/")
             pyttsx3.speak("linkedin is launched tell me how can i help you")
             print("linkedin is launched")
             print("please tell me your next requirement :")
             p=input()
    elif (("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p)) and (("windows media player" in p) or ("media player" in p)) :
             webbrowser.open("wmplayer")
             pyttsx3.speak("vlc media player is launched tell me how can i help you")
             print("VLC media player is launched")
             print("please tell me your next requirement :")
             p=input()
    elif ("youtube" in p)  :
             webbrowser.open("https://www.youtube.com/")
             pyttsx3.speak("youtube is launched tell me how can i help you")
             print("youtube is launched")
             print("please tell me your next requirement :")
             p=input()
    elif ("exit" in p) or ("stop" in p) or ("dont" in p):
             pyttsx3.speak("Thank You Have a great day")
             print("      *****THANK YOU*****       ")
             break
    else :
             pyttsx3.speak("sorry , did not match any requirements  tell me your next valid requirement")
             print("Sorry , i ddidn't get it\n"
                   ""
                   "       Suggestions:\n"
                   "Make sure that all words are spelled correctly.\n"
                   "Try different keywords.\n"
                   ""
                    "please tell me your next requirement :\n")
             p=input()


