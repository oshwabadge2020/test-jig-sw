from jig import TestJig as Jig
import os
import time
from bcolors import TITLE,ERR,OK,STEP
import results as r

jig = Jig()
os.system("echo NONE > result.txt")

# Try and program the device
STEP("Attempting to flash the bootloader onto the badge")
jig.EraseDevice()
if not jig.ProgramBootloader():
	ERR("Failed to flash the bootloader!!")
	exit(r.FAIL_BOOT)
OK("Bootloader Programmed Sucesfully")

#Device programmed.
#Reset device so it's in a known state
STEP("Attempting to Reset Badge")
if not jig.ResetDevice():
	ERR("Failed to reset device!!")
	exit(r.FAIL_RESET)
OK("Device Reset Sucesfully")

STEP("Attempting to load CircuitPython")
#Try and copy over the circuitpython uf2
if not jig.ProgramMicroPython():
	#Copy failed, Try again
	ERR("Failed to load CircuitPython, Attempting again.")
	if not jig.ProgramMicroPython():
		ERR("Failed to load CircuitPython a secnd time. Resetting Badge")
		time.sleep(2)
		jig.ResetDevice()
		time.sleep(2)
		if not jig.ProgramMicroPython():
			ERR("Failed to load CircuitPython a 3rd time, Badge Failed.")
			exit(r.FAIL_CPY)
OK("CircuitPython Loaded onto badge")


STEP("Loading Test Code onto Badge")
if not jig.ProgramTestCode():
	ERR("Failed to load test code!")
	exit(r.FAIL_TEST)
OK("Test Code loaded succesfully")

os.system("echo PASS > result.txt")
