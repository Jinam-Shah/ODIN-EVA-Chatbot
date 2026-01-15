#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ODIN EVA Chatbot - Production Voice Assistant
Dual-mode: ODIN (system control) + EVA (OpenAI chat)
"""

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
import sys

# === CONFIGURATION IMPORT ===
try:
    from config import OPENAI_API_KEY, FOLDERS, APPS, WEBSITES
except ImportError:
    print("\nERROR: config.py not found!")
    print("SETUP INSTRUCTIONS:")
    print("  1. Copy config.example.py to config.py")
    print("  2. Edit config.py with YOUR OpenAI key and paths")
    print("  3. Run: python main.py\n")
    sys.exit(1)

# === GLOBAL STATE ===
chatStr = ""
current_mode = "ODIN"
pygame.mixer.init()


# === HELPER FUNCTIONS ===
def open_desktop_app(app_path):
    """Open desktop app or shortcut"""
    try:
        os.startfile(app_path)
        return True
    except Exception as e:
        print(f"Error opening app: {e}")
        return False


def close_browser():
    """Close Chrome/Firefox processes"""
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if 'chrome.exe' in process.info['name']:
                psutil.Process(process.info['pid']).terminate()
            elif 'firefox.exe' in process.info['name']:
                psutil.Process(process.info['pid']).terminate()
        return True
    except Exception as e:
        print(f"Error closing browser: {e}")
        return False


def is_open(folder_path):
    """Check if folder exists"""
    try:
        os.listdir(folder_path)
        return True
    except FileNotFoundError:
        return False


def open_folder(folder_path):
    """Open folder in Explorer"""
    try:
        subprocess.Popen(["explorer", folder_path])
        return True
    except Exception as e:
        print(f"Error opening folder: {e}")
        return False


def close_folder(folder_name):
    """Close folder window by title"""
    try:
        folder_window = gw.getWindowsWithTitle(folder_name)
        if folder_window:
            folder_window[0].close()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error closing folder: {e}")
        return False


def say(text, mode="ODIN"):
    """Text-to-speech with voice selection and console output"""
    print(f"{mode}: {text}")

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
    """Minimize foreground window"""
    try:
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    except Exception as e:
        print(f"Error minimizing window: {e}")


def switch_to_next_window():
    """Alt+Tab to next window"""
    pyautogui.hotkey('alt', 'tab')


def switch_to_previous_window():
    """Alt+Shift+Tab to previous window"""
    pyautogui.hotkey('alt', 'shift', 'tab')


def chat(query):
    """OpenAI chat in EVA mode"""
    global chatStr
    openai.api_key = OPENAI_API_KEY
    chatStr += f"User: {query}\nEVA:"

    print("EVA thinking...")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response["choices"][0]["text"].strip()
    chatStr += f"{response_text}\n"

    say(response_text, mode="EVA")
    return response_text


def ai(prompt):
    """OpenAI text generation and save to file"""
    openai.api_key = OPENAI_API_KEY
    text = f"OpenAI response for Prompt: {prompt}\n{'=' * 50}\n\n"

    print("EVA generating text...")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response["choices"][0]["text"].strip()
    text += response_text

    # Create output directory
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Save file
    filename = ''.join(prompt.split('write')[1:]).strip()[:50]
    filepath = f"Openai/{filename}.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved to: {filepath}")
    say(response_text, mode="EVA")


def switch_mode(new_mode):
    """Switch between ODIN/EVA"""
    global current_mode
    if new_mode == "ODIN" or new_mode == "EVA":
        current_mode = new_mode
    else:
        print("Invalid mode. Use 'ODIN' or 'EVA'.")


def takeCommand():
    """Speech to text with console output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"USER: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Timeout - no speech detected")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""


# === MAIN PROGRAM ===
if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("ODIN EVA Chatbot - Production v2.0")
    print("=" * 60 + "\n")

    # Startup message
    startup_msg = "Hello Sir! I am Odin, your personalized system AI. For enhanced assistance activate EVA!"
    say(startup_msg, mode="ODIN")

    while True:
        query = takeCommand()

        if not query:
            continue

        # === MODE SWITCHING ===
        if "activate eva" in query.lower():
            switch_mode("EVA")
            say("EVA mode activated. Welcome Sir!", mode="EVA")

        elif "activate odin" in query.lower():
            switch_mode("ODIN")
            say("ODIN mode activated. Welcome back Sir!")

        elif "exit" in query.lower():
            say("Goodbye Sir!")
            break

        # === ODIN MODE: System Control ===
        elif current_mode == "ODIN":

            # --- Websites (from config) ---
            handled = False
            for site_name, site_url in WEBSITES.items():
                if f"open {site_name}" in query.lower():
                    say(f"Opening {site_name} Sir...")
                    webbrowser.open(site_url)
                    handled = True
                    break
                elif f"close {site_name}" in query.lower():
                    say(f"Closing browser Sir...")
                    close_browser()
                    handled = True
                    break

            if handled:
                continue

            # --- Folders (from config) ---
            for folder_name, folder_path in FOLDERS.items():
                if f"open {folder_name.lower()}" in query.lower():
                    say(f"Opening {folder_name} Sir...")
                    open_folder(folder_path)
                    handled = True
                    break
                elif f"close {folder_name.lower()}" in query.lower():
                    if is_open(folder_path):
                        say(f"Closing {folder_name} Sir...")
                        close_folder(folder_name)
                    else:
                        say(f"{folder_name} is not open. Would you like me to open it?")
                        response = input("Yes or No: ").lower()
                        if response == "yes":
                            open_folder(folder_path)
                    handled = True
                    break

            if handled:
                continue

            # --- Apps (from config) ---
            for app_name, app_path in APPS.items():
                if f"open {app_name.lower()}" in query.lower():
                    say(f"Opening {app_name} Sir...")
                    open_desktop_app(app_path)
                    handled = True
                    break

            if handled:
                continue

            # --- System Commands ---
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H hours %M minutes and %S seconds")
                say(f"Sir the time is {strfTime}")

            elif "switch to next" in query.lower():
                switch_to_next_window()
                say("Switched to the next window Sir.")

            elif "switch to previous" in query.lower():
                switch_to_previous_window()
                say("Switched to the previous window Sir.")

            elif "minimise" in query.lower() or "minimize" in query.lower():
                minimize_active_window()
                say("Minimizing the active window Sir.")

        # === EVA MODE: AI Chat ===
        elif current_mode == "EVA":
            if "write" in query.lower():
                chatStr = ""
                ai(prompt=query)
            elif "reset chat" in query.lower():
                chatStr = ""
                say("Chat history reset.", mode="EVA")
            else:
                chat(query)
