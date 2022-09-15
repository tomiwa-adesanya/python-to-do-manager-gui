from tkinter import ttk
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

        

        #-----------------------------------------------------------------
        self.__build_components()
        self.__bind_events()

    def __build_components(self):
        """
        Builds and places required widgets within Toplevel tool window
        """
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
        new_task.focus()

        #-------------------------------------------------------------------
        #                           BUTTON
        #-------------------------------------------------------------------
        add_button = Button(self.window, text="add", command=self.__update_task_value)
        add_button.grid(
            column=1, row=1, sticky="e", ipadx=10, ipady=5
        )

    def __bind_events(self):

        self.window.bind(
            "<Destroy>",lambda event=None: self.__window_destroyed()
        ) # 
        self.window.bind(
            "<Return>", lambda event=None: self.__update_task_value()
        )
        self.window.bind(
            "<Control-w>",lambda event=None: self.window.destroy()
        ) # 
        self.window.bind(
            "<Control-W>",lambda event=None: self.window.destroy()
        ) # 
    
    def __update_task_value(self):
        """
        Updates the value of the task_value attribute that stores the raw string input from entry. Invoked by the add button
        """
        self.task_value = self.new_task_var.get()
        
    def __window_destroyed(self):
        """
        Updates the value of the task_value attribute to an empty string if window is closed before clicking add button
        """
        self.task_value = ""