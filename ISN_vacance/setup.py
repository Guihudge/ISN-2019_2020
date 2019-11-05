import os
import sys

try:
    import PIL
except ImportError:
    os.system("py -m pip install Pillow")

os.system(sys.executable + " main.py")
