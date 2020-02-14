import os

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
		if os.system("cat /proc/mounts | grep BADGEBOOT") == 0:
			os.system("cp binaries/*.uf2 /media/pi/BADGEBOOT/ ")
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
