import sys
from xdict.ide import *
from efuntool.efuntool import dflt_sysargv

def main():
    pre = dflt_sysargv("",1)
    verb = dflt_sysargv("return",2)
    suf = dflt_sysargv("",3)
    print(sys.argv,pre,verb,suf)
    creat_apis_from_verb(pre,verb,suf)

