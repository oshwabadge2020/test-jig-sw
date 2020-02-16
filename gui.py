#!/usr/bin/python
import thorpy
import pygame
import subprocess


application = thorpy.Application((480,730), "Badge Programmer")

#vfile = open('fwver.txt','r')
#fwver = vfile.read()

resultf = open('result.txt','r')
result = resultf.read()

fwver = thorpy.OneLineText.make("Firmware Version   :  %s" % (" ")) 
swver = thorpy.OneLineText.make("Provisioner Version:  %s" % (" ")) 

def getNewFW():
  exit(0)
  pass


def getNewProv():
  exit(0)
  pass

def programDev():
  command = "xterm -fn fixed -fullscreen -e %s" % "python3 testapp.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  exit(0)


icon = thorpy.Image("none.png")
if result=="PASS":
	icon = thorpy.Image("pass.png")

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
