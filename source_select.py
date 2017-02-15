from Tkinter import *
import tkMessageBox
from ttk import *

def select_sources():
    def add_source():
        if not select_from.get(select_from.curselection()) in selected.get(0, END):
            selected.insert(END, select_from.get(select_from.curselection()))

    def remove_source():
        if not selected.curselection() == (0,):
            selected.delete(ANCHOR)
            selected.pack()
        else:
            tkMessageBox.showinfo('Oops!', 'You cannot remove the Core Rulebook from sources')

    def source_done():
        global SOURCES
        SOURCES = selected.get(0, END)
        source_select.destroy()

    source_select = Tk()
    source_select.wm_title("Select Sources")
    select_from = Listbox(source_select)
    for item in ['Heroes and Villains', 'Pirate Nations']:
        select_from.insert(END, item)
    selected = Listbox(source_select)
    selected.insert(0, 'Core Rulebook')
    add_button = Button(source_select, text='Add >', command=add_source)
    remove_button = Button(source_select, text='< Remove', command=remove_source)
    okay_button = Button(source_select, text='Done', command=source_done)
    select_from.grid(row=0, rowspan=2, column=0)
    add_button.grid(row=0, column=1)
    remove_button.grid(row=1, column=1)
    selected.grid(row=0, rowspan=2, column=2)
    okay_button.grid(row=2, column=2)
    source_select.mainloop()


