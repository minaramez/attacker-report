#!/usr/bin/env python3
#above is the shebang line which tells the OS to run the script using python3

#os is used to communicate with system related operations
import os
#re provides support for regular expressions
import re
#the collections module provides alternatives to built-in types that can be more effiecient, and the counter class desgined for counting hashable objects. 
from collections import Counter
#from datetime import datetime provides the current date and time that the operating system is set to.
from datetime import datetime
#the geolite2 submodule provides access to the free geolite2 databases from maxmind which contain information about ip address ranges and their associated geolocation data. 
from geoip import geolite2

#command to clear the terminal
os.system('clear')

#print functions to show the student name and date, along with information about the script.
print(" ")
print("Script written by: Mina Ramez Farag")
print("Email ID: mrf7074")
print("Date: May 3, 2023")
print("")
print("       ***********************")
print("       ****Attacker Report****")
print("       ***********************")
print("")



#pattern set up by regex to find the IP address of every line
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

#command to open and read the syslog.log file from the /home/student/student/scripts/script04 directory
with open('/home/student/student/scripts/script04/syslog.log', 'r') as f:
    log_lines = f.readlines()

#command to read the lines on the file and count the number of failed log in attempts 
failed_attempts = Counter()
for line in log_lines:
    if 'Failed password for' in line:
        match = re.search(ip_pattern, line)
        if match:
            ip = match.group(0)
            failed_attempts[ip] += 1

#command to sort the number of failed attempts in ascending order
sorted_attempts = sorted(failed_attempts.items(), key=lambda x: x[1])

#command to print the header of the report in a table manner
print(f'Login attempts report ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})\n')
print('{:<10} {:<20} {:<20}'.format('Count', 'IP Address', 'Country'))

#command to print the top 10 failed log in attempts with their ip, count and country
for ip, count in sorted_attempts[:10]:
    match = geolite2.lookup(ip)
    country = match.country if match else 'Unknown'
    print('{:<10} {:<20} {:<20}'.format(count, ip, country))