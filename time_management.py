import time

hours_today_gym = 0

hours_today_work = 0

hours_today_coding = 0

hours_today_socialising = 0

last_log_file = open("time_log.csv", "r")

last_log_time = last_log_file.read()

name = ""

currrent_time = time.time()

# A welcome message to tell the user what the app does
def get_name():
	global name
	name = input("Hi! What's your name? ")


def welcome_message():
	print("""
		  Hi {}! Well done on keeping up-to-date with your schedule. 
		  Let's help keep you on track by logging how much time you spend doing each activity
		  First, let's check if you've already entered your hours for today.
		  """.format(name))


def check_already_logged():
	hours_between_logs = float(last_log_time) - currrent_time

	if hours_between_logs < 86400:
		print("You've already logged your hours today. See you tomorrow!")
	else:
		ask_for_hours()


# Ask user if they want to log hours. If yes, enter_hours() function is called; if no, we print "goodbye" message
def ask_for_hours():
	log_hours = input("You haven't logged any hours for today. Would you like to log your hours now?")

	if log_hours == "YES":
		start_logging()
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


#Updates CSV file so last log time changes to current time
def update_last_log_time():
	last_log_file_write_mode = open("time_log.csv", 'w')
	last_log_file_write_mode.write(str(time.time()))

def start_logging():
	enter_hours()
	show_hours()
	update_last_log_time()

get_name()
welcome_message()
check_already_logged()