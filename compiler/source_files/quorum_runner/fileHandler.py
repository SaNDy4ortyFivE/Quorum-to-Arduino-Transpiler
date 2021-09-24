import os

def deleteFile(fileName):
    print("File to delete:{}".format(fileName))
    fileName_class = fileName.replace(".quorum",".class")
    fileName_underscore_class = fileName.replace(".quorum","_.class")

    ##remove class file
    if os.path.exists("Build/quorum/" + fileName_class):
        print("Removing:{}".format(fileName_class))
        os.remove("Build/quorum/" + fileName_class)
    else:
        print("cannot find path of {}...".format(fileName_class))
    ##remove _class file
    if os.path.exists("Build/quorum/" + fileName_underscore_class):
        print("Removing:{}".format(fileName_underscore_class))
        os.remove("Build/quorum/" + fileName_underscore_class)
    else:
        print("cannot find path of {}...".format(fileName_underscore_class))
    ##remove downloaded quorum file
    if os.path.exists("quorum_user_code/" + fileName):
        print("Removing:{}".format(fileName))
        os.remove("quorum_user_code/" + fileName)
    else:
        print("cannot find path of {}...".format(fileName))

def replaceN(fileName):
    #read input file
    fin = open("quorum_user_code/"+fileName, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace("\r\n", '\n')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("quorum_user_code/"+fileName, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
