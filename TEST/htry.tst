



from xdict.jprint import pobj
from xdict.jprint import pdir
from xdict.cmdline import Hentry
# init a Hentry
htry = Hentry(html_text=html_text)
# search via cmd 'ead met'

#nested output
html_entry = htry.query('ead met',style='nested')
