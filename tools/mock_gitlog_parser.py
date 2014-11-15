import pickle
import copy

class commit:
    def __init__(self,hash,author,email,date):
        self.hash = hash
        self.author = author
        self.authorEmail = email
        self.date = date
        self.fileChanges = dict()
        self.validation = 0
    def updateFileChanges(self, filename, linecount):
        if filename in self.fileChanges:
           self.fileChanges[filename] += linecount
        else:
            self.fileChanges[filename] = linecount

commits = {}

def main():
	c1 = commit("hash1","author1","email1","date1")
	c2 = commit("hash2","author2","email2","date4")
	c1.updateFileChanges("class0",100)
	c1.updateFileChanges("class1",100)
	commits["1"] = c1
	c2.updateFileChanges("class0",100)
	c2.updateFileChanges("class1",100)
	commits["2"] = c2
	c3 = copy.deepcopy(c1)
	c3.updateFileChanges("class0",100) 
	c3.updateFileChanges("class1",100)
	commits["3"] = c3
	
	
	pickle.dump(commits, open("mockgitlogresult.pkl","wb"))
		
if __name__ == "__main__":
	main()
	