import os
from art import logo


print(logo)
bids = {}
more_bids = "y"

while more_bids == "y":
    name = input("What is your name?:  ")
    amount = int(input("What is your bid?:  "))
    bids[name] = amount
    more_bids = input("Are there any more bids? 'y' for yes or any other key for no.").lower()
    os.system('cls')

highest_bidder = ""
highest_bid = 0

for _ in bids:
    if bids[_] > highest_bid:
        highest_bidder = _
        highest_bid = bids[_]

print(f"{highest_bidder} won with a bid of ${highest_bid}")

