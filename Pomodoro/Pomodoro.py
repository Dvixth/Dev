import tkinter as tk
from tkinter import messagebox
import winsound
import time
import threading

class PomodoroTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.geometry("300x300")
        self.configure(bg='black')
        self.overrideredirect(True)  # Remove window decorations
        self.wm_attributes("-topmost", True)  # Keep window on top

        self.session_time = 0.1 * 60  # 25 minutes
        self.short_break_time = 5 * 60  # 5 minutes
        self.long_break_time = 20 * 60  # 20 minutes

        self.time_left = self.session_time
        self.is_running = False

        self.create_widgets()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=300, height=300, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.timer_text = self.canvas.create_text(150, 150, text="25:00", fill="white", font=("Helvetica", 48))

        self.start_button = tk.Button(self, text="Start", command=self.start_timer, bg='white', fg='black')
        self.start_button.place(x=125, y=250)

    def update_timer(self):
        minutes, seconds = divmod(self.time_left, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.canvas.itemconfig(self.timer_text, text=time_str)
        
        if self.time_left > 0:
            self.time_left -= 1
            self.after(1000, self.update_timer)
        else:
            self.is_running = False
            self.notify("Time's up!", "The timer has ended.")
            self.start_button.config(state=tk.NORMAL)
    
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.update_timer()
    
    def notify(self, title, message):
        # Play sound
        #winsound.Beep(1000, 500)  # Frequency in Hertz, Duration in milliseconds
        winsound.PlaySound('Pomodoro/src/notification.wav', winsound.SND_FILENAME)  

if __name__ == "__main__":
    app = PomodoroTimer()
    app.mainloop()
