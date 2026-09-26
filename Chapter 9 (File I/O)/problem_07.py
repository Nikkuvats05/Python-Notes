# TEll either two files are identical or not 

with open("poem.txt") as f:
    c1 = f.read()

with open("poem_copy.txt") as f:
    c2 = f.read()

if(c1 == c2):
    print("Yes files are identical")
else:
    print("No, files are not identical")