saved_time = "2017-08-09 20:01:26.412393"

def practice_reading():
	last_log_file = open("time_log.csv", "r")
	last_log_time = last_log_file.read()
	print(last_log_time)
	last_log_file.close()

def practice_writing():
	open_file_to_read = open("time_log.csv", "w")
	open_file_to_write = open_file_to_read.write("diet coke")
	last_log_file.close()

practice_reading()
practice_writing()
practice_reading()