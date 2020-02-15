from jig import TestJig as Jig
import time

jig = Jig()

# Try and program the device
print("Attempting to flash the bootloader onto the badge")
jig.EraseDevice()
if not jig.ProgramBootloader():
	print("Failed to flash the bootloader!!")
	exit(-1)

#Device programmed.
#Reset device so it's in a known state
print("Resettign device into a known state")
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


print("Loading Test Code onto Badge")
if not jig.ProgramTestCode():
	print("Failed to load test code!")
	exit(-3)
print("Test Code loaded succesfully")

