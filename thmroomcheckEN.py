from tabulate import tabulate
import json, urllib.request

custom_goals = [["\033[4mJunior Path\033[0m","\033[4mSenior Path\033[0m"],
	["Junior Security Analyst Intro","Introductory Networking"],
	["Careers in Cyber","Network Services"],
	["Pyramid of Pain","Network Services 2"],
	["Cyber Kill Chain","Wireshark 101"],
	["MITRE","Windows Fundamentals 1"],
	["Security Operations","Firewalls"],
	["Phishing Analysis Fundamentals","Nmap"],
	["Phishing Emails in Action","Nessus"],
	["Phishing Analysis Tools","Yara"],
	["Phishing Prevention","OpenVAS "],
	["The Greenbolt Phish","Snort"],
	["Mr.Phisher","Snort Challenge"],
	["Introduction to SIEM","OWASP Top 10"],
	["Splunk: Basics","OWASP Juice Shop"],
	["Incident handling with Splunk","Upload Vulnerabilities"],
	["Investigating with Splunk",""],
	["Benign",""]]

### This is used to start the count of rooms completed
totalmetasL1 = 0
totalmetasL2 = 0

###
print("Type TryHackMe username (case sensitive):")
username = input()

### Since THM block URLib requests, we are setting a custom user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
headers = {"User-Agent":user_agent,}

### request will return a JSON
user_url = f"https://tryhackme.com/api/all-completed-rooms?username={username}&limit=100&page=1"
### crafting the request to pass the user-agent
request = urllib.request.Request(user_url,None,headers)

###
with urllib.request.urlopen(request) as output:
    ### function .read return the json as str, json lib allows to load it as list.
	thmroom_str = output.read()
	thmroom_list = json.loads(thmroom_str)
	totalrooms = len(thmroom_list)
	for thmroom in range(totalrooms):
		for metaroom in custom_goals:
			if thmroom_list[thmroom]["title"] == metaroom[0]:
				metaroom[0] = str(f"\033[0;32m[X] {metaroom[0]}\033[0m")
				totalmetasL1 += 1
			elif thmroom_list[thmroom]["title"] == metaroom[1]:
				metaroom[1] = str(f"\033[0;32m[X] {metaroom[1]}\033[0m")
				totalmetasL2 += 1

print(f"\nRooms \033[0;32mhighlighted\033[0m were completed by \033[0;32m{username}\033[0m for each path:")
print(tabulate(custom_goals))
print(f"\n\033[1m\033[4m{username} has completed:\033[0m\n\n\033[1mJunior Path:\033[0m \033[0;32m{totalmetasL1}\033[0m rooms.\n\033[1mSenior Path:\033[0m \033[0;32m{totalmetasL2}\033[0m rooms.\n\033[1mOther out of the path rooms:\033[0m \033[0;32m{totalrooms-totalmetasL1-totalmetasL2}\033[0m.\n\033[1mRoom totals:\033[0m \033[0;32m{totalrooms}\033[0m.\n")