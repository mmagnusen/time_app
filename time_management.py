# Welcome message, something like "Hi Marilyn! Well done on keeping up-to-date with your schedule. Let's help keep you on track :)"

# There will be a prompt to ask me: how long at gym, how long at work, how long coding, how long socialising

# I should be able to enter a command which tells the app I've finished entering my hours for today

# It should give me a summary of each thing I've done today

#Create variables for storing hours:

hours_today_gym = 0

hours_today_work = 0

hours_today_coding = 0

hours_today_socialising = 0

name = "Marilyn"


# A welcome message to tell the user what the app does
def welcome_message():
	print("""
		  Hi {}! Well done on keeping up-to-date with your schedule. 
		  Let's help keep you on track by logging how much time you spend doing each activity
		  """.format(name))


# Ask user if they want to log hours. If yes, enter_hours() function is called; if no, we print "goodbye" message
def ask_for_hours():
	log_hours = input("Would you like to log your hours now?").upper()

	if log_hours == "YES":
		enter_hours()
	else:
		print("Maybe next time. Bye!")
	

#Ask the user to log hours spent doing each activity
def enter_hours():
	print("Ok, time to log your hours.")
	global hours_today_gym
	hours_today_gym = input("How many hours have you spent at the gym today?")
	global hours_today_work
	hours_today_work = input("How many hours have you spent at work today?")
	global hours_today_coding
	hours_today_coding = input("How many hours have you spent coding today?")
	global hours_today_socialising
	hours_today_socialising = input("How many hours have you spent socialising today?")


#Tell the users how many hours they've spent on each activity today and a goodbye message
def show_hours():
	print("""
    Thanks for taking the time to log your hours.
	This is how you've spent today:
	Gym: {}
	Work: {}
	Coding: {}
	Socialising: {} 
	""".format(hours_today_gym, hours_today_work, hours_today_coding, hours_today_socialising))

	print("See you next time {}!".format(name))


welcome_message()
ask_for_hours()
show_hours()
