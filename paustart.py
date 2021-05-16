import subprocess
import os
import time
import signal

def go_exit(sig,stack):
    proccess.kill()
    exit(0)

def go_exit2(sig,stack):
    if proccess.poll() is not None:
        exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT,go_exit)
    signal.signal(signal.SIGCHLD,go_exit2)
    global proccess
    path='./'
    proccess = subprocess.Popen(['vlc', path + 'video.mp4'])
    time.sleep(3)
    while 1:
        os.system('playerctl pause vlc')
        time.sleep(4)
        os.system('playerctl play vlc')
        time.sleep(3)
