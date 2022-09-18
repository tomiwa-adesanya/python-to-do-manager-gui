""" PYTHON GUI PROJECT
    ABOUT: A task/to-do list manager GUI that enables users to add, remove, edit and check completed tasks
    AUTHOR: Tomiwa G. Adesanya<t.g.adesanya392@gmail.com>
"""

from threading import Thread
from tkinter.messagebox import showerror
from todo.task import *

try:
    from playsound import playsound
except(ModuleNotFoundError):
    playsound = lambda void_arg: ""


icon_path = "data\\img\\icon.ico"
tone_path = "data\\audio\\tone.mp3"

beep_tone = lambda : Thread(target=playsound, kwargs={"sound":tone_path}).start()

class ToDoManagerGUI(tk.Tk):
    def __init__(self):
        """
        Builds a To-Do Manager GUI
        """
        super().__init__() # Calling Parent class constructor

        #-------------------------------------------------------------------------------
        #                           ROOT WINDOW CONFIGURATION
        #-------------------------------------------------------------------------------
        
        geometry = "800x750+0+0"
        opaque_level = 0.95
        maxsize = (800, 750) # Width, Height
        minsize = (750, 700) # Width, Height

        self.title("To Do Manager")
        self.iconbitmap(icon_path)
        self.geometry(geometry)
        self.maxsize(*maxsize)
        self.minsize(*minsize)
        self.attributes("-alpha", opaque_level)

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.columnconfigure(index=3, weight=1)
        self.columnconfigure(index=4, weight=1)

        self.index_error_response = lambda action: showerror("select task", message=f"Please select task to {action}")
        
        #------------------------------------------------------------------------------
        self.__build_components()
        self.__bind_events()
        self.mainloop()
    
    def __clear_completed_task(self) -> None: 
        """
        Clears all completed tasks from the completed tasks Listbox
        """
        self.completed_task_items = []
        self.completed_task_var.set(
            self.completed_task_items
        )

    def __task_input_window(self, task_edit_window: bool=False, task_value: str="") -> str | None:
        """
        Creates a Toplevel tool window to prompt user to type new task into the provided entry widget, or edit selected task.
        Arguments:
            `task_edit_window`: bool -> specifies toolwindow built should be for the purpose of editing task rather than entering a new task.
            `task_value1`: str -> specifies the initial value to insert into a task edit tool window for user to edit.
        """

        if (not task_edit_window):
            _task_manager = NewTaskManager(self)
            _task_manager.window.grab_set() # Prevents any further action within main window

        else: 
            _task_manager = EditTaskManager(self, task_value)
            _task_manager.window.grab_set()

        while _task_manager.task_value == None:
            # Updates window if user is yet to input value. Breaks if tool window is destroyed or if user enters a value
            self.update() # Ensures root window doesn't start hanging

        new_task = _task_manager.task_value #  Task input into the task window has been added or destroyed

        _task_manager.window.destroy()

        if new_task:
            return new_task
            
        else: 
            return None

    def __add_task(self, _completed: bool=False) -> None:
        """
        Adds tasks to either Ongoing tasks or completed tasks.
        Arguments:
            `completed`: bool -> specifies task should be added to Completed tasks ListBox if True
        """

        if (not _completed):
            new_task_input = self.__task_input_window() # Creates new tool window with entry for user to type in new task to add

            if (new_task_input):
                number_of_ongoing_tasks = len(self.ongoing_task_items)
                self.ongoing_task_items.append(f"{number_of_ongoing_tasks+1}. {new_task_input}")
                self.ongoing_task_var.set(
                    self.ongoing_task_items
                ) # Updates list of ongoing task

        else:
            number_of_completed_tasks = len(self.completed_task_items)
            _completed_task = self.__delete_task() # Removes task from Ongoing task before adding it to completed tasks
            completed_task = " ".join(
                _completed_task.split()[1:]
            ) # Removes the index added to task str, e.g "1. study python" becomes "study python", with "1." removed
            self.completed_task_items.append(
                f"{number_of_completed_tasks+1}. {completed_task}"
            )
            self.completed_task_var.set(
                self.completed_task_items
            ) # Updates list of tasks
            beep_tone() # Plays out tone.mp3 audio file
            self.update() # Updates GUI window
    def add_task(self, completed: bool=False):
        """
        Adds new task to list of ongoing tasks or list of completed task(if `completed` is `True`). 
        Displays an error message if an error is encountered while trying to edit a task.
        """
        try:
            self.__add_task(completed)
        except (IndexError): 
            self.index_error_response("mark as completed")
            
    def __delete_task(self) -> str:
        """
        Removes selected ongoing task on Listbox and returns the removed task. 
        """

        selected_task_index = self.ongoing_tasks_listbox.curselection()[0] # index of selected Task on Listbox to be deleted
        ongoing_tasks = self.ongoing_task_items.copy() 
        removed_item = ongoing_tasks.pop(selected_task_index)
        ongoing_tasks = [
           " ".join(task.split()[1:]) for task in ongoing_tasks
        ]
        new_ongoing_task = [ ]

        for task_id, task in enumerate(ongoing_tasks): 
            new_ongoing_task.append(
                f"{task_id+1}. {task}"
            )

        self.ongoing_task_items = new_ongoing_task 
        self.ongoing_task_var.set(
            self.ongoing_task_items
        )

        return removed_item
    def delete_task(self):
        """
        Deletes task from list of ongoing tasks. 
        Shows an error message if no task is selected and the `delete` button is clicked on the GUI
        """
        try:
            self.__delete_task()
        except(IndexError):
            self.index_error_response("delete")

    def __edit_task(self) -> None:
        """
        Creates tool window to prompt users to edit selected ongoing task
        """

        selected_task_index = self.ongoing_tasks_listbox.curselection()[0]
        selected_task = self.ongoing_task_items[selected_task_index].split()[1:]

        new_task_input = self.__task_input_window(True, selected_task)

        if (new_task_input):
            self.ongoing_task_items[selected_task_index] = f"{selected_task_index+1}. {new_task_input}"
            self.ongoing_task_var.set(
                self.ongoing_task_items
            )
    def edit_task(self):
        """
        Edits selected task from the list of ongoing tasks
        Shows an error message if the `edit` button is clicked without selecting task to be edited
        """
        try:
            self.__edit_task()
        except(IndexError):
            self.index_error_response("to be edited")

    def __build_components(self) -> None:
        """
        Builds GUI required components and places them into root window
        """

        Button = ttk.Button
        Frame = ttk.Frame
        Label = ttk.Label
        Listbox = tk.Listbox
        Variable = tk.Variable

        #-------------------------------------------------------------------------------
        #               Default Widget Options and Variables
        #-------------------------------------------------------------------------------
        
        label_font = (
            "Helvetica", 10
        )
        listbox_font = (
            "Helvetica", 12
        )

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
        ongoing_tasks_label = Label(self, text="ONGOING TASKS", font=label_font)
        ongoing_tasks_label.grid(
            column=0, row=0, **label_grid_options
        )
        self.ongoing_tasks_listbox = Listbox(self, listvariable=self.ongoing_task_var, selectmode="single", font=listbox_font)
        self.ongoing_tasks_listbox.grid(
            column=0, row=1, sticky="w", ipadx=255, ipady=85, padx=1.5, columnspan=4, 
        )

        completed_task_label = Label(self, text="COMPLETED TASKS", font=label_font)
        completed_task_label.grid(
            column=0, row=2, **label_grid_options
        )
        completed_task_listbox = Listbox(self, listvariable=self.completed_task_var, state="disabled", font=listbox_font)
        completed_task_listbox.grid(
            column=0, row=3, sticky="w", ipadx=265, ipady=50, padx=1.5, columnspan=4,
        )

        #---------------------------------------------------------------------------------
        #                               BUTTONS
        #---------------------------------------------------------------------------------
        button_frame = Frame(self, width=100, height=200, cursor="dot")
        button_frame.grid(
            column=4, row=1, sticky="nw", ipadx=1.5
        )

        add_button = Button(button_frame, text="add task", command=self.__add_task)
        add_button.grid(
            column=0, row=0, **button_grid_options
        )

        edit_button = Button(button_frame, text="edit task", command=lambda: self.edit_task())
        edit_button.grid(
            column=0, row=1, **button_grid_options
        )

        remove_button = Button(button_frame, text="remove task", command=lambda: self.delete_task())
        remove_button.grid(
            column=0, row=2, **button_grid_options
        )

        check_button = Button(button_frame, text="completed", command=lambda: self.add_task(True))
        check_button.grid(
            column=0, row=3, **button_grid_options
        )

        clear_button = Button(
            self, text="clear", command=self.__clear_completed_task
        )
        clear_button.grid(
            column=4, row=3, sticky="nw", ipadx=15, ipady=15
        )

    def __bind_events(self) -> None:
        """
        Binds events to GUI widgets
        """
        #--------------------------------------------------------------------------------
        #                               ROOT WINDOW
        # -------------------------------------------------------------------------------
        self.bind(
            "<Control-w>", lambda event=None: self.destroy(), add="+"
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy(), add="+"
        )
        self.bind(
            "<Control-n>", lambda event=None: self.__add_task(), add="+"
        )
        self.bind(
            "<Control-N>", lambda event=None: self.__add_task(), add="+"
        )
        self.bind(
            "<Control-Shift-d>", lambda event=None: self.__delete_task(), add="+"
        )
        self.bind(
            "<Control-Shift-D>", lambda event=None: self.__delete_task(), add="+"
        )
        
        
ToDoManagerGUI()