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
  process.wait()
  time.sleep(0.1)
