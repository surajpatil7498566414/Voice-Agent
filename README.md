# 🎙️ TezAgent - Offline Voice Assistant

**TezAgent** is a Python-based **offline voice assistant** designed for hackathons and AI innovation projects.  
It uses **VOSK** for speech recognition and **pyttsx3** for text-to-speech — enabling smooth, hands-free interaction **without internet connectivity**.

---

## 🧠 Overview

TezAgent is a lightweight, rule-based **offline AI voice assistant** that can understand voice commands and respond in real-time.  
It can greet users, tell the time or date, share fun facts or jokes, and provide motivational quotes — all locally processed.  

The system is written entirely in Python, ensuring easy customization and deployment even in low-resource environments.

---

## 💡 Problem Statement

Voice assistants today depend heavily on the internet. In many scenarios — such as rural areas, embedded systems, or privacy-focused devices —  
internet access isn’t guaranteed.  

The challenge: **Create a voice assistant that works completely offline while maintaining real-time interaction and simplicity.**

---

## 🧩 Solution

**TezAgent** solves this by combining:
- ✅ **VOSK** for offline speech recognition  
- ✅ **pyttsx3** for offline text-to-speech  
- ✅ A rule-based NLP engine for flexible responses  
- ✅ A modular and extendable Python framework  
- ✅ Zero dependency on external APIs  

This makes TezAgent fast, private, and hackathon-friendly.

---

## ✨ Features

- 🎤 **Offline Speech Recognition**
- 🗣️ **Offline Text-to-Speech**
- 💬 **Predefined Knowledge Base** for common queries  
- 🕐 **Dynamic Time & Date** responses  
- 🤖 **Lightweight & Expandable** — Add your own commands easily  
- 🧠 **Fully Offline Processing**
- 💻 Works on **Windows, macOS, and Linux**

---

## 🧱 Architecture
              🎙️
    +-------------------+
    |    User Speech    |
    +---------+---------+
              |
              v
    +-------------------+
    |  VOSK Recognizer  |
    | (Offline ASR)     |
    +---------+---------+
              |
              v
    +-------------------+
    |  Command Parser   |
    |  (Text Processor) |
    +---------+---------+
              |
              v
    +-------------------+
    |  Rule-Based Logic |
    |  (Knowledge Base) |
    +---------+---------+
              |
              v
    +-------------------+
    | pyttsx3 (TTS)     |
    | Offline Speech Out|
    +---------+---------+
              |
              v
         🔊 Audio Output

         
---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|----------------|
| Language | Python 3 |
| Speech Recognition | VOSK |
| Text-to-Speech | pyttsx3 |
| Audio Input | sounddevice |
| Threading / Logic | Python (threading, queue, json, time) |

---

## 🧪 Example Interaction

=== Simple Offline Voice Agent ===
Listening... Speak into your microphone. Press Ctrl+C to stop.

You: hello
<< Agent: Hello! I am your voice agent. How can I help you today?

You: what is your name
<< Agent: I am called TezAgent, your hackathon voice agent.

You: tell me a joke
<< Agent: Why did the computer get cold? Because it left its Windows open!

## 📊 Future Enhancements

- 🌍 Multilingual speech model support
- 🧠 Integration with offline chatbot (RASA / Transformers)
- 😊 Emotion recognition from voice tone
- 🖥️ GUI version using Tkinter or Electron
- ☁️ Optional online search integration


## 🧑‍💻 Team Members

| Name               | Role                  | Responsibility                           |
|-------------------|----------------------|----------------------------------------|
| Om Koli           | Lead Developer        | Python backend, speech recognition logic |
| Suraj Pati        | UI Developer          | Interface & GUI (future)                 |
| Saurabh Ganbote   | Research & Testing    | Knowledge base, QA, documentation        |
| Pradip Khatal     | Documentation & Testing | Prepare documentation, test commands, ensure knowledge base accuracy |


---

## 📜 License

This project is **open-source** and is available for **educational, hackathon, and research purposes**.  
You are free to **modify, extend, and distribute** the code with proper attribution to the authors.

---

## 💬 Acknowledgements

We gratefully acknowledge the following resources and contributors:

- [VOSK Speech Recognition Toolkit](https://alphacephei.com/vosk/)  
- [pyttsx3 Text-to-Speech Library](https://pypi.org/project/pyttsx3/)  
- Python open-source community and contributors  

---

> 🗣️ **“Your voice has power — even offline.”**  
> — *Team Code Storm*


