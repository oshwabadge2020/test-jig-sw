import os
import time
from bcolors import TITLE,ERR,OK,CMD
import json

class TestJig:
	def __init__(self):
		pass

	def ResetDevice(self):	
		TITLE("Resetting Device using SWD")
		time.sleep(2)
		self.execute("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -c \"init\" -c \"reset run\" -c \"exit\"")
		time.sleep(2)
		return True

	def EraseDevice(self):
		TITLE("Erasing Device using SWD..")
		self.execute("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/mass-erase.ocd")
		return True

	def ProgramBootloader(self):
		# Execute command.
		TITLE("Programming device using SWD..")
		res = self.execute("openocd -s tcl -f openocd-scripts/swd-pi.ocd  -f openocd-scripts/flash-boot.ocd")
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
			self.execute("cp temp/*.uf2 /media/pi/BADGEBOOT/ ")
			TITLE("Done!")
		else:
			TITLE("Cound not find bootloader mass storage devic")
			return False
		TITLE("Waiting CircuitPython mass storage device")
		if self.waitForDrive("CIRCUITPY",to=10):
			TITLE("Found CircuitPython mass storage device")
			return True
		else:
			TITLE("Cound not find CircuitPython mass storage device")
			return False
		return False


	def ProgramApplication(self):
		TITLE("Copying over application files..")
		if self.execute("cp -vr temp/app/* `cat /proc/mounts | grep CIRCUIT |  awk -F ' ' '{print $2;}' `/") ==0:
			TITLE("Done!")
			return True
		return False

	def ProgramTestCode(self):
		TITLE("Copying over badge test files..")
		if self.execute("cp -vr test/* `cat /proc/mounts | grep CIRCUIT |  awk -F ' ' '{print $2;}' `/") == 0:
			TITLE("Done!")
			return True
		return False

	def waitForDrive(self,drive,to=15):
		timeout=to
		res=255
		while ( timeout>0):
			res = self.execute("cat /proc/mounts | grep %s"%(drive))
			if res==0:
				TITLE("Drive found")
				return True
			time.sleep(1)
			timeout -= 1
		print()
		
		TITLE("Timed out waiting for %s"%(drive))
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

	def updateJigCode(self):
		TITLE("Updating Jig Code to latest..")
		self.execute("git pull")

	def ProgramSafeModeImage(self):
		TITLE("Programming Safe Mode Image..")
		if self.waitForDrive("BADGEBOOT"):
			time.sleep(5)
			TITLE("Copying over Recovery Image...")
			res = self.execute("cp safe/safemode.uf2 /media/pi/BADGEBOOT/ ")
			TITLE("Done!")
			if res == 0:
				return True
		return False

	def readDisplayQRCode(self):
		TITLE("Reading Displayed QR code..")
		time.sleep(4)
		self.execute("rm testimg.png processed.png testimg.txt")
		self.execute("ffmpeg -f video4linux2 -s 1920x1080 -i /dev/video0 -vframes 1 testimg.png")
		self.execute("python3 processimg.py testimg.png")
		scanres = self.execute("zbarimg -q processed.png > testimg.txt")
		if scanres==0:
			rfile = open('testimg.txt','r')
			code = rfile.read()
			TITLE("Got data: %s"%(code))
			code = code.split(",")
			if len(code)>=1:
				d = {}
				for c in code:
					f = c.split(":")
					d[f[0]]=f[1]	
				return d
			return False
		TITLE("No Data Found")
		return False

	def DisplayImageOnBadge(self,image):
		pass

	def execute(self,cmd):
		CMD(cmd)
		return os.system(cmd)
