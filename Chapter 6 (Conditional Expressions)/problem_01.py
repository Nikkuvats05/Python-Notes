# spam filtring if given words or phases are used in sentences then its a spam -> "Make a lot of money",  "buy now", "subscribe it",  "click this"

p1= "Make a lot of money"
p2 = "buy now"
p3 = "subscribe it"
p4 = "click this"

message = input("Enter your comment = ")

if(p1 in message or p2 in message or p3 in message or p4 in message) :
    print("Its a spam comment")

else:
    print("Its safe")