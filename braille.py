# imports libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# sets braille dots to corresponding pin numbers
one =  18
two = 23
three = 15
four = 24
five = 14
six = 25

# sets time a braille character is displayed in seconds
displayTime = 1

# creates a matrix for the keypad
keypadMatrix = [ ['a','b','c','d'],
	  	 ['e','f','g','h'],
	  	 ['i','j','k','l'],
	  	 ['m','n','o','p'] ]

# creates arrays for the row and column pin numbers
row = [21,20,16,12]
col = [1,7,8,26]

# sets up the rows and column pins
for j in range(4):
	GPIO.setup(col[j], GPIO.OUT)
	GPIO.output(col[j],1)

for i in range(4):
	GPIO.setup(row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# sets up the braille dot pins as output pins
GPIO.setup(one,GPIO.OUT)
GPIO.setup(two, GPIO.OUT)
GPIO.setup(three,GPIO.OUT)
GPIO.setup(four,GPIO.OUT)
GPIO.setup(five, GPIO.OUT)
GPIO.setup(six, GPIO.OUT)

# function for the braille character 'a'
def aActuate():
	GPIO.output(one, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)

# function for the braille character 'b'
def bActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)

# function for the braille character 'c'
def cActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)

# function for the braille character 'd'
def dActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)

# function for the braille character 'e'
def eActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)

# function for the braille character 'f'
def fActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)

# function for the braille character 'g'
def gActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)

# function for the braille character 'h'
def hActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)

# function for the braille character 'i'
def iActuate():
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(three,GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)

# function for the braille character 'j'
def jActuate():
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)

# function for the braille character 'k'
def kActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

# function for the braille character 'l'
def lActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

# function for the braille character 'm'
def mActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

# function for the braille character 'n'
def nActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

# function for the braille character 'o'
def oActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(four, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(four, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

# function for the braille character 'p'
def pActuate():
	GPIO.output(one, GPIO.HIGH)
	GPIO.output(two, GPIO.HIGH)
	GPIO.output(three, GPIO.HIGH)
	GPIO.output(five, GPIO.HIGH)
	time.sleep(displayTime)
	GPIO.output(one, GPIO.LOW)
	GPIO.output(two, GPIO.LOW)
	GPIO.output(three, GPIO.LOW)
	GPIO.output(five, GPIO.LOW)

try:
	# loops forever until broken
	while(True):
		for j in range(4):
			GPIO.output(col[j],0)

			for i in range(4):
				if GPIO.input(row[i]) == 0:
					"""
					prints letter typed into keypad
					to terminal 
					"""
					print keypadMatrix[i][j]

					"""
					displays corresponding braille chracter
					to key pressed on keypad
					"""
					if i == 0 and j == 0:
						aActuate()
					if i == 0 and j == 1:
						bActuate()
					if i == 0 and j == 2:
						cActuate()
					if i == 0 and j == 3:
						dActuate()
					if i == 1 and j == 0:
						eActuate()
					if i == 1 and j == 1:
						fActuate()
					if i == 1 and j == 2:
						gActuate()
					if i == 1 and j == 3:
						hActuate()
					if i == 2 and j == 0:
						iActuate()
					if i == 2 and j == 1:
						jActuate()
					if i == 2 and j == 2:
						kActuate()
					if i == 2 and j == 3:
						lActuate()
					if i == 3 and j == 0:
						mActuate()
					if i == 3 and j == 1:
						nActuate()
					if i == 3 and j == 2:
						oActuate()
					if i == 3 and j == 3:
						pActuate()
					while GPIO.input(row[i]) == 0:
						pass
			GPIO.output(col[j],1)

except KeyboardInterrupt:
	GPIO.cleanup()
