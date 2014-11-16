from web import visualizer
import sys
import os
import shutil
import json
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
    log_location = os.path.dirname(os.path.realpath(__file__)) +"\PMDResult"
    # generate and parse gitlog
    generate_git_log()
    commits = fuser.parse_gitlog(log_location)
    # filter out commits without any changes
    commit_with_changes = []
    hashes = []
    for commit in commits:
        if len(commit.fileChanges) > 0:
            commit_with_changes.append(commit)
            hashes.append(commit.hash)
    # PMD these commits and parse them
    #PMD(hashes)
    pmd = fuser.parse_PMD(log_location)
    #fuse them to JSON
    result = fuser.fuse_to_JSON(commit_with_changes,pmd)
    count = 0
    for r in result:
        with open('web/static/'+str(count)+'.json' , "w") as output:
            output.write(json.dumps(r))
        count = count + 1
    # create dir to cache gravatar icons
    if not os.path.isdir("./web/gravatars"):
        os.mkdir("./web/gravatars")



def generate_git_log():
    g = Git('./Target/')
    gitLog = g.log("--reverse","--numstat")
    if not os.path.isdir("./PMDResult"):
        os.mkdir("PMDResult")
    with open('./PMDResult/gitLog.txt','w') as r:
        r.write(gitLog)
    print ("gitLog.txt is placed in PMDResult")

def PMD(commits):
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
    print "        GenerateJSON               - generate JSON from the fuser "
    print "        GenerateGraph              - generate the result with D3 using JSON"
#
if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1:])



