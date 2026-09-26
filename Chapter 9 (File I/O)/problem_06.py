# co[py the data of one file into another

with open("poem.txt") as f:
    content = f.read()

with open(("poem_copy.txt"), "w") as f:
    f.write(content)