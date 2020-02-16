import os
import subprocess
import time

while True:
  command = "python gui.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  time.sleep(2)
