with open('Sample_File.txt', 'w') as file:
    file.write("Hi, I'm Shivika, I'm 13 years old, studying in 8th grade.")
    file.close()

with open('Sample_File.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()

import os
if os.path.exists('My_File.txt'):
    print("My_File.txt exists.")
else:
    print("My_File.txt does not exist.")
    with open('My_File.txt', 'w') as file:
        file.write("Hi, I'm Shivika, I'm 13 years old, studying in 8th grade.")


if os.path.exists('sample.doc.txt'):
    os.remove('sample.doc.txt')
    print("sample.doc.txt has been deleted.")
else:
    print("sample.doc.txt does not exist.")
