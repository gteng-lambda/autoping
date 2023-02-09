import os
from datetime import datetime


#Written by Grant Tengler
#This is my start with shell scripting and the os interface.
#The objective of this program is meant to act as a log which will record successfull pings to websites, essentially a first responder if the internet goes down with time stamps
#WARNING, THIS PROGRAM UTLIZES THE OS PACKAGE, PLEASE BE DILLIGENT AND LOOK THROUGH THE SCRIPT TO SEE IF IT WONT AFFECT ANY IMPORTANT FILES
#I reccommend making a directory will use this
#This is intended to be utilized inside a private environment


#This overwrites a file, which will solely be used to get output from shell
#Think of it as an output that is written and then immediately replaced
#And this will write to a file that we will then use to make our conclusions



class dataCreate():

	#Constructor that will accept inputs and such for our console and construct a string
	def __init__(self,ping_num,link_str):
		self.ping_num = ping_num
		self.link_str = link_str 

	def returnPingCommands(self):
		#This will compile our file into a "malleable" structure
		ping_array = []
		#This grabs the time so we can compare it to the time later if we decide to run it
		before = datetime.now()

		#If the file doesn't already exists then we need to create a file, other wise do nothing.
		if os.path.exists("pingtest.csv") == False:
			os.system("touch pingtest.txt")

		#This is the string that gets passed to the terminal and then we pre-process the output into a new csv, this temp file gets erassed and the lines append to the main file
		cmd_str = f"ping -c {self.ping_num} {self.link_str} > pingtest.txt"


		#Debug line to check if the datetime method is working# print("Time Before:",now)
		os.system(cmd_str)

		#This reads the file
		with open("pingtest.txt","r") as conffile:
			ping_array = conffile.readlines()
			
		#Regardless of the ping requests, I think that the last two elements are the most important, the rest is formatting

		#The reasons that I did this is because the terminal originally posts these results with a new line escape character. I removed those to make a cleaner file
		stats_summ = (ping_array[-2:])
		temp_var1 = stats_summ[0]
		temp_var2 = stats_summ[1]
		stats_summ[0] = temp_var1[:-1]
		stats_summ[1] = temp_var2[:-1]
		


		#Need to instantiate two datetime variables
		
		after = datetime.now()
		
		#The reason that these times are at the end of the file is because the after time object needs to instantiated after the entire script has run
		stats_summ.append(before.strftime("%m/%d/%Y. %H:%M:%S"))
		stats_summ.append(after.strftime("%m/%d/%Y. %H:%M:%S\n"))
		return(stats_summ)
		



if __name__ == "__main__":
	#You can add your own intervals
	new_class = dataCreate(1,"google.com")
	instance_list = new_class.returnPingCommands()

	#These are the category columns
	cat_columns = ["Package Transmit","Package Receive","Package Loss Rate","Network Standard Deviation","Start Time","Ending Time\n"]
	

	#We need to make the comma delimmeted strings in order for the file object to be able to pass it
	column_string = ",".join(cat_columns)
	instance_string = ",".join(instance_list)

	#We need to see if the ping_report.csv has been created else, we need to create it

	#If the file does not exist; create it
	if os.path.exists("ping_report.csv") == False:
		os.system("touch ping_report.csv")


	#If the file is empty, we can assume it is the first time the user has ran it
	if os.stat("ping_report.csv").st_size == 0:
		#Using the w arg, we are overwritting the file
		f = open("ping_report.csv","w")
		#Write the columns to the file
		f.write(column_string)
		#Write the initial content
		f.write(instance_string)
		f.close()
	#If the file exsists, and is not empty, we can assume that we just need to append the returnPingCommands from the class we created
	#The reason we append and not write over, is this is meant to be a file that we can view later.
	else:
		f = open("ping_report.csv","a")
		f.write(instance_string)
		f.close()


	



	
		
	
	


	


			
	


	
		


		
		
	


	
	


