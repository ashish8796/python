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

