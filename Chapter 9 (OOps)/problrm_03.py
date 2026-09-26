# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self, trainNo):
        print(f"TrainNo; {self.trainNo} is runing on time")

    def getfare(self, fro, to):
        print(f"Ticket fare of Train No: {self.trainNo} from {fro} to {to} is {random.randint(100, 200)}")


t = Train(638674)
t.book("Jhajjar", "Delhi")
t.getfare("Jhajjar", "Delhi")
t.getStatus(638674)
