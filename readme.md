# florinsim
A monte-carlo simulation of the Forge of Empires Carnival mini-game

## Background
Forge of Empires is a popular mobile real-time strategy/turn-based strategy game for iOS and Android. My girlfriend made me play it and now I have no time for real people things.

## Motivation
Forge has little mini-games that pop up every couple months tracking special events, like Christmas or the superbowl. You can progress in the mini-games by completing quests in the main game.

At time of writing (March 1, 2018), the current mini-game for the next few days is based on Venice's Carnival, and includes a betting component. You earn tickets over time, and you can bet them on games of chance to win Florins, the mini-game currency. With Florins, you can buy main-game items.

![Forge of Empires](IMG_0837.PNG)

There are three bets you can make in the game of chance:
1) a sure thing bet, where one ticket wins a pot of 10 Florins with 100% probability.
2) a safe-ish bet, where one ticket wins the pot with 15% probability.
3) a long-shot bet where one ticket wins the pot with 5% probability. 

Bets (2) and (3) have a modification. While the pots start off at 50 and 100 Florins, respectively, each pot grows on failure: the (2) pot grows by 10 Florins each failed play, and the (3) pot grows by 15.

There's another modification - you're actually playing with "neighbors." If a "neighbor" has played the (3) bet a bunch of times, but failed, the pot might be relatively high for you to come in and scoop up. Similarly, if you play that bet a bunch and fail consistently, you've just raised the pot for your neighbor, potentially giving away steaks you've earned by playing.

And finally, there's one last modifier: you can choose to bet a ticket AND 20 florins from your current wallet in order to double the odds of winning bets (2) and (3).

## The Simulation
All of this is just complicated enough that I got curious about the best betting strategy, and decided to waste some otherwise productive billable hours on writing up a monte carlo simulation of a few possibilities. I came up with what you see here in about 45 minutes, not including documentation. 

I tested 5 strategies specifically:

1) The sure thing. This is basically a check that my code is sane - it should just be 10 Florins *n tickets played (it is)

2) Bet (2), 15% likelihood of winning a pot that starts at 50 Florins.

3) Bet (2), but with the modification that you pick "double my odds" at a cost of 20 Florins per bet

4) Bet (3), 5% likelihood of winning a pot that starts at 100 Florins

5) Same, but with the 20 Florin chance-doubler.

Additionally, I re-ran 2-5 above with a higher initial purse, to simulate the condition that you ONLY start betting when your neighbors have already sweetened the deal a bit.

All simulations started with n_tickets=10000, for the sake of getting a long-term expected payout. This leaves a lot to be desired, as noted below.

## Running the code yourself
1) install Python 2.7, or change the print statements for Python 3
2) `python florinsim.py`

## Conclusions
In the base-cases:
```
Tickets spent: 10000
Florins at start: 1000

Strategy 1: 10 florins, 100%
Final florins: 101000
Profit: 100000
Profit per ticket: 10.0

Strategy 2: 50+ florins, 15%
Initial Purse: 50
Final florins: 161690
Profit: 160690
Profit per ticket: 16.069

Strategy 2.5: 50+ florins, 30% with 20 florins
Initial Purse: 50
Final florins: 21920
Profit: 20920
Profit per ticket: 2.092

Strategy 3: 100+ florins, 5%
Initial Purse: 100
Final florins: 192295
Profit: 191295
Profit per ticket: 19.1295

Strategy 3.5: 100+ florins, 10% + 20 florins
Initial Purse: 100
Final florins: 38605
Profit: 37605
Profit per ticket: 3.7605
```
Takeaway: you definitely don't want to always-double, the profit is not there. If you're betting in the base-purse case, the 5% option (3) is actually higher payout long term, but for a reasonable and finite number of tickets, youre also much more likely to leave another player to bet on a huge pot you can't claim.

Higher-start cases (bets 2 and 3 at double their base pots when you start a betting round):
```
Tickets spent: 10000
Florins at start: 1000

Strategy 1: 10 florins, 100%
Final florins: 101000
Profit: 100000
Profit per ticket: 10.0

Strategy 2: 50+ florins, 15%
Initial Purse: 100
Final florins: 235350
Profit: 234350
Profit per ticket: 23.435

Strategy 2.5: 50+ florins, 30% with 20 florins
Initial Purse: 100
Final florins: 172260
Profit: 171260
Profit per ticket: 17.126

Strategy 3: 100+ florins, 5%
Initial Purse: 200
Final florins: 247315
Profit: 246315
Profit per ticket: 24.6315

Strategy 3.5: 100+ florins, 10% + 20 florins
Initial Purse: 200
Final florins: 128770
Profit: 127770
Profit per ticket: 12.777
```
You win more money in all cases, the F20 probability doubler becomes less of a screw job, and perhaps most importantly of all, you waste a whole bunch of IRL time and money waiting for your neighbors to bump the pot :)

## Future Work (that I'm not going to do)
This is hardly an exhaustive list of betting strategies, and doesn't anser a number of questions about what to do during individual conditions of the cases included. For example, what's the probability that, betting on (3), you leave other players to take a huge pot, thereby screwing yourself? That is, low n_tickets between resetting the pot to zero. Also for example, does it make sense to pay 20 Florins to double my odds if the 5% purse is all the way up at 1000 Florins? Probably - that's 20 Florins for a marginal expected profit of 50 florins, rather than 20 Florins for 2.5 in the base-case. Actually, the static break-even point in that case is a purse of 400 florins - in excess of F400, you should double-down.

Anyway, getting you to read all the way to this point is way more valuable than the in-game currency, so now that I've already broken my promise once, I'm going to leave it at that, for real. 