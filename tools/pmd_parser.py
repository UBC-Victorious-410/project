__author__ = 'Austin'


import os,os.path


#get the path to the pmd commits
#gwtcwd = get current working directory

#print os.getcwd()

def parse(logpath):
    rootdir = os.path.abspath(os.path.dirname(os.getcwd()))
    #print rootdir

    pmd_folder = logpath

    print pmd_folder

    i = 0
    commit_result = []
    file_name = 'commit'

    if not os.path.isfile(pmd_folder+"\\"+"CommitResult.txt"):
        print "CommitResult doesn't exist"

        completeName = os.path.join(pmd_folder, "CommitResult.txt")

        file1 = open(completeName, "w")

        for file in os.listdir(pmd_folder):
            print file
            num_viol = 0
            i = i + 1

            if os.path.isfile(pmd_folder +"\\"+ "commit"+str(i)+".xml"):
                file1.write("commit"+str(i)+".xml")
                f = open(pmd_folder +"\\"+ "commit"+str(i)+".xml")
                lines = f.readlines()

                for line in lines:
                    #print line

                    if '</violation>' in line:
                        num_viol = num_viol + 1

                commit_result.append(file)
                commit_result.append(num_viol)
                file1.write(" "+str(num_viol) +"\n")
                print num_viol
                f.close()

        print commit_result
        file1.close()
    elif os.path.isfile(pmd_folder+"\\"+"CommitResult.txt") is True:
        print "CommitResult already exists!"
