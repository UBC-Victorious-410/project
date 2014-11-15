import pickle
import json
from json import JSONEncoder
import gitlog_parser
from gitlog_parser import commit
import pmd_parser
import copy

def parse_gitlog(logpath):
    return gitlog_parser.parse(logpath)
def parse_PMD(logpath):
    return pmd_parser.parse(logpath)
def fuse_to_JSON(gitlog, pmd):
    i = 0
    for commit in gitlog:
        commit.state = pmd[i]
        if i == 0:
            commit.all = copy.deepcopy(commit.fileChanges)
        else:
            commit.all = copy.deepcopy(gitlog[i-1].all)
            for item in commit.fileChanges.keys():
                if item in commit.all:
                    commit.all[item] = commit.all[item] + commit.fileChanges[item]
                    # remove if the result is 0
                    # if commit.all[item] == 0:
                    #     del commit.all[item]
                else:
                    commit.all[item] = commit.fileChanges[item]
        i = i + 1

    # walk through all commit again insert class from last commit
    # completekey = gitlog[-1].all.keys()
    # for commit in gitlog:
    #     for key in completekey:
    #         if key not in commit.all:
    #             commit.all[key] = 0




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
    children = []
    for key in commit.all.keys():
        tempdict = dict()
        tempdict["name"] = key
        tempdict["size"] = commit.all[key]
        children.append(tempdict)
    result = {
        'hash':commit.hash,
        'author':commit.author,
        'authorEmail':commit.authorEmail,
        'date':commit.date,
        'fileChanges':commit.fileChanges,
        'state':commit.state,
        'children':children
    }
    return result
