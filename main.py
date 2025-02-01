import tkinter as tk
from tkinter import messagebox
import cv2
import os

# Function to play the video using OpenCV
def play_video():
    # Set the path to your video
    video_path = os.path.join(os.getcwd(), 'temp.mp4')  # Ensure 'temp.mp4' is in the same folder

    # Open the video using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        messagebox.showerror("Error", "Unable to open video file.")
        return

    # Create a tkinter window for video display
    window = tk.Toplevel()
    window.title("Video Player")
    window.geometry('640x480')

    # Create a canvas for video display
    canvas = tk.Canvas(window, width=640, height=480)
    canvas.pack()

    # Read and display video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB format (OpenCV uses BGR)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PhotoImage for tkinter
        photo = tk.PhotoImage(image=tk.Image.fromarray(frame_rgb))

        # Display the frame on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        window.update_idletasks()

        # Allow for tkinter window events to be processed
        window.update()

    # Release the video capture when done
    cap.release()

# Main function to handle button clicks and popups
def onClick():
    messagebox.showinfo("Happy Valentines Babe.", "Hi, I'm your message")  # First message popup
    
    # Second message popup
    result = messagebox.askyesno("Something", "Do you want to proceed to the next message?")
    if result:  # If user clicks "Yes"
        messagebox.showinfo("Something2", "Here's the second message!")
        
        # After second message is clicked, set the flag and play the video
        flag = True
        if flag:
            play_video()

# Set up the Tkinter window
root = tk.Tk()
root.title("Press button")
root.geometry('500x300')

# Create the button that triggers the onClick function
button = tk.Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom')

# Run the Tkinter event loop
root.mainloop()
