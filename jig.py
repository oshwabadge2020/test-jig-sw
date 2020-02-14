import os
import time

class TestJig:
	def __init__(self):
		pass

	def ResetDevice(self):
		os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -c \"init\" -c \"reset run\" -c \"exit\"")
		return True

	def EraseDevice(self):
		os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/mass-erase.ocd")
		return True

	def ProgramBootloader(self):
		# Execute command.

		res = os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/flash-boot.ocd")
		if res == 0:
			return True
		return False

	def ProgramMicroPython(self):
		# Do we have the bootloader partition mounted?
		print("Waiting for BADGEBOOT...")
		if self.waitForDrive("BADGEBOOT"):
			time.sleep(5)
			print("Copying over Micropython...")
			os.system("cp temp/*.uf2 /media/pi/BADGEBOOT/ ")
			print("Done!")
		print("Waiting for CIRCUITPY")
		if self.waitForDrive("CIRCUITPY",to=10):
			return True
		#Sometimes the copy doesn't take on the first try
		os.system("cp temp/*.uf2 /media/pi/BADGEBOOT/ ")
		if self.waitForDrive("CIRCUITPY",to=40):
                        return True
		return False

	def waitForDrive(self,drive,to=15):
		timeout=to
		res=255
		while ( timeout>0):
			res = os.system("cat /proc/mounts | grep %s"%(drive))
			if res==0:
				print("Drive found")
				return True
			time.sleep(1)
			timeout -= 1
			print(timeout)
		
		print("Timed out waiting for %s"%(drive))
		return False

	def LoadTestScript(self):
		pass

	def GetVoltage(self,rail):
		pass

	def CheckVoltageRange(self,rail,vhigh,vlow):
		pass

	def GetCurrent(self,rail):
		pass

	def CheckCurrenRange(self,rail,high,low):
		pass

	def DisplayImageOnBadge(self,image):
		pass
