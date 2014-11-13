import pickle
import json
import gitlog_parser
import pmd_parser


def parse_to_JSON(path):
    gitLogPath = path + '/gitLog.txt'
    pmdPath = path
    gitlog = parse_gitlog(gitLogPath)
    pmd = parse_PMD(pmdPath)
    return fuse_to_JSON(gitlog,pmd)

def parse_gitlog(logpath):
    gitlog_parser.parse(logpath)
    return
def parse_PMD(logpath):
    pmd_parser.parse(logpath)
    return
def fuse_to_JSON(gitlog, pmd):
    return