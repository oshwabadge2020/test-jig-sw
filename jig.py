import os
import time

class TestJig:
	def __init__(self):
		pass

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
		if self.waitForDrive("BADGEBOOT"):
			os.system("cp binaries/*.uf2 /media/pi/BADGEBOOT/ ")

	def waitForDrive(self,drive,timeout=15):
		res=255
		while (res!=0 or timeout<=0):
			res = os.system("cat /proc/mounts | grep %s"%(drive))
			time.sleep(1)
			timeout -= 1
		if (timeout<=0 or res !=0):
			return false
		return true



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
