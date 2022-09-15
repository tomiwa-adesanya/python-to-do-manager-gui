from tkinter import ttk
import tkinter as tk

class Tasks(tk.Tk): 
    def __init__(self):
        super().__init__() # Calling Parent class constructor
        #-----------------------------------------------------------------
        #                ROOT WINDOW CONFIGURATIONS
        #-----------------------------------------------------------------
        self.title("Add task")
        self.geometry("450x100")
        self.resizable(False, False)
        self.attributes("-toolwindow", True)
        self.attributes("-alpha", 0.95)

        #-----------------------------------------------------------------
        self.__build_components()
        self.mainloop()

    def __build_components(self):

        Button = ttk.Button 
        Entry = ttk.Entry
        Label = ttk.Label

        StringVar = tk.StringVar

        self.new_task_var = StringVar()

        #-----------------------------------------------------------------
        #                        LABEL AND ENTRY
        #-----------------------------------------------------------------
        new_task_label = Label(self, text="Add task:", font=("Helvetica", 12))
        new_task_label.grid(
            column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="w"
        )
        new_task = Entry(self, textvariable=self.new_task_var, font=("Helvetica", 12))
        new_task.grid(
            column=1, row=0, ipadx=75, ipady=5, pady=5
        )

        #-------------------------------------------------------------------
        #                           BUTTON
        #-------------------------------------------------------------------
        add_button = Button(self, text="add", command=self._add_task)
        add_button.grid(
            column=1, row=1, sticky="e", ipadx=10, ipady=5
        )
    
    def _add_task(self):
        self.destroy()

if __name__ == "__main__":
    Tasks()