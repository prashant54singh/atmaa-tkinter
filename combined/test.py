import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime


class AlertDialog:

    def __init__(self):

        self.invalidDiag = tk.Toplevel()
        invalidInput = tk.Label(master=self.invalidDiag,
                                text='Error: Invalid Input').grid(row=1, column=1)
        closeButton = tk.Button(master=self.invalidDiag,
                                text='Close',
                                command=self.invalidDiag.destroy).grid(row=2, column=1)

    def start(self):
        # self.invalidDiag.grab_set() #takes control over the dialog (makes it active)
        self.invalidDiag.wait_window()


class  QuitDialog():

    def __init__(self, instance):

        self.instance = instance

        self.quitDialog = tk.Toplevel()

        warnMessage = tk.Label(master=self.quitDialog,
                                text='Are you sure that you want to quit? ').grid(row=1, column=1, columnspan=2)
        quitButton = tk.Button(master= self.quitDialog ,
                                text='Yes',
                                command = self.quitALL).grid(row=2, column=1)
        cancelButton = tk.Button(master= self.quitDialog,
                                text='No',
                                command = lambda: self.quitDialog.destroy()).grid(row=2, column=2)

    def start(self):
        # self.invalidDiag.grab_set() #takes control over the dialog (makes it active)
        self.quitDialog.wait_window()

    def quitALL(self):
        self.quitDialog.destroy()
        self.instance.destroy()


class TimeConverter:

    def __init__(self):

        self.mainWindow = tk.Tk()
        self.mainWindow.title("Seconds Converter")
        self.results = tk.StringVar()
        self.inputSecs = tk.StringVar()
        secLabel = tk.Label(master=self.mainWindow,
                            text="Seconds:").grid(row=0, sticky="W")
        resultLabel = tk.Label(master=self.mainWindow,
                               text="Converted Time:\n(H:M:S)").grid(row=1, sticky="W")
        calcResults = tk.Label(master=self.mainWindow,
                               background='light gray', width=20,
                               textvariable=self.results,
                               anchor="w").grid(row=1, column=1)
        secEntry = tk.Entry(master=self.mainWindow,
                            width=24,
                            textvariable=self.inputSecs).grid(row=0, column=1)

        calcButton = tk.Button(master=self.mainWindow,
                               text='Calculate',
                               command=self.SecondsToHours).grid(row=2,
                                                                 column=0, sticky="w")
        quitButton = tk.Button(master=self.mainWindow,
                               text='Quit',
                               command=self.showQuitDialog).grid(row=3, column=1, sticky="E")

    def invalidInputEntered(self):
        errorDiag = AlertDialog()
        errorDiag.start()

    def showQuitDialog(self):
        quitdialog = QuitDialog(self.mainWindow)
        quitdialog.start()

    def startDisplay(self) -> None:
        self.mainWindow.mainloop()

    def destroyit(self):
        self.mainWindow.destroy()

    def SecondsToHours(self):
        try:
            inputseconds = int(self.inputSecs.get())
            seconds = int(inputseconds % 60)
            minutes = int(((inputseconds - seconds) / 60) % 60)
            hours = int((((inputseconds - seconds) / 60) - minutes) / 60)
            tempResults = str(hours) + ':' + str(minutes) + ':' + str(seconds)
            self.results.set(tempResults)
            return

        except ValueError:
            self.invalidInputEntered()
            #self.showQuitDialog()

if __name__ == '__main__':
    TimeConverter().startDisplay()