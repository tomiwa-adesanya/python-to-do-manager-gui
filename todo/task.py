from tkinter import ttk
from os import remove, path
import tkinter as tk

class NewTaskManager():

    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.task_value = None
        #-----------------------------------------------------------------
        #                ROOT WINDOW CONFIGURATIONS
        #-----------------------------------------------------------------
        self.window.title("Add task")
        self.window.geometry("450x100")
        self.window.resizable(False, False)
        self.window.attributes("-toolwindow", True)
        self.window.attributes("-alpha", 0.95)

        self.window.bind(
            "<Destroy>",lambda event=None: self._window_destroyed()
        ) # 

        #-----------------------------------------------------------------
        self.__build_components()

    def __build_components(self):
        Button = ttk.Button 
        Entry = ttk.Entry
        Label = ttk.Label

        StringVar = tk.StringVar

        self.new_task_var = StringVar()

        #-----------------------------------------------------------------
        #                        LABEL AND ENTRY
        #-----------------------------------------------------------------
        new_task_label = Label(self.window, text="Add task:", font=("Helvetica", 12))
        new_task_label.grid(
            column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="w"
        )
        new_task = Entry(self.window, textvariable=self.new_task_var, font=("Helvetica", 12))
        new_task.grid(
            column=1, row=0, ipadx=75, ipady=5, pady=5
        )

        #-------------------------------------------------------------------
        #                           BUTTON
        #-------------------------------------------------------------------
        add_button = Button(self.window, text="add", command=self.__update_task)
        add_button.grid(
            column=1, row=1, sticky="e", ipadx=10, ipady=5
        )
    
    def __update_task(self):
        self.task_value = self.new_task_var.get()
        
    def _window_destroyed(self):
        self.task_value = ""