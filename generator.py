from Tkinter import *
import tkMessageBox
from ttk import *

from nationalities import core_nationalities

class The7thSeaCharacterGenerator(object):
    def __init__(self):
        self.SOURCES = []
        self.nationalities = []
        for item in core_nationalities:
            self.nationalities.append(item['nationality'])

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
        self.select_from.grid(row=0, rowspan=2, column=0)
        add_button.grid(row=0, column=1)
        remove_button.grid(row=1, column=1)
        self.selected.grid(row=0, rowspan=2, column=2)
        okay_button.grid(row=2, column=2)
        self.source_select.mainloop()
    
    def character_generator(self):
        root = Tk()
        root.wm_title("7th Sea Character Generator")
        character_tabs = Notebook(root)
        page = Frame(character_tabs, height=5, width=5)
        generation_tabs = Notebook(page)
        general = PanedWindow(generation_tabs, orient=HORIZONTAL)
        info_pane = Frame(general)
        info_frame=Labelframe(info_pane, text='Character Info')
        name_label = Label(info_frame, text='Name:')
        name_var = StringVar()
        name_var.set('Unnamed Character 1')
        name_box = Entry(info_frame, textvariable=name_var)
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
        traits_label = Label(trait_frame, text='Trait')
        final_score_label = Label(trait_frame, text='Final Score')
        base_score_label = Label(trait_frame, text='Base Score')
        brawn_label = Label(trait_frame, text='Brawn')
        finesse_label = Label(trait_frame, text='Finesse:')                                       
        resolve_label = Label(trait_frame, text='Resolve:')                                       
        wits_label = Label(trait_frame, text='Wits:')                                             
        panache_label = Label(trait_frame, text='Panache:')                                       
        traits_label.grid(row=0, column=0)                                                        
        final_score_label.grid(row=0, column=1)                                                   
        base_score_label.grid(row=0, column=2)                                                    
        brawn_label.grid(row=1, column=0)                                                         
        finesse_label.grid(row=2, column=0)                       
        resolve_label.grid(row=3, column=0)                       
        wits_label.grid(row=4, column=0)                          
        panache_label.grid(row=5, column=0)                       
        trait_frame.pack()                                        
        general.add(trait_pane)                                   
        advantages = Frame(generation_tabs)                       
        skills = Frame(generation_tabs)                           
        generation_tabs.add(general, text='General')              
        generation_tabs.add(advantages, text='Advantages')        
        generation_tabs.add(skills, text='Skills')                
        generation_tabs.pack()                                    
        character_tabs.add(page, text=name_var.get())           
        character_tabs.pack()                    
        root.mainloop()