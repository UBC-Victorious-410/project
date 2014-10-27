import pickle
import json
from mock_gitlog_parser import commit

frames = {} # frameno : Frame

class Frame:
	def __init__(self,number):
		self.number = number
		self.files = {} # filename: [author, lines_mod, filesize, smells]
		self.authors = []
	
	def addFile(self, name, author, linesmod, size):
		self.files[name] = [author, linesmod, size, 0]
		if author not in self.authors:
			self.authors.append(author)
			
	def removeFile(self, name):
		del self.files[name]
	
	def addSmell(self, name, smells):
		# print (self.files.keys())
		self.files[name][3] = smells 
	
def main():
	
	commits = pickle.load(open("mockgitlogresult.pkl","rb"))
	smells = open("mockpmdresult.txt","r")
	
	for k,commit in commits.iteritems():
		frameno = k
		newframe = Frame(frameno)
		frames[frameno] = newframe
		for filename,changes in commit.fileChanges.iteritems():
			newframe.addFile(filename, commit.author, changes, changes)
			
	parseSmells(smells)
	
	output = json.dumps(frames,sort_keys=True, default=lambda o: o.__dict__)
	jsonfile = open("generated_json.json","w")
	jsonfile.write(output)
	jsonfile.close()
	
# writes smells for each file from the input string into correct Frame and file
def parseSmells(smelldata):
	lines = smelldata.readlines()
	commitno = 0
	for line in lines:
		if "c*" in line:
			commitno += 1
		elif "smells=" in line:
			rawdata2 = line.split("smells=")
			filename = rawdata2[0].strip()
			smells = rawdata2[1].strip()
			# print(str(commitno) + " " + filename + " " + str(smells))
			key = str(commitno)
			frames[key].addSmell(filename,smells)
			
if __name__ == "__main__":
	main()
	