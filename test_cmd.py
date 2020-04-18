import os
import subprocess
import time

#os.system("echo Hello from the other side!")
#os.system(".py --led-cols=64 --led-rows=32 -b 25 -t 'Welcome to the hom$
#")

# Try creating a subprocess call
proc1 = subprocess.Popen(args=["sudo", 
"./image-scroller.py", "--led-cols", 64, 
"--led-rows", 32, "-b", 20, "-i", "you_got_this.png"])

time.sleep(360)
proc1.terminate()