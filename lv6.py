import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import board
import neopixel
from time import sleep


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pixels = neopixel.NeoPixel(board.D12, 5)
movie1 = ("/home/pi/Desktop/prodigynasty.mp4")
last_state1 = True
last_state2 = True

input_state1 = True


quit_video = True
player = False



while True:
    #Read states of inputs
    input_state1 = GPIO.input(17)
    
    quite_video = GPIO.input(18)

    #If GPIO(17) conectado a ground
    if input_state1 != last_state1:
        if (player and not input_state1):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
            

        elif not input_state1:
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
            
            print("inicio")
            pixels[1] = (255, 0, 0)
            sleep(1)
            pixels[1] = (0, 0, 0)
            pixels[0] = (255, 0, 0)
            sleep(1)
            pixels[0] = (0, 255, 0)
            pixels[1] = (0, 0, 0)
            sleep(1)
            pixels[0] = (0, 0, 0)
            pixels[1] = (0, 255, 0)
            sleep(1)
            pixels[0] = (0, 0, 255)
            pixels[1] = (0, 0, 0)
            sleep(1)
            pixels[0] = (0, 0, 255)
            pixels[1] = (0, 0, 0)
            sleep(1)
            pixels[0] = (100, 0, 0)
            pixels[1] = (100, 0, 0)
            sleep(1)
            pixels[0] = (0, 100, 0)
            pixels[1] = (0, 100, 0)
            sleep(1)
            pixels[0] = (0, 0, 100)
            pixels[1] = (0, 0, 100)
            sleep(1)
            pixels[0] = (0, 0, 0)
            pixels[1] = (0, 0, 0)
            print("final")
            

  

  

    #GPIO(24) cerrar omxplayer manual - used during debug
    if quit_video == False:
        os.system('killall omxplayer.bin')
        player = False

    #Set last_input states
    last_state1 = input_state1
    

