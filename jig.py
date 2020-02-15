import os
import time
from bcolors import TITLE,ERR,OK


class TestJig:
	def __init__(self):
		pass

	def ResetDevice(self):	
		TITLE("Resetting Device using SWD")
		time.sleep(2)
		os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -c \"init\" -c \"reset run\" -c \"exit\"")
		time.sleep(2)
		return True

	def EraseDevice(self):
		TITLE("Erasing Device using SWD..")
		os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/mass-erase.ocd")
		return True

	def ProgramBootloader(self):
		# Execute command.
		TITLE("Programming device using SWD..")
		res = os.system("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/flash-boot.ocd")
		if res == 0:
			return True
		return False

	def ProgramMicroPython(self):
		TITLE("Copying CircuotPython uf2 over USB")
		# Do we have the bootloader partition mounted?
		TITLE("Waiting for bootloader mass storage device...")
		if self.waitForDrive("BADGEBOOT"):
			time.sleep(5)
			TITLE("Copying over Micropython...")
			os.system("cp temp/*.uf2 /media/pi/BADGEBOOT/ ")
			OK("Done!")
		else:
			ERR("Cound not find bootloader mass storage devic")
			return False
		TITLE("Waiting CircuitPython mass storage device")
		if self.waitForDrive("CIRCUITPY",to=10):
			OK("Found CircuitPython mass storage device")
			return True
		else:
			ERR("Cound not find CircuitPython mass storage device")
			return False
		return False


	def ProgramApplication(self):
		TITLE("Copying over application files..")
		os.system("cp temp/app/* `cat /proc/mounts | grep CIRCUIT |  awk -F ' ' '{print $2;}' `/")
		OK("Done!")
		return True

	def ProgramTestCode(self):
		TITLE("Copying over badge test files..")
		os.system("cp temp/test/code.py `cat /proc/mounts | grep CIRCUIT |  awk -F ' ' '{print $2;}' `/")
		OK("Done!")
		return True

	def waitForDrive(self,drive,to=15):
		timeout=to
		res=255
		while ( timeout>0):
			res = os.system("cat /proc/mounts | grep %s"%(drive))
			if res==0:
				OK("Drive found")
				return True
			time.sleep(1)
			timeout -= 1
			print(timeout,end='.')
		print()
		
		ERR("Timed out waiting for %s"%(drive))
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
