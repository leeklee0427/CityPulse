from tkinter import *
import tkinter.messagebox


# Main application window
root = Tk()
root.geometry("800x600")
root.title("CityPulse - City Recommendation System")

# Function placeholders
def recommendForYoungProfessionals():
    # create new window
    newWindow = Toplevel(root)
    newWindow.title("Recommendations for Young Professionals and Graduates")
    newWindow.geometry("700x350")

    # create label in new window
    lblcondition1 = Label(newWindow, text="condition 1")
    lblcondition1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    lblcondition2 = Label(newWindow, text="condition 2")
    lblcondition2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    lblcondition3 = Label(newWindow, text="condition 3")
    lblcondition3.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    lblcondition4 = Label(newWindow, text="condition 4")
    lblcondition4.grid(row=3, column=0, padx=10, pady=10, sticky=W)

    lblcondition5 = Label(newWindow, text="condition 5")
    lblcondition5.grid(row=4, column=0, padx=10, pady=10, sticky=W)

    lblcondition6 = Label(newWindow, text="condition 6")
    lblcondition6.grid(row=5, column=0, padx=10, pady=10, sticky=W)

    # create checkbutton
    check1 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    check2 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    check3 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    check4 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check4.grid(row=3, column=1, padx=10, pady=10, sticky=W)

    check5 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check5.grid(row=4, column=1, padx=10, pady=10, sticky=W)

    check6 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check6.grid(row=5, column=1, padx=10, pady=10, sticky=W)

def recommendForRemoteWorkers():
    # create new window
    newWindow = Toplevel(root)
    newWindow.title("Recommendations for Remote Workers")
    newWindow.geometry("700x350")

    # create label in new window
    lblcondition1 = Label(newWindow, text="condition 1")
    lblcondition1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    lblcondition2 = Label(newWindow, text="condition 2")
    lblcondition2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    lblcondition3 = Label(newWindow, text="condition 3")
    lblcondition3.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    lblcondition4 = Label(newWindow, text="condition 4")
    lblcondition4.grid(row=3, column=0, padx=10, pady=10, sticky=W)

    lblcondition5 = Label(newWindow, text="condition 5")
    lblcondition5.grid(row=4, column=0, padx=10, pady=10, sticky=W)

    lblcondition6 = Label(newWindow, text="condition 6")
    lblcondition6.grid(row=5, column=0, padx=10, pady=10, sticky=W)

    # create checkbutton
    check1 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    check2 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    check3 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    check4 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check4.grid(row=3, column=1, padx=10, pady=10, sticky=W)

    check5 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check5.grid(row=4, column=1, padx=10, pady=10, sticky=W)

    check6 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check6.grid(row=5, column=1, padx=10, pady=10, sticky=W)


def recommendForRetiredWorkers():
    # create new window
    newWindow = Toplevel(root)
    newWindow.title("Recommendations for Retired Workers")
    newWindow.geometry("700x350")

    # create label in new window
    lblcondition1 = Label(newWindow, text="condition 1")
    lblcondition1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    lblcondition2 = Label(newWindow, text="condition 2")
    lblcondition2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    lblcondition3 = Label(newWindow, text="condition 3")
    lblcondition3.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    lblcondition4 = Label(newWindow, text="condition 4")
    lblcondition4.grid(row=3, column=0, padx=10, pady=10, sticky=W)

    lblcondition5 = Label(newWindow, text="condition 5")
    lblcondition5.grid(row=4, column=0, padx=10, pady=10, sticky=W)

    lblcondition6 = Label(newWindow, text="condition 6")
    lblcondition6.grid(row=5, column=0, padx=10, pady=10, sticky=W)

    # create checkbutton
    check1 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    check2 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    check3 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    check4 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check4.grid(row=3, column=1, padx=10, pady=10, sticky=W)

    check5 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check5.grid(row=4, column=1, padx=10, pady=10, sticky=W)

    check6 = Checkbutton(newWindow, text="Add", onvalue=1, offvalue=0, width=20, anchor=NW)
    check6.grid(row=5, column=1, padx=10, pady=10, sticky=W)

# Frame for centering buttons
centerFrame = Frame(root)
centerFrame.pack(expand=True)

# Buttons
btnYoungProfessionals = Button(centerFrame, text='Young Professionals and Graduates', command=recommendForYoungProfessionals)
btnYoungProfessionals.pack(pady=10)

btnRemoteWorkers = Button(centerFrame, text='Remote Workers', command=recommendForRemoteWorkers)
btnRemoteWorkers.pack(pady=10)

btnRetiredWorkers = Button(centerFrame, text='Retired Workers', command=recommendForRetiredWorkers)
btnRetiredWorkers.pack(pady=10)

root.mainloop()

