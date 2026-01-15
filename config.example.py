#!/usr/bin/env python3
"""
ODIN EVA Chatbot - SETUP GUIDE
1. Copy this → config.py
2. Fill API key + YOUR paths
3. Run main.py
"""

# OpenAI API (platform.openai.com)
OPENAI_API_KEY = "sk-paste-your-key-here"

# Folders (update YOUR paths)
FOLDERS = {
    "Downloads": r"C:\Users\YourName\Downloads",
    "Documents": r"C:\Users\YourName\Documents", 
    "Pictures": r"C:\Users\YourName\Pictures",
    "Videos": r"C:\Users\YourName\Videos"
}

# Apps (update YOUR .lnk/.exe paths)
APPS = {
    "Notepad": r"C:\Windows\System32\notepad.exe",
    "Valorant": r"C:\Users\Public\Desktop\VALORANT.lnk",
    # Add more...
}

# Websites (URLs - rarely change)
WEBSITES = {
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    "spotify": "https://open.spotify.com/",
    # Add from your list...
}
