import random

def did_i_win(p=.5):
    if random.random() < p:
        return True
    else:
        return False

tickets_to_spend = 10000
florins = 1000
florins_start = florins
print "Tickets spent: {}".format(tickets_to_spend)
print "Florins at start: {}".format(florins_start)

# Strategy 1, the sure thing
florins = florins_start
payout = 10
print ""
print "Strategy 1: 10 florins, 100%"
for ticket in range(0, tickets_to_spend):
    if did_i_win(p=1):
        florins += payout
print "Final florins: {}".format(florins)
print "Profit: {}".format(florins-florins_start)
print "Profit per ticket: {}".format(float((florins-florins_start))/float(tickets_to_spend))


# Strategy 2, 15% chance
# Ultra-long-term, about 16.3 florins per ticket.
florins = florins_start
payout_start = 50
payout = payout_start
print ""
print "Strategy 2: 50+ florins, 15%"
print "Initial Purse: {}".format(payout_start)
for ticket in range(0, tickets_to_spend):
    if did_i_win(p=.15):
        florins += payout
        payout = payout_start
    else:
        payout +=10
print "Final florins: {}".format(florins)
print "Profit: {}".format(florins-florins_start)
print "Profit per ticket: {}".format(float((florins-florins_start))/float(tickets_to_spend))

# This strategy sucks, uncomment to see for yourself.

# Strategy 2.5, 30% chance for 20 florins
florins = florins_start
payout_start = 50
payout = payout_start
print ""
print "Strategy 2.5: 50+ florins, 30% with 20 florins"
print "Initial Purse: {}".format(payout_start)
for ticket in range(0, tickets_to_spend):
    florins -= 20
    if did_i_win(p=.3):
        florins += payout
        payout = payout_start
    else:
        payout +=10
print "Final florins: {}".format(florins)
print "Profit: {}".format(florins-florins_start)
print "Profit per ticket: {}".format(float((florins-florins_start))/float(tickets_to_spend))

# Strategy 3, 5% chance
# Ultra-long-term, about 14.1 florins per ticket.
florins = florins_start
payout_start = 100
payout = payout_start
print ""
print "Strategy 3: 100+ florins, 5%"
print "Initial Purse: {}".format(payout_start)
for ticket in range(0, tickets_to_spend):
    if did_i_win(p=.05):
        florins += payout
        payout = payout_start
    else:
        payout +=15
print "Final florins: {}".format(florins)
print "Profit: {}".format(florins-florins_start)
print "Profit per ticket: {}".format(float((florins-florins_start))/float(tickets_to_spend))

# This strategy sucks, uncomment to see for yourself.

# Strategy 3.5, 10% chance + 20 florins
florins = florins_start
payout_start = 100
payout = payout_start
print ""
print "Strategy 3.5: 100+ florins, 10% + 20 florins"
print "Initial Purse: {}".format(payout_start)
for ticket in range(0, tickets_to_spend):
    florins -= 20
    if did_i_win(p=.1):
        florins += payout
        payout = payout_start
    else:
        payout +=15
print "Final florins: {}".format(florins)
print "Profit: {}".format(florins-florins_start)
print "Profit per ticket: {}".format(float((florins-florins_start))/float(tickets_to_spend))

# Test did_i_win

# answers = []
# trials = 100000
# for num in range(0, trials):
#     answers.append(did_i_win(p=1))

# print "N: {}".format(len(answers))
# print "Average: {}".format(float(sum(answers))/float(len(answers)))