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
############################################################################

import os

# def is_integer(n):
#     try:
#         float(n)
#     except ValueError:
#         return False
#     else:
#         return float(n).is_integer()
# 
print ("Start...")

thisdict = {
  "name": [],
  "type": [],
  "size": [],
  "level": []
  }

print("Setup[",thisdict,"]")
#      Setup[
#      {'name': [], 'type': [], 'size': []}
#      ]
       
sepStr = "/"

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

filename = '/home/pi/list.txt'
# writing to file
file2 = open(filename, 'w')
file2.writelines(word)
file2.close()

# Using readlines()
filename = '/home/pi/AAAsortlist.txt'
filename = '/home/pi/sortlist.txt'

totalsize = 0
asize = 0

count = 0

