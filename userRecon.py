from tkinter import *
import customtkinter as ttk


App = ttk.CTk()
App.title("userRecon System")
App.geometry("400x700+700+50")
App.resizable(False, False)

img = PhotoImage(file='assets/Menu.png')
menu = img.subsample(1, 1)

topBar = ttk.CTkFrame(App, height=50, fg_color='#0B3838')
ttk.CTkLabel(topBar, text="userRecon system", font=("arial", 20, "bold")).pack(pady=10, padx=10, side=LEFT)
menuButton = ttk.CTkButton(topBar, text="", image=menu, width=30, fg_color='#0B3838')
menuButton.pack(side=RIGHT, pady=5, padx=10, ipady=5)
topBar.pack(fill=X, pady=5, padx=10)


def moveIn(e):
    if userName.get() != "":
        userName.delete(0, 'end')
    else:
        pass


userName = ttk.CTkEntry(App, height=40, font=("arial", 15, "bold"))
userName.pack(fill=X, padx=10, ipadx=10)
userName.insert(0, 'Enter User Name')
userName.bind("<FocusIn>", moveIn)


def start():
    pass


def stop():
    pass


buttonFrame = ttk.CTkFrame(App)
stopButton = ttk.CTkButton(buttonFrame, text="STOP", font=("arial", 20, "bold"), width=170, fg_color='#BA5151',
                           command=stop)
stopButton.pack(side=LEFT, padx=10, ipady=8, pady=10)
startButton = ttk.CTkButton(buttonFrame, text="START", font=("arial", 20, "bold"), width=170, fg_color='#3E94B9',
                            command=start)
startButton.pack(side=LEFT, padx=10, ipady=8, pady=10)

buttonFrame.pack(fill=X, padx=10, pady=5)

outputWindow = Listbox(App, bg='#0B3838', font=('arial', 15), foreground='white')
outputWindow.pack(fill=BOTH, expand=True, padx=15, pady=10, ipadx=15, ipady=15)

App.mainloop()
