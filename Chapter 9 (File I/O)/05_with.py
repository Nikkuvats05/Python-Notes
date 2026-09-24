f = open("file.txt")
print(f.read)
f.close()

# Same can be done with following method and we donot have to close the file at last it will do automatic

with open("file.txt") as f:
    print(f.read())

# All done no need to close the file