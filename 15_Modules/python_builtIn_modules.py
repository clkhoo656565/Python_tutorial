#There are many availables build-in Python modules ready to be use for example logging, os, platform, datetime, ...
import platform

version = platform.version()
system = platform.system()
release = platform.release()
win32_ver = platform.win32_ver()
_platform = platform.platform()

print("Version: ", version)
print("System: ", system)
print("Release: ", release)
print("Win32_ver: ", win32_ver)
print("Platform: ", _platform)