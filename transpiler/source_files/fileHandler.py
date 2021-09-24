import os

def deleteFile(fileName):
    if os.path.exists("quorum_user_code/" + fileName):
        os.remove("quorum_user_code/" + fileName)

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
