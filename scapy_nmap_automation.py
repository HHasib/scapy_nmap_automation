from scapy.all import *
from apscheduler.schedulers.background import BackgroundScheduler
import time
import nmap


sched = BackgroundScheduler()
sched2 = BackgroundScheduler()
init_time = time.time()
time_interval_in_sec = 5 
total_program_time = 20
scanner = nmap.PortScanner()

#runs commands in schduled time
def scheduled_job():
	# seconds can be replaced with minutes, hours, or days
	sched.add_job(nmap_command, 'interval', seconds = time_interval_in_sec)
	sched2.add_job(scapy_command, 'interval', seconds = time_interval_in_sec)
	sched.start()
	time.sleep(total_program_time)
	sched.shutdown()
	sched2.start()
	time.sleep(total_program_time)
	sched2.shutdown()

#prints the current time since the program started
def time_passed():
	print('Time passed: '+ str(time.time()-init_time))

#nmap commands	
def nmap_command():
	# scanner.scaninfo()
	temp = scanner.scan('127.0.0.1','21-24')
	print(temp)
	time_passed()
	print()

#scapy commands
def scapy_command():
	a = sniff(count = 2)
	a.summary()
	time_passed()
	print()


#the main function
if __name__ == "__main__":
	print("Program started...")
	print()
	scheduled_job()