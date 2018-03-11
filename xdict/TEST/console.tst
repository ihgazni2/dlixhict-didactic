from xdict.console import *
from xdict.jprint import pobj



# 1. paint(s,**kwargs)

# new_style_color_sec is a tuple_list
# [tuple,tuple,tuple.......]
# each tuple with the below format (start_index,end_index,foreground_color)
s = "却说钟会正与姜维谋反"
new_style_color_sec = [(0, 2, 'green'), (2, 5, 'yellow'), (5, 6, 'blue'),(6,8,'yellow'),(8,10,'red')]
paint(s,color_sec = new_style_color_sec)

![](Images/console.paint.0.png) 

# new_style_color_sec is a list_stlye_dict(ltdict), index start from 1
# { 1:tuple,2:tuple,3:tuple .......}
# each tuple with the below format (start_index,end_index,foreground_color)
# important : end_index is included ! 
# for example (0,3) means 0 ,1,2,3 !  
# 3 is included !!
s = "却说钟会正与姜维谋反"
old_style_color_sec = {1: (0, 1, 'green'), 2: (2, 4, 'yellow'), 3: (5, 5, 'blue'), 4: (6, 7, 'yellow'), 5: (8, 9, 'red')}
paint(s,color_sec = old_style_color_sec)

![](Images/console.paint.1.png) 



# 2. paint_singleline(line,color,**kwargs)

prefix = '<div>'
line = "the colored content"
suffix = '</div>'
paint_singleline(line,'blue',prefix=prefix,suffix=suffix)
paint_singleline(line,'blue',prefix=prefix,suffix=suffix,prefix_color='green',suffix_color='green')

![](Images/console.paint_singleline.0.png) 

# 3. paint_multilines(lines,colors,line_sp='\n')

lines = [
    'the first green line',
    'the second yellow line',
    'the third blue line'
]

colors = ['green','yellow','blue']
paint_multilines(lines,colors)

![](Images/console.paint_multilines.0.png) 




# 4. oldStylize(color_sec)
new_style_color_sec = [(0, 2, 'green'), (2, 5, 'yellow'), (5, 6, 'blue'),(6,8,'yellow'),(8,10,'red')]
old_style_color_sec = oldStylize(new_style_color_sec)
pobj(old_style_color_sec,fixed_indent=True)

![](Images/console.oldStylize.0.png) 



# 5. newStylize(color_sec)
old_style_color_sec = {1: (0, 1, 'green'), 2: (2, 4, 'yellow'), 3: (5, 5, 'blue'), 4: (6, 7, 'yellow'), 5: (8, 9, 'red')}
new_style_color_sec = newStylize(old_style_color_sec)
pobj(new_style_color_sec,fixed_indent=True)

![](Images/console.newStylize.0.png) 


# 6.

pobj(xdict.console.COLORS_MD)

![](Images/console.COLORS_MD.linux.0.png) 

![](Images/console.COLORS_MD.windows.0.png) 




#7 . standlize_color_sec(color_sec,COLORS_MD)
new_style_color_sec = [(0, 2, 'green'), (2, 5, 'yellow'), (5, 6, 'blue'),(6,8,'yellow'),(8,10,'red')]
internal_color_sec = standlize_color_sec(new_style_color_sec,COLORS_MD)
pobj(internal_color_sec,fixed_indent=True)

![](Images/console.standlize_color_sec.linux.0.png) 

![](Images/console.standlize_color_sec.windows.0.png) 


#only for linux
#8. ansi_8color_control(**kwargs)
#control = '\033[' + str(style)+ ";" +str(fg) +";"+str(bg) +"m"

#only for linux
#9. ansi_256color_control(**kwargs)
#control = '\033[38;5;' +str(fg) +"m" + '\033[48;5;' +str(bg) +"m"








# just for compatible to old code, use paint instead
10. paint_str(text,**kwargs)
# just for compatible to old code, use paint instead
11. print_str(text,**kwargs)









