#!/usr/bin/python
import thorpy
import pygame
import subprocess
import os
from results import *


application = thorpy.Application((480,730), "Badge Programmer")

#vfile = open('fwver.txt','r')
#fwver = vfile.read()

rfile = open('result.txt','r')
try
	res = int(rfile.read())
except ValueError:
	res=100

fwver = thorpy.OneLineText.make("Firmware Version   :  %s" % (res)) 
swver = thorpy.OneLineText.make("Provisioner Version:  %s" % (" ")) 

icon = thorpy.Image("none.png")

if res == results.PASS:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_BOOT:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_RESET:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_CPY:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_TEST:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_SCREEN:
	icon = thorpy.Image("fail.png")
elif res == results.FAIL_APP:
	icon = thorpy.Image("fail.png")
else:
	icon = thorpy.Image("none.png")


def getNewFW():
  #exit(0)
  icon.image="pass.png"
  pygame.display.update()
  pass


def getNewProv():
  exit(0)
  pass

def programDev():
  command = "xterm -fn fixed -fullscreen -e %s" % "python3 testapp.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  exit(0)




division = thorpy.Line.make(size=300, type_="horizontal") 
ProgramDevice = thorpy.make_button("Program Device",func = programDev)
ProgramDevice.set_size((480,200))
ProgramDevice.set_font_size(40)

UpdateFirmware = thorpy.make_button("Load Latest Firmware",func=getNewFW)
UpdateFirmware.set_size((480,140))
UpdateFirmware.set_font_size(40)

UpdateProvisioner = thorpy.make_button("Update Provisioner",func=getNewProv)
UpdateProvisioner.set_size((480,140))
UpdateProvisioner.set_font_size(40)

background = thorpy.Background.make(
elements=[icon,fwver,swver,division,ProgramDevice,UpdateFirmware,UpdateProvisioner])


thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
