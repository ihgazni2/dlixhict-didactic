import xdict.utils
import sys
import copy


def oldStylize(color_sec):
    '''
        for compatible with old code
        old_style_color_sec = {1: (0, 11, 'white'), 2: (12, 19, 'blue'), 3: (20, 21, 'white')}
        new_style_color_sec = [(0, 12, 'white'), (12, 20, 'blue'), (20, 22, 'white')]
        oldStylize(new_style_color_sec)
    '''
    if(xdict.utils.is_dict(color_sec)):
        return(copy.deepcopy(color_sec))
    else:
        pass
    new = {}
    for i in range(0,color_sec.__len__()):
        sec = color_sec[i]
        new[i+1] = copy.deepcopy(list(sec))
        new[i+1][1] = sec[1] - 1
        new[i+1] = tuple(new[i+1])
    return(new)



def newStylize(color_sec):
    '''
        for compatible with old code
        old_style_color_sec = {1: (0, 11, 'white'), 2: (12, 19, 'blue'), 3: (20, 21, 'white')}
        new_style_color_sec = [(0, 12, 'white'), (12, 20, 'blue'), (20, 22, 'white')]
        newStylize(old_style_color_sec)
    '''
    if(xdict.utils.is_list(color_sec)):
        return(copy.deepcopy(color_sec))
    else:
        pass
    new = []
    for i in range(0,color_sec.__len__()):
        sec = color_sec[i+1]
        sec = copy.deepcopy(list(sec))
        sec[1] = sec[1] + 1
        sec = tuple(sec)
        new.append(sec)
    return(new)




def standlize_color_sec(color_sec,COLORS_MD):
    #now we can accept either new_style_color_sec or old_style_color_sec
    #the internal function use old_style_color_sec
    color_sec = oldStylize(color_sec)
    new = {}
    for seq in color_sec:
        sec = color_sec[seq]
        color = sec[2]
        if(xdict.utils.is_str(color)):
            color = color.lower()
            if(xdict.utils.is_win()):
                color = color.replace('bright','light')
            else:
                color = color.replace('light','bright')
            color = COLORS_MD[color]
        new[seq] = copy.deepcopy(list(sec))
        new[seq][2] = color
        new[seq] = tuple(new[seq])
    return(new)


if(xdict.utils.is_win()):
    from ctypes import *
    from win32con import *
    
    COLORS_MD = {
     'darkgray': 9,
     'lightblue': 10,
     'brightblue':10,
     'magenta': 6,
     'default': 0,
     'lightmagenta': 14,
     'black': 1,
     'cyan': 4,
     'red': 5,
     'lightcyan': 12,
     'brown': 7,
     'lightgreen': 11,
     'lightred': 13,
     'blue': 2,
     'yellow': 15,
     'lightgray': 8,
     'white': 16,
     'green': 3,
      0: 'default',
     1: 'black',
     2: 'blue',
     3: 'green',
     4: 'cyan',
     5: 'red',
     6: 'magenta',
     7: 'brown',
     8: 'lightgray',
     9: 'darkgray',
     10: 'lightblue',
     11: 'lightgreen',
     12: 'lightcyan',
     13: 'lightred',
     14: 'lightmagenta',
     15: 'yellow',
     16: 'white'
    }
    
    
    CloseHandle = windll.kernel32.CloseHandle
    GetStdHandle = windll.kernel32.GetStdHandle
    GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
    SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
    
    
    STD_OUTPUT_HANDLE = -11
    
    class COORD(Structure):
        _fields_ = [
            ('X', c_short),
            ('Y', c_short),
        ]
    
    class SMALL_RECT(Structure):
        _fields_ = [
            ('Left', c_short),
            ('Top', c_short),
            ('Right', c_short),
            ('Bottom', c_short),
        ]
    
    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
        _fields_ = [
            ('dwSize', COORD),
            ('dwCursorPosition', COORD),
            ('wAttributes', c_uint),
            ('srWindow', SMALL_RECT),
            ('dwMaximumWindowSize', COORD),
        ]
    
    def paint_str(text,**kwargs):
        '''for compatible with old code'''
        return(text)    

    def print_str(text,**kwargs):
        hconsole = GetStdHandle(STD_OUTPUT_HANDLE)
        cmd_info = CONSOLE_SCREEN_BUFFER_INFO()
        GetConsoleScreenBufferInfo(hconsole, byref(cmd_info))
        old_color = cmd_info.wAttributes
        if('colors_md' in kwargs):
            colors_md = kwargs['colors_md']
        else:
            colors_md = COLORS_MD
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 16
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 1
        if(xdict.utils.is_int(fg)):
            pass
        else:
            fg = colors_md[fg]
        if(xdict.utils.is_int(bg)):
            pass
        else:
            bg = colors_md[bg]
        if('single_color' in kwargs):
            single_color = kwargs['single_color']
            if(xdict.utils.is_str(single_color)):
                single_color = single_color.lower()
                single_color = single_color.replace('bright','light')
                if(single_color in COLORS_MD):
                    single_color = COLORS_MD[single_color]
                else:
                    print("please input correct color name")
                    pass
            elif(xdict.utils.is_int(single_color)):
                pass
            else:
                print("color must be name or int ")
                pass
        else:
            single_color = None
        ####color_sec multicolor for string (si,ei,fg,bg,style), ei is included
        ####"ab" +"bc"
        ####color_sec = {1:(0,1,2),2:(2,3,4)}
        if('color_sec' in kwargs):
            color_sec = kwargs['color_sec']
        else:
            color_sec = None
        if(color_sec):
            color_sec = standlize_color_sec(color_sec,COLORS_MD)
            color_sec_len = color_sec.__len__()
            for i in range(1,color_sec_len + 1):
                ele = color_sec[i]
                si = color_sec[i][0]
                ei = color_sec[i][1]
                tmpfg = color_sec[i][2]
                length = ele.__len__()
                if(length == 3):
                    tmpbg = bg
                elif(length == 4):
                    tmpbg = color_sec[i][3]
                else:
                    tmpbg = color_sec[i][3]
                tmpfg = (tmpfg -1) & 0x0f
                tmpbg = ((tmpbg -1)<<4) & 0xf0
                sec = text[si:ei+1]
                SetConsoleTextAttribute(hconsole, tmpfg + tmpbg)
                #dont use print("xxxx",end=""),important!
                sys.stdout.write(sec)
                sys.stdout.flush()
            SetConsoleTextAttribute(hconsole, old_color)
            print("")
        else:
            fg = single_color
            bg = bg
            fg = (fg -1) & 0x0f
            bg = ((bg -1)<<4) & 0xf0
            SetConsoleTextAttribute(hconsole, fg + bg)
            print(text)
            SetConsoleTextAttribute(hconsole, old_color)
else:
    #for compatible with old code
    def print_str(text,**kwargs):
        print(text)
    def paint_str(orig_string,**kwargs):
        '''
            currently only support 8 color name,
            if using 256 color need using color number
        '''
        default =  "\033[0m"
        painted_string = default
        #####mode 
        if('mode' in kwargs):
            mode = kwargs['colors']
        else:
            mode = 8
        if(mode == 8):
            color_control = ansi_8color_control
        elif(mode == 256):
            color_control = ansi_256color_control
        else:
            print("mode : " +mode +"not supported!,fallback to 8color ")
            color_control = ansi_8color_control
        ######color name<->number mapping
        if('colors' in kwargs):
            colors = kwargs['colors']
        else:
            colors = COLORS_MD
        ####singlecolor for string
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 30
        if("style" in kwargs):
            style = kwargs['style']
        else:
            style = 1
        if('single_color' in kwargs):
            single_color = kwargs['single_color']
            if(xdict.utils.is_str(single_color)):
                single_color = single_color.lower()
                single_color = single_color.replace('light','bright')
                if(single_color in COLORS_MD):
                    single_color = COLORS_MD[single_color]
                else:
                    print("please input correct color name")
                    pass
            elif(xdict.utils.is_int(single_color)):
                pass
            else:
                print("color must be name or int ")
                pass
        else:
            single_color = None
        ####color_sec multicolor for string (si,ei,fg,bg,style), ei is included
        ####"ab" +"bc"
        ####color_sec = {1:(0,1,'blue'),2:(2,3,'green')}
        if('color_sec' in kwargs):
            color_sec = kwargs['color_sec']
        else:
            color_sec = None
        if(color_sec):
            color_sec = standlize_color_sec(color_sec,COLORS_MD)
            color_sec_len = color_sec.__len__()
            for i in range(1,color_sec_len + 1):
                ele = color_sec[i]
                si = color_sec[i][0]
                ei = color_sec[i][1]
                fg = color_sec[i][2]
                length = ele.__len__()
                if(length == 3):
                    color = color_control(fg=fg)
                elif(length == 4):
                    bg = color_sec[i][3]
                    color = color_control(fg=fg,bg=bg)
                else:
                    bg = color_sec[i][3]
                    style = color_sec[i][4]
                    color = color_control(fg=fg,bg=bg,style=style)
                sec = ''.join((color,orig_string[si:ei+1]))
                painted_string = ''.join((painted_string,sec))
            painted_string = ''.join((painted_string,default))
        else:
            fg = single_color
            bg = bg
            style = style
            color = color_control(fg=fg,bg=bg,style=style)
            painted_string = ''.join((painted_string,color,orig_string,default))
        return(painted_string)

    COLORS_MD = {
        'black': 30,
        'red': 31,
        'brightwhite': 97,
        'brightyellow': 93,
        97: 'brightwhite',
        'brightblack': 90,
        'brightred': 91,
        'blue': 34,
        'brightcyan': 96,
        'brightmagenta': 95,
        90: 'brightblack',
        91: 'brightred',
        'white': 37,
        93: 'brightyellow',
        30: 'black',
        31: 'red',
        32: 'green',
        33: 'yellow',
        34: 'blue',
        35: 'magenta',
        36: 'cyan',
        37: 'white',
        'cyan': 36,
        92: 'brightgreen',
        95: 'brightmagenta',
        'brightgreen': 92,
        'magenta': 35,
        96: 'brightcyan',
        'green': 32,
        94: 'brightblue',
        'brightblue': 94,
        'lightblue':94,
        'yellow': 33
    }
    
    def ansi_8color_control(**kwargs):
        '''
            The original specification only had 8 colors, and just gave them names. 
            The SGR parameters 30-37 selected the foreground color, 
            while 40-47 selected the background. 
            Quite a few terminals implemented "bold" (SGR code 1) 
            as a brighter color rather than a different font, 
            thus providing 8 additional foreground colors. 
            Usually you could not get these as background colors,
            though sometimes inverse video (SGR code 7) would allow that.
            Examples: to get black letters on white background use ESC[30;47m, to get red use ESC[31m, 
            to get bright red use ESC[1;31m. To reset colors to their defaults, 
            use ESC[39;49m (not supported on some terminals), or reset all attributes with ESC[0m. 
            Later terminals added the ability to directly specify the "bright" colors with 90-97 and 100-107.
        '''
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 37
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 30
        bg = bg + 10
        if("style" in kwargs):
            style = kwargs['style']
        else:
            style = 1
        control = '\033[' + str(style)+ ";" +str(fg) +";"+str(bg) +"m"
        return(control)
    
    def ansi_256color_control(**kwargs):
        '''
            ESC[ … 38;5;<n> … m Select foreground color
            ESC[ … 48;5;<n> … m Select background color
              0-  7:  standard colors (as in ESC [ 30–37 m)
              8- 15:  high intensity colors (as in ESC [ 90–97 m)
             16-231:  6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
            232-255:  grayscale from black to white in 24 steps
        '''
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 255
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 0
        control = '\033[38;5;' +str(fg) +"m" + '\033[48;5;' +str(bg) +"m"
        return(control)


if(xdict.utils.is_win()):
    paint = print_str
else:
    def paint(s,**kwargs):
        if('end' in kwargs):
            end = kwargs['end']
        else:
            end = '\n'
        print(paint_str(s,**kwargs),end=end)




def paint_singleline(line,color,**kwargs):
    '''
        prefix = '<div>'
        line = "the colored content"
        suffix = '</div>'
        paint_singleline(line,'blue',prefix=prefix,suffix=suffix)
        paint_singleline(line,'blue',prefix=prefix,suffix=suffix,prefix_color='green',suffix_color='green')
    '''
    if('prefix' in kwargs):
        prefix = kwargs['prefix']
    else:
        prefix = ''
    if('prefix_color' in kwargs):
        prefix_color = kwargs['prefix_color']
    else:
        prefix_color = 'white'
    if('suffix' in kwargs):
        suffix = kwargs['suffix']
    else:
        suffix = ''
    if('suffix_color' in kwargs):
        suffix_color = kwargs['suffix_color']
    else:
        suffix_color = 'white'
    plen = prefix.__len__()
    paint_len = line.__len__()
    slen = suffix.__len__()
    color_sec = {1:(0,plen-1,prefix_color),2:(plen,plen+paint_len-1,color),3:(plen+paint_len,plen+paint_len+slen-1,suffix_color)}
    s = prefix+line+suffix
    paint(s,color_sec=color_sec)




def paint_multilines(lines,colors,line_sp='\n'):
    '''
        lines = [
            'the first green line',
            'the second yellow line',
            'the third blue line'
        ]
        
        colors = ['green','yellow','blue']
        paint_multilines(lines,colors)
    '''
    s = ''
    length = lines.__len__()
    clen = colors.__len__()
    if(clen < length):
        colors = copy.deepcopy(colors)
        colors.extend(['white'] * (length-clen))
    else:
        pass
    color_sec = {}
    cursor = 0
    for i in range(0,length):
        line = lines[i] + line_sp
        llen = line.__len__()
        color = colors[i]
        color_sec[i+1] = (cursor,cursor+llen-1,color)
        cursor = cursor + llen
        s = s + line
    s = xdict.utils.str_rstrip(s,line_sp,1)
    paint(s,color_sec=color_sec)


