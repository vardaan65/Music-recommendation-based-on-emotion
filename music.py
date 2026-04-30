import cv2
import pandas as pd
import numpy as np
import os
from collections import Counter
from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- MODEL ----------------
model = load_model("best_model.h5")

emotion_labels = [
    "angry","contempt","disgust","fear",
    "happy","sad","surprise","neutral"
]

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ---------------- MUSIC ----------------
emotion_files = {
    "happy": "songs/happy.csv",
    "sad": "songs/sad.csv",
    "angry": "songs/angry.csv",
    "neutral": "songs/neutral.csv",
    "surprise": "songs/surprised.csv",
    "fear": "songs/fearful.csv",
    "disgust": "songs/disgusted.csv",
    "contempt": "songs/contempt.csv"
}

music_data = {}
for emotion, file in emotion_files.items():
    if os.path.exists(file):
        df = pd.read_csv(file)
        if "Name" in df.columns and "Artist" in df.columns:
            songs = (df["Name"] + " - " + df["Artist"]).dropna().tolist()
        else:
            songs = df.iloc[:, 0].dropna().tolist()
        music_data[emotion] = songs

# ---------------- SMOOTHING ----------------
emotion_buffer = []
def get_stable_emotion(new_emotion):
    emotion_buffer.append(new_emotion)
    if len(emotion_buffer) > 5:
        emotion_buffer.pop(0)
    return Counter(emotion_buffer).most_common(1)[0][0]

# ---------------- DETECTION ----------------
def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (48, 48)) / 255.0
        face = np.reshape(face, (1, 48, 48, 3))

        preds = model.predict(face, verbose=0)
        idx = np.argmax(preds)
        confidence = float(preds[0][idx]) * 100

        emotion = emotion_labels[idx] if idx < len(emotion_labels) else "neutral"
        if emotion == "contempt":
            emotion = "neutral"

        return emotion, confidence, (x, y, w, h)

    return "neutral", 0, None

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Emotion Music Player")
root.geometry("1100x600")
root.configure(bg="#121212")

# STYLE
style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Segoe UI", 10), padding=6)

# LEFT: VIDEO
video_frame = tk.Frame(root, bg="#121212")
video_frame.pack(side="left", padx=10, pady=10)

video_label = tk.Label(video_frame, bg="#000")
video_label.pack()

# RIGHT: CONTROL PANEL
panel = tk.Frame(root, bg="#1e1e1e", width=350)
panel.pack(side="right", fill="y")

title = tk.Label(panel, text="Emotion Music", fg="white",
                 bg="#1e1e1e", font=("Segoe UI", 18, "bold"))
title.pack(pady=20)

emotion_label = tk.Label(panel, text="Emotion: -", fg="#00ffcc",
                         bg="#1e1e1e", font=("Segoe UI", 14))
emotion_label.pack(pady=5)

confidence_label = tk.Label(panel, text="Confidence: -", fg="#00ffcc",
                            bg="#1e1e1e", font=("Segoe UI", 12))
confidence_label.pack(pady=5)

# SONG LIST WITH SCROLL
frame_list = tk.Frame(panel)
frame_list.pack(pady=15)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

songs_box = tk.Listbox(frame_list, width=40, height=15,
                       bg="#2b2b2b", fg="white",
                       yscrollcommand=scrollbar.set)
songs_box.pack()

scrollbar.config(command=songs_box.yview)

# BUTTONS
btn_frame = tk.Frame(panel, bg="#1e1e1e")
btn_frame.pack(pady=20)

start_btn = ttk.Button(btn_frame, text="Start Camera")
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ttk.Button(btn_frame, text="Stop Camera")
stop_btn.grid(row=0, column=1, padx=10)

exit_btn = ttk.Button(panel, text="Exit", command=root.destroy)
exit_btn.pack(pady=10)

# ---------------- CAMERA ----------------
cap = None
running = False
last_emotion = ""

# ---------------- LOOP ----------------
def update_frame():
    global last_emotion

    if not running:
        return

    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.resize(frame, (640, 480))

    detected_emotion, confidence, face_coords = detect_emotion(frame)
    emotion = get_stable_emotion(detected_emotion)

    if emotion not in music_data:
        emotion = "neutral"

    if face_coords:
        x, y, w, h = face_coords
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        label = f"{emotion} ({confidence:.1f}%)"
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    emotion_label.config(text=f"Emotion: {emotion}")
    confidence_label.config(text=f"Confidence: {confidence:.1f}%")

    if emotion != last_emotion:
        songs_box.delete(0, tk.END)
        for song in music_data.get(emotion, [])[:10]:
            songs_box.insert(tk.END, song)
        last_emotion = emotion

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    root.after(10, update_frame)

# ---------------- BUTTON FUNCTIONS ----------------
def start_camera():
    global cap, running
    if not running:
        cap = cv2.VideoCapture(0)
        running = True
        update_frame()

def stop_camera():
    global cap, running
    running = False
    if cap:
        cap.release()

start_btn.config(command=start_camera)
stop_btn.config(command=stop_camera)

# ---------------- RUN ----------------
root.mainloop()

if cap:
    cap.release()
cv2.destroyAllWindows()