from jig import TestJig as Jig
import os
import time
from bcolors import TITLE,ERR,OK,STEP
from results import *
import logsheet

netlog=None
mac = ""
try:
	netlog = logsheet.LogSheet()
except:
	ERR("Count not connect to google docs sheet")

def appexit(result):
	#print(result)
	try:
		netlog.logResult(mac,result)
	except:
		ERR("Could not record test result")
	if result != results.PASS:
		time.sleep(8)
	else:
		time.sleep(2)
	os.system("echo %d > result.txt"%(result))
	exit(result)

jig = Jig()

#Read device MAC

# Try and program the device
STEP("Attempting to flash the bootloader onto the badge")
jig.EraseDevice()

mac = jig.GetMACviaSWD()
if mac==False:
	ERR("Could not read MAC Address")
	appexit(results.FAIL_BOOT)

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


STEP("Reading Test results from badge.")
results = jig.readDisplayQRCode()
if results!=False:
	appexit(results.FAIL_TEST)
	ERR("No Data from badge!")

if results['post']!=1:
	print(results)
	ERR("Badge reports failed POST!")
	appexit(results.FAIL_TEST)

if selftest['IIC']:
	print("IIC OK")
else:
	ERR("IIC Fail, We are missing devices. %s"%selftest['IIC'])
	appexit(results.FAIL_TEST)
OK("Badge Passed!")
appexit(results.PASS)
