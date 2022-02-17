# Python code to
#
############################################################################
# pi@raspberrypi:~ $ sudo du --block-size  1 -c /* | sort -n -r >sortlist.txt
# du: cannot access '/proc/6017/task/7852': No such file or directory
# du: cannot access '/proc/8041/task/8041/fd/4': No such file or directory
# du: cannot access '/proc/8041/task/8041/fdinfo/4': No such file or directory
# du: cannot access '/proc/8041/fd/3': No such file or directory
# du: cannot access '/proc/8041/fdinfo/3': No such file or directory
# du: cannot access '/run/user/1000/gvfs': Permission denied
# pi@raspberrypi:~ $ nano sortlist.txt
# sudo apt list >packagelist.txt
# Nano packagelist.txt
#  Read 62712 Lines
# mv package0list.txt pack0list.txt
# sudo nano -o package1list.txt /
############################################################################

import os

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
 
print ("Program","start")

print ("Introduction","start")

thisdict0 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "year": 1969
}
print("Setup thisdict0:\t",thisdict0)

thisdict1 = {
  "name": [],
  "type": [],
  "size": [],
  "level": []
  }
thisdict1.clear
print("Setup thisdict1:\t",thisdict1)
#Setup[ {'name': [], 'type': [], 'size': [], 'level': []} ]

word = 'geeks for Geeks'
  
# returns first occurrence of Substring
result = word.find('Geeks')
print ("Substring 'Geeks' found at index:", result )
  
result = word.find('for')
print ("Substring 'for ' found at index:", result )
  
# How to use find()
if (word.find('pawan') != -1):
    print ("Contains given substring ")
else:
    print ("Doesn't contains given substring")
    
#defining string and substring
str1 = "This dress looks good; you have good taste in clothes."
substr = "good"

#occurrence of word 'good' in whole string
print(str1.count(substr))

#occurrence of word 'good' from index 0 to 25
print(str1.count(substr,0,25))

#occurrence of word 'good' from index 0 to 10
print(str1.count(substr,0,10))

print ("Introduction","end")

filename = '/home/pi/list.txt'
# writing to file
file2 = open(filename, 'w')
file2.writelines(word)
file2.close()

# Using readlines()
filename = '/home/pi/AAAsortlist.txt'
filename = '/home/pi/sortlist.txt'

print("Process",filename)

totalsize = 0
asize = 0

levelsep = "/"

levelmax = -1000 #pick a small number
levelmin = 10000 #pick a large number

count = 0
fcount = 0
dcount = 0

#Does 'file' exist?
if os.path.isfile(filename):

    file1 = open(filename, 'r')
    print("file openned")

    if file1.readable():

        for line in file1.readlines():
            
            count += 1
            atext=line.split()

            if count == 1:
                
                totalsize = int(atext[0])
                              
            if count > 1:

                ccount=len(line)-1
                
                thisdict1["size"].append(atext[0])
                #print(is_integer(100))
                ## True

                thisdict1["name"].append(atext[1])
                
                if os.path.isdir(atext[1]):
                    dcount += 1
                    thisdict1["type"].append("directory")
                else:
                    fcount += 1
                    thisdict1["type"].append("file")
                    
                level=atext[1].count(levelsep)
                if levelmax < level:
                    levelmax = level
                if levelmin > level:
                    levelmin = level
                thisdict1["level"].append(level)
                
else:
    print("Error:\tInput file ",filename," does not exist!")
    
file1.close()
print("file closed")

print("Analysis start")
print(count,"lines and",totalsize,"bytes processed.")

if dcount == 1:
    print(dcount,"directory")
else:
    print(dcount,"directories")

if fcount == 1:
    print(fcount,"file")
else:
    print(fcount,"files")

print("Maximum level:",levelmax)
print("Minimum level:",levelmin)

print("all values in dictionary:")

i_list = list(thisdict1.items())
print(i_list)
print(type(i_list))
# [('key1', 1), ('key2', 2), ('key3', 3)]
# <class 'list'>

print(i_list[0])
print(type(i_list[0]))
# ('key1', 1)
# <class 'tuple'>
print(i_list[1])
print(type(i_list[1]))
print(i_list[2])
print(type(i_list[2]))

print("Analysis end")

print ("Program","end")

