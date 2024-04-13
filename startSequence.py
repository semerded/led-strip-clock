import neopixel
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
def startSequence(neopixel: neopixel):
    for color in colors:
        for index in range(60):
            neopixel[index] = color