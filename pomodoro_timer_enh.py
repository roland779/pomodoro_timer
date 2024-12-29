import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import winsound
from plyer import notification
import threading


# Function to play a sound based on the phase type
def play_sound(sound_type):
    if mute_flag.get():
        return
    if sound_type == "work":
        winsound.Beep(440, 500)  # Beep sound for the work phase
    elif sound_type == "break":
        winsound.Beep(880, 500)  # Beep sound for the break phase


# Function to log messages in the log box
def log_message(message):
    log_box.config(state=tk.NORMAL)
    log_box.insert(tk.END, message + "\n")
    log_box.config(state=tk.DISABLED)
    log_box.see(tk.END)


# Function to send desktop notifications
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Pomodoro Timer",
        timeout=10
    )


# Countdown timer with progress bar updates and logging
def countdown(minutes, label, progress, end_message, sound_type):
    global pause_flag
    seconds = minutes * 60
    total_seconds = seconds

    while seconds >= 0:
        if pause_flag:
            time.sleep(1)
            continue
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        label.config(text=timer)
        progress["value"] = ((total_seconds - seconds) / total_seconds) * 100
        label.update()
        progress.update()
        time.sleep(1)
        seconds -= 1

    play_sound(sound_type)
    log_message(end_message)
    send_notification("Pomodoro Timer", end_message)


# Main Pomodoro logic
def start_pomodoro():
    global pause_flag
    pause_flag = False
    try:
        work_duration = int(work_entry.get())
        short_break = int(short_break_entry.get())
        long_break = int(long_break_entry.get())
        cycles = int(cycle_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for durations and cycles.")
        start_button.config(state=tk.NORMAL)
        return

    for cycle in range(1, cycles + 1):
        cycle_label.config(text=f"Cycle {cycle} - Work Phase")
        log_message(f"Cycle {cycle}: Work phase started at {time.strftime('%Y-%m-%d %I:%M:%S')}")
        countdown(work_duration, timer_label, progress_bar, "Work phase completed. Time for a break!", "work")

        if cycle < cycles:
            cycle_label.config(text="Short Break")
            log_message(f"Cycle {cycle}: Short break started at {time.strftime('%Y-%m-%d %I:%M:%S')}")
            countdown(short_break, timer_label, progress_bar, "Break over. Back to work!", "break")
        else:
            cycle_label.config(text="Long Break")
            log_message(f"Cycle {cycle}: Long break started at {time.strftime('%Y-%m-%d %I:%M:%S')}")
            countdown(long_break, timer_label, progress_bar, "Well done! Pomodoro session complete.", "break")
            break


# Function to start the Pomodoro process in a separate thread
def start_timer():
    start_button.config(state=tk.DISABLED)
    threading.Thread(target=start_pomodoro).start()


# Pause/Resume functionality
def toggle_pause():
    global pause_flag
    pause_flag = not pause_flag
    if pause_flag:
        pause_button.config(text="Resume")
        log_message(f"Timer paused - {time.strftime('%Y-%m-%d %I:%M:%S')}")
    else:
        pause_button.config(text="Pause")
        log_message(f"Timer resumed - {time.strftime('%Y-%m-%d %I:%M:%S')}")

# GUI Setup
root = tk.Tk()
root.title("Enhanced Pomodoro Timer")
root.geometry("500x1000")  # Larger default window size
root.resizable(True, True)  # Allow window resizing

# Title Label
title_label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# Input Section
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=20, fill=tk.BOTH, expand=False)

tk.Label(frame_inputs, text="Work Duration (min):", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
work_entry = tk.Entry(frame_inputs, width=10)
work_entry.insert(0, "25")
work_entry.grid(row=0, column=1)

tk.Label(frame_inputs, text="Short Break (min):", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=5)
short_break_entry = tk.Entry(frame_inputs, width=10)
short_break_entry.insert(0, "5")
short_break_entry.grid(row=1, column=1)

tk.Label(frame_inputs, text="Long Break (min):", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5)
long_break_entry = tk.Entry(frame_inputs, width=10)
long_break_entry.insert(0, "15")
long_break_entry.grid(row=2, column=1)

tk.Label(frame_inputs, text="Number of Cycles:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", pady=5)
cycle_entry = tk.Entry(frame_inputs, width=10)
cycle_entry.insert(0, "4")
cycle_entry.grid(row=3, column=1)

# Cycle and Timer Labels
cycle_label = tk.Label(root, text="", font=("Helvetica", 16))
cycle_label.pack(pady=10)

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Control Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Start", command=start_timer, font=("Helvetica", 14))
start_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(button_frame, text="Pause", command=toggle_pause, font=("Helvetica", 14))
pause_button.grid(row=0, column=1, padx=10)

# Mute Checkbox
mute_flag = tk.BooleanVar()
mute_checkbox = tk.Checkbutton(root, text="Mute Notifications", variable=mute_flag, font=("Helvetica", 12))
mute_checkbox.pack(pady=10)

# Log Section with Scrollable Frame
log_label = tk.Label(root, text="Activity Log:", font=("Helvetica", 14))
log_label.pack(pady=5)

log_frame = tk.Frame(root)
log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

log_scrollbar = tk.Scrollbar(log_frame)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_box = tk.Text(log_frame, height=15, width=60, state=tk.DISABLED, font=("Helvetica", 12), wrap=tk.WORD, yscrollcommand=log_scrollbar.set)
log_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
log_scrollbar.config(command=log_box.yview)

# Start the main application loop
root.mainloop()
