"""
Blind Auction
Click "Open Preview" above to see this file rendered with the markdown.

Instructions
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

Welcome to the secret auction program. 
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no'.
yes
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.

The winner is Elon with a bid of $55000000000
Use your knowledge of Python dictionaries and loops to solve this challenge.

"""

from logo import logo

print(logo)
bid_list = []
auction = True
while auction:
    auction_bider = {}
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_bider[name] = bid
    bid_list.append(auction_bider)
    other_bider = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bider == "no":
        auction = False

bider = ""
highest_bid = 0

for bides in bid_list:
    for name, bid in bides.items():
        if bid > highest_bid:
            highest_bid = bid
            bider = name
print(f"The winner is {name} with a bid of ${highest_bid}")


# instructor solution below 👇
"""
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

"""
