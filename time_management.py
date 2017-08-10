import datetime 

hours_today_gym = 0

hours_today_work = 0

hours_today_coding = 0

hours_today_socialising = 0

name = ""


# A welcome message to tell the user what the app does
def get_name():
	global name
	name = input("Hi! What's your name? ")

def welcome_message():
	print("""
		  Hi {}! Well done on keeping up-to-date with your schedule. 
		  Let's help keep you on track by logging how much time you spend doing each activity
		  """.format(name))


# Ask user if they want to log hours. If yes, enter_hours() function is called; if no, we print "goodbye" message
def ask_for_hours():
	last_log_file = open("time_log.csv", "r")

	last_log_time = last_log_file.read()

	log_hours = input("""
				FYI, the last time you logged your hours was {}. 
				Are you sure you'd like to log your hours now? 
				""".format(last_log_time)).upper()

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

def update_last_log_time():
	open_file_to_read = open("time_log.csv", "w")
	currrent_time = str(datetime.datetime.now())
	open_file_to_read.write(currrent_time)
	open_file_to_read.close()


get_name()
welcome_message()
ask_for_hours()
show_hours()
update_last_log_time()
