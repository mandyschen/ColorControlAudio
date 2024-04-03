# import subprocess
# import re
from subprocess import call

# def getVolume():
#     cmd = "osascript -e 'get volume settings'"
#     process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
#     output = process.stdout.strip().decode('ascii')

#     pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
#                         r"alert volume:(\d+), output muted:(true|false)")
#     volume, _, _, muted = pattern.match(output).groups()

#     volume = int(volume)
#     muted = (muted == 'true')

#     return 0 if muted else volume

class VolumeChange:
    # currentVolume = getVolume()
    def maxVolume():
        call(["osascript -e 'set volume output volume 100'"], shell=True)
    def muteVolume():
        call(["osascript -e 'set volume output volume 0'"], shell=True)
    # def raiseVolume():
    #     call(["osascript -e 'f'set volume output volume {currentVolume}''"], shell=True)