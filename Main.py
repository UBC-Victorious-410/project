from web import visualizer
import sys
import os
from git import *


def main(argv):
    opt = argv[0]
    if opt == "getRepo":
        if not os.path.isdir("./Target"):
            os.mkdir("Target")
        Repo.clone_from(argv[1], "./Target")
    elif opt == "gitLog":
        
        print "do git log"
    elif opt == "PMD":
        print "do PMD"
    elif opt == "Parse":
        print "do parse"
    elif opt == "GenerateJSON":
        print "do GenerateJSON"
    elif opt == "GenerateGraph":
        visualizer.begin()



    else:
        usage()

def PMD(argv):

    print "do PMD"



def usage():
    print "Usage: Main.py <option> "
    print "option  :      getRepo <git repo address> - perform 'git pull' with given repoURL at ./target"
    print "               gitLog                     - generate gitLog.xml in PMDResult"
    print "               PMD                        - analyze target/ with PMD. place xml results in PMDResults"
    print "               Parse                      - execute parsers to parse result within PMDResults"
    print "               GenerateJSON               - generate JSON from the fuser "
    print "               GenerateGraph              - generate the result with D3 using JSON"

if __name__ == "__main__":
    main(sys.argv[1:])



