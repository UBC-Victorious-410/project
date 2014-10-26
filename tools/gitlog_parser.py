import os
import sys
import re
import pprint

# global vars
commits = {}
messages = {}
inMessage = False
message = ""
i = 1
currenthash = ""
lasthash = ""


def main(argv):
	# no args given:
	numargs = len(argv)
	if numargs == 0:
		usage()
		return
	# assume a non-empty filepath	
	path = argv[0]
	if path:
		parselog (path)
	
	else:
		usage()
			

# parses only git logs formatted using --numstat flag (and optionally --reverse)			
def parselog (path):
	global message
	global i
	global currenthash
	global lasthash
	global inMessage
	
	raw_log = open(path, 'r').readlines()
	
	hashpattern = re.compile("commit\s[0-9A-Fa-f]{40}")
	datepattern = re.compile("Date:\s{3}\w{3}\s\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}\s-\d{4}")
	

	for line in raw_log:
		
		if hashpattern.match(line):
			
			# save commit msg in case commit summary not detected
			saveMsg(lasthash)
			
			#get the hash
			result = line.split("commit")
			hash = result[1].strip()
			if hash:
				print("\nCommit #: " + str(i))
				print(hash)
				#do something
			
			# remember current and previous hashes so we can do stuff
			lasthash, currenthash =  currenthash, hash
			i += 1
			
		elif 'Author: ' in line and '@' in line:
			result1 = line.split("Author:")
			result2 = result1[1].split("<")
			result3 = result2[1].split(">")
			
			name = result2[0].strip()
			email = result3[0].strip()
			print(name)
			print(email)
			#do something
			
		elif datepattern.match(line):
			result = line.split("Date:")
			date = result[1].strip()
			print(date)
			#do something
			
		elif '|' in line:
			# TODO handle deleted files
			# TODO handle modified files (total lines)
			
			# check file suffix inside or its passed to else block below...
			if ".java" in line:
				split1 = line.split("|")
				filename = split1[0].split("/")[-1].strip()
				
				split2 = split1[1].split("+")
				split3 = split2[0].split("-")
				lines_modified = split3[0].strip()
				print("Lines changed: " + lines_modified + "  " + filename)
		elif (
				("file changed" in line or "files changed" in line)
				and
				("insertions(+)" in line or "deletions(-)" in line)
			):
			# in a summary line for current commit
			# previous commit message ended when we reach here, save it and reset
			saveMsg(currenthash)
		else:
			if "Merge:" not in line:
			#its a commit message line
				cleanedline = line.strip()
				if inMessage:
					message += cleanedline
				else:
					inMessage = True
					message += cleanedline


	# uncomment to print the messages dictionary
	# printer = pprint.PrettyPrinter()
	# printer.pprint (messages)
		
# saves non-empty message to dict
def saveMsg (hash):
	global inMessage
	global message
	global messages
	if inMessage:
		inMessage = False
		if message:
			messages[currenthash] = message
			message = "";

def usage ():
	print ("Usage: gitlog_parser.py <path>")
	print ("<path> must be absolute filepath to a git log txt file generated using --stat flag and preferably --reverse")
	
if __name__ == "__main__":
    main(sys.argv[1:])
	





