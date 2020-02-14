from jig import TestJig as Jig

jig = Jig()

jig.EraseDevice()
jig.ProgramBootloader()
jig.ProgramMicroPython()
