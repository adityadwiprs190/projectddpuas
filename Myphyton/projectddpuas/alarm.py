import tkinter as tk
from tkinter import ttk,messagebox
import time
import pygame
from datetime import datetime

class AlarmApp:
    def __init__(self, pemula):
        self.pemula = pemula
        self.pemula.title("Alarm")
        self.pemula.geometry("250x150")
        self.label = ttk.Label(pemula, text="Pilih waktu alarm (HH:MM:SS am/pm):")
        self.label.pack(pady=10)
        self.entry = ttk.Entry(pemula)
        self.entry.pack(pady=10)
        self.button = ttk.Button(pemula, text="Set Alarm", command=self.set_alarm)
        self.button.pack(pady=20)
        pygame.mixer.init()
    def set_alarm(self):
        alarm_time_str = self.entry.get()
        try:        
             alarm_time = datetime.strptime(alarm_time_str, "%I:%M:%S %p").time()            
             waktu_saat_ini = datetime.now().time()           
             selisih_waktu = datetime.combine(datetime.today(), alarm_time) - datetime.combine(datetime.today(), waktu_saat_ini)             
             selisih_waktu_seconds = selisih_waktu.total_seconds()
             self.pemula.after(int(selisih_waktu_seconds * 1000), self.run_alarm)
             self.pemula.withdraw()
             messagebox.showinfo("Alarm diatur","Alarm diatur pada waktu yang telah dibuat")
        except ValueError:
            messagebox.showerror("Error", "Masukkan format dengan benar!")
            
    def run_alarm(self):
        time.sleep(1)
        pygame.mixer.music.load("Alarm.mp3") 
        pygame.mixer.music.play()
        messagebox.showinfo("Warning!", "Waktu alarm telah habis!")
        pygame.mixer.music.stop()
        self.pemula.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()
