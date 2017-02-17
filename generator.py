from Tkinter import *
import tkMessageBox
from ttk import *

from nationalities import core_nationalities

TRAITS = ['Brawn', 'Finesse', 'Resolve', 'Wits', 'Panache']
SKILLS = ['Aim', 'Athletics', 'Brawl', 'Convince', 'Empathy', 'Hide', 'Intimidate', 'Notice',
          'Perform', 'Ride', 'Sailing', 'Scholarship', 'Tempt', 'Theft', 'Warfare', 'Weaponry']
TRAIT_PANE_LABELS = ['Trait:', 'Final Score', 'Base Score']

class The7thSeaCharacterGenerator(object):
    def __init__(self):
        self.unnamed_characters = 0
        self.SOURCES = []
        self.nationalities = ["Choose One"]
        for item in core_nationalities:
            self.nationalities.append(item['nationality'])
        self.base_trait_points = 2
        self.name_vars = {}

    def run(self):
        self.select_sources()
        self.update_nationalities()
        self.character_generator()

    def update_nationalities(self):
        if 'Pirate Nations' in self.SOURCES:
            from nationalities import pirate_nationalities
            for item in pirate_nationalities:
                self.nationalities.append(item['nationality'])

    def add_source(self):
        if not self.select_from.get(self.select_from.curselection()) in self.selected.get(0, END):
            self.selected.insert(END, self.select_from.get(self.select_from.curselection()))

    def remove_source(self):
        if not self.selected.curselection() == (0,):
            self.selected.delete(ANCHOR)
            self.selected.pack()
        else:
            tkMessageBox.showinfo('Oops!', 'You cannot remove the Core Rulebook from sources')

    def source_done(self):
        self.SOURCES = self.selected.get(0, END)
        self.source_select.destroy()

    def add_all_sources(self):
        choices = self.select_from.get(0, END)
        if choices not in self.selected.get(1, END):
            for choice in choices:
                self.selected.insert(END, choice)

    def remove_all_sources(self):
        self.selected.delete(1, END)

    def select_sources(self):
        self.source_select = Tk()
        self.source_select.wm_title("Select Sources")
        self.select_from = Listbox(self.source_select)
        for item in ['Heroes and Villains', 'Pirate Nations']:
            self.select_from.insert(END, item)
        self.selected = Listbox(self.source_select)
        self.selected.insert(0, 'Core Rulebook')
        add_button = Button(self.source_select, text='Add >', command=self.add_source)
        remove_button = Button(self.source_select, text='< Remove', command=self.remove_source)
        okay_button = Button(self.source_select, text='Done', command=self.source_done)
        add_all_button = Button(self.source_select, text='Add All >>', command=self.add_all_sources)
        remove_all_button = Button(self.source_select, text='<< Remove All', command=self.remove_all_sources)
        self.select_from.grid(row=0, rowspan=4, column=0)
        add_button.grid(row=0, column=1)
        add_all_button.grid(row=1, column=1)
        remove_all_button.grid(row=2, column=1)
        remove_button.grid(row=3, column=1)
        self.selected.grid(row=0, rowspan=4, column=2)
        okay_button.grid(row=4, column=2)
        self.source_select.mainloop()

    def make_root(self):
        self.root = Tk()
        self.root.wm_title("7th Seas Character Generator")

    def make_character_tabs(self):
        self.character_tabs = Notebook(self.root)

    def make_new_character(self):
        page = Frame(self.character_tabs)
        generator_tabs = Notebook(page)
        name_var_key = 'name_var{0}'.format(self.unnamed_characters + 1)
        self.name_vars.update({name_var_key: StringVar()})
        self.name_vars[name_var_key].set("Unnamed Characters {0}".format(self.unnamed_characters + 1))
        self.unnamed_characters += 1
        self.make_general_tab(generator_tabs, name_var_key)
        self.make_advantages_tab(generator_tabs)
        self.make_skills_tab(generator_tabs)
        generator_tabs.pack()
        self.character_tabs.add(page, text=self.name_vars[name_var_key].get())
        self.character_tabs.pack()
        self.character_tabs.select(self.unnamed_characters - 1)

    def make_general_tab(self, notebook, name_var_key):
        general = PanedWindow(notebook, orient=HORIZONTAL)
        info_pane = Frame(general)
        info_frame = Labelframe(info_pane, text='Character Info')
        name_label = Label(info_frame, text='Name:')
        name_box = Entry(info_frame, textvariable=self.name_vars[name_var_key])
        player_label = Label(info_frame, text='Player:')
        player_box = Entry(info_frame)
        nation_label = Label(info_frame, text='Nationality:')
        nationality_var = StringVar(info_frame)
        nationality_var.set("Choose One")
        nationalities = apply(OptionMenu, (info_frame, nationality_var) + tuple(self.nationalities))
        name_label.grid(row=0, column=0, sticky=W)
        name_box.grid(row=0, column=1, sticky=E)
        player_label.grid(row=1, column=0, sticky=W)
        player_box.grid(row=1, column=1, sticky=E)
        nation_label.grid(row=2, column=0, sticky=W)
        nationalities.grid(row=2, column=1, sticky=E)
        info_frame.pack()
        general.add(info_pane)
        trait_pane = Frame(general)
        trait_frame = Labelframe(trait_pane, text='Traits')
        for i in range(len(TRAIT_PANE_LABELS)):
            Label(trait_frame, text=TRAIT_PANE_LABELS[i]).grid(row=0, column=i)
        for i in range(len(TRAITS)):
            Label(trait_frame, text=TRAITS[i]).grid(row=i + 1, column=0, sticky=W)
        trait_frame.pack()
        general.add(trait_pane)
        notebook.add(general, text='General')

    def make_advantages_tab(self, notebook):
        advantages = Frame(notebook)
        notebook.add(advantages, text='Advantages')

    def make_skills_tab(self, notebook):
        skills = Labelframe(notebook, text='Skills')
        for i in range(len(SKILLS)):
            Label(skills, text=SKILLS[i]).grid(row=i, column=0, sticky=W)
        notebook.add(skills, text='Skills')

    def make_menu_pane(self):
        menu_pane = Frame(self.root)
        new_button = Button(menu_pane, text='New', command=self.make_new_character)
        new_button.pack(side=LEFT)
        menu_pane.pack()

    def character_generator(self):
        self.make_root()
        self.make_menu_pane()
        self.make_character_tabs()
        self.make_new_character()
        self.root.mainloop()
