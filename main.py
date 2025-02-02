import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
from ffpyplayer.player import MediaPlayer  # For audio playback

def play_video():
    video_path = os.path.join(os.getcwd(), 'temp.mp4')

    if not os.path.exists(video_path):
        messagebox.showerror("Error", "Video file not found.")
        return

    cap = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)  # Load audio

    if not cap.isOpened():
        messagebox.showerror("Error", "Unable to open video file.")
        return

    # Create a new window for video
    window = tk.Toplevel()
    window.title("Video Player")

    # Create a label to display video frames
    label = tk.Label(window)
    label.pack()

    def update_frame():
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()  # Get audio frame

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            label.imgtk = imgtk  # Prevent garbage collection
            label.config(image=imgtk)

            if val != 'eof' and audio_frame is not None:
                window.after(10, update_frame)  # Schedule next frame
        else:
            cap.release()
            player.close_player()
            window.destroy()  # Close the window when the video ends

    update_frame()  # Start video playback

# Main function to handle button clicks
def onClick():
    messagebox.showinfo("Happy Valentines Babe.", "Hi, I'm your message")  # First message popup
    
    result = messagebox.askyesno("Something", "Do you want to proceed to the next message?")
    if result:
        messagebox.showinfo("Something2", "Here's the second message!")
        play_video()

# Tkinter main window setup
root = tk.Tk()
root.title("Press button")
root.geometry('500x300')

button = tk.Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom')

root.mainloop()
