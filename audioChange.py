from subprocess import call

class VolumeChange:
    def maxVolume():
        call(["osascript -e 'set volume output volume 100'"], shell=True)
    def muteVolume():
        call(["osascript -e 'set volume output volume 0'"], shell=True)
    def raiseVolume():
        call(["osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'"], shell=True)
    def lowerVolume():
        call(["osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'"], shell=True)