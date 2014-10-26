from web import visualizer
import sys
import os
import shutil
from git import *


def main(argv):
    opt = argv[0]
    if opt == "getRepo":
        try:
            git_pull(argv[1])
        except Exception, e:
            print (str(e))
    elif opt == "gitLog":
        git_log()
    elif opt == "PMD":
        PMD()
    elif opt == "Parse":
        print "do parse"
    elif opt == "GenerateJSON":
        print "do GenerateJSON"
    elif opt == "GenerateGraph":
        visualizer.begin()
    else:
        usage()



def git_pull(git_dir):
    if not os.path.isdir("./Target"):
        os.mkdir("Target")
        Repo.clone_from(git_dir, "./Target")
    else:
        print "/Target folder exist, please remove it to get new repository"

def git_log():
    g = Git('./Target/')
    gitLog = g.log("--reverse","--stat")
    if not os.path.isdir("./PMDResult"):
        os.mkdir("PMDResult")
    with open('./PMDResult/gitLog.txt','w') as r:
        r.write(gitLog)
    print ("gitLog.txt is placed in PMDResult")

def PMD():
    g = Git('./Target/')
    commits = g.log("--reverse", "--pretty=%h").split("\n")
    for c in commits:
        print ("git checkout -b " + c)
        print ("Execute PMD on commit: " + c)




def usage():
    print "Usage: Main.py <option> "
    print "option: getRepo <git repo address> - perform 'git pull' with given repoURL at ./target"
    print "        gitLog                     - generate gitLog.xml in PMDResult"
    print "        PMD                        - analyze target/ with PMD. place xml results in PMDResults"
    print "        Parse                      - execute parsers to parse result within PMDResults"
    print "        GenerateJSON               - generate JSON from the fuser "
    print "        GenerateGraph              - generate the result with D3 using JSON"
#
if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1:])



