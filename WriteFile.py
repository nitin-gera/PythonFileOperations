# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:58:12 2018

@author: nitingera
"""

#myfile = open("employees.txt", "r")

#print(myfile.read())
#print(myfile.read(13))
#print(myfile.readline())
#print(myfile.readline())

#for line in myfile:
#    print("1:", line)


writefile = open("names.txt", "a")

name = ""
listofnames = ""

while(name != "XXX"):
    name = input("Enter your name:")
    if(name != "XXX"):
        listofnames += name
        listofnames += "\n"
        
print("Saving:", listofnames)
writefile.write(listofnames)
writefile.close()
    
