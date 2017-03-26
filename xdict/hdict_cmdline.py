import re
import copy
from xdict import utils
from xdict import ltdict
from xdict import hdict_object
from xdict import hdict_xml
from xdict import jprint
from operator import itemgetter


def format_cmd_str(cmd_str,cmd_sp=' '):
    '''
        >>> cmd_sp = ' '
        >>> cmd_str = 'defaultComponents header    props navigation menu items 2   link disabled'
        >>> format_cmd_str(cmd_str)
        'defaultComponents header props navigation menu items 2 link disabled'
        >>> 
        >>> cmd_sp = '#'
        >>> cmd_str = 'defaultComponents##header##prop##navigation##men##items##2##link##disabled'
        >>> format_cmd_str(cmd_str,cmd_sp='#')
        'defaultComponents#header#prop#navigation#men#items#2#link#disabled'
        >>> 
    '''
    regex_str = ''.join(('[',cmd_sp,']','+'))
    regex = re.compile(regex_str)
    cmd_str = re.sub(regex,cmd_sp,cmd_str)
    cmd_str = utils.str_rstrip(cmd_str,cmd_sp,1)
    cmd_str = utils.str_lstrip(cmd_str,cmd_sp,1)
    return(cmd_str)


def cmd_str_to_cmd_pl(cmd_str,cmd_sp = ' '):
    '''
        >>> cmd_sp = ' '
        >>> cmd_str = 'defaultComponents header    props navigation menu items 2   link disabled'
        >>> cmd_str_to_cmd_pl(cmd_str,cmd_sp = ' ')
        ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
        >>> 
        >>> cmd_sp = '#'
        >>> cmd_str = 'defaultComponents##header##prop##navigation##men##items##2##link##disabled'
        >>> cmd_str_to_cmd_pl(cmd_str,cmd_sp = '#')
        ['defaultComponents', 'header', 'prop', 'navigation', 'men', 'items', '2', 'link', 'disabled']
        >>> 
    '''
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    cmd_pl = cmd_str.split(cmd_sp)
    return(cmd_pl)


def path_to_cmd_str(path_list_or_path_string,**kwargs):
    '''
        >>> 
        >>> cmd_sp = ' '
        >>> path_sp = "/"
        >>> path = 'defaultComponents/header/prop/navigation/men/items/2/link/disabled'
        >>> path_to_cmd_str(path,cmd_sp=cmd_sp,path_sp=path_sp)
        'defaultComponents header prop navigation men items 2 link disabled'
        >>> 
        >>> cmd_sp = ' '
        >>> path_sp = "|"
        >>> path = 'defaultComponents|header|props|navigation|menu|items|2|link|disabled'
        >>> path_to_cmd_str(path,cmd_sp=cmd_sp,path_sp=path_sp)
        'defaultComponents header props navigation menu items 2 link disabled'
        >>> 
        >>> cmd_sp = ' '
        >>> path_sp = "/"
        >>> path = ['defaultComponents', 'header', 'prop', 'navigation', 'men', 'items', '2', 'link', 'disabled']
        >>> path_to_cmd_str(path,cmd_sp=cmd_sp,path_sp=path_sp)
        'defaultComponents header prop navigation men items 2 link disabled'
        >>> 
    '''
    if('path_sp' in kwargs):
        path_sp = kwargs['path_sp']
    else:
        path_sp = '/'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    path_list = hdict_object.get_path_list(path_list_or_path_string,path_sp)
    cmd_str = ''
    for i in range(0,path_list.__len__()):
        cmd_str = ''.join((cmd_str,cmd_sp,str(path_list[i])))
    cmd_str = utils.str_rstrip(cmd_str,cmd_sp,1)
    cmd_str = utils.str_lstrip(cmd_str,cmd_sp,1)
    return(cmd_str)


def cmd_str_to_path_str(cmd_str,**kwargs):
    '''
        >>> 
        >>> cmd_sp = ' '
        >>> cmd_str = 'defaultComponents header    props navigation menu items 2   link disabled'
        >>> cmd_str_to_path_str(cmd_str)
        'defaultComponents/header/props/navigation/menu/items/2/link/disabled'
        >>> 
        >>> cmd_sp = ' '
        >>> cmd_str = 'defaultComponents header    props navigation menu items 2   link disabled'
        >>> cmd_str_to_path_str(cmd_str,path_sp='|')
        'defaultComponents|header|props|navigation|menu|items|2|link|disabled'
        >>> 
        >>> cmd_sp = '#'
        >>> cmd_str = 'defaultComponents##header##prop##navigation##men##items##2##link##disabled'
        >>> cmd_str_to_path_str(cmd_str,cmd_sp = '#')
        'defaultComponents/header/prop/navigation/men/items/2/link/disabled'
        >>> 
    '''
    if('path_sp' in kwargs):
        path_sp = kwargs['path_sp']
    else:
        path_sp = '/'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    path_str = cmd_str.replace(cmd_sp,path_sp)
    return(path_str)



def get_cmd_char_position_desc(cmd_pl,cmd_sp=' '):
    '''
        >>> 
        >>> cmd_pl = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
        >>> cpdesc = get_cmd_char_position_desc(cmd_pl,cmd_sp=' ')
        >>> cpdesc
        [(0, 16), (18, 23), (25, 29), (31, 40), (42, 45), (47, 51), (53, 53), (55, 58), (60, 67)]
        >>> si = 21
        >>> ei = 35
        >>> get_interval_si_from_char_position_desc(si,cpdesc)
        18
        >>> get_interval_ei_from_char_position_desc(ei,cpdesc)
        40
        >>> si in range(18,23+1)
        True
        >>> ei in range(31,40+1)
        True
        >>> 
    '''
    sp_len = cmd_sp.__len__()
    desc = []
    curr = 0
    for i in range(0,cmd_pl.__len__()):
        supp = sp_len * i
        kw = cmd_pl[i]
        l = kw.__len__()
        end = curr + l - 1 
        desc.append((curr+supp,end+supp))
        curr = end + 1
    return(desc)

def get_interval_si_from_char_position_desc(si,cpdesc):
    '''
        >>> 
        >>> cmd_pl = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
        >>> cpdesc = get_cmd_char_position_desc(cmd_pl,cmd_sp=' ')
        >>> cpdesc
        [(0, 16), (18, 23), (25, 29), (31, 40), (42, 45), (47, 51), (53, 53), (55, 58), (60, 67)]
        >>> si = 21
        >>> ei = 35
        >>> get_interval_si_from_char_position_desc(si,cpdesc)
        18
        >>> get_interval_ei_from_char_position_desc(ei,cpdesc)
        40
        >>> si in range(18,23+1)
        True
        >>> ei in range(31,40+1)
        True
        >>> 
    '''
    for i in range(0,cpdesc.__len__()):
        rsi = cpdesc[i][0]
        rei = cpdesc[i][1]
        if((si>=rsi) & (si<=rei)):
            return(rsi)
        else:
            pass
    return(None)

def get_interval_ei_from_char_position_desc(ei,cpdesc):
    '''
        >>> 
        >>> cmd_pl = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
        >>> cpdesc = get_cmd_char_position_desc(cmd_pl,cmd_sp=' ')
        >>> cpdesc
        [(0, 16), (18, 23), (25, 29), (31, 40), (42, 45), (47, 51), (53, 53), (55, 58), (60, 67)]
        >>> si = 21
        >>> ei = 35
        >>> get_interval_si_from_char_position_desc(si,cpdesc)
        18
        >>> get_interval_ei_from_char_position_desc(ei,cpdesc)
        40
        >>> si in range(18,23+1)
        True
        >>> ei in range(31,40+1)
        True
        >>> 
    '''
    for i in range(0,cpdesc.__len__()):
        rsi = cpdesc[i][0]
        rei = cpdesc[i][1]
        if((ei>=rsi) & (ei<=rei)):
            return(rei)
        else:
            pass
    return(None)


def cmdpl_in_cmdpl(cmdpl1,cmdpl2,**kwargs):
    '''
    cmdpl2 ={0: 'client', 1: 'userImage', 2: 'default', 3: 'size222'}
    secarino1:
        cmdpl1=['ent', 'userImage', 'default', 'size']
        cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose') == True
        cmdpl_in_cmdpl(cmdpl1,cmdpl2) == False
    secarino2:
        cmdpl1=[]
        cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose') == True
        cmdpl_in_cmdpl(cmdpl1,cmdpl2) == True
    secarino3:
        cmdpl1=['cli']
        cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose') == True
        cmdpl_in_cmdpl(cmdpl1,cmdpl2) == True
    secarino4:
        cmdpl1=['erIma']
        cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose') == True
        cmdpl_in_cmdpl(cmdpl1,cmdpl2) == False
    secarino5:
        cmdpl1=['client','use']
        cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose') == True
        cmdpl_in_cmdpl(cmdpl1,cmdpl2) == False
    >>> 
    >>> cmdpl1 = ['defaultComp']
    >>> cmdpl2 = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='strict')
    True
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose')
    True
    >>> cmdpl1 = ['defaultComponents', 'header', 'props', 'navi']
    >>> cmdpl2 = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='strict')
    True
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose')
    True
    >>> cmdpl1 = ['items']
    >>> cmdpl2 = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='strict')
    False
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose')
    True
    >>> cmdpl1 = ['ader', 'props', 'navi']
    >>> cmdpl2 = ['defaultComponents', 'header', 'props', 'navigation', 'menu', 'items', '2', 'link', 'disabled']
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='strict')
    False
    >>> cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode='loose')
    True
    >>> 
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    cmdpl1_len = cmdpl1.__len__()
    cmdpl2_len = cmdpl2.__len__()
    if(cmdpl1_len > cmdpl2_len):
        return(False)
    else:
        pass
    if(mode == 'strict'):
        if(cmdpl1_len == 0):
            return(True)
        elif(cmdpl1_len==1):
            start1 = cmdpl1[0]
            start2 = cmdpl2[0]
            cond = utils.str_at_begin_of_str(start1,start2)
            if(cond):
                return(True)
            else:
                return(False)
        else:
            for i in range(0,cmdpl1_len-1):
                if(cmdpl1[i]==cmdpl2[i]):
                    pass
                else:
                    return(False)
            end1 = cmdpl1[cmdpl1_len-1]
            end2 = cmdpl2[cmdpl1_len-1]
            cond = utils.str_at_begin_of_str(end1,end2)
            if(cond):
                return(True)
            else:
                return(False)
    else:
        if(cmdpl1_len == 0):
            return(True)
        elif(cmdpl1_len==1):
            ele1 = cmdpl1[0]
            for i in range(0,cmdpl2_len):
                ele2 = cmdpl2[i]
                cond = (ele1 in ele2)
                if(cond):
                    return(True)
                else:
                    pass
            return(False)
        else:
            #---------debug--------#
            def try_to_find_match(lb2,cmdpl1_len,cmdpl2_len,cmdpl1,cmdpl2):
                distance = lb2 - 1
                if(lb2>cmdpl2_len - 1):
                    return((False,0,distance))
                else:
                    for i in range(1,cmdpl1_len-1):
                        index = i + distance
                        if(index > (cmdpl2_len -1)):
                            return((False,i,distance))
                        else:
                            if(cmdpl1[i]==cmdpl2[index]):
                                pass
                            else:
                                return((False,i,distance))
                    return((True,i,distance))
            #---------debug--------#
            
            lb2 = 0
            finded = 0 
            start1 = cmdpl1[0]
            for j in range(0,cmdpl2_len):
                start2 = cmdpl2[j]
                cond = utils.str_at_end_of_str(start1,start2)
                if(cond):
                    lb2 = j+1
                    finded,lb1,distance = try_to_find_match(lb2,cmdpl1_len,cmdpl2_len,cmdpl1,cmdpl2)
                    if(finded):
                        break
                    else:
                        pass
                else:
                    pass
            if(finded):
                pass
            else:
                return(False)
            if(lb2>cmdpl2_len - 1):
                return(False)
            else:
                index = cmdpl1_len-1+distance
                if(index > (cmdpl2_len -1)):
                    return(False)
                else:
                    end1 = cmdpl1[cmdpl1_len-1]
                    end2 = cmdpl2[index]
                    cond = utils.str_at_begin_of_str(end1,end2)
                    if(cond):
                        return(True)
                    else:
                        return(False)            


def cmd_in_cmd(cmd1,cmd2,**kwargs):
    '''
        >>> 
        >>> cmd1_sp=' '
        >>> cmd1 = 'defaultComp'
        >>> cmd2_sp=' '
        >>> cmd2 = 'defaultComponents header props navigation menu items 2 link disabled'
        >>> cmd_in_cmd(cmd1,cmd2,mode='strict',cmd1_sp=cmd1_sp,cmd2_sp=cmd2_sp)
        False
        >>> cmd_in_cmd(cmd1,cmd2,mode='loose',cmd1_sp=cmd1_sp,cmd2_sp=cmd2_sp)
        True
        >>> 
        >>> cmd1_sp=' '
        >>> cmd1 = 'defaultComp'
        >>> cmd2_sp=' '
        >>> cmd2 = 'Components header props navi'
        >>> cmd_in_cmd(cmd1,cmd2,mode='strict',cmd1_sp=cmd1_sp,cmd2_sp=cmd2_sp)
        False
        >>> cmd_in_cmd(cmd1,cmd2,mode='loose',cmd1_sp=cmd1_sp,cmd2_sp=cmd2_sp)
        True
        >>> 
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    if('cmd1_sp' in kwargs):
        cmd1_sp = kwargs['cmd1_sp']
    else:
        cmd1_sp = ' '
    if('cmd2_sp' in kwargs):
        cmd2_sp = kwargs['cmd2_sp']
    else:
        cmd2_sp = ' '
    cmd1 = format_cmd_str(cmd1,cmd_sp=cmd1_sp)
    cmd2 = format_cmd_str(cmd2,cmd_sp=cmd2_sp)
    cmd1_pl = cmd1.split(cmd1_sp)
    cmd2_pl = cmd2.split(cmd2_sp)
    return(cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode=mode))


def cmdlines_str_to_ltdict(cmdlines_str,**kwargs):
    '''
        >>> 
        >>> print(cmdlines_str)
        client
        client defaultActivityID
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        client gender
        client geoIPLocation
        client geoIPLocation lat
        >>> cmdlines_ltdict = cmdlines_str_to_ltdict(cmdlines_str)
        >>> pobj(cmdlines_ltdict)
        {
         0: 'client', 
         1: 'client defaultActivityID', 
         2: 'client formattingOptions', 
         3: 'client formattingOptions decimalSeparator', 
         4: 'client formattingOptions language', 
         5: 'client formattingOptions startOfWeek', 
         6: 'client formattingOptions unitSystem', 
         7: 'client gender', 
         8: 'client geoIPLocation', 
         9: 'client geoIPLocation lat'
        }
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('ltdict' in kwargs):
        lt = kwargs['ltdict']
    else:
        lt = 1
    lines = cmdlines_str.split(line_sp)
    for i in range(0,lines.__len__()):
        line = lines[i]
        line = format_cmd_str(line)
        lines[i] = line
    if(lt):
        lines = ltdict.list_to_ltdict(lines)
    else:
        pass
    return(lines)

def cmdlines_ltdict_to_str(cmdlines_ltdict,**kwargs):
    '''
        >>> 
        >>> pobj(cmdlines_ltdict)
        {
         0: 'client', 
         1: 'client defaultActivityID', 
         2: 'client formattingOptions', 
         3: 'client formattingOptions decimalSeparator', 
         4: 'client formattingOptions language', 
         5: 'client formattingOptions startOfWeek', 
         6: 'client formattingOptions unitSystem', 
         7: 'client gender', 
         8: 'client geoIPLocation', 
         9: 'client geoIPLocation lat'
        }
        >>> 
        >>> cmdlines_str = cmdlines_ltdict_to_str(cmdlines_ltdict,line_sp='\n')
        >>> print(cmdlines_str)
        client
        client defaultActivityID
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        client gender
        client geoIPLocation
        client geoIPLocation lat
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmdlines_str = ''
    for i in range(0,cmdlines_ltdict.__len__()):
        cmdlines_str = ''.join((cmdlines_str,cmdlines_ltdict[i],line_sp))
    cmdlines_str = utils.str_rstrip(cmdlines_str,line_sp,1)
    return(cmdlines_str)

def cmdlines_ltdict_to_deep(cmdlines_ltdict,**kwargs):
    '''
        >>> pobj(cmdlines_ltdict)
        {
         0: 'client', 
         1: 'client defaultActivityID', 
         2: 'client formattingOptions', 
         3: 'client formattingOptions decimalSeparator', 
         4: 'client formattingOptions language', 
         5: 'client formattingOptions startOfWeek', 
         6: 'client formattingOptions unitSystem', 
         7: 'client gender', 
         8: 'client geoIPLocation', 
         9: 'client geoIPLocation lat'
        }
        >>> cmdlines_deep_ltdict = cmdlines_ltdict_to_deep(cmdlines_ltdict)
        >>> pobj(cmdlines_deep_ltdict[3])
        {
         0: 'client', 
         1: 'formattingOptions', 
         2: 'decimalSeparator'
        }
        >>> cmdlines_deep_ltdict
        {0: {0: 'client'}, 1: {0: 'client', 1: 'defaultActivityID'}, 2: {0: 'client', 1: 'formattingOptions'}, 3: {0: 'client', 1: 'formattingOptions', 2: 'decimalSeparator'}, 4: {0: 'client', 1: 'formattingOptions', 2: 'language'}, 5: {0: 'client', 1: 'formattingOptions', 2: 'startOfWeek'}, 6: {0: 'client', 1: 'formattingOptions', 2: 'unitSystem'}, 7: {0: 'client', 1: 'gender'}, 8: {0: 'client', 1: 'geoIPLocation'}, 9: {0: 'client', 1: 'geoIPLocation', 2: 'lat'}}
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    lines = copy.deepcopy(cmdlines_ltdict)
    for i in range(0,lines.__len__()):
        line = lines[i]
        line = format_cmd_str(line)
        line_lt = line.split(cmd_sp)
        line_lt = ltdict.list_to_ltdict(line_lt)
        lines[i] = line_lt
    return(lines)

def cmdlines_deep_to_ltdict(deep,**kwargs):
    '''
        >>> 
        >>> 
        >>> cmdlines_deep_ltdict
        {0: {0: 'client'}, 1: {0: 'client', 1: 'defaultActivityID'}, 2: {0: 'client', 1: 'formattingOptions'}, 3: {0: 'client', 1: 'formattingOptions', 2: 'decimalSeparator'}, 4: {0: 'client', 1: 'formattingOptions', 2: 'language'}, 5: {0: 'client', 1: 'formattingOptions', 2: 'startOfWeek'}, 6: {0: 'client', 1: 'formattingOptions', 2: 'unitSystem'}, 7: {0: 'client', 1: 'gender'}, 8: {0: 'client', 1: 'geoIPLocation'}, 9: {0: 'client', 1: 'geoIPLocation', 2: 'lat'}}
        >>> 
        >>> cmdlines_ltdict = cmdlines_deep_to_ltdict(cmdlines_deep_ltdict)
        >>> pobj(cmdlines_ltdict)
        {
         0: 'client', 
         1: 'client defaultActivityID', 
         2: 'client formattingOptions', 
         3: 'client formattingOptions decimalSeparator', 
         4: 'client formattingOptions language', 
         5: 'client formattingOptions startOfWeek', 
         6: 'client formattingOptions unitSystem', 
         7: 'client gender', 
         8: 'client geoIPLocation', 
         9: 'client geoIPLocation lat'
        }
        >>> 
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    lines = copy.deepcopy(deep)
    for i in range(0,lines.__len__()):
        line = lines[i]
        if(ltdict.is_ltdict(line)):
            line = ltdict.ltdict_to_list(line)
        else:
            pass
        line = path_to_cmd_str(line,cmd_sp=cmd_sp)
        lines[i] = line
    return(lines)

def cmdlines_str_to_deep(cmdlines_str,**kwargs):
    '''
        >>> 
        >>> print(cmdlines_str)
        client
        client defaultActivityID
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        client gender
        client geoIPLocation
        client geoIPLocation lat
        >>> cmdlines_deep_ltdict = cmdlines_str_to_deep(cmdlines_str)
        >>> pobj(cmdlines_deep_ltdict[9])
        {
         0: 'client', 
         1: 'geoIPLocation', 
         2: 'lat'
        }
        >>> cmdlines_deep_ltdict
        {0: {0: 'client'}, 1: {0: 'client', 1: 'defaultActivityID'}, 2: {0: 'client', 1: 'formattingOptions'}, 3: {0: 'client', 1: 'formattingOptions', 2: 'decimalSeparator'}, 4: {0: 'client', 1: 'formattingOptions', 2: 'language'}, 5: {0: 'client', 1: 'formattingOptions', 2: 'startOfWeek'}, 6: {0: 'client', 1: 'formattingOptions', 2: 'unitSystem'}, 7: {0: 'client', 1: 'gender'}, 8: {0: 'client', 1: 'geoIPLocation'}, 9: {0: 'client', 1: 'geoIPLocation', 2: 'lat'}}
        >>> 
        >>> 
    '''
    if('ltdict' in kwargs):
        lt = kwargs['ltdict']
    else:
        lt = 1
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    lines = cmdlines_str.split(line_sp)
    for i in range(0,lines.__len__()):
        line = lines[i]
        line = format_cmd_str(line)
        line_lt = line.split(cmd_sp)
        if(lt):
            lines[i] = ltdict.list_to_ltdict(line_lt)
        else:
            lines[i] = line_lt
    if(lt):
        lines = ltdict.list_to_ltdict(lines)
    else:
        pass
    return(lines)

def cmdlines_deep_to_str(deep_ltdict,**kwargs):
    '''
        >>> 
        >>> cmdlines_deep_ltdict
        {0: {0: 'client'}, 1: {0: 'client', 1: 'defaultActivityID'}, 2: {0: 'client', 1: 'formattingOptions'}, 3: {0: 'client', 1: 'formattingOptions', 2: 'decimalSeparator'}, 4: {0: 'client', 1: 'formattingOptions', 2: 'language'}, 5: {0: 'client', 1: 'formattingOptions', 2: 'startOfWeek'}, 6: {0: 'client', 1: 'formattingOptions', 2: 'unitSystem'}, 7: {0: 'client', 1: 'gender'}, 8: {0: 'client', 1: 'geoIPLocation'}, 9: {0: 'client', 1: 'geoIPLocation', 2: 'lat'}}
        >>> pobj(cmdlines_deep_ltdict[9])
        {
         0: 'client', 
         1: 'geoIPLocation', 
         2: 'lat'
        }
        >>> cmdlines_str = cmdlines_deep_to_str(cmdlines_deep_ltdict,line_sp='\n',cmd_sp='|')
        >>> 
        >>> print(cmdlines_str)
        client
        client|defaultActivityID
        client|formattingOptions
        client|formattingOptions|decimalSeparator
        client|formattingOptions|language
        client|formattingOptions|startOfWeek
        client|formattingOptions|unitSystem
        client|gender
        client|geoIPLocation
        client|geoIPLocation|lat
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmdlines_ltdict = cmdlines_deep_to_ltdict(deep_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    lines = cmdlines_ltdict_to_str(cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    return(lines)


def show_prompt_from_cmdlines_str(cmd_str,cmdlines_str,**kwargs):
    '''
        >>> 
        >>> print(cmdlines_str)
        client
        client defaultActivityID
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        client gender
        client geoIPLocation
        client geoIPLocation lat
        >>> 
        >>> cmd_str = "formatting"
        >>> show_prompt_from_cmdlines_str(cmd_str,cmdlines_str)
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        [2, 3, 4, 5, 6]
        >>> 
        >>> cmd_str = "client formatting"
        >>> show_prompt_from_cmdlines_str(cmd_str,cmdlines_str)
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        [2, 3, 4, 5, 6]
    >>> 
    
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'loose'
    if('single_color' in kwargs):
        single_color_cmd = kwargs['single_color_cmd']
    else:
        single_color_cmd = 'green'
    if('single_color' in kwargs):
        single_color_rsi = kwargs['single_color_rsi']
    else:
        single_color_rsi = 'blue'
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    cmd_nocaps = cmd_str.lower()
    cmd_pl = cmd_str.split(cmd_sp)
    cmdpl_len = cmd_pl.__len__()
    cmd_nocaps_pl = cmd_nocaps.split(cmd_sp.lower())
    cmdlines_deep = cmdlines_str_to_deep(cmdlines_str,cmd_sp=cmd_sp,line_sp=line_sp)
    cmdlines_nocaps = cmdlines_str.lower()
    cmdlines_nocaps_deep = cmdlines_str_to_deep(cmdlines_nocaps,cmd_sp=cmd_sp.lower(),line_sp=line_sp.lower())
    cmdlines_len  = cmdlines_nocaps_deep.__len__()
    rslt = ''
    orig_seqs = []
    for i in range(0,cmdlines_len):
        p = cmdlines_nocaps_deep[i]
        pnoc = cmdlines_deep[i]
        full_cmdpl_len = p.__len__()
        cond = cmdpl_in_cmdpl(cmd_nocaps_pl,p,mode=mode)
        if(cond):
            line = ''
            for k in range(0,full_cmdpl_len):
                line = ''.join((line,pnoc[k],cmd_sp))
            line = utils.str_rstrip(line,cmd_sp,1)
            #-----------paint---------------
            si = line.find(cmd_str)
            ei = si+cmd_str.__len__()-1
            cpdesc = get_cmd_char_position_desc(pnoc,cmd_sp=cmd_sp)
            rsi = get_interval_si_from_char_position_desc(si,cpdesc)
            rei = get_interval_ei_from_char_position_desc(ei,cpdesc)
            cmd_len = cmd_str.__len__()
            s1 = line[:rsi]
            s2 = jprint.paint_str(line[rsi:si],single_color=single_color_rsi)
            s3 = jprint.paint_str(cmd_str,single_color=single_color_cmd)
            s4 = jprint.paint_str(line[(si+cmd_len):(rei+1)],single_color=single_color_rsi)
            s5 = line[(rei+1):]
            line = ''.join((s1,s2,s3,s4,s5))
            #-----------paint---------------           
            rslt = ''.join((rslt,line,line_sp))
            orig_seqs.append(i)
        else:
            pass
    rslt = utils.str_rstrip(rslt,line_sp,1)
    print(rslt)
    return(orig_seqs)



def show_prompt_from_cmdlines_ltdict(cmd_str,cmdlines_ltdict,**kwargs):
    '''
        >>> 
        >>> pobj(cmdlines_ltdict)
        {
         0: 'client', 
         1: 'client defaultActivityID', 
         2: 'client formattingOptions', 
         3: 'client formattingOptions decimalSeparator', 
         4: 'client formattingOptions language', 
         5: 'client formattingOptions startOfWeek', 
         6: 'client formattingOptions unitSystem', 
         7: 'client gender', 
         8: 'client geoIPLocation', 
         9: 'client geoIPLocation lat'
        }
        >>> cmd_str = "formatting"
        >>> show_prompt_from_cmdlines_ltdict(cmd_str,cmdlines_ltdict)
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        [2, 3, 4, 5, 6]
        >>> 
        >>> cmd_str = "client formatting"
        >>> show_prompt_from_cmdlines_ltdict(cmd_str,cmdlines_ltdict)
        client formattingOptions
        client formattingOptions decimalSeparator
        client formattingOptions language
        client formattingOptions startOfWeek
        client formattingOptions unitSystem
        [2, 3, 4, 5, 6]
        >>> 
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'loose'
    if('single_color' in kwargs):
        single_color_cmd = kwargs['single_color_cmd']
    else:
        single_color_cmd = 'green'
    if('single_color' in kwargs):
        single_color_rsi = kwargs['single_color_rsi']
    else:
        single_color_rsi = 'blue'
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    cmd_nocaps = cmd_str.lower()
    cmd_pl = cmd_str.split(cmd_sp)
    cmdpl_len = cmd_pl.__len__()
    cmd_nocaps_pl = cmd_nocaps.split(cmd_sp.lower())
    cmdlines_deep = cmdlines_ltdict_to_deep(cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    cmdlines_nocaps = copy.deepcopy(cmdlines_ltdict)
    for seq in cmdlines_nocaps:
        cmdlines_nocaps[seq] = cmdlines_nocaps[seq].lower()
    cmdlines_nocaps_deep = cmdlines_ltdict_to_deep(cmdlines_nocaps,cmd_sp=cmd_sp.lower(),line_sp=line_sp.lower())
    cmdlines_len  = cmdlines_nocaps_deep.__len__()
    rslt = ''
    orig_seqs = []
    for i in range(0,cmdlines_len):
        p = cmdlines_nocaps_deep[i]
        pnoc = cmdlines_deep[i]
        full_cmdpl_len = p.__len__()
        cond = cmdpl_in_cmdpl(cmd_nocaps_pl,p,mode=mode)
        if(cond):
            line = ''
            for k in range(0,full_cmdpl_len):
                line = ''.join((line,pnoc[k],cmd_sp))
            line = utils.str_rstrip(line,cmd_sp,1)
            #-----------paint---------------
            si = line.find(cmd_str)
            ei = si+cmd_str.__len__()-1
            cpdesc = get_cmd_char_position_desc(pnoc,cmd_sp=cmd_sp)
            rsi = get_interval_si_from_char_position_desc(si,cpdesc)
            rei = get_interval_ei_from_char_position_desc(ei,cpdesc)
            cmd_len = cmd_str.__len__()
            s1 = line[:rsi]
            s2 = jprint.paint_str(line[rsi:si],single_color=single_color_rsi)
            s3 = jprint.paint_str(cmd_str,single_color=single_color_cmd)
            s4 = jprint.paint_str(line[(si+cmd_len):(rei+1)],single_color=single_color_rsi)
            s5 = line[(rei+1):]
            line = ''.join((s1,s2,s3,s4,s5))
            #-----------paint---------------           
            rslt = ''.join((rslt,line,line_sp))
            orig_seqs.append(i)
        else:
            pass
    rslt = utils.str_rstrip(rslt,line_sp,1)
    print(rslt)
    return(orig_seqs)


def hdict_to_cmdlines_full_dict(hdict,**kwargs):
    '''
        >>> 
        >>> html_text = 
        ... <html class="" lang="zh">
        ... <head>
        ... <meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1" />
        ... </head>
        ... <body class="zh" >
        ...     <header id="ctl00_leftColumn_PersonalSectionTitle" class="section-heading accordion-title">
        ...         <a name="personal"></a>
        ...         <ul>
        ...             <li class="row-flex row-flex--middle">
        ...               <div>
        ...                 <div class="accordion-icons">
        ...                   <i class="icon-159"></i>
        ...                   <i class="icon-160"></i>
        ...                 </div>
        ...               </div>
        ...               <div class="row-flex row-flex--middle">
        ...                   <div class="fl0 fs12">
        ...                       <div class="h4">personal settings</div>
        ...                   </div>
        ...                   <div class="align--right fs12"></div>
        ...               </div>
        ...             </li>
        ...         </ul>
        ...     </header>
        ...     <script type="text/javascript" src="//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99"></script>
        ... </body>
        ... </html>
        ... 
        >>> 
        
        >>> 
        >>> temp = html_to_hdict(html_text=html_text)
        >>> hdict = temp['hdict']
        >>> sdict = temp['sdict']
        >>> prdict = temp['prdict']
        >>> cmdlines_full_dict = hdict_to_cmdlines_full_dict(hdict)
        >>> cmdlines_full_dict.keys()
        dict_keys(['attribs', 'results', 'cmds'])
        >>> cmdlines_ltdict = cmdlines_full_dict['cmds']
        >>> pobj(cmdlines_ltdict)
            {
                0: 'html', 
                1: 'html body', 
                2: 'html head', 
                3: 'html body header', 
                4: 'html head meta', 
                5: 'html body script', 
                6: 'html body header ul', 
                7: 'html body header a', 
                8: 'html body header ul li', 
                9: 'html body header ul li div', 
                10: 'html body header ul li div', 
                11: 'html body header ul li div div', 
                12: 'html body header ul li div div', 
                13: 'html body header ul li div div', 
                14: 'html body header ul li div div i', 
                15: 'html body header ul li div div i', 
                16: 'html body header ul li div div div'
            }
        >>> 
    >>> results = cmdlines_full_dict['results']
    >>> pobj(results)
        {
         0: 
            {}, 
         1: 
            {}, 
         2: 
            {}, 
         3: 
            {}, 
         4: None, 
         5: None, 
         6: 
            {}, 
         7: None, 
         8: 
            {}, 
         9: 
            {}, 
         10: 
             {}, 
         11: 
             {}, 
         12: 
             {}, 
         13: None, 
         14: None, 
         15: None, 
         16: 'personal settings'
        }
    >>> 
    >>> 
        >>> attribs = cmdlines_full_dict['attribs']
        >>> pobj(attribs)
        {
         0: 
            {
             'lang': 'zh', 
             'class': ''
            }, 
         1: 
            {
             'class': 'zh'
            }, 
         2: 
            {}, 
         3: 
            {
             'id': 'ctl00_leftColumn_PersonalSectionTitle', 
             'class': 'section-heading accordion-title'
            }, 
         4: 
            {
             'content': 'IE=EDGE,chrome=1', 
             'http-equiv': 'X-UA-Compatible'
            }, 
         5: 
            {
             'type': 'text/javascript', 
             'src': '//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99'
            }, 
         6: 
            {}, 
         7: 
            {
             'name': 'personal'
            }, 
         8: 
            {
             'class': 'row-flex row-flex--middle'
            }, 
         9: 
            {}, 
         10: 
             {
              'class': 'row-flex row-flex--middle'
             }, 
         11: 
             {
              'class': 'accordion-icons'
             }, 
         12: 
             {
              'class': 'fl0 fs12'
             }, 
         13: 
             {
              'class': 'align--right fs12'
             }, 
         14: 
             {
              'class': 'icon-160'
             }, 
         15: 
             {
              'class': 'icon-159'
             }, 
         16: 
             {
              'class': 'h4'
             }
        }
    >>> 
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('ignore_type' in kwargs):
        ignore_type = kwargs['ignore_type']
    else:
        ignore_type = 0
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if(deepcopy):
        hdict = copy.deepcopy(hdict)
    else:
        pass
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    if('sdict' in kwargs):
        sdict = kwargs['sdict']
    else:
        sdict = None
    if('prdict' in kwargs):
        prdict = kwargs['prdict']
    else:
        prdict = None
    if((sdict!=None) & (prdict!=None)):
        pass
    else:
        temp = hdict_object.get_sdict_and_prdict_from_hdict(hdict,disable_type =disable_type)
        sdict = temp['sdict']
        prdict = temp['prdict']
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    #-----
    cxtll = hdict_object.creat_xml_tag_line_label(sdict)
    sdict = cxtll['sdict']
    html_lines = cxtll['html_lines']
    
    
    #-----
    lines = {}
    values = {}
    attribs = {}
    stagns = {}
    textns = {}
    etagns = {}
    slines = {}
    elines = {}
    tlines = {}
    temp = []
    seq = 0
    #-----------------need fix-------------------
    for hpath in  prdict['h:o']:
        opath = prdict['h:o'][hpath]
        if(hpath == ()):
            pass
        else:
            line = path_to_cmd_str(list(opath),cmd_sp=cmd_sp)
            hp = hpath
            bp = prdict['h:b'][tuple(hp)]
            r,c = hdict_object.breadth_path_to_sdict_location(bp)
            leaf = sdict[r][c]['leaf']
            #
            start_tagn = sdict[r][c]['start_tagn']
            end_tagn = sdict[r][c]['end_tagn']
            start_html_line = sdict[r][c]['start_html_line']
            end_html_line = sdict[r][c]['end_html_line']
            text_html_line = sdict[r][c]['text_html_line']
            #
            attrib = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)['attrib']
            if(leaf):
                if(ignore_type):
                    value = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                    value = value['text']
                else:
                    if((sdict[r][c]['type']== '') | (sdict[r][c]['type']=='dict') ):
                        value = {}
                    elif((sdict[r][c]['type']== 'list')):
                        value = []
                    elif((sdict[r][c]['type']== 'tuple')):
                        value =()
                    elif((sdict[r][c]['type']== 'set')):
                        value = set({})
                    elif((sdict[r][c]['type']== 'str')):
                        value = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = str(value)
                    elif((sdict[r][c]['type']== 'int')):
                        value = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = int(value)
                    elif((sdict[r][c]['type']== 'float')):
                        value = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = float(value)
                    else:
                        value = utils.get_dict_items_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
            else:
                value = {}
            cmd_pl_len = opath.__len__() 
            temp.append((cmd_pl_len,line,value,attrib,start_tagn,end_tagn,start_html_line,end_html_line,text_html_line))
            seq = seq + 1
    if(reorder):
        temp.sort(key=itemgetter(1))
    else:
        temp.sort(key=itemgetter(4))
    for i in range(0,temp.__len__()):
        t = temp[i]
        lines[i] = t[1]
        values[i] = t[2]
        attribs[i] = t[3]
        stagns[i] = t[4]
        etagns[i] = t[5]
        slines[i] = t[6]
        elines[i] = t[7]
        tlines[i] = t[8]
        if(tlines[i] == None):
            textns[i] = None
        else:
            textns[i] = stagns[i] + 1
    if('keep_order_info' in kwargs):
        keep_order_info = kwargs['keep_order_info']
    else:
        keep_order_info = 0
    if(keep_order_info):
        return({'cmds':lines,'results':values,'attribs':attribs,'stagns':stagns,'etagns':etagns,'slines':slines,'elines':elines,'tlines':tlines,'textns':textns})
    else:
        return({'cmds':lines,'results':values,'attribs':attribs})




#------------------------------------------------------------
def cmdlines_full_dict_to_hdict(cmdlines_full_dict,**kwargs):
    cmdlines_ltdict = cmdlines_full_dict['cmds']
    results = cmdlines_full_dict['results']
    attribs = cmdlines_full_dict['attribs']
#---------------------------------------------------------


#-------------------------------------------

def get_obj_value_from_cmd(cmd,obj,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    cmd = format_cmd_str(cmd,cmd_sp=cmd_sp)
    path_list = cmd.split(cmd_sp)
    rslt = utils.get_dict_items_via_path_list(obj,path_list,n2s=n2s,s2n=s2n)
    print(rslt)
    return(rslt)

def cmdlines_to_obj(cmdlines,**kwargs):
    if('results' in kwargs):
        results = kwargs['results']
    else:
        results = {}
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('ltdict' in kwargs):
        lt = kwargs['ltdict']
    else:
        lt = 1
    ltd = cmdlines_str_to_ltdict(cmdlines,line_sp=line_sp,ltdict=lt)
    obj = {}
    for i in range(0,ltd.__len__()):
        pl = hdict_object.get_path_list(ltd[i],sp=cmd_sp)
        utils.set_default_dict_items_via_path_list(obj,pl,n2s=n2s,s2n=s2n)
        if(results=={}):
            pass
        else:
            utils.set_dict_items_via_path_list(obj,pl,results[i],n2s=n2s,s2n=s2n)
    return(obj)

def cmdlines_to_xml(cmdlines,**kwargs):
    if('results' in kwargs):
        results = kwargs['results']
    else:
        results = {}
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('ltdict' in kwargs):
        lt = kwargs['ltdict']
    else:
        lt = 1
    obj = cmdlines_to_obj(cmdlines,results=results,n2s=n2s,s2n=s2n,line_sp=line_sp,cmd_sp=cmd_sp,lt=lt)
    rslt = obj_to_xml(obj,n2s=n2s,s2n=s2n,line_sp=line_sp)
    return(rslt)

#
def xml_to_cmdline_dict(**kwargs):
    if('html_file_path' in kwargs):
        html_file_path = kwargs['html_file_path']
        fd = open(html_file_path,'r') 
        html_text = fd.read()
        fd.close()
        root = etree.HTML(html_text)
    elif('html_text' in kwargs):
        html_text = kwargs['html_text']
        root = etree.HTML(html_text)
    else:
        root = kwargs['root']
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('get_sdict' in kwargs):
        get_sdict = kwargs['get_sdict']
    else:
        get_sdict =1
    if('sdict' in kwargs):
        sdict = kwargs['sdict']
    else:
        sdict = {}
    temp = html_to_hdict(root=root)
    hdict=temp['hdict']
    sdict=temp['sdict']
    prdict=temp['prdict']
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    rslt = hdict_to_cmdlines_full_dict(hdict,sdict=sdict,prdict=prdict,s2n=s2n,n2s=n2s,disable_type=disable_type,cmd_sp=cmd_sp)
    if('save' in kwargs):
       if(kwargs['save']==1):
        cmds = ''
        results = ''
        attribs = ''
        for i in range(0,rslt['cmds'].__len__()):
            cmds = ''.join((cmds,str(rslt['cmds'][i]),line_sp))
            results = ''.join((results,str(rslt['results'][i]),line_sp))
            attribs = ''.join((attribs,str(rslt['attribs'][i]),line_sp))
        fd = open(kwargs['fn_cmdlines'],kwargs['op'])
        fd.write(cmds)
        fd.close()
        fd = open(kwargs['fn_results'],kwargs['op'])
        fd.write(results)
        fd.close()
        fd = open(kwargs['fn_attribs'],kwargs['op'])
        fd.write(attribs)
        fd.close()
    else:
        pass
    return(rslt)


def show_xml(cmd,**kwargs):
    if('html_file_path' in kwargs):
        html_file_path = kwargs['html_file_path']
        fd = open(html_file_path,'r') 
        html_text = fd.read()
        fd.close()
        root = etree.HTML(html_text)
    elif('html_text' in kwargs):
        html_text = kwargs['html_text']
        root = etree.HTML(html_text)
    else:
        if('handled' in kwargs):
            pass
        else:
            root = kwargs['root']
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('get_all' in kwargs):
        get_all = kwargs['get_all']
    else:
        get_all = 0
    if(handled):
        temp = handled
    else:
        temp = xml_to_cmdline_dict(root=root,s2n=s2n,n2s=n2s,disable_type=1,cmd_sp=cmd_sp,line_sp=line_sp)
    cmdlines_ltdict = temp['cmds']
    results = temp['results']
    attribs = temp['attribs']
    rslt_seqs = show_prompt_from_cmdlines_ltdict(cmd,cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    if(get_all):
            rslt = {}
            for i in range(0,rslt_seqs.__len__()):
                seq = rslt_seqs[i]
                print('cmd: {0}'.format(cmdlines_ltdict[seq]))
                print('result: {0}'.format(results[seq]))
                print('attrib: {0}'.format(attribs[seq]))
                rslt[i] = {'cmd':cmdlines_ltdict[seq],'result':results[seq],'attrib':attribs[seq]}
            return(rslt)
    else:
        if(rslt_seqs.__len__()==1):
            seq = rslt_seqs[0]
            cmd = jprint.paint_str(str(cmdlines_ltdict[seq]),single_color='yellow')
            result = jprint.paint_str(str(results[seq]),single_color='blue')
            attrib = jprint.paint_str(str(attribs[seq]),single_color='green')
            print('cmd: {0}'.format(cmd))
            print('result: {0}'.format(result))
            print('attrib: {0}'.format(attrib))
            return({'cmd':cmdlines_ltdict[seq],'result':results[seq],'attrib':attribs[seq],'seq':seq})
        else:
            rslt = ''
            for i in range(0,rslt_seqs.__len__()):
                seq = rslt_seqs[i]
                rslt = ''.join((rslt,cmdlines_ltdict[seq],line_sp))
            print(jprint.paint_str(rslt,single_color='yellow'))
            return({'rslt':rslt, 'seqs':rslt_seqs})    




def obj_to_cmdlines_dict(obj):
    #cmdlines,results,attribs = obj_to_cmdlines(obj)
    temp = hdict_object.obj_to_hdict(obj)
    hdict = temp['hdict']
    cmdlines_dict = hdict_to_cmdlines_full_dict(hdict)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']
    return(cmdlines_dict)

def show_obj(cmd,obj,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmdlines_dict = obj_to_cmdlines_dict(obj)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']    
    try:
        rslt = get_obj_value_from_cmd(cmd,obj,line_sp=line_sp,cmd_sp=cmd_sp)
    except:
        prompt = show_prompt_from_cmdlines_ltdict(cmd,cmdlines)
        return(prompt)
    else:
        return(rslt)


def show_hdict(cmd,hdict,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('prdict' in kwargs):
        prdict = kwargs['prdict']
    else:
        prdict = hdict_object.hdict_get_paths_relationship(hdict)
    cmdlines_dict = hdict_to_cmdlines_full_dict(obj)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']    
    try:
        pl = cmd_str_to_cmd_pl(cmd,cmd_sp)
        rslt =hdict_get_value(hdict,pl,prdict=prdict) 
    except:
        prompt = show_prompt_from_cmdlines_ltdict(cmd,cmdlines)
        return(prompt)
    else:
        return(rslt)
        
        



            
