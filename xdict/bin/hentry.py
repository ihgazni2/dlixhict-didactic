from xdict.jprint import pobj
from xdict.jprint import pdir
from xdict.cmdline import Hentry
from efuntool.efuntool import dflt_sysargv
import sys
from efdir import fs

html_text = fs.rfile(sys.argv[1])
match = dflt_sysargv('',2)
style = dflt_sysargv('flat',3)
# init a Hentry 
def main():
    htry = Hentry(html_text=html_text)
    html_entry = htry.query(match,style=style)

