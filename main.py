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

from todo.task import *

icon_path = "data\\img\\icon.ico"

class ToDoManager(tk.Tk):
    def __init__(self):
        """
        Builds a To-Do Manager widget
        """
        super().__init__() # Calling Parent class constructor

        #-------------------------------------------------------------------------------
        #                           ROOT WINDOW CONFIGURATION
        #-------------------------------------------------------------------------------
        
        geometry = "750x700"
        maxsize = (800, 750) # Width, Height
        minsize = (700, 650) # Width, Height

        self.title("To-Do")
        self.iconbitmap(icon_path)
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
        self.__bind_events()
        self.mainloop()
    
    def __task_input_dialog(self):
        """
        Creates a tool Toplevel window to prompt user to type new task into the provided entry widget
        """

        new_task_manager = NewTaskManager(self)
        new_task_manager.window.grab_set() # Prevents any further action within main window

        while new_task_manager.task_value == None:
            # Updates window if user is yet to input value. Breaks if tool window is destroyed or if user enters a value
            self.update() # Ensures root window doesn't start hanging

        new_task = new_task_manager.task_value #  Task input from the task Dialog is no longer empty, it is either 

        new_task_manager.window.destroy()

        if new_task:
            return new_task
        else: 
            return None

    def __add_task(self):
        """
        Adds new task to Tasks Listbox
        """
        new_task_input = self.__task_input_dialog()
        if (new_task_input):

            number_of_tasks = len(self.ongoing_task_items)
            self.ongoing_task_items.append(f"{number_of_tasks+1}. {new_task_input}")
            self.ongoing_task_var.set(
                self.ongoing_task_items
            )

    def __delete_task(self):
        """
        Deletes task selected from the Listbox
        """
        print(
            
        )
    def __edit_task(self):
        """
        Prompts user to edit selected task
        """
        pass

    def __build_components(self):
        """
        Builds GUI required components and places them into root window
        """

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
            "ipadx" : 15, "ipady" : 15, "padx" : 1.5, "sticky" : "ne", 
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
        self.tasks_listbox = Listbox(self, listvariable=self.ongoing_task_var, font=("Helvetica", 12))
        self.tasks_listbox.grid(
            column=0, row=1, sticky="w", ipadx=255, ipady=85, padx=1.5, columnspan=4, 
        )

        completed_task_label = Label(self, text="COMPLETED")
        completed_task_label.grid(
            column=0, row=2, **label_grid_options
        )
        completed_task_listbox = Listbox(self, listvariable=self.completed_task_var)
        completed_task_listbox.grid(
            column=0, row=3, sticky="w", ipadx=265, ipady=50, padx=1.5, columnspan=4,
        )

        #---------------------------------------------------------------------------------
        #                               BUTTONS
        #---------------------------------------------------------------------------------
        button_frame = Frame(self, cursor="dot", width=100, height=200)
        button_frame.grid(
            column=4, row=1, sticky="nw",
        )

        add_button = Button(button_frame, text="add task", command=self.__add_task)
        add_button.grid(
            column=0, row=0, **button_grid_options
        )

        edit_button = Button(button_frame, text="edit task", command=lambda: print("Edit button pressed"))
        edit_button.grid(
            column=0, row=1, **button_grid_options
        )

        remove_button = Button(button_frame, text="remove task", command=lambda: print("Remove button pressed"))
        remove_button.grid(
            column=0, row=2, **button_grid_options
        )

        check_button = Button(button_frame, text="completed", command=lambda: print("Check button pressed"))
        check_button.grid(
            column=0, row=3, **button_grid_options
        )

    def __bind_events(self):
        #--------------------------------------------------------------------------------
        #                               ROOT WINDOW
        # -------------------------------------------------------------------------------
        self.bind(
            "<Control-w>", lambda event=None: self.destroy()
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy()
        )
        self.bind(
            "<Control-n>", lambda event=None: self.__add_task()
        )
        self.bind(
            "<Control-n>", lambda event=None: self.__add_task()
        )
        
ToDoManager()