import os 

from src.utils import get_arch, get_version

dist_file = "src/dist"

def find_whl():
    arch = get_arch()[:2]
    version = str(get_version()[0]) + str(get_version()[1])
    for file in os.listdir(dist_file):
        if (version in file) and (arch in file):
            break 
    return file     

def install_pyopencl():
    whl = find_whl()
    os.system(f"pip install {dist_file}/{whl}")
    print("\n\n CONGRATULATIONS! PYOPENCL INSTALLED SUCCESSFULLY!! \n\n")