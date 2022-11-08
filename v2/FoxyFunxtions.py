import os

"""
FOXY FUNCTIONS v1.0

function you can interact with:
1. ff(program_name, program_ver) initialization
    when initializing foxy-functions specify the name and revision of you app

2. display_menu(header, menu)
    the header is the name of the menu (for example: MAIN MENU, SETTINGS ect...)
    the menu is a list of tuples that specify the menu text and the function it is activating. (for example: [('f', f), ('g', g)])

3. display_line(line, leng)
    for example: line="hello world", leng=20 hello_world_________ where _ is an empty space not underscore

4. error(text)
    displays an error message

5. exit()
    finishes the program
"""

class ff():
    def __init__(self, program_name, program_ver):
        self.version = "1.0"
        self.program_name = program_name
        self.program_ver = str(program_ver)
        self.display_header()
    
    # public
    def display_line(self, line, leng):
        spaces = leng - len(line)
        return line+" "*spaces
    
    # private
    def display_header(self):
        display_expression = "-- "+self.program_name+" v"+self.program_ver+" ff"+self.version+" --"
        print("-"*len(display_expression))
        print(display_expression)
        print("-"*len(display_expression))

    # header for example: MAIN MENU, menu structure exmple: [('start', start), ('edit', edit), ('exit', exit)]
    def display_menu(self, header, menu):
        os.system('cls') # clear screen
        self.display_header()
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
    
    # public fnnction
    def exit():
        input("DONE >")
    
    # public fnnction
    def error(text):
        input("ERROR! "+text+" >")

    # private function
    def internal_error(self, text):
        input("ERROR! "+text+" >")
