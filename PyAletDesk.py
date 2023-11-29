import tkinter as tk
from tkinter import ttk  # For improved widgets and theming
from threading import Thread
import time
from plyer import notification

def start_notification_thread(interval, title, message):
    def notify_periodically():
        while True:
            notification.notify(title=title, message=message, timeout=10)
            time.sleep(interval)

    notification_thread = Thread(target=notify_periodically, daemon=True)
    notification_thread.start()

def on_submit():
    interval = int(interval_entry.get()) * 60
    title = title_entry.get()
    message = message_entry.get()
    start_notification_thread(interval, title, message)

# Initialize main application window
app = tk.Tk()
app.title("Break Notification Settings")
app.geometry("300x200")  # Set window size

# Use a better-looking theme
style = ttk.Style()
style.theme_use('clam')

# Create a frame for input fields
input_frame = ttk.Frame(app, padding="10")
input_frame.pack(fill='both', expand=True)

# Interval input
ttk.Label(input_frame, text="Interval (minutes):").grid(row=0, column=0, sticky="w")
interval_entry = ttk.Entry(input_frame)
interval_entry.grid(row=1, column=0, pady=5)

# Title input
ttk.Label(input_frame, text="Notification Title:").grid(row=2, column=0, sticky="w")
title_entry = ttk.Entry(input_frame)
title_entry.grid(row=3, column=0, pady=5)

# Message input
ttk.Label(input_frame, text="Notification Message:").grid(row=4, column=0, sticky="w")
message_entry = ttk.Entry(input_frame)
message_entry.grid(row=5, column=0, pady=5)

# Submit button
submit_button = ttk.Button(input_frame, text="Start Notifications", command=on_submit)
submit_button.grid(row=6, column=0, pady=10)

app.mainloop()
