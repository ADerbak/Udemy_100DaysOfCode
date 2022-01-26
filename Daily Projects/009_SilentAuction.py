from replit import clear
#HINT: You can call clear() to clear the output in the console.
#import 009art

#print(art.logo)
print("Welcome to the secret auction program.")

auction = []
auction_game = True

def add_bidder(name_of_bidder, bid_amount):
  auction.append({
    "Name":name_of_bidder,
    "Bid": bid_amount
  })

while auction_game:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_bidder(name, bid)
  others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  if others == 'yes':
    clear()
  else:
    clear()
    auction_game = False

max_bid = 0
winner = ''

for i in range(0,len(auction)):
  if auction[i]["Bid"] > max_bid:
    max_bid = auction[i]["Bid"]
    winner = auction[i]["Name"]

print(f"The winner is {winner} with a bid of ${max_bid}!")