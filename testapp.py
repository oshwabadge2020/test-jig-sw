from jig import TestJig as Jig
import time

jig = Jig()

jig.EraseDevice()
jig.ProgramBootloader()
time.sleep(5)
jig.ProgramMicroPython()
