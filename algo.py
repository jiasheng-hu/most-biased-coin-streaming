import coins
import numpy as np

def calculateS(diff, delta, l):
    return 4.0/(diff ** 2)*np.log(1/delta)*(3**l)

def challengeKing(king, challenger, diff, delta, C, kingBudget):
    b = 4.0/(diff ** 2)*np.log(1/delta)*C + calculateS(diff, delta, 1)
    challengerBudget = 0
    kingBudget += b
    l = 1
    while (True):
        sl = int(calculateS(diff, delta, l))
        if kingBudget < sl:
            return (challenger, 0)
        kingBudget -= sl
        kingTossesCount, challengerTossesCount = king.countHeads(sl), challenger.countHeads(sl)
        if kingTossesCount > challengerTossesCount:
            return (king, kingBudget)
        l += 1
    pass

def gameOfCoins(coinSystem, delta, C):
    diff = coinSystem.getDelta()
    king = coinSystem.nextCoin()
    kingBudget = 0
    challenger = coinSystem.nextCoin()
    while (challenger != None):
        king, kingBudget = challengeKing(king, challenger, diff, delta, C, kingBudget)
        challenger = coinSystem.nextCoin()
    return coinSystem.checkIfMostBiased(king.getID())
