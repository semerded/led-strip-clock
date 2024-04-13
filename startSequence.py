import neopixel, time
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
def startSequence(neopixel: neopixel.NeoPixel):
    for color in colors:
        for index in range(60):
            neopixel[index] = color
            time.sleep(0.01)
    neopixel.fill((0,0,0))