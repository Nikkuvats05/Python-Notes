# Find the line in which word "winner" is present in prob4 file

with open("prob4.txt") as f:
    lines = f.readlines()
lineno =1
for line in lines:
    if("winner" in line):
        print("Yes! winner is present in line = ", lineno)
        break
    lineno += 1
else:
    print("NO, winner is not present in file")