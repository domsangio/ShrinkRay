import os
WORD_SIZE = 500
MAX_WORD_LENGTH = 6

# First step
# Loop through the text document and create the word map

word_map = {"and": 0,"the": 0}

filename = "alice29.txt"

f = open(filename,"r")

if f.mode == 'r':
    f1 = f.readlines()
    for line in f1:
        for word in line.split():
            if len(word) <= MAX_WORD_LENGTH and len(word) > 2:
                if word_map.get(word) == None:
                    if len(word_map) < WORD_SIZE:
                        word_map[word] = 1
                else:
                    word_map[word] += 1

# Created the word_map
# create the word map text onto the file

compress_file = "c_" + filename
new_file = open(compress_file, "w+")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")

count = 0

for word in word_map.keys():
    new_file.write(word + ",")
    word_map[word] = count
    count += 1
new_file.write("!!")

# loop through the file and write the converted into file
f1 = open(filename, "r").readlines()
for line in f1:
    for word in line.split():
        place = ""
        if word_map.get(word) != None:
            place = "/" + str(word_map[word]) + " " 
        else:
            place = word + " "
        new_file.write(place)
        new_file.write("\n")
