#!/usr/bin/python

from pathlib import Path

path = '.'

for path in Path(path).iterdir():

    print(path)
    
    #need to install path lib using pip :sudo pip install pathlib
    
