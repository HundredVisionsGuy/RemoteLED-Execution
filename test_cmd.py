import os
import subprocess
import time
import image_scroller
import signal

#os.system("echo Hello from the other side!")
#os.system(".py --led-cols=64 --led-rows=32 -b 25 -t 'Welcome to the hom$
#")

# Try creating a subprocess call
proc1 = subprocess.Popen(args=["sudo", "python", 
"image_scroller.py", "--led-cols", "64", 
"--led-rows", "32", "-b", "20", "-i", "you_got_this.png"])
# Get the process id
pid = proc1.pid

time.sleep(10)

proc1.send_signal(signal.SIGINT)
if not proc1.poll():
    print("Process correctly halted")
proc1.terminate()
proc1.wait(5)