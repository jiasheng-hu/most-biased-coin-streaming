import coins
import algo
import timer

algoTimer = timer.Timer()
outputFile = open("results.csv", "wb")
outputFile.write("Delta, Time Used, Result\n")
diffs, results, times = [],[],[]
for i in range (500):
    coinSystem = coins.CoinSystem(500, special=True)
    diffs.append(int(coinSystem.getDelta()*1000)/1000.0)
    algoTimer.startTiming()
    result = algo.gameOfCoins(coinSystem, 0.995, 1)
    timeUsed = algoTimer.getCurrentTime()
    times.append(int(timeUsed*1000)/1000.0)
    results.append(result)
    outputFile.write(str(int(coinSystem.getDelta()*1000)/1000.0) + "," + str(int(timeUsed*1000)/1000.0) + "," + str(result) + "\n")

countTrue = 0
for result in results:
    if result:
        countTrue += 1

print("Accuracy is ", countTrue/1000.0)

totalTime = 0
for time in times:
    totalTime += time

print("Average time per run is ",totalTime/1000.0)
outputFile.close()
