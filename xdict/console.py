import xdict.utils

if(xdict.utils.is_win()):
    from ctypes import *
    from win32con import *
    
    COLORS_MD = {
     'darkgray': 9,
     'lightblue': 10,
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
        fg = (fg -1) & 0x0f
        bg = ((bg -1)<<4) & 0xf0
        SetConsoleTextAttribute(hconsole, fg + bg)
        print(text)
        SetConsoleTextAttribute(hconsole, old_color)
else:
    def paint_str(orig_string,**kwargs):
        grey = "\033[1;30;40m"
        red =  "\033[1;31;40m"
        green =  "\033[1;32;40m"
        yellow =  "\033[1;33;40m"
        blue =  "\033[1;34;40m"
        purple = "\033[1;35;40m"
        azure = "\033[1;36;40m"
        white =  "\033[1;37;40m"
        default =  "\033[0m"
        painted_string = default
        if('colors' in kwargs):
            colors = kwargs['colors']
        else:
            colors = {1:grey,2:red,3:green,4:yellow,5:blue,6:purple,7:azure,8:white,9:default}
        if('color_sec' in kwargs):
            color_sec = kwargs['color_sec']
        else:
            color_sec = None
        colors_dict = {
            'grey' : "\033[1;30;40m",
            'red' :  "\033[1;31;40m",
            'green' :  "\033[1;32;40m",
            'yellow' :  "\033[1;33;40m",
            'blue' :  "\033[1;34;40m",
            'purple' : "\033[1;35;40m",
            'azure' : "\033[1;36;40m",
            'white' :  "\033[1;37;40m",
            'default' :  "\033[0m"
        }
        if('single_color' in kwargs):
            single_color = kwargs['single_color']
            if(single_color in colors_dict):
                single_color = colors_dict[single_color]
        else:
            single_color = None
        if(color_sec):
            color_sec_len = color_sec.__len__()
            for i in range(1,color_sec_len + 1):
                si = color_sec[i][0]
                ei = color_sec[i][1]
                color = colors[color_sec[i][2]]
                sec = ''.join((color,orig_string[si:ei+1]))
                painted_string = ''.join((painted_string,sec))
            painted_string = ''.join((painted_string,default))
        else:
            color = single_color
            painted_string = ''.join((painted_string,color,orig_string,default))
        return(painted_string)


    
    
    

