class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
	 CYAN = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ERR(st):
	print("%s%s%s%s"%(bcolors.FAIL,bcolors.BOLD,st,bcolors.ENDC))

def OK(st):
	print("%s%s%s%s"%(bcolors.OKGREEN,bcolors.BOLD,st,bcolors.ENDC))

def TITLE(st):
		print("%s%s%s%s"%(bcolors.WARNING,bcolors.BOLD,st,bcolors.ENDC))

def CMD():
		print("%s%s%s%s"%(bcolors.CYAN,"",st,bcolors.ENDC))

def STEP(st):
		print("\n\n%s%s%s%s%s\n"%(bcolors.UNDERLINE,bcolors.BOLD,bcolors.OKBLUE,st,bcolors.ENDC))

