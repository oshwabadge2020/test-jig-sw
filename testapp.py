from jig import TestJig as Jig
import time
from bcolors import TITLE,ERR,OK,STEP

jig = Jig()

# Try and program the device
STEP("Attempting to flash the bootloader onto the badge")
jig.EraseDevice()
if not jig.ProgramBootloader():
	print("Failed to flash the bootloader!!")
	exit(-1)

#Device programmed.
#Reset device so it's in a known state
STEP("Attempting to load CircuitPython")
time.sleep(2)
jig.ResetDevice()
time.sleep(2)

#Try and copy over the circuitpython uf2
if not jig.ProgramMicroPython():
	#Copy failed, Try again
	print("Failed to load CircuitPython, Attempting again.")
	if not jig.ProgramMicroPython():
		print("Failed to load CircuitPython a secnd time. Resetting Badge")
		time.sleep(2)
		jig.ResetDevice()
		time.sleep(2)
		if not jig.ProgramMicroPython():
			print("Failed to load CircuitPython a 3rd time, Badge Failed.")
			exit(-2)
print("CircuitPython Loaded onto badge")


STEP("Loading Test Code onto Badge")
if not jig.ProgramTestCode():
	print("Failed to load test code!")
	exit(-3)
print("Test Code loaded succesfully")

