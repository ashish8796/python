#Reading a File
f = open('/home/papa-ka-para/Documents/python/day-19/some_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)
'''When finished with the file, 
use the close method to free up any system resources taken up by the file'''

#Writing to a File
f = open('/home/papa-ka-para/Documents/python/day-19/some_file.txt', 'w')
file_data = f.write("Hello there!")
f.close()
print(file_data)

#Too Many Open Files
files = []
for i in range(10000):
    files.append(open('/home/papa-ka-para/Documents/python/day-19/some_file.txt', 'r'))
    print(i)
#With
'''Python provides a special syntax that auto-closes a file for you once you're finished using it.'''
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

#Calling the read Method with an Integer
with open('my_path/my_file.txt ') as file_name:
    print(file_name.read(number)) #any number to that character file  is  read

#Reading Line by Line
song = open('my_path/my_file.txt', 'r')
song.readline() #use python ide to execute this code
song.close()
print(song)

#Python will loop over the lines of a file using the syntax for line in file.
#Use to remove new line character .strip()
camelot_lines = []
with open("my_path/my_file.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
