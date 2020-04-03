# modified-blackjack-probability-calculator

The rules of modified blackjack are as follows:

Each roll the better must hit or stay (H/S)
The goal is for both players to hit as close to 100 as possible
If the host rolls higher than the better and doesn't bust over 100, the host wins
If the player hits the highest number and host busts, the host pays x2 of the bet
Players go first and host must try to beat the players highest rolls.

The python file simulates 10,000 games at each of 1-100 as the player score.
The simulation then generates a random number for the host and adheres to the game(keeps hitting until higher than player).
The output is the win ratio of the player at each of 1-100 and generates a graph to show what numbers the player has the highest chance of winning at.
The range seems to be around 54-62.
