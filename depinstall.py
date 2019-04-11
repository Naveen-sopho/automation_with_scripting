import json
import os

def getJSON(filePathAndName):
    with open(filePathAndName, 'r')as fp:
        return json.load(fp)

myObj = getJSON('./dependencies.json')

depen = myObj.get("Dependencies") #parsing dependencies

os.system("sudo easy_install python3-pip") #installing pip

fail = []
for i in depen:
	j = "pip install "+i
	os.system(j)	#installing all dependencies

f= open("installed.txt","w+")	#creating a txt file to check installed dependencies
installed = []

os.system("pip freeze > installed.txt")

ins = f.readlines()
for i in ins:
    a = i.rstrip('\n')
    installed.append(a)

depen = set(depen)
installed = set(installed)

fail = list(depen - installed) #creating a list(fail) for failed dependencies
if not fail:
	print("success")
else :
	print("Following Dependenciesare not installed :")	
	for i in fail:
		print(i)