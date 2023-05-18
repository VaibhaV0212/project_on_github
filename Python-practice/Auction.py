bids = {}
bidding_finish = False

def highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""
    print('bidding record----->', bidding_record)
    for bidders in bidding_record:
        print('-------bidders---------', bidders)
        bid_amount = bidding_record[bidders]
        print('bid amount==>', bid_amount)
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidders
    print(f'Winner is {winner} with the highest bid of {highest_amount}')




while not bidding_finish:
    name = input('Enter bidder name:')
    price = int(input("Enter bidder's price:"))
    bids[name] = price
    print('bidssss==', bids)
    # print('bids[name] ======', bids[name] )
    new_bids = input('Are there any new bidders? "yes" or "No" ==> ').lower()
    if new_bids == 'no':
        bidding_finish = True
        highest_bidder(bids)

