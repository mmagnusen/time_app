import time

hours_today_gym = 0

hours_today_work = 0

hours_today_coding = 0

hours_today_socialising = 0

last_log_file = open("time_log.csv", "r")

last_log_time = last_log_file.read()

name = ""

current_time = time.time()

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
	hours_between_logs = float(last_log_time) - current_time

	if hours_between_logs < 86400:
		ask_for_hours()
	else:
		ask_for_hours()


# Ask user if they want to log hours. If yes, enter_hours() function is called; if no, we print "goodbye" message
def ask_for_hours():
	log_hours = input("You haven't logged any hours for today. Would you like to log your hours now?").upper()

	if log_hours == "YES":
		start_logging()
	else:
		print("Maybe next time. Bye!")
	


#Ask the user to log hours spent doing each activity
def enter_hours():
	print("Ok, time to log your hours.")

	global hours_today_gym
	hours_today_gym = input("How many hours have you spent at the gym today?")
	open_gym = open("gym.csv", "a")
	open_gym.write(str(current_time) + "," + hours_today_gym + "\n") 

	global hours_today_work
	hours_today_work = input("How many hours have you spent at work today?")
	open_work = open("work.csv", "a")
	open_work.write(str(current_time) + "," + hours_today_work  + "\n") 

	global hours_today_coding
	hours_today_coding = input("How many hours have you spent coding today?")
	open_coding = open("coding.csv", "a")
	open_coding.write(str(current_time) + "," + hours_today_coding  + "\n") 

	global hours_today_socialising
	hours_today_socialising = input("How many hours have you spent socialising today?")
	open_socialising = open("socialising.csv", "a")
	open_socialising.write(str(current_time) + "," + hours_today_socialising  + "\n") 


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

def report_hours():
	print("Since the beginning of time, you have spent: \n")
	report__total_hours("gym")
	report__total_hours("coding")
	report__total_hours("socialising")
	report__total_hours("work")

def report__total_hours(activity):
	total = 0
	open_file = open(activity + ".csv", "r")
	read_file = open_file.read()
	for hours in read_file.split("\n"):
		if hours:
			stored_hours = (hours.split(","))
			total = total + int(stored_hours[1])

	print(str(total) + " hours spent in/on " + activity)



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
dcheck_already_logged()
report_hours()