import sys
from xdict.jprint import pobj
from efdir import fs

def main():
    obj = fs.rjson(sys.argv[1])
    pobj(obj)
