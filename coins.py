import numpy as np
import scipy as sci
import sys

class Coin:
    """
    docstring
    """
    def __init__(self, ID, bias):
        """
        name: name of the coin
        bias: the bias of the coin. We assume that the bias is one-sided, i.e. 0 <= bias <= 0.5. 
        If a coin has bias x, then, it will have probability (0.5+x) to come up with head, and (0.5-x) probability to come up with tail
        """
        self.ID = ID
        self.bias = bias
    '''
    Save memory
    '''
    def countHeads(self, num = 1):
        count = 0
        for i in range(num):
            randomNumber = np.random.rand() - 0.5
            if randomNumber <= self.bias:
                count += 1
        return count

    def toss(self, num = 1):
        """
        Return the result of [num] tosses in a numpy array, where 1 represents head and 0 represents tail.
        """
        results = []
        randomNumbers = np.random.uniform(low = -0.5, high = 0.5, size = num)
        for i in range (num):
            if randomNumbers[i] > self.bias:
                results.append(0)
            else:
                results.append(1)
        
        return np.array(results)

    def getID(self):
        return self.ID


class CoinSystem:
    def __init__(self, num, minDelta = 0):
        biases = []
        if minDelta > 0:
            biases.append(0.49)
            for i in range(1, num):
                biases.append(np.random.uniform(low = 0.0, high = 0.49-minDelta))
            biases = np.array(biases)
            np.random.shuffle(biases)
        else:
            biases = np.random.uniform(low = 0.0, high = 0.49, size = num)
        highestBias, mostBiasedCoinID, secondHighestBias = -1, -1, -1
        for i in range(num):
            if biases[i] > highestBias:
                highestBias = biases[i]
                mostBiasedCoinID = i
        self.mostBiasedCoinID = mostBiasedCoinID
        for i in range(num):
            if biases[i] > secondHighestBias and i != mostBiasedCoinID:
                secondHighestBias = biases[i]
        self.Delta = highestBias - secondHighestBias
        self.coins = []
        for i in range(num):
            self.coins.append(Coin(i, biases[i]))
        self.currentCoinID = 0
        self.coinsNumber = num

    def nextCoin(self):
        if self.currentCoinID >= self.coinsNumber:
            return None
        else:
            nextCoin = self.coins[self.currentCoinID]
            self.currentCoinID += 1
            return nextCoin
    
    def getDelta(self):
        return self.Delta

    def checkIfMostBiased(self, coinID):
        if coinID == self.mostBiasedCoinID:
            return True
        else:
            return False

    def reset(self):
        self.currentCoinID = 0


