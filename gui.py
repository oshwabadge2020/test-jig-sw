#!/usr/bin/python
import thorpy
import pygame
import subprocess


application = thorpy.Application((0,0), "Badge Programmer")
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#vfile = open('fwver.txt','r')
#fwver = vfile.read()

fwver = thorpy.OneLineText.make("Firmware Version   :  %s" % (" ")) 
swver = thorpy.OneLineText.make("Provisioner Version:  %s" % (" ")) 

def getNewFW():
  exit(0)
  pass


def getNewProv():
  exit(0)
  pass

def programDev():
  pass




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
elements=[fwver,swver,division,ProgramDevice,UpdateFirmware,UpdateProvisioner])


thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
