import os
import subprocess
import time

firstboot=True
while True:
  if firstboot:
    firstboot=False
    os.system("echo > result.txt")
  command = "python3 gui.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  time.sleep(2)
  os.system("xdotool mousemove 100 100 click 1")
  process.wait()
  time.sleep(0.1)
