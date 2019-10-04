import sys
from xdict.ide import *
from efuntool.efuntool import dflt_sysargv

def main():
    s = dflt_sysargv(1,1)
    print(indent(code,int(s)))

