from tkinter import *
from gpiozero import LED as Relay


class App:
    def __init__(self, window):
        self.relay = Relay(25)

        #interface
        self.buttonText = StringVar();

        mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
        Button(mainFrame, textvariable=self.buttonText, command=self.userClick).pack(expand=YES, fill=BOTH, padx=40, pady=25)
        self.buttonText.set("OPEN")
        mainFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)

    def userClick(self):
        if self.buttonText.get() == "CLOSE":
            self.buttonText.set("OPEN")
        else:
            self.buttonText.set("CLOSE")


if __name__ == "__main__":
    window = Tk()
    window.title("relayControl")
    window.geometry("300x200")
    window.option_add("*Font", ('verdana', 20))
    window.option_add('*Label.Font', ('verdana', 18))
    window.option_add('*Button.Background', "dark gray")
    app = App(window)
    window.mainloop()