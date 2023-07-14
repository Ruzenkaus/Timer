import tkinter
import time
import customtkinter
import customtkinter as ctk


class Timer(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.label_timer = ctk.CTkLabel(self, text='00:00:00')
        self.label_timer.grid(row=2, column=2, pady=5, padx=10)
        self.button_start = ctk.CTkButton(self, text='Start Timer', command=self.start_timer)
        self.button_start.grid(row=3, column=1)
        self.button_stop = ctk.CTkButton(self, text='Stop Timer', command=self.stop_timer)
        self.button_stop.grid(row=3, column=2)
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.running = False

    def start_timer(self):
        self.running = True

        while self.running:
            self.update()
            self.seconds += 1

            self.label_timer.configure(text=f'{self.hours}:{self.minutes}:{self.seconds}')
            
            if self.seconds % 60 == 0 and self.seconds!= 0:
                self.seconds = 0
                self.minutes+=1
            if self.minutes % 60 == 0 and self.minutes !=0:
                self.hours+=1
                self.minutes = 0

            time.sleep(1)


    def stop_timer(self):
        self.running = False
app = Timer()
app.mainloop()