import pickle

commits = {}

def main():
	output = ""
	for commit in range(0,3):
		output += "c*\n"
		for file in range(0,2):
			smells = str(commit+file*2)
			output += "class"+str(file)+" smells="+smells+"\n"
			
	result = open("mockpmdresult.txt","w")
	result.write(output)
	result.close()
		
if __name__ == "__main__":
	main()