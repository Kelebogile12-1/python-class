#Create file
myfile =open ('myfile.txt','w')
# Printing file name 
print('Name:',myfile.name)
#Checking if file is closed
print('Is closed',myfile.closed)
#Checking the mode of file
print('Mode',myfile.mode)
#Writing to file
myfile.write('Its Monday its going to be a hectic day\n')
myfile.write ('Monday motivation:Do not stress my child friday is coming tomorrow')
# Closing File
myfile.close()
print('Is closed',myfile.closed)

myfile = open('myfile.txt','a')
myfile.write('Keep going my child')
myfile.close()

#Read from file
myfile =open('myfile.txt','r+')
text=myfile.read(100)
print('File content\n' , text)



#create file
hobbies_file =open ('hobbies.txt','w')
hobbies_file .write('Let me tell you about my hobbies:/n')
hobbies_file.write('1. Coding in Python\n')
hobbies_file.write('2. Playing tennis\n')
hobbies_file.write('3. Watching movies\n')
hobbies_file.write('4. Reading books\n')
hobbies_file.close()

# Append another hobbies
hobbies_file = open('hobbies.txt', 'a')
hobbies_file.write('\n5. Listening to music')
hobbies_file.close()

# Read from the file
hobbies_file = open('hobbies.txt', 'r+')
content = hobbies_file.read(200)
print('Hobbies file content:\n', content)

