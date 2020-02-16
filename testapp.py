from jig import TestJig as Jig
import os
import time
from bcolors import TITLE,ERR,OK,STEP
from results import *

def appexit(result):
	print(result)
	if result != results.PASS:
		time.sleep(8)
	else:
		time.sleep(2)
	os.system("echo %d > result.txt"%(result))
	exit(result)

jig = Jig()


# Try and program the device
STEP("Attempting to flash the bootloader onto the badge")
jig.EraseDevice()
if not jig.ProgramBootloader():
	ERR("Failed to flash the bootloader!!")
	appexit(results.FAIL_BOOT)
OK("Bootloader Programmed Sucesfully")

#Device programmed.
#Reset device so it's in a known state
STEP("Attempting to Reset Badge")
if not jig.ResetDevice():
	ERR("Failed to reset device!!")
	appexit(results.FAIL_RESET)
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
			appexit(results.FAIL_CPY)
OK("CircuitPython Loaded onto badge")


STEP("Loading Test Code onto Badge")
if not jig.ProgramTestCode():
	ERR("Failed to load test code!")
	appexit(results.FAIL_TEST)
OK("Test Code loaded succesfully")

appexit(results.PASS)
