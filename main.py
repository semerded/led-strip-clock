import board, neopixel
ledstrip = neopixel.NeoPixel(board.D18, 60, brightness = 0.1)

import time
def getTimeInList():
    return list([int(x) for x in time.ctime().split(" ")[3].split(":")])

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

import startSequence
startSequence.startSequence(ledstrip)

previousTime = getTimeInList()
for i in range(previousTime[1]):
    ledstrip[i] = colors[1]

while True:
    
    if (currentTime := getTimeInList()) != previousTime:
        if previousTime[0] != currentTime[1]:
            pass
        if previousTime[1] != currentTime[1]:
            ledstrip[currentTime[1]] = colors[1]
        if previousTime[2] != currentTime[2]:
            pass
        
        
        previousTime = currentTime
        
    time.sleep(0.1)