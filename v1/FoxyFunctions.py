class init:
	def display_menu(s,header,menu):
		#argument menu structure [(label1, function1),(label2, function2) ... (labelN, functionN)]
		#make a list of functions
		print("\n----------------------------------------------------")
		print("\n"+header)
		functions = []
		i = 0
		for item in menu:
			i += 1
			print("%s. %s" % (i, item[0]))
			functions.append(item[1])
		#get user choise and call function once user make valid choise
		call_approve = False
		while not call_approve:
			entry = input(">")
			try:
				entry = int(entry)-1
				call_function = functions[entry]
				if entry >= 0:
					call_approve = True
				else:
					raise TypeError()
			except:
				print("Invalid Input! Try again")
		#call user chosen function
		call_function(entry)
		
	def display_settings(s,settings):
		#settings example: [('setting1',value1),('setting2',value2),('setting3',value3)]
		print("\n----------------------------------------------------")
		print("CURRENT SETTINGS:")
		for s in settings:
			print("%s: %s" % (s[0],s[1]))
		
	def exit(s,n):
		#display goodbye dialog
		input("\nGoodbye! See you later\nPress Enter to exit >")