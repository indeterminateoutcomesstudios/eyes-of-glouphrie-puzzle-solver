import os
from distutils.core import setup
import py2exe

Mydata_files = []
for files in os.listdir('./images/'):
    file = './images/' + files
    if os.path.isfile(file): # skip directories
        f2 = 'images', [f1]
        Mydata_files.append(f2)

setup(
    console=['eyescalc.py'],
    data_files = Mydata_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)