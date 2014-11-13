from web import visualizer
import sys
import os
import shutil
from git import *
from subprocess import *
from tools import fuser


def main(argv):
    opt = argv[0]
    if opt == "getRepo":
        try:
            git_pull(argv[1])
        except Exception, e:
            print (str(e))
    elif opt == "GenerateJSON":
        generateJson()
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

def generateJson():
    git_log()
    PMD()
    log_location = os.path.dirname(os.path.realpath(__file__)) +"\PMDResult"
    result = fuser.parse_to_JSON(log_location)


def git_log():
    g = Git('./Target/')
    gitLog = g.log("--reverse","--numstat")
    if not os.path.isdir("./PMDResult"):
        os.mkdir("PMDResult")
    with open('./PMDResult/gitLog.txt','w') as r:
        r.write(gitLog)
    print ("gitLog.txt is placed in PMDResult")

def PMD():
    g = Git('./Target/')
    commits = g.log("--reverse", "--pretty=%h").split("\n")
    g = Git('./Target/')

    # create a branch for all commits
    # will reduce branch one we figure out the what to left out
    for c in commits:
        g.branch(c, c)
    print (g.branch())

    # run PMD to ./Target
    # place results in PMDResult
    i = 1
    for b in commits:
        g.checkout(b)
        os.system("tools\\pmd-bin-5.1.3\\bin\\pmd.bat -dir ./Target -format xml "
                  "-rulesets java-basic,java-coupling,java-design,java-codesize > " +
                  "PMDResult\\commit" + str(i) + ".xml")
        i = i + 1

def usage():
    print "Usage: Main.py <option> "
    print "option: getRepo <git repo address> - perform 'git pull' with given repoURL at ./target"
    # print "        gitLog                     - generate gitLog.xml in PMDResult"
    # print "        PMD                        - analyze target/ with PMD. place xml results in PMDResults"
    # print "        Parse                      - execute parsers to parse result within PMDResults"
    print "        GenerateJSON               - generate JSON from the fuser "
    print "        GenerateGraph              - generate the result with D3 using JSON"
#
if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1:])



