# ODIN EVA Chatbot

**ODIN EVA** is a Windows desktop voice assistant built with Python that combines system automation with AI-powered conversation. It features dual personalities: **ODIN** for hands-free system control and **EVA** for intelligent chat powered by OpenAI.

---

## Project Overview

This voice assistant demonstrates practical applications of speech recognition, text-to-speech, process management, and AI integration. Users can control their computer, browse the web, manage windows, and engage in natural language conversations—all through voice commands.

---

## Key Features

### Dual-Mode Operation

**ODIN Mode** (System Controller):
- Open/close websites, folders, and applications via voice
- Window management (minimize, switch between windows)
- Time queries and system information
- Browser process control

**EVA Mode** (AI Assistant):
- Natural language conversation with context awareness
- AI-powered text generation and content creation
- Chat history management
- Response saving to local files

**Switch between modes instantly:**
- "Activate EVA" → AI conversation mode
- "Activate ODIN" → System control mode

### Voice Interaction

- **Speech Recognition**: Continuous microphone listening with Google Speech-to-Text API
- **Text-to-Speech**: Dual voice personalities (David for ODIN, Zira for EVA) using `pyttsx3`
- **Real-time Feedback**: All user inputs and bot responses printed to console

### System Control (ODIN Mode)

- **Websites**: Voice-activated browser control for YouTube, Google, Spotify, ChatGPT, WhatsApp Web, Netflix, Reddit, Instagram, Discord, and more
- **Folders**: Open/close Downloads, Documents, Pictures, Videos
- **Applications**: Launch desktop apps, games, PDFs via shortcuts or executables
- **Window Management**: 
  - Minimize active window
  - Alt+Tab navigation (next/previous window)
- **System Info**: Current time announcements

### AI Features (EVA Mode)

- **Conversational AI**: Maintains chat history for contextual responses using OpenAI's GPT-3.5
- **Content Generation**: Create text on demand with "write" commands
- **File Output**: Automatically saves generated content to `Openai/` folder
- **Chat Reset**: Clear conversation history on command

---

## Tech Stack

**Language**: Python 3.9+

**Core Libraries**:
- `SpeechRecognition` – Google Speech-to-Text integration
- `pyttsx3` – Offline text-to-speech engine
- `openai` – GPT-3.5 text completion API
- `psutil` – Process and system utilities
- `pyautogui` – Keyboard/mouse automation
- `pygetwindow` – Window management
- `pygame` – Audio system initialization
- `pypiwin32` (`win32gui`, `win32con`) – Windows API access

**Standard Library**: `webbrowser`, `os`, `subprocess`, `datetime`, `sys`

---

## Project Structure

```
ODIN-EVA-Chatbot/
├── main.py                # Main application
├── config.example.py      # Configuration template
├── requirements.txt       # Python dependencies
├── .gitignore            # Protects sensitive files
├── README.md             # This file
└── Openai/               # Generated text output (auto-created)
```

---

## Getting Started

### Prerequisites

- **OS**: Windows 10 or later
- **Python**: 3.9 or higher
- **Hardware**: Working microphone
- **API**: OpenAI API key ([get yours here](https://platform.openai.com/api-keys))

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Jinam-Shah/ODIN-EVA-Chatbot.git
cd ODIN-EVA-Chatbot
```

**2. Create virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Configuration

**IMPORTANT**: Create your configuration file before running.

**1. Copy the template**

```bash
copy config.example.py config.py
```

**2. Edit `config.py`** with your settings:

```python
# Your OpenAI API key
OPENAI_API_KEY = "sk-your-actual-key-here"

# Update folder paths to YOUR Windows paths
FOLDERS = {
    "Downloads": r"C:\Users\YourName\Downloads",
    "Documents": r"C:\Users\YourName\Documents",
    "Pictures": r"C:\Users\YourName\Pictures",
    "Videos": r"C:\Users\YourName\Videos"
}

# Update app paths to YOUR .lnk or .exe files
APPS = {
    "Notepad": r"C:\Windows\System32\notepad.exe",
    "YourApp": r"C:\Path\To\YourApp.lnk"
}

# Customize websites (URLs rarely need changes)
WEBSITES = {
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    # Add more...
}
```

**3. Security Note**: Never commit `config.py` to version control. The `.gitignore` file protects your API key automatically.

---

## Usage

### Starting the Assistant

```bash
python main.py
```

You will hear ODIN's greeting and see console output for all interactions.

### Example Commands

**System Control (ODIN Mode)**:
- "Open YouTube"
- "Open Downloads"
- "Open Notepad"
- "What is the time?"
- "Switch to next window"
- "Minimize"
- "Close browser"

**AI Conversation (EVA Mode)**:
- "Activate EVA" (switch to AI mode)
- "What is Python?"
- "Explain quantum computing"
- "Write an email to my professor about the project deadline"
- "Reset chat" (clear conversation history)
- "Activate ODIN" (return to system mode)

**Exit**:
- "Exit" (from any mode)

### Console Output

All interactions are logged to the console:

```
============================================================
ODIN EVA Chatbot - Production v2.0
============================================================

ODIN: Hello Sir! I am Odin, your personalized system AI...

Listening...
Recognizing...
USER: open youtube
ODIN: Opening youtube Sir...

Listening...
USER: activate eva
EVA: EVA mode activated. Welcome Sir!

USER: what is machine learning
EVA thinking...
EVA: Machine learning is a subset of artificial intelligence...
```

---

## Configuration Details

### Folder Paths
Update `FOLDERS` dictionary in `config.py` with your actual Windows paths. Use raw strings (`r"..."`) to handle backslashes.

### Application Shortcuts
Add `.lnk` shortcuts or `.exe` executables to the `APPS` dictionary. Find shortcuts in:
- `C:\Users\Public\Desktop\`
- `C:\Users\YourName\Desktop\`
- `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\`

### Website URLs
Customize the `WEBSITES` dictionary with your frequently visited sites. Use lowercase keys for voice recognition.

---

## Security & Privacy

- **API Key Protection**: `config.py` is gitignored and never committed
- **Local Processing**: Speech recognition uses Google's API; text-to-speech runs offline
- **File Storage**: Generated content saved locally in `Openai/` folder
- **Process Control**: Browser termination affects Chrome/Firefox only

---

## Troubleshooting

**"config.py not found"**:
- Copy `config.example.py` to `config.py` and fill your values

**Speech recognition errors**:
- Check microphone permissions in Windows settings
- Ensure stable internet connection (Google Speech API)
- Speak clearly near the microphone

**Voice not changing between modes**:
- Verify "David" and "Zira" voices are installed in Windows
- Run: Settings → Time & Language → Speech → Manage voices

**OpenAI API errors**:
- Verify API key is valid and has credits
- Check `OPENAI_API_KEY` in `config.py`

---

## Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---


## Disclaimer

This software controls system-level operations (opening/closing applications, managing processes). Use responsibly and review the code before granting execution permissions. The author is not responsible for unintended system changes.

---

## Author

**Jinam Shah**  
- GitHub: [@Jinam-Shah](https://github.com/Jinam-Shah)
