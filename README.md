# ODIN EVA Chatbot

ODIN EVA is a desktop voice assistant built in Python that runs on Windows.  
It listens to your voice, executes system commands (open apps, manage windows, browse the web), and can switch into an AI assistant mode powered by OpenAI for chat and text generation.

---

## Project Overview

This project explores practical voice interfaces and desktop automation using Python.  
It combines speech recognition, text‑to‑speech, process control, and web automation to create a hands‑free assistant with two personalities: **ODIN** (system controller) and **EVA** (AI copilot).

---

## Key Features

### Dual modes: ODIN and EVA

- **ODIN mode**: Focused on system control (open/close apps, folders, websites, window management, time queries).  
- **EVA mode**: AI conversation and text generation using OpenAI completions, with a separate female voice.  

Switching modes is done via voice commands like:

- “Activate EVA”  
- “Activate ODIN”

---

### Voice input and output

- Listens to the microphone using `SpeechRecognition` and Google’s speech‑to‑text API.  
- Provides spoken responses using `pyttsx3`, with different voices configured for ODIN and EVA.  
- Basic error handling when speech is not recognized.

---

### System and browser control (ODIN mode)

- Opens frequently used websites (YouTube, Google, Spotify, ChatGPT, WhatsApp Web, Netflix, Reddit, Instagram, etc.) in the default browser via voice commands like  
  - “Open YouTube”  
  - “Open Google”  

- Closes browsers (Chrome/Firefox) by terminating their processes with `psutil`.  
- Opens common user folders (Downloads, Documents, Pictures, Videos) in Explorer and can close them by window title.  
- Launches desktop apps or files (e.g., Valorant, Notepad, PDF documents, games) using their paths or shortcuts.  
- Tells the current time in a spoken format on request (“What is the time?”).  
- Performs simple window management:
  - Minimize active window.  
  - Switch to next or previous window using Alt+Tab simulation with `pyautogui`.

---

### EVA mode: AI chat and content generation

- Maintains a running chat history string so EVA can respond contextually within a session.  
- Uses OpenAI’s text completion API (e.g., `text-davinci-003`) for:
  - General chat.  
  - Text/content generation when the command contains the word “write”.  
- Speaks the generated response and optionally saves generated text to disk with a timestamped file name.

> Note: The project expects an `apikey` defined in a separate `config.py` file which is not committed to version control for security reasons.

---

## Tech Stack

- **Language**: Python  
- **Libraries**:
  - `SpeechRecognition` – speech‑to‑text from microphone input  
  - `pyttsx3` – offline text‑to‑speech voices  
  - `pygame` – audio system initialization  
  - `openai` – AI chat/text completions  
  - `psutil`, `os`, `subprocess` – process and system operations  
  - `pyautogui`, `pygetwindow`, `win32gui`, `win32con` – window and input control  
  - Standard library modules: `random`, `webbrowser`, `datetime`

---

## Getting Started

### Prerequisites

- Windows 10 or later  
- Python 3.9+ installed  
- A working microphone  
- An OpenAI API key

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Jinam-Shah/ODIN-EVA-Chatbot.git
cd ODIN-EVA-Chatbot

python -m venv venv
```

### Configuration
Create a file named config.py in the project root with:
`apikey = "YOUR_OPENAI_API_KEY"`

You may also need to update hard‑coded paths (for games, PDFs, folders) inside main.py to match your machine.

## Usage
Activate your virtual environment (if not already active), then:

```bash
python main.py
# You should hear an introduction from ODIN.
Try commands such as:
“Activate EVA”
“Open YouTube”
“Open Downloads”
“Switch to next”
“What is the time?”
“Write an email to my manager about our project status”
```
The assistant will listen continuously in a loop until you close the program.

## Disclaimer
This project is intended for personal and educational use.
Be careful when granting system‑level access to scripts that can open, close, and control applications on your machine.
