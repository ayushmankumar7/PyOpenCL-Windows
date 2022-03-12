import sys 
import platform

def get_version():
    return sys.version_info[:2]

def get_arch():
    return platform.architecture()[0]