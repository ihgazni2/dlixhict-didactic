

from xdict.console import *


prefix = '<div>'
line = "the colored content"
suffix = '</div>'
paint_singleline(line,'blue',prefix=prefix,suffix=suffix)
paint_singleline(line,'blue',prefix=prefix,suffix=suffix,prefix_color='green',suffix_color='green')



lines = [
    'the first green line',
    'the second yellow line',
    'the third blue line'
]

colors = ['green','yellow','blue']
paint_multilines(lines,colors)




s = "却说钟会正与姜维谋反"
new_style_color_sec = [(0, 2, 'green'), (2, 5, 'yellow'), (5, 6, 'blue'),(6,8,'yellow'),(8,10,'red')]
paint(s,color_sec = new_style_color_sec)


old_style_color_sec = oldStylize(new_style_color_sec)
old_style_color_sec
paint(s,color_sec = old_style_color_sec)



