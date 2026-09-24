f = open("file.txt")

lines = f.readlines()
print(lines)

f.seek(0) # Upper puri file read krne ke bad curcer end me a gaya tha to curcer ko starting me le jane ke liye is fxn ka use hua

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4)

f.close()
