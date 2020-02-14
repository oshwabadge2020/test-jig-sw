from jig import TestJig as Jig
import time

jig = Jig()

jig.EraseDevice()
jig.ProgramBootloader()
time.sleep(2)
jig.ResetDevice()
time.sleep(2)
# Try and flash cPy
while not jig.ProgramMicroPython():
	#Device didn't take the FW, Reset it and try again.
	jig.ResetDevice()
	time.sleep(1)
	pass
