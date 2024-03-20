import os

# R => Read
# A => Append
# W => Write
# X => Create

# Read - error if it does not exist

f = open("names.txt")
# print(f.read())
# print(f.read(4)) # first 4 chars
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

f.close()

try:
    f = open("names.txt")
    # print(f.read())
except:
    print("error: ")
finally:
    f.close()

# Append - creates the file if it does not exist

f = open("names.txt", "a")
f.write("\nNeil")
f.close()


f = open("names.txt", "r")
print(f.read())
f.close()

# Write (overwrite)

f = open("context.txt", "w")
f.write("I deleted all of the context.")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doe not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("jeet.txt"):
    f = open("jeet.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("jeet.txt"):
    os.remove("jeet.txt")

else:
    print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
    content = f.read()


with open("names.txt", "w") as f:
    f.write(content)
