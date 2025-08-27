import game
import tkinter as tk
from tkinter import simpledialog, messagebox
from myinterface import App



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    num_sets = simpledialog.askinteger("Input", "Enter a number (2-8):", parent=root, minvalue=2, maxvalue=8)
    if num_sets is None:
        messagebox.showinfo("Exit", "No number entered. Exiting.", parent=root)
        root.destroy()
        exit()
    root.destroy()
    cardList, oddsList = game.getOdds(num_sets)
    for row in oddsList:
        for i in range(len(row)):
            row[i] = f"{row[i]}%"


    print(cardList)
    print(oddsList)

    app = App(numSets=num_sets, cardList=cardList, oddsList=oddsList)
    app.mainloop()
