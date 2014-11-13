import pickle
import json
from json import JSONEncoder
import gitlog_parser
from gitlog_parser import commit
import pmd_parser

def parse_gitlog(logpath):
    return gitlog_parser.parse(logpath)
def parse_PMD(logpath):
    return pmd_parser.parse(logpath)
def fuse_to_JSON(gitlog, pmd):
    i = 0
    for commit in gitlog:
        commit.state = pmd[i]
        i = i + 1


    with open('./PMDResult/quack.txt', "w") as f:
        for commit in gitlog:
            f.write("===========================" + "\n")
            f.write("commit: " + commit.hash + "\n")
            f.write("author: "+ commit.author + "\n")
            f.write("eMail: " + commit.authorEmail + "\n")
            f.write("date : " + commit.date + "\n")

            f.write("file changes : \n ")
            for key in commit.fileChanges.keys():
                f.write("\t" + key + " : " + str(commit.fileChanges[key]) + "\n")

            f.write("State: \n")
            for key2 in commit.state.keys():
                f.write("\t" + key2 + " : " + str(commit.state[key2]) + "\n")
    result = []
    for commit in gitlog:
        result.append(convert_to_json(commit))

    return result

def convert_to_json(commit):
    result = {
        'hash':commit.hash,
        'author':commit.author,
        'authorEmail':commit.authorEmail,
        'date':commit.date,
        'fileChanges':commit.fileChanges,
        'state':commit.state
    }
    return result
