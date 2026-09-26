# Tell word "winner"  is present in prob4 file or not

with open("prob4.txt") as f:
    con = f.read()

if "winner" in con:
    print("Yes! word winner is present file")
else:
    print("No word winner is not present file")