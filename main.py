import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import pygetwindow as gw
import subprocess
import psutil
import pyautogui
import win32con
import win32gui
import pygame
import openai
from config import apikey


chatStr = ""
current_mode = "ODIN"
pygame.mixer.init()
current_program = None
program_stack = []
def open_desktop_app(app_path):
    try:
        os.startfile(app_path)  # Use os.startfile for shortcut files (.lnk)
        return True
    except Exception as e:
        print(f"Error opening desktop app: {str(e)}")
        return False
def close_browser():
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if 'chrome.exe' in process.info['name']:
                psutil.Process(process.info['pid']).terminate()
            elif 'firefox.exe' in process.info['name']:
                psutil.Process(process.info['pid']).terminate()
        return True
    except Exception as e:
        print(f"Error closing browser: {str(e)}")
        return False
def is_open(folder_path):
    try:
        os.listdir(folder_path)
        return True
    except FileNotFoundError:
        return False
def open_folder(folder_path):
    try:
        subprocess.Popen(["explorer", folder_path])
        return True
    except Exception as e:
        print(f"Error opening folder: {str(e)}")
        return False
def close_folder(folder_name):
    try:
        folder_window = gw.getWindowsWithTitle(folder_name)
        if folder_window:
            folder_window[0].close()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error closing folder: {str(e)}")
        return False
def say(text, mode="ODIN"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if mode == "ODIN":
        for voice in voices:
            if "david" in voice.name.lower() and "united states" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    elif mode == "EVA":
        for voice in voices:
            if "zira" in voice.name.lower() and "united states" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    engine.say(text)
    engine.runAndWait()

def minimize_active_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    except Exception as e:
        print(f"Error minimizing window: {str(e)}")

def switch_to_next_window():
    pyautogui.hotkey('alt', 'tab')

def switch_to_previous_window():
    pyautogui.hotkey('alt', 'shift', 'tab')

# def play_pause_media():
#     pygame.mixer.music.pause()

# def play_next_media():
#     pygame.mixer.music.load(random.choice(music_files))
#     pygame.mixer.music.play()
#
# def play_previous_media():
#     pygame.mixer.music.load(random.choice(music_files))
#     pygame.mixer.music.play()
# def resume_media():
#     pygame.mixer.music.unpause()
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query}\n{current_mode}EVA:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response["choices"][0]["text"]
    chatStr += f"{response_text}\n"
    print(response_text)
    say(response_text, mode="EVA")
    return response_text
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response["choices"][0]["text"]
    print(response_text)
    text += response_text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"RR/{''.join(prompt.split('write')[1:]).strip()}.txt", "w") as f:
        f.write(text)
    say(response_text, mode="EVA")
def switch_mode(new_mode):
    global current_mode
    if new_mode == "ODIN" or new_mode == "EVA":
        current_mode = new_mode
    else:
        print("Invalid mode. Use 'ODIN' or 'EVA'.")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred."
if __name__ == '__main__':
    # music_dir = r"C:\Users\Dell\Downloads\MUSIC"
    # music_files = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]
    print("Hello Sir! I am Odin, your personalized system AI. For enhanced assistance activate EVA!")
    say("Hello Sir! I am Odin, your personalized system AI. For enhanced assistance activate EVA!", mode="ODIN")

    while True:
        print("Listening.....")
        query = takeCommand()
        if "activate eva" in query.lower():
            switch_mode("EVA")
            print("EVA mode activated. Welcome Sir!")
            say("EVA mode activated. Welcome Sir!", mode="EVA")
        elif "activate odin" in query.lower():
            switch_mode("ODIN")
            print("ODIN mode activated. Welcome back Sir!")
            say("ODIN mode activated. Welcome back Sir!")
        elif current_mode == "ODIN":
            sites = [["Youtube", "https://www.youtube.com/"],
                     ["tes", "https://www.microsoft.com/en-in/microsoft-teams"],
                     ["Spotify", "https://open.spotify.com/"],
                     ["GPT", "https://chat.openai.com/"],
                     ["Google", "https://www.google.com/"],
                     ["Amazon", "https://www.amazon.in/"],
                     ["Geeks For Geeks", "https://www.geeksforgeeks.org/"],
                     ["Whatsapp", "https://web.whatsapp.com/"],
                     ["Facebook", "https://www.facebook.com/"],
                     ["Netflix", "https://www.netflix.com/in/"],
                     ["Reddit", "https://www.reddit.com/"],
                     ["Instagram", "https://www.instagram.com/"],
                     ["Pininterest", "https://in.pinterest.com/"],
                     ["Bing", "https://www.bing.com/"],
                     ["Yahoo", "https://in.search.yahoo.com/?fr2=inr"],
                     ["Outlook", "https://outlook.live.com/owa/"],
                     ["Zomato", "https://www.zomato.com/mumbai"],
                     ["Swiggy", "https://www.swiggy.com/"],
                     ["Discord", "https://discord.com/"]
                     ]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} Sir....")
                    webbrowser.open(site[1])
                elif f"Close {site[0]}".lower() in query.lower():
                    say(f"Closing {site[0]} Sir....")
                    close_browser()
            folders = [["Downloads", r"C:\Users\Dell\Downloads"],
                       ["Documents", r"C:\Users\Dell\OneDrive\Documents"],
                       ["Pictures", r"C:\Users\Dell\OneDrive\Pictures"],
                       ["Video", r"C:\Users\Dell\Videos"],
                       ]
            for folder in folders:
                if f"Open {folder[0]}".lower() in query.lower():
                    say(f"Opening {folder[0]} Sir....")
                    open_folder(folder[1])
                elif f"Close {folder[0]}".lower() in query.lower():
                    if is_open(folder[1]):
                        say(f"Closing {folder[0]} Sir....")
                        close_folder(folder[0])
                    else:
                        say(f"{folder[0]} is not open. Would you like me to open it?")
                        response = input("Yes or No: ").lower()
                        if response == "yes":
                            open_folder(folder[1])
            apps = [
                ["Valorant", r'C:\Users\Public\Desktop\VALORANT.lnk'],
                ["AI", r"C:\Users\Dell\Downloads\B030-AI-EXP6.pdf"],
                ["Notepad", r'C:\Windows\System32\notepad.exe'],
                ["Need For Speed", r"C:\Users\Public\Desktop\Need for Speed - Payback.lnk"]
            ]
            for app in apps:
                if f"Open {app[0]}".lower() in query.lower():
                    say(f"Opening {app[0]} Sir....")
                    if app[0].lower() == "valorant":
                        os.system(f'start "" "{app[1]}"')
                    elif app[0].lower() == "Need For Speed":
                        os.system(f'start "" "{app[1]}"')
                    elif app[0].lower() == "notepad":
                        os.system(app[1])
                    else:
                        os.system(f'start "" "{app[1]}"')
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H hours %M minutes and %S seconds")
                say(f"Sir the time is {strfTime}")
            if "switch to next" in query.lower():
                switch_to_next_window()
                say("Switched to the next window Sir.")
            if "switch to previous" in query.lower():
                switch_to_previous_window()
                say("Switched to the previous window Sir.")
            if "minimise" in query.lower():
                minimize_active_window()
                say("Minimizing the active window Sir.")
            # if "play music" in query.lower():
            #     pygame.mixer.music.load(random.choice(music_files))
            #     pygame.mixer.music.play()
            # if "pause music" in query.lower():
            #     play_pause_media()
            # if "next song" in query.lower():
            #     play_next_media()
            # if "previous song" in query.lower():
            #     play_previous_media()
            # if "resume music" in query.lower():
            #     resume_media()
        elif current_mode == "EVA":
            if "write" in query.lower():
                chatStr = ""
                ai(prompt=query)
            elif "reset chat" in query.lower():
                chatStr = ""
            else:
                chat(query)
        elif "Exit".lower() in query.lower():
            exit()