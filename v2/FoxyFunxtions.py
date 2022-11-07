import os

"""
function you can interact with:
1. initialization(program_name, program_ver)
    when initializing foxy-functions specify the name and revision of you app

2. display_menu(self, header, menu)
    the header is the name of the menu (for example: MAIN MENU, SETTINGS ect...)
    the menu is a list of tuples that specify the menu text and the function it is activating. (for example: [('f', f), ('g', g)])

3. error(text)
    displays an error message

4. exit()
    finishes the program
"""

class ff():
    def __init__(self, program_name, program_ver):
        self.program_name = program_name
        self.program_ver = str(program_ver)
        self.display_header()
    
    # private
    def display_header(self):
        display_expression = "-- "+self.program_name+" v"+self.program_ver+" --"
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