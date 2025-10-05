

"""
Simple Offline Voice Agent
- Uses VOSK for offline speech -> text
- Uses pyttsx3 for text -> speech
- Simple rule-based responder with fallback
- Easy to run and submit (works offline)

Run:
1) Install requirements: pip install -r requirements.txt
2) Download a small VOSK model (see README) and place it in ./model
3) python voice_agent.py

Press Ctrl+C to stop.
"""

import os
import queue
import sys
import json
import threading
import time

try:
    import sounddevice as sd
    from vosk import Model, KaldiRecognizer
    import pyttsx3
except Exception as e:
    print("Missing packages or audio devices. Install requirements and check your audio hardware.")
    print(e)
    sys.exit(1)

# ---------------------------
# Configuration
# ---------------------------
MODEL_PATH = "model"  # Put your VOSK model folder here (see README)
SAMPLE_RATE = 16000
DEVICE = None  # None = default input device
RECORD_SECONDS = 8  # length used for each recognition chunk (continuous mode below uses stream)

# Simple knowledge base (you can add more)
KNOWLEDGE = {
    "hello": "Hello! I am your voice agent. How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! Nice to see you here.",
    "how are you": "I'm a program, so I don't have feelings, but I'm here to help you!",
    "what is your name": "I am called TezAgent, your hackathon voice agent.",
    "who created you": "I was created by awesome developers like you for the hackathon project!",
    "what can you do": "I can answer basic questions, tell you the time or date, and keep you company while you code!",
    "time": lambda: f"The current time is {time.strftime('%I:%M %p')}.",
    "date": lambda: f"Today's date is {time.strftime('%Y-%m-%d')}.",
    "thank you": "You're welcome! Good luck with your hackathon!",
    "thanks": "Anytime! Let me know if you need anything else.",
    "help": "You can ask me things like: what's the time, what's your name, who created you, or say hello.",
    "good morning": "Good morning! I hope your day is productive and positive!",
    "good afternoon": "Good afternoon! Keep going, you're doing great!",
    "good evening": "Good evening! Ready to wrap up your day or start something new?",
    "by": "Goodbye! See you soon!",
    "goodbye": "Take care! Hope to talk to you again!",
    "what is hackathon": "A hackathon is an event where people come together to code, create, and build cool projects in a short time!",
    "who are you": "I’m TezAgent — your friendly AI voice assistant built for this project.",
    "open google": "Sorry, I work offline, but you can open Google manually in your browser.",
    "joke": "Why did the computer get cold? Because it left its Windows open!",
    "fun fact": "Did you know? The first computer mouse was made of wood in 1964!",
    "motivate me": "Don’t give up! Every expert was once a beginner. Keep going!",
    "how old are you": "I was created recently, so I’m quite young — but learning fast!",
    "sing a song": "I can’t sing yet, but if I could, I’d sing the debug blues!",
    "what is your purpose": "My purpose is to assist you with your tasks and make your hackathon project awesome!",
    "where are you from": "I live right inside your computer — no rent needed!",
    "tell me about yourself": "I’m TezAgent, a smart yet simple voice assistant running offline using Python and VOSK.",
    "are you real": "I exist in your computer, so that makes me real enough for now!",
}

# ---------------------------
# Helper functions
# ---------------------------
def text_to_speech(text):
    """Speak text using pyttsx3 (offline)."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)  # speech rate
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def generate_response(text):
    """Very simple response generator: keyword matching + fallback."""
    if not text:
        return "I didn't catch that. Could you say it again?"
    t = text.lower().strip()
    # direct matches
    for k, v in KNOWLEDGE.items():
        if k in t:
            return v() if callable(v) else v
    # small commands
    if t.startswith("open ") or t.startswith("search "):
        return "I can help with that, but web search is disabled in this offline demo."
    # fallback: simple echo + suggestion
    return "You said: " + text + ". (Sorry Your Voice is not clear!.)"

# ---------------------------
# VOSK listening worker
# ---------------------------
def recognize_microphone(model_path=MODEL_PATH, sample_rate=SAMPLE_RATE, device=DEVICE):
    if not os.path.exists(model_path):
        print(f"Model not found at '{model_path}'. Please download a VOSK model and extract to this folder.")
        return

    model = Model(model_path)
    q = queue.Queue()

    def audio_callback(indata, frames, time_info, status):
        """Called (from sounddevice) for each audio block."""
        if status:
            print("Audio status:", status, file=sys.stderr)
        q.put(bytes(indata))

    rec = KaldiRecognizer(model, sample_rate)

    with sd.RawInputStream(samplerate=sample_rate, blocksize = 8000, device=device, dtype='int16',
                           channels=1, callback=audio_callback):
        print("Listening... Speak into your microphone. Press Ctrl+C to stop.")
        try:
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    res = rec.Result()
                    j = json.loads(res)
                    text = j.get("text", "")
                    if text:
                        print(">> You:", text)
                        resp = generate_response(text)
                        print("<< Agent:", resp)
                        # speak in a background thread so recognition continues
                        t = threading.Thread(target=text_to_speech, args=(resp,), daemon=True)
                        t.start()
                else:
                    # partial result (optional)
                    # print(rec.PartialResult(), end="\r")
                    pass
        except KeyboardInterrupt:
            print("\nStopped by user")
        except Exception as e:
            print("Error while listening:", e)

# ---------------------------
# Fallback text-mode (fast testing)
# ---------------------------
def text_mode():
    print("TEXT MODE: Type your message and press Enter. Type 'exit' to quit.")
    while True:
        try:
            line = input("You: ").strip()
        except EOFError:
            break
        if not line:
            continue
        if line.lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        resp = generate_response(line)
        print("Agent:", resp)
        # optionally speak
        speak = input("Speak response? (y/N): ").strip().lower()
        if speak == "y":
            text_to_speech(resp)

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    print("=== Simple Offline Voice Agent ===")
    print("Mode options:")
    print("1) Voice (microphone) mode — needs VOSK model in ./model")
    print("2) Text mode (fast, no audio)")
    try:
        choice = input("Choose mode [1/2, default 1]: ").strip() or "1"
    except EOFError:
        choice = "1"
    if choice == "2":
        text_mode()
    else:
        recognize_microphone()
