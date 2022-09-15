"""
This is a listbox project to create a to do list app manager

REQUIRED WIDGETS:
    *** Button:
        > Add task button
        > Remove task button
        > Check task button
        > Edit task button
    *** Listbox:
        > Just one main list box with "single" select mode
    *** Scrollbar:
        > Horizontal
        > Vertical
    *** Frame:
        > To arrange the Listbox and Scrollbars together
    *** Labels:
        > To display information
"""



from tkinter import ttk
from os import remove, path
from todo.task import Tasks
import tkinter as tk

class ToDoManager(tk.Tk):
    def __init__(self):
        super().__init__() # Calling Parent class constructor

        #-------------------------------------------------------------------------------
        #                           ROOT WINDOW CONFIGURATION
        #-------------------------------------------------------------------------------
        
        geometry = "750x700"
        maxsize = (800, 750) # Width, Height
        minsize = (700, 650) # Width, Height

        self.geometry(geometry)
        self.maxsize(*maxsize)
        self.minsize(*minsize)
        self.attributes("-alpha", 0.95)

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.columnconfigure(index=3, weight=1)
        self.columnconfigure(index=4, weight=1)
        
        #------------------------------------------------------------------------------
        self.__build_components()
        self.__event_binding()
        self.mainloop()
    
    def __add_task(self):
        pass

    def __delete_task(self):
        pass
    def __edit_task(self):
        pass

    def __build_components(self):

        Button = ttk.Button
        Frame = ttk.Frame
        Label = ttk.Label
        Listbox = tk.Listbox
        Scrollbar = ttk.Scrollbar
        Variable = tk.Variable

        #-------------------------------------------------------------------------------
        #               Default Widget Options and Variables
        #-------------------------------------------------------------------------------
        
        label_grid_options = {
            "ipadx" : 5, "ipady" : 5, "padx" : 1.5, "pady" : 1.5, "sticky" : "w"
        } 
        button_grid_options = {
            "ipadx" : 17.5, "ipady" : 15, "padx" : 1.5, "sticky" : "ne"
        }

        self.ongoing_task_items = []
        self.completed_task_items = []
        self.ongoing_task_var = Variable(value=self.ongoing_task_items)
        self.completed_task_var = Variable(value=self.completed_task_items)
    
        #-------------------------------------------------------------------------------
        #                        LABELS AND LISTBOXES
        #--------------------------------------------------------------------------------
        tasks_label = Label(self, text="TASKS")
        tasks_label.grid(
            column=0, row=0, **label_grid_options
        )
        tasks_listbox = Listbox(self, listvariable=self.ongoing_task_var)
        tasks_listbox.grid(
            column=0, sticky="w", ipadx=255, ipady=85, padx=1.5, columnspan=4, 
        )

        completed_task_label = Label(self, text="COMPLETED")
        completed_task_label.grid(
            column=0, row=2, **label_grid_options
        )
        completed_task_listbox = Listbox(self, listvariable=self.completed_task_var)
        completed_task_listbox.grid(
            column=0, row=3, sticky="w", ipadx=255, ipady=50, padx=1.5, columnspan=4,
        )

        #---------------------------------------------------------------------------------
        #                               BUTTONS
        #---------------------------------------------------------------------------------
        button_frame = Frame(self, cursor="dot", width=100, height=200)
        button_frame.grid(
            column=4, row=1, sticky="nw", padx=1.5, pady=1.5
        )

        add_button = Button(button_frame, text="add task", command=self.__add_task)
        add_button.grid(
            column=0, row=0, **button_grid_options
        )

        edit_button = Button(button_frame, text="edit task")
        edit_button.grid(
            column=0, row=1, **button_grid_options
        )

        remove_button = Button(button_frame, text="remove task")
        remove_button.grid(
            column=0, row=2, **button_grid_options
        )

        check_button = Button(button_frame, text="completed")
        check_button.grid(
            column=0, row=3, **button_grid_options
        )

    def __event_binding(self):

        #--------------------------------------------------------------------------------
        #                               ROOT WINDOW
        # -------------------------------------------------------------------------------
        self.bind(
            "<Control-w>", lambda event=None: self.destroy()
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy()
        )
        
        

        
        
        

ToDoManager()