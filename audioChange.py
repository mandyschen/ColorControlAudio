from subprocess import call

class VolumeChange:
    def maxVolume(self):
        call(["osascript -e 'set volume output volume 100'"], shell=True)
    def muteVolume(self):
        call(["osascript -e 'set volume output volume 0'"], shell=True)
    def raiseVolume(self):
        call(["osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'"], shell=True)
    def lowerVolume(self):
        call(["osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'"], shell=True)