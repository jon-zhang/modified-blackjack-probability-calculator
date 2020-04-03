import random
import numpy as np
import matplotlib.pyplot as plt



def roll(playerthres):
    
    playercount = 0
    hostcount = 0
    dice = 0
    while playercount < playerthres and playercount <= 100:
        dice = random.randint(1,101)
        playercount += dice
        print('Player rolled a {:.0f}'.format(dice))
    if playercount > 100:
        print("player had a {:.0f}. Host didn't roll. Host wins".format(playercount))
        return (0, 1)
    else:
        while hostcount < playercount and hostcount <= 100:
            dice = random.randint(1,101)
            hostcount +=dice
            print('Host rolled a {:.0f}'.format(dice))
        if hostcount > 100:
            print("Player had a {:.0f} and host had a {:.0f}. Player wins".format(playercount, hostcount))
            return (1, 0)
        elif hostcount == 100:
            print("Player had a {:.0f} and host had a {:.0f}. Nobody wins".format(playercount, hostcount))
            return (0, 0)
        else:
            print("player had a {:.0f} and host had a {:.0f}. Host wins".format(playercount,hostcount))
            return (0, 1)

def looproll(playerthres, sim):
    playerwin = 0
    hostwin = 0
    playercount = 0
    hostcount = 0
    dice = 0
    for i in range(sim):
        while playercount < playerthres and playercount <= 100:
            dice = random.randint(1,101)
            playercount += dice
        if playercount > 100:
            hostwin += 1
            #print("player had a {:.0f}. Host didn't roll. Host wins".format(playercount))
        else:
            while hostcount <= playercount and hostcount <= 100:
                dice = random.randint(1,101)
                hostcount +=dice
            if hostcount > 100:
                playerwin +=1
                #print("Player had a {:.0f} and host had a {:.0f}. Player wins".format(playercount, hostcount))
            elif hostcount == 100:
                playerwin +=0
                #print("Player had a {:.0f} and host had a {:.0f}. Nobody wins".format(playercount, hostcount))
            else:
                hostwin +=1
                #print("player had a {:.0f} and host had a {:.0f}. Host wins".format(playercount,hostcount))
        hostcount =0
        playercount =0
    #print("At a player threshold of {:.0f} and a simulation number of {:.0f}, the player won {:.0f} games and the host won {:.0f} games.".format(playerthres,sim,playerwin,hostwin))
    return playerwin/hostwin


#playerwin, hostwin = looproll(5, 500)
threshold = np.arange(1,101)
wratio1 = []
wratio2 = []
wratio3 = []
wratio4 = []
wratio5 = []
ratios = [wratio1, wratio2, wratio3, wratio4, wratio5]
playerwinratio = 0
for ratio in ratios:
    for i in range(1, 101):
        playerwinratio = looproll(i, 10000)
        ratio.append(playerwinratio)
npwratio1 = np.asarray(wratio1)
npwratio2 = np.asarray(wratio2)
npwratio3 = np.asarray(wratio3)
npwratio4 = np.asarray(wratio4)
npwratio5 = np.asarray(wratio5)
npratios = (npwratio1 + npwratio2 + npwratio3 + npwratio4 + npwratio5)/5
print(npratios)
plt.plot(threshold, npratios)
plt.show()




    