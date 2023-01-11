import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

class ff:
    def __init__(self, program_name, rev, main_menu):
        # GLOBAL VALUES
        self.console_line_number = 0
        self.form_data = {}

        # CREATE GUI
        
        # main window
        self.root = tkinter.Tk()
        self.root.geometry("640x480")
        self.root.minsize(320,240)
        title = program_name+" v."+rev+" / ff 3.0"
        self.root.title(title)

        # main menu
        # frame
        frame = LabelFrame(self.root, text="Main Menu")
        frame.pack(expand=True, fill="both", padx=10, pady=10)
        # buttons
        for button in main_menu:
            btn = Button(frame, text=button[0], command=button[1])
            btn.pack(expand=True, fill="both", padx=10, pady=5)
        btn = Button(frame, text="SETTING", command=self.settings_display)
        btn.pack(expand=True, fill="both", padx=10, pady=5)

        # progress bar
        self.progress = ttk.Progressbar(frame, orient='horizontal', mode='determinate')
        self.progress.pack(expand=True, fill="both", padx=10, pady=5)
        # scrollbar for console
        console_frame = Frame(frame)
        console_frame.pack(expand=True, fill="both", padx=10, pady=5)
        vscrollbar = Scrollbar(console_frame, orient='vertical')
        vscrollbar.pack(side=RIGHT, fill='y')
        # console
        self.console = Text(console_frame, state=DISABLED, yscrollcommand=vscrollbar.set)
        self.console.pack(expand=True, fill="both")
        vscrollbar.config(command=self.console.yview) # attach scrollbar to console
        self.write(title+" is ready")
    
    def write(self, text):
        self.console_line_number += 1
        self.console.config(state=NORMAL)
        self.console.insert(END, str(self.console_line_number)+". "+text+"\n")
        self.console.config(state=DISABLED)
        self.console.see(END)

    def form(self, form_title, variables):
        # top window
        self.inputbox = Toplevel(self.root)
        self.inputbox.geometry("320x240")
        self.inputbox.minsize(320,240)
        self.inputbox.columnconfigure(0, weight=1)
        self.inputbox.rowconfigure(0, weight=1)

        # frame
        frame = LabelFrame(self.inputbox, text=form_title)
        frame.grid(sticky='nsew', padx=10, pady=10)
        frame.columnconfigure(0, weight=1)

        # enteries
        i = 0
        self.form_values = {}
        for var in variables:
            lbl = Label(frame, text=var+":")
            lbl.grid(column=0, row=i, sticky='w', padx=5)
            entr = Entry(frame)
            entr.grid(column=0, row=i+1, sticky='nsew', padx=5, pady=(0,5), columnspan=2)
            self.form_values[var] = entr
            i += 2

        # submit button
        btn = Button(frame, text="Submit", command=self.form_submit)
        btn.grid(column=0, sticky='nsew', row=i, padx=5, pady=5)
        # cancel button
        btn = Button(frame, text="Cancel", command=self.form_cancel)
        btn.grid(column=1, sticky='nsew', row=i, padx=5, pady=5)
    
    def form_submit(self):
        for key, value in self.form_values.items():
            self.form_data[key] = value.get()
        print(self.form_data)
        self.inputbox.destroy()
    
    def form_cancel(self):
        self.inputbox.destroy()

    def progress_bar_value_set(self, percent):
        self.progress['value'] = percent
    
    def progress_bar_value_get(self):
        return self.progress['value']
    
    def settings_display(self):
        # top window
        self.settings = Toplevel(self.root)
        self.settings.geometry("640x480")
        self.settings.minsize(320,240)
        self.settings.columnconfigure(0, weight=1)
        self.settings.rowconfigure(0, weight=1)
        title = "Settings"

        # frame
        frame = LabelFrame(self.settings, text="Settings")
        frame.grid(sticky='nsew', padx=10, pady=10)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        # enteries
        file = open("settings.txt", 'r')
        lines = file.readlines()
        file.close()
        i = 0
        self.settings_values = {}
        for line in lines:
            line = line.replace("\n", "")
            line = line.split(" --> ")
            lbl = Label(frame, text=line[0])
            lbl.grid(column=0, row=i, padx=5, pady=5)
            entr = Entry(frame)
            entr.grid(column=1, row=i, sticky='nsew', padx=5, pady=5, columnspan=2)
            entr.insert(END, line[1])
            self.settings_values[line[0]] = entr
            i += 1
        
        # save button
        btn = Button(frame, text="Save", command=self.settings_save)
        btn.grid(column=1, sticky='nsew', row=i, padx=5, pady=5)
        # cancel button
        btn = Button(frame, text="Cancel", command=self.settings_cancel)
        btn.grid(column=2, sticky='nsew', row=i, padx=5, pady=5)
    
    def settings_save(self):
        file = open("settings.txt", "w")
        for key, value in self.settings_values.items():
            file.write(key+" --> "+value.get()+"\n")
        file.close()
        self.settings.destroy()
    
    def settings_cancel(self):
        self.settings.destroy()

    def msg(self, text):
        tkinter.messagebox.showinfo(title="Info", message=text)
    
    def error(self, text):
        tkinter.messagebox.showerror(title="Error", message=text)
        self.exit()
    
    def run(self):
        self.root.mainloop()
    
    def exit(self):
        self.root.destroy()

class testclass:
    def __init__(self):
        main_menu = (("F FUNTION", self.f), ("G FUNTION", self.g))
        self.ff = ff("TEST PROGRAM", "2.0", main_menu)
        self.ff.write("hello world")
        self.ff.run()
    
    def f(self):
        self.ff.write("f function")
        p = self.ff.progress_bar_value_get()
        self.ff.progress_bar_value_set(p + 1)

    def g(self):
        self.ff.write("g function")
        self.ff.form("Insert data", ("VAR1", "VAR2", "VAR3"))

testclass()
