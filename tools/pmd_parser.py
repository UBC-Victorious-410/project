__author__ = 'Austin'


import os,os.path
import xml.etree.ElementTree as ET

#get the path to the pmd commits
#gwtcwd = get current working directory

#print os.getcwd()

def parse(logpath):
    rootdir = os.path.abspath(os.path.dirname(os.getcwd()))
    #print rootdir
    LoR= []
    pmd_folder = logpath

    print pmd_folder

    i = 0

    completeName = os.path.join(pmd_folder, "CommitResult.txt")
    with open(completeName, "w") as output:
        for file in os.listdir(pmd_folder):
            Result = dict()
            currentfile = ""
            num_viol = 0
            i = i + 1

            if os.path.isfile(pmd_folder +"\\"+ "commit"+str(i)+".xml"):
                output.write("commit"+str(i)+".xml: \n")
                f = open(pmd_folder +"\\"+ "commit"+str(i)+".xml")
                lines = f.readlines()
                for line in lines:
                    if '<file name=' in line:
                        temp = line.split("\\")
                        if currentfile == "":
                            currentfile = temp[-1][:-3]
                            Result[currentfile] = num_viol
                        else:
                            if currentfile not in Result:
                                Result[currentfile] = num_viol
                            else:
                                Result[currentfile] += num_viol
                            num_viol = 0
                            currentfile = temp[-1][:-3]

                    if '</violation>' in line:
                        num_viol = num_viol + 1

                for key in Result.keys():
                    output.write("\t" +key + " : " + str(Result[key]) + "\n")

                # print num_viol
                f.close()
                LoR.append(Result)

    return LoR


