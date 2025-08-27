import tkinter as tk
from tkinter import simpledialog, messagebox

class App(tk.Tk):
    def __init__(self, numSets=2, cardList=None, oddsList=None):
        super().__init__()
        self.title("Poker Odd Calculator")

        self.geometry("1280x720")
        self.resizable(False, False)
        #Inputs needed for strucrture and updating labels
        self.numSets = numSets
        self.cardList = cardList
        self.oddsList = oddsList

        topFrame = tk.Frame(self)

        topFrame.pack(pady=10)

        tk.Label(topFrame, text="Community Cards:").grid(row=0, column=0, columnspan=5, pady=(0, 5))
        #Community Cards
        self.topLabels = []
        for i in range(5):
            lbl = tk.Label(topFrame, text="", width=8, relief="solid")
            lbl.grid(row=1, column=i, padx=3)
            self.topLabels.append(lbl)

        for lbl in self.topLabels:
            lbl.grid_remove()

        self.topType1 = tk.Label(topFrame, text="")
        self.topType1.grid(row=3, column=0, columnspan=5, pady=(5, 0))

        self.topDrawLabel = tk.Label(topFrame, text="Draw")
        self.topDrawLabel.grid(row=4, column=0, columnspan=5, pady=(2, 0))

        self.dynamicFrame = tk.Frame(self)
        self.dynamicFrame.pack(pady=15)

        self.dynamicSets = []

        #Player
        for i in range(numSets):
            setFrame = tk.Frame(self.dynamicFrame)
            setFrame.pack(side=tk.LEFT, padx=10, pady=5)

            playerLabel = tk.Label(setFrame, text=f"Player {i+1}")
            playerLabel.grid(row=0, column=0, columnspan=2, pady=(0, 3))

            lbl1 = tk.Label(setFrame, text="", width=6, relief="solid")
            lbl2 = tk.Label(setFrame, text="", width=6, relief="solid")
            lbl1.grid(row=1, column=0, padx=2)
            lbl2.grid(row=1, column=1, padx=2)

            type1Label = tk.Label(setFrame, text="")
            type1Label.grid(row=2, column=0, columnspan=2, pady=3)

            self.dynamicSets.append((lbl1, lbl2, type1Label))
        #Update Button 
        self.endButton = tk.Button(self, text="Next", command=self.onSubmit)
        self.endButton.pack(pady=15)

        self.pressCount = 0

        if self.cardList:
            self.loadCards()
        if self.oddsList:
            self.loadOdds(0) 

    #Functions that update the labels
    def loadCards(self):
        for i in range(5):
            self.topLabels[i].config(text=self.cardList[0][i])

        for i, setData in enumerate(self.cardList[1:]):
            lbl1, lbl2, _ = self.dynamicSets[i]
            lbl1.config(text=setData[0])
            lbl2.config(text=setData[1])

    def loadOdds(self, index):
        if index >= len(self.oddsList):
            self.endButton.config(state="disabled")
            return

        oddsRow = self.oddsList[index]
        if len(oddsRow) < len(self.dynamicSets) + 1:
            print(f"Warning: oddsRow too short: {oddsRow}")
            return

        self.topType1.config(text=oddsRow[0])


        for i, (_, _, type1Label) in enumerate(self.dynamicSets):
            type1Label.config(text=oddsRow[i + 1]) 

    def onSubmit(self):
        if self.pressCount == 0:
            for i in range(3):
                self.topLabels[i].grid()
        elif self.pressCount == 1:
            self.topLabels[3].grid()
        elif self.pressCount == 2:
            self.topLabels[4].grid()



        self.loadOdds(self.pressCount + 1)

        self.pressCount += 1
