# Python has functions for creating, reading, updating, and deleting files.

myFile = open("demo.txt","w")

print('Name: ',myFile.name)
print('Closed: ',myFile.closed)
print('Opning Mode: ',myFile.mode)

myFile.write("I Love Allah")
myFile.close()
myFile = open("demo.txt","a")
myFile.write(" & I Love My Mom")
myFile.close()

myFile = open("demo.txt","r+")
text = myFile.read(1)
print(text)
