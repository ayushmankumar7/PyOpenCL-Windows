from utils import get_arch, get_version 
from main import find_whl, install_pyopencl

print(get_version(), get_arch())
print(type(get_version()), type(get_arch()))
print(find_whl())
install_pyopencl()