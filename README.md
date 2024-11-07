## Jarvis AI Assistant

This project is a voice-activated virtual assistant inspired by Iron Man’s Jarvis. It allows users to perform a variety of tasks, including web browsing, task management, and other commands, using voice input. Jarvis can open specific websites, manage tasks through a Flask API server, and provide responses via text-to-speech (TTS).

## Table of Contents

1. [Features](#features)
2. [Setup and Installation](#setup-and-installation)
3. [Project Structure](#project-structure)
4. [Usage](#usage)
5. [API Reference](#api-reference)
6. [Troubleshooting](#troubleshooting)

---

## Features

- **Voice Command Recognition**: Activate Jarvis with the keyword “Jarvis” to perform tasks.
- **Web Browsing Commands**: Open Google, YouTube, LinkedIn, Facebook, and other websites via voice.
- **Task Management**: Add, view, and delete tasks with voice commands using a Flask API backend.
- **Text-to-Speech Responses**: Jarvis responds to commands with voice feedback.

---

## Setup and Installation

### Prerequisites

- **Python 3.7+**
- **Flask** (for task management API)
- **SpeechRecognition**: Library for recognizing speech input.
- **Pyttsx3**: Text-to-Speech library.
- **Requests**: For making API requests.
- **Microphone** (for voice input)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:

   ```bash
   python app.py
   ```

4. Start the Jarvis Assistant:

   ```bash
   python main.py
   ```

---

## Project Structure

```plaintext
jarvis-ai-assistant/
├── app.py                 # Flask API server for task management
├── main.py                # Main Jarvis AI script with voice recognition and TTS
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation
```

---

## Usage

### Running the Assistant

1. **Start the Flask API Server**: `app.py` hosts endpoints to manage tasks.
   ```bash
   python app.py
   ```

2. **Run Jarvis AI**: `main.py` activates Jarvis, awaiting the keyword “Jarvis” to begin processing commands.
   ```bash
   python main.py
   ```

3. **Voice Commands**: Speak commands like “Jarvis, open Google” or “Jarvis, add task read emails.”

### Available Commands

- **Open Websites**: "open google", "open youtube", "open linkedin", etc.
- **Manage Tasks**:
  - **Add Task**: "add task [task details]"
  - **Get Tasks**: "get task"
  - **Remove Task**: "remove task [task details]"

---

## API Reference

The Flask API handles task management (adding, viewing, and deleting tasks) and is used by `main.py` to manage tasks.

### Endpoints

1. **Add Task**: `POST /add-task`
   - **Data**: `{ "task": "task details" }`
   - **Response**: `{ "message": "Task added successfully!" }`

2. **Get Tasks**: `GET /get-tasks`
   - **Response**: `{ "tasks": ["task1", "task2", ...] }`

3. **Delete Task**: `POST /delete-task`
   - **Data**: `{ "task": "task details" }`
   - **Response**: `{ "message": "Task deleted successfully!" }`

---

## Troubleshooting

- **404 Error on Delete Task**: If you encounter a `404` error on deleting tasks, ensure the exact task name is being passed. Verify the API URL (`http://127.0.0.1:5000/delete-task`) is correct and check the console for errors.
- **Flask Server Not Responding**: Ensure `app.py` is running, and check if Flask debug mode is properly reloading routes after code changes.
- **Speech Recognition Timeout**: Increase `timeout` or `phrase_time_limit` in `main.py` if Jarvis times out too quickly while listening.

---

## Contributing

Feel free to submit issues or pull requests for improvements! Contributions and suggestions are welcome.

## License

This project is licensed under the MIT License.
