import os
import subprocess
import time

while True:
  command = "python3 gui.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  time.sleep(2)
