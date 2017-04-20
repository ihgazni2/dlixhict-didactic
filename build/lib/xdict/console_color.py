import collections

#client TERM can NOT be dumb  
foreground_Dict = {
    'black':30,
    'red':31,
    'green':32,
    'yellow':33,
    'blue':34,
    'purple':35,
    'azure':36,
    'grey':37,
    30:'black',
    31:'red',
    32:'green',
    33:'yellow',
    34:'blue',
    35:'purple',
    36:'azure',
    37:'grey'
}


background_Dict = {
    'black':40,
    'red':41,
    'green':42,
    'yellow':43,
    'blue':44,
    'purple':45,
    'azure':46,
    'grey':47,
    40:'black',
    41:'red',
    42:'green',
    43:'yellow',
    44:'blue',
    45:'purple',
    46:'azure',
    47:'grey'
}

mode_Dict = collections.OrderedDict()
mode_Dict = {
    'default':0,
    'highlight':1,
    'underscore':4,
    'blink':5,
    'reverse':7,
    'unseen':8,
    0:'default',
    1:'highlight',
    4:'underscore',
    5:'blink',
    7:'reverse',
    8:'unseen'
}

def help():
    for each in mode_Dict:
        if(type(each) == type(0)):
            print('mode:{0}:{1}'.format(each,mode_Dict[each]))
    print('------------------------------------------------------')
    for i in range(30,38):
        print('fore:{0}:{1}'.format(i,foreground_Dict[i]))
    print('------------------------------------------------------')
    for i in range(40,48):
        print('back:{0}:{1}'.format(i,background_Dict[i]))


def set(mode,fore,back,md=mode_Dict,fd=foreground_Dict,bd=background_Dict):
    if(type(mode)==type(0)):
        m = mode
    else:
        m = md[mode]
    if(type(fore)==type(0)):
        f = fore
    else:
        f = fd[fore]
    if(type(back)==type(0)):
        b = back
    else:
        b = bd[back]
    setting = '\033[{0};{1};{2}m'.format(m,f,b)
    print(setting)


def reset():
    print('\033[0m')
