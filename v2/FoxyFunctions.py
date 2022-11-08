import os

"""
FOXY FUNCTIONS v1.0

To add FoxyFunctions to your code put the file FoxyFunxtions.py in the same folder as your file and write: 
    from FoxyFunctions import ff
Then initialize foxyfunctions as following 
    ff("your program name", "your program version")

function you can interact with:
1. ff(program_name, program_ver) initialization
    when initializing foxy-functions specify the name and revision of you app

2. display_menu(header, menu)
    the header is the name of the menu (for example: MAIN MENU, SETTINGS ect...)
    the menu is a list of tuples that specify the menu text and the function it is activating. (for example: [('f', f), ('g', g)])

3. display_header()
    displays the name and verstion of your program + the version of foxy functions you are using at the moment. no arguments needed
    
4. display_line(line, leng)
    for example: line="hello world", leng=20 hello_world_________ where _ is an empty space not underscore

5. exit()
    finishes the program
    
6. error(text)
    displays an error message
    
7. get_input(text, type)
    text = input text for the user
    type = foxy functions in making sure that it gets legal input STR, INT, FLOAT

8. indexed_print(text)
    displays output with a line number
"""

class ff():
    def __init__(self, program_name, program_ver):
        self.version = "1.0"
        self.program_name = program_name
        self.program_ver = str(program_ver)
        self.LINE_NUMBER = 1

    # header for example: MAIN MENU, menu structure exmple: [('start', start), ('edit', edit), ('exit', exit)]
    def display_menu(self, header, menu):
        os.system('cls') # clear screen
        print(header)
        i = 0
        
        # display main menu items
        valid_selections = []
        for item in menu:
            i += 1
            num = str(i)
            valid_selections.append(num)
            print(num+". "+item[0])
        
        # get user input
        user_input = input("> ")
        if user_input in valid_selections:
            call_function = menu[int(user_input)-1][1]
            call_function()
        else:
            self.internal_error("INVALID INPUT")
            self.display_menu(header, menu)
    
    def display_header(self):
        display_expression = "-- "+self.program_name+" v"+self.program_ver+" ff"+self.version+" --"
        print("-"*len(display_expression))
        print(display_expression)
        print("-"*len(display_expression))
        
    def display_line(self, line, leng):
        spaces = leng - len(line)
        return line+" "*spaces
      
    def exit(self):
        input("DONE >")
    
    def error(self, text):
        input("ERROR! "+text+" >")
    
    def get_input(self, text, type):
        inp = input(text)
        type = type.upper()
        if type == "INT":
            try:
                inp = int(inp)
            except:
                self.error("INVALID INPUT")
                self.get_input(text, type)
        elif type == "FLOAT":
            try:
                inp = float(inp)
            except:
                self.error("INVALID INPUT")
                self.get_input(text, type)
        return inp
    
    def indexed_print(self, text):
        print(str(self.LINE_NUMBER)+". "+text)
        self.LINE_NUMBER += 1
