import os 

def One(a,b,c):
    resultstring = "[{0}]\nrole_arn = arn:aws:iam::{1}:role/{2}\n\n\n".format(a,str(b),c)
    return resultstring

def main(inputfile,outputfile):
    AccName = ""
    AccNum = 0
    Role = ""
    linenumber = 0

    with open(inputfile, "r") as infile:       
        for line in infile:
            
            if linenumber % 4 == 0:
                AccName = line[:-1]

            elif line[0] == "#":
                AccNum = line[1:13]

            elif ((linenumber -3) % 4) == 0: # line[:13] == "ReadOnlyAdmin" or line[:14] == "ViewOnlyAccess":
                print(line)
                listline = line.split(" ")
                Role = listline[0]

                with open (outputfile, "a") as outfile:
                    outfile.write(One(AccName,AccNum,Role))

                AccName = ""
                AccNum = 0
                Role = ""

            linenumber = linenumber + 1

dir_path = os.path.dirname(os.path.realpath(__file__))
inputfilepath = dir_path + "\input.txt"
outputfilepath = dir_path + "\Output.txt"                 
main(inputfilepath,outputfilepath)