Music Recommendation based on emotion 
A real-time deep learning application that detects facial emotions through a webcam and recommends music based on the detected emotion — built with PyTorch and OpenCV.
📸 Demo
Webcam detects your face → Classifies emotion → Recommends matching music in real time
✨ Features
🎯 Real-time facial emotion detection via webcam
🧠 Custom CNN model trained from scratch using PyTorch
🎵 Music recommendation based on detected emotion
🟩 Face bounding box with emotion label and confidence score
💾 Auto-saves best model during training
⚡ GPU acceleration supported (auto-detects CUDA)
🎭 Supported Emotions
Emotion
Music Mood Recommended
😊 Happy
Upbeat / Pop / Dance
😢 Sad
Calm / Acoustic / Lo-fi
😠 Angry
Heavy / Rock / Metal
😨 Fear
Ambient / Instrumental
😲 Surprise
Energetic / Electronic
🤢 Disgust
Chill / Indie
😐 Neutral
Jazz / Classical
🗂️ Project Structure
Code
🧠 Model Architecture
A custom Convolutional Neural Network (CNN) built with PyTorch:
Code
Training configuration:
Optimizer: Adam (lr = 0.002)
Loss: CrossEntropyLoss
Epochs: 50
Batch size: 32
Image size: 64 × 64
Validation split: 20%
⚙️ Setup & Installation
1. Clone the repository
Bash
2. Create a virtual environment
Bash
3. Install dependencies
Bash
4. GPU support (optional but recommended)
Visit pytorch.org and install the CUDA version matching your system. Example for CUDA 12.1:
Bash
🏋️ Training
Place emotion-detector-data.zip in the project root folder
Run:
Bash
Training output example:
Code
The best model is automatically saved to model.pth.
🎵 Music Recommendation
The music recommendation module maps detected emotions to curated playlists or song suggestions. When an emotion is detected with high confidence, the system suggests music that matches the user's current mood.
To run the full application with music recommendation:
Bash
📷 Running the Webcam
Bash
A window opens with your live webcam feed
Detected faces are highlighted with a bounding box
Emotion label and confidence score are shown above the face
Music recommendation is displayed based on emotion
Press Q to quit
🛠️ Troubleshooting
Problem
Solution
Webcam not opening
Ensure no other app is using the camera. Try VideoCapture(1)
CUDA not available
Code auto-falls back to CPU — no action needed
ModuleNotFoundError
Make sure (venv) is active before running
Wrong Python in VS Code
Click Python version (bottom-left) → select venv interpreter
num_workers error on Windows
Already set to 0 in code — this is correct
📦 Dependencies
Code
🚀 Training on Google Colab (Free GPU)
You can train on Colab's free GPU and run inference locally:
Upload your code and dataset to Colab
Train the model
Download model.pth:
Python
Place model.pth in your local project folder
Run python inference.py in VS Code
📄 License
This project is for educational purposes.
🙋 Author
Your Name
GitHub: @yourname Music Recommendation
A real-time deep learning application that detects facial emotions through a webcam and recommends music based on the detected emotion — built with PyTorch and OpenCV.
📸 Demo
Webcam detects your face → Classifies emotion → Recommends matching music in real time
✨ Features
🎯 Real-time facial emotion detection via webcam
🧠 Custom CNN model trained from scratch using PyTorch
🎵 Music recommendation based on detected emotion
🟩 Face bounding box with emotion label and confidence score
💾 Auto-saves best model during training
⚡ GPU acceleration supported (auto-detects CUDA)
🎭 Supported Emotions
Emotion
Music Mood Recommended
😊 Happy
Upbeat / Pop / Dance
😢 Sad
Calm / Acoustic / Lo-fi
😠 Angry
Heavy / Rock / Metal
😨 Fear
Ambient / Instrumental
😲 Surprise
Energetic / Electronic
🤢 Disgust
Chill / Indie
😐 Neutral
Jazz / Classical
🗂️ Project Structure
Code
🧠 Model Architecture
A custom Convolutional Neural Network (CNN) built with PyTorch:
Code
Training configuration:
Optimizer: Adam (lr = 0.002)
Loss: CrossEntropyLoss
Epochs: 50
Batch size: 32
Image size: 64 × 64
Validation split: 20%
⚙️ Setup & Installation
1. Clone the repository
Bash
2. Create a virtual environment
Bash
3. Install dependencies
Bash
4. GPU support (optional but recommended)
Visit pytorch.org and install the CUDA version matching your system. Example for CUDA 12.1:
Bash
🏋️ Training
Place emotion-detector-data.zip in the project root folder
Run:
Bash
Training output example:
Code
The best model is automatically saved to model.pth.
🎵 Music Recommendation
The music recommendation module maps detected emotions to curated playlists or song suggestions. When an emotion is detected with high confidence, the system suggests music that matches the user's current mood.
To run the full application with music recommendation:
Bash
📷 Running the Webcam
Bash
A window opens with your live webcam feed
Detected faces are highlighted with a bounding box
Emotion label and confidence score are shown above the face
Music recommendation is displayed based on emotion
Press Q to quit
🛠️ Troubleshooting
Problem
Solution
Webcam not opening
Ensure no other app is using the camera. Try VideoCapture(1)
CUDA not available
Code auto-falls back to CPU — no action needed
ModuleNotFoundError
Make sure (venv) is active before running
Wrong Python in VS Code
Click Python version (bottom-left) → select venv interpreter
num_workers error on Windows
Already set to 0 in code — this is correct
📦 Dependencies
Code
🚀 Training on Google Colab (Free GPU)
You can train on Colab's free GPU and run inference locally:
Upload your code and dataset to Colab
Train the model
Download model.pth:
Python
Place model.pth in your local project folder
Run python inference.py in VS Code
📄 License
This project is for educational purposes.
🙋 Author
Your Name
GitHub: @yourname# Music-recommendation-based-on-emotion