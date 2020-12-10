import coins
import algo
import timer

algoTimer = timer.Timer()
diffs, results, times = [],[],[]
for i in range (100):
    coinSystem = coins.CoinSystem(100, special=True)
    diffs.append(int(coinSystem.getDelta()*1000)/1000)
    algoTimer.startTiming()
    result = algo.gameOfCoins(coinSystem, 0.99, 1)
    timeUsed = algoTimer.getCurrentTime()
    times.append(int(timeUsed*1000)/1000)
    results.append(result)

countTrue = 0
for result in results:
    if result:
        countTrue += 1

print(countTrue/100)

totalTime = 0
for time in times:
    totalTime += time

print(totalTime/100)