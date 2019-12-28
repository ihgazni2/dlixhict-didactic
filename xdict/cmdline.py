import re
import copy
from xdict import utils
import ltdict.ltdict as  ltdict
from xdict import hdict_object
from xdict import hdict_xml
from xdict import jprint
from lxml import etree
from operator import itemgetter
import spaint.spaint as spaint
import elist.elist as elel

#cmdele      command-element
#cmdsp       command-separator
#cmdpsp      command-path-separator


#cmdl        command-list
#cmdstr      command-string
#cmdp        command-path
#cmd         cmdl | cmdstr | cmdp
#cmdexll     command-extracted-list-list
#cmdexsl     command-extracted-string-list
#cmdexpl     command-extracted-path-list
#cmdex       cmdexll | cmdexsl | cmdexpl

#cmdsbs      commands-block-string
#cmdslt      commands-ltdict
#cmdsdlt     commands-deep-ltdict
#cmdsfd      commands-fullDict
#cmds        cmdsbs | cmdslt | cmdsdlt | cmdsfd



# cmd_str 和 cmdpl 不一定能一一对应
# 例如: ['1']['a'][1], [1]['a'][1] ,['1']['a']['1'] ,[1]['a']['1']  都对应到'1 a 1'
# 要增加path_list ['1','a',1].....的结构来实现一一对应 cmdlines_strict_full_dict
# 把hdict 

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


def cmd_str_to_cmd_pl(cmd_str,cmd_sp = ' ',**kwargs):
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
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 1
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    cmd_pl = cmd_str.split(cmd_sp)
    cmdpl = []
    for i in range(0,cmd_pl.__len__()):
        v = cmd_pl[i]
        if(n2s ==1):
            v = str(v)
        if(s2n==1):
            try:
                int(v)
            except:
                pass
            else:
                v = int(v)
        cmdpl.append(v)
    return(cmdpl)


####
def cmdstr2pl(cmdstr,cmdsp=' '):
    '''
        cmdstr = 'html body form div input'
        cmdstr2pl(cmdstr)
    '''
    cmdstr = format_cmd_str(cmdstr,cmdsp)
    cmdpl = cmdstr.split(cmdsp)
    return(cmdpl)


def cmdpl2str(cmdpl,cmdsp=' '):
    '''
        cmdpl = ['html', 'body', 'form', 'div', 'input']
        cmdpl2str(cmdpl)
    '''
    cmdstr = ''
    length = cmdpl.__len__()
    for i in range(0,length):
        word = cmdpl[i]
        cmdstr = cmdstr + word + cmdsp
    cmdstr = utils.str_rstrip(cmdstr,cmdsp,1)
    return(cmdstr)        
        

def path_split(arr):
    '''
        arr = ['html', 'body', 'form', 'div', 'input']
        path_split(arr)
    '''
    rslt = []
    length = arr.__len__()
    for i in range(0,length):
        path = arr[:(i+1)]
        rslt.append(path)
    return(rslt)


def cmdstr_path_split(cmdstr,cmdsp=' '):
    '''
        cmdstr = 'html body form div input'
        rslt = cmdstr_path_split(cmdstr)
        pobj(rslt)
    '''
    cmdpl = cmdstr2pl(cmdstr,cmdsp)
    pspl = path_split(cmdpl)
    length = pspl.__len__()
    rslt = []
    for i in range(0,length):
        cmd = cmdpl2str(pspl[i],cmdsp)
        rslt.append(cmd)
    return(rslt)


def promptableize(cmds_ltdict,cmdsp=' '):
    table = {}
    length = cmds_ltdict.__len__()
    for i in range(0,length):
        cmdstr = cmds_ltdict[i]
        eles = cmdstr_path_split(cmdstr,cmdsp)
        for j in range(0,eles.__len__()):
            ele = eles[j]
            if(j in table):
                cond = (ele in table[j])
                if(cond):
                    pass
                else:
                    table[j].append(ele)
            else:
                table[j] = [ele]
    return(table)


def cmdslt_prompt(cmdslt,*args,**kwargs):
    if('cmdsp' in kwargs):
        cmdsp = kwargs['cmdsp']
    else:
        cmdsp=' '
    if('cmdstr' in kwargs):
        cmdstr = kwargs['cmdstr']
    else:
        cmdstr = cmdpl2str(list(args),cmdsp)
    table = promptableize(cmdslt,cmdsp)
    length = table.__len__()
    cmdl = cmdstr2pl(cmdstr,cmdsp)
    depth = cmdl.__len__()
    if(depth<length):
        level = table[depth]
        llen = level.__len__()
        prompt = []
        for j in range(0,llen):
            cmdstr2 = level[j]
            cond = cmd_in_cmd(cmdstr,cmdstr2)
            if(cond):
                cmdl2 = cmdstr2pl(cmdstr2,cmdsp)
                lastcmd = cmdl2[-1]
                prompt.append(cmdstr2)
                print(lastcmd + '    <'+cmdstr2+'>')
            else:
                pass
        return(prompt)
    else:
        return([])


####


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
    cmd_pl1 = copy.deepcopy(cmdpl1)
    cmd_pl2 = copy.deepcopy(cmdpl2)
    cmdpl1 = []
    for i in range(0,cmd_pl1.__len__()):
        v = cmd_pl1[i]
        v = str(v)
        cmdpl1.append(v)
    cmdpl2 = []
    for i in range(0,cmd_pl2.__len__()):
        v = cmd_pl2[i]
        v = str(v)
        cmdpl2.append(v)
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
                    i = -1
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
    return(cmdpl_in_cmdpl(cmd1_pl,cmd2_pl,mode=mode))


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
        lines = ltdict.list2ltdict(lines)
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
        line_lt = ltdict.list2ltdict(line_lt)
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
            line = ltdict.to_list(line)
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
            lines[i] = ltdict.list2ltdict(line_lt)
        else:
            lines[i] = line_lt
    if(lt):
        lines = ltdict.list2ltdict(lines)
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
    if('caps_strict' in kwargs):
        caps_strict = kwargs['caps_strict']
    else:
        caps_strict = 0
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    if(cmd_str == ''):
        rslt = ''
        for i in range(0,cmdlines_ltdict.__len__()):
            rslt = ''.join((rslt,cmdlines_ltdict[i],line_sp))
        rslt = utils.str_rstrip(rslt,line_sp,1)
        print(rslt)
        return(list(cmdlines_ltdict.keys()))
    else:
        pass
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
        pnoc = cmdlines_nocaps_deep[i]
        origp = cmdlines_deep[i]
        full_cmdpl_len = pnoc.__len__()
        if(caps_strict):
            cond = cmdpl_in_cmdpl(cmd_pl,origp,mode=mode)
        else:
            cond = cmdpl_in_cmdpl(cmd_nocaps_pl,pnoc,mode=mode)
        if(cond):
            line = ''
            for k in range(0,full_cmdpl_len):
                line = ''.join((line,origp[k],cmd_sp))
            line = utils.str_rstrip(line,cmd_sp,1)
            #-----------paint---------------
            if(caps_strict):
                si = line.find(cmd_str)
            else:
                si = line.lower().find(cmd_nocaps)
            ei = si+cmd_nocaps.__len__()-1
            cpdesc = get_cmd_char_position_desc(origp,cmd_sp=cmd_sp)
            rsi = get_interval_si_from_char_position_desc(si,cpdesc)
            rei = get_interval_ei_from_char_position_desc(ei,cpdesc)
            cmd_len = cmd_nocaps.__len__()
            s1 = line[:rsi]
            s2 = jprint.paint_str(line[rsi:si],single_color=single_color_rsi)
            s3 = jprint.paint_str(line[si:(si+cmd_len)],single_color=single_color_cmd)
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
    if('caps_strict' in kwargs):
        caps_strict = kwargs['caps_strict']
    else:
        caps_strict = 0
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
    cmd_str = format_cmd_str(cmd_str,cmd_sp=cmd_sp)
    if(cmd_str == ''):
        rslt = ''
        for i in range(0,cmdlines_ltdict.__len__()):
            rslt = ''.join((rslt,cmdlines_ltdict[i],line_sp))
        rslt = utils.str_rstrip(rslt,line_sp,1)
        print(rslt)
        return(list(cmdlines_ltdict.keys()))
    else:
        pass
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
        pnoc = cmdlines_nocaps_deep[i]
        origp = cmdlines_deep[i]
        full_cmdpl_len = pnoc.__len__()
        if(caps_strict):
            cond = cmdpl_in_cmdpl(cmd_pl,origp,mode=mode)
        else:
            cond = cmdpl_in_cmdpl(cmd_nocaps_pl,pnoc,mode=mode)
        if(cond):
            line = ''
            for k in range(0,full_cmdpl_len):
                line = ''.join((line,origp[k],cmd_sp))
            line = utils.str_rstrip(line,cmd_sp,1)
            #-----------paint---------------
            if(caps_strict):
                si = line.find(cmd_str)
            else:
                si = line.lower().find(cmd_nocaps)
            ei = si+cmd_nocaps.__len__()-1
            cpdesc = get_cmd_char_position_desc(origp,cmd_sp=cmd_sp)
            rsi = get_interval_si_from_char_position_desc(si,cpdesc)
            rei = get_interval_ei_from_char_position_desc(ei,cpdesc)
            cmd_len = cmd_nocaps.__len__()
            #
            #s1 = line[:rsi]
            #s2 = jprint.paint_str(line[rsi:si],single_color=single_color_rsi)
            #s3 = jprint.paint_str(line[si:(si+cmd_len)],single_color=single_color_cmd)
            #s4 = jprint.paint_str(line[(si+cmd_len):(rei+1)],single_color=single_color_rsi)
            #s5 = line[(rei+1):]
            #
            s1 = line[:rsi]
            s2 = line[rsi:si]
            s3 = line[si:(si+cmd_len)]
            s4 = line[(si+cmd_len):(rei+1)]
            s5 = line[(rei+1):]
            
            line = ''.join((s1,s2,s3,s4,s5))
            length = line.__len__()

            color_sec = {}
            color_sec[1] = (0,rsi-1,"white")
            color_sec[2] = (rsi,si-1,single_color_rsi)
            color_sec[3] = (si,si+cmd_len-1,single_color_cmd)
            color_sec[4] = (si+cmd_len,rei,single_color_rsi)
            color_sec[5] = (rei+1,length-1,"white")
            
            spaint.paint(line,color_sec=color_sec)
            #-----------paint---------------           
            #rslt = ''.join((rslt,line,line_sp))
            orig_seqs.append(i)
        else:
            pass
    #rslt = utils.str_rstrip(rslt,line_sp,1)
    #print(rslt)
    return(orig_seqs)

####







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
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
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
    #-----
    temp = []
    seq = 0
    #-----------------need fix-------------------
    for hpath in  prdict['h:o']:
        opath = prdict['h:o'][hpath]
        if(hpath == ()):
            pass
        else:
            if(path_list_cmd):
                line = list(opath)
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
            attrib = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)['attrib']
            if(leaf):
                if(ignore_type):
                    value = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
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
                        value = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = str(value)
                    elif((sdict[r][c]['type']== 'int')):
                        value = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = int(value)
                    elif((sdict[r][c]['type']== 'float')):
                        value = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
                        value = value['text']
                        value = float(value)
                    else:
                        value = utils.dict_getitem_via_path_list(hdict,hp,n2s=n2s,s2n=s2n)
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
        return({'cmds':lines,'results':values,'attribs':attribs,'stagns':stagns,'etagns':etagns,'slines':slines,'elines':elines,'tlines':tlines,'textns':textns,'html_lines':html_lines})
    else:
        return({'cmds':lines,'results':values,'attribs':attribs})

#

#


def get_tags_info_from_cmdlines_ltdict(cmdlines_ltdict):
    '''
        >>> pobj(cmds)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 

    '''
    def increase_seqs_after(stagns,index):
        for i in range(index,stagns.__len__()):
            stagns[i] = stagns[i] + 1
    deep = cmdlines_ltdict_to_deep(cmdlines_ltdict)
    stagns = list(deep.keys())
    etagns = {}
    prev_pl = copy.deepcopy(deep[0])
    #----------------------------------------------------------->
    lefted = copy.deepcopy(deep)
    #初始和cursor一起指向当前要处理的cmd
    #回溯寻找parent过程中，始终指向已经检查过的那一条
    find_parent_cursor = 1
    cursor = 1
    ################################################################################
    while(cursor<deep.__len__()):
        curr_pl = deep[cursor]
        cond = utils.path_list_is_parent(prev_pl,curr_pl)
        #如果上一条cmd是当前cmd的parent,没有结束tag的插入,stagns etagns的序号不变
        if(cond):
            prev_pl = copy.deepcopy(deep[find_parent_cursor])
            find_parent_cursor = find_parent_cursor + 1
            cursor = cursor + 1
        # 
        #如果上一条cmd不是当前cmd的parent,那么上一条cmd需要闭合,要在当前cursor所在位置之前插入一条闭合
        #此时find_parent_cursor 和 cursor  均指向当前cmd 
        else:
            ##added
            #例如:
            #{ 
            #  0: [html,head]
            #  1: [html,head,meta]
            #  2: [html,head,meta,x]
            #  next = 3
            #}
            #初次闭合会加1: added = 1
            #{ 
            #  0 [html,head]
            #  1 [html,head,meta]
            #  2 [html,head,meta,x]----
            #  3 [html,head,meta,/x]--- 2+ 1(added) = 3
            #  next = 4
            #}
            #后续闭合会加2: added = added + 2 = 3
            #{ 
            #  0 [html,head]
            #  1 [html,head,meta]--------
            #  2 [html,head,meta,x]
            #  3 [html,head,meta,/x]
            #  4 [html,head,/meta] ------1+3(added) = 4 
            #  next = 5
            #}
            #后续闭合会加2: added = added + 2 = 5
            #{ 
            #  0 [html,head]--------------0
            #  1 [html,head,meta]
            #  2 [html,head,meta,x]
            #  3 [html,head,meta,/x]
            #  4 [html,head,/meta] 
            #  5 [html,/head] ------------0 + 5(added) = 5
            #  next = 6
            #}
            
            #added  初始为1
            added = 1
            while((find_parent_cursor>=1) & (cond == False)):
                etagn_cursor = find_parent_cursor - 1
                if(etagn_cursor in etagns):
                    pass
                else:
                    increase_seqs_after(stagns,cursor)
                    etagns[etagn_cursor] = stagns[etagn_cursor] + added 
                    del lefted[etagn_cursor]
                #每闭合一次 距离会加2
                added = added + 2
                find_parent_cursor = etagn_cursor
                next_etagn_cursor = find_parent_cursor - 1
                prev_pl = copy.deepcopy(deep[next_etagn_cursor])
                cond = utils.path_list_is_parent(prev_pl,curr_pl)
            cursor = cursor+1
            find_parent_cursor = cursor
            prev_pl = copy.deepcopy(curr_pl)
        #--------------------------------------------------------#
    last_line = stagns[deep.__len__() - 1]
    lefted_len = lefted.__len__()
    lefted_seqs = []
    for seq in lefted:
        lefted_seqs.append(seq)
    lefted_seqs = sorted(lefted_seqs)
    for i in range(0,lefted_len):
        etagns[lefted_seqs[i]] = last_line + lefted_len -i
    stagns = ltdict.list2ltdict(stagns)
    return({'stagns':stagns,'etagns':etagns})

def get_cmdlines_ltdict_open_close_structute(cmdlines_ltdict,stagns,etagns):
    '''
        >>> pobj(cmds)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> pobj(stagns)
        {
         0: 0, 
         1: 1, 
         2: 2, 
         3: 5, 
         4: 6, 
         5: 7, 
         6: 9, 
         7: 10, 
         8: 11, 
         9: 12, 
         10: 13, 
         11: 15, 
         12: 19, 
         13: 20, 
         14: 21, 
         15: 24, 
         16: 30
        }
        >>> pobj(etagns)
        {
         0: 33, 
         1: 4, 
         2: 3, 
         3: 32, 
         4: 29, 
         5: 8, 
         6: 28, 
         7: 27, 
         8: 18, 
         9: 17, 
         10: 14, 
         11: 16, 
         12: 26, 
         13: 23, 
         14: 22, 
         15: 25, 
         16: 31
        }
        >>> 
        >>> x = get_cmdlines_open_close_structute(cmds,stagns,etagns)
        {
         0: '<<<<html', 
         1: '<<<<html head', 
         2: '<<<<html head meta', 
         3: 'html head meta>>>>', 
         4: 'html head>>>>', 
         5: '<<<<html body', 
         6: '<<<<html body header', 
         7: '<<<<html body header a', 
         8: 'html body header a>>>>', 
         9: '<<<<html body header ul', 
         10: '<<<<html body header ul li', 
         11: '<<<<html body header ul li div', 
         12: '<<<<html body header ul li div div', 
         13: '<<<<html body header ul li div div i', 
         14: 'html body header ul li div div i>>>>', 
         15: '<<<<html body header ul li div div i', 
         16: 'html body header ul li div div i>>>>', 
         17: 'html body header ul li div div>>>>', 
         18: 'html body header ul li div>>>>', 
         19: '<<<<html body header ul li div', 
         20: '<<<<html body header ul li div div', 
         21: '<<<<html body header ul li div div div', 
         22: 'html body header ul li div div div>>>>', 
         23: 'html body header ul li div div>>>>', 
         24: '<<<<html body header ul li div div', 
         25: 'html body header ul li div div>>>>', 
         26: 'html body header ul li div>>>>', 
         27: 'html body header ul li>>>>', 
         28: 'html body header ul>>>>', 
         29: 'html body header>>>>', 
         30: '<<<<html body script', 
         31: 'html body script>>>>', 
         32: 'html body>>>>', 
         33: 'html>>>>'
        }
        >>> 
    '''
    rslt = {}
    for i in range(0,cmdlines_ltdict.__len__()):
        si = stagns[i]
        ei = etagns[i]
        scmd = ''.join(('<<<<',cmdlines_ltdict[i]))
        ecmd = ''.join((cmdlines_ltdict[i],'>>>>'))
        rslt[si] = scmd
        rslt[ei] = ecmd
    pobj(rslt)
    return(rslt)

def update_tags_info_with_results(stagns,etagns,results):
    '''
        tmp = get_tags_info_from_cmdlines_ltdict(cmds)
        stagns = tmp['stagns']
        etagns = tmp['etagns']
        >>> pobj(stagns)
        {
         0: 0, 
         1: 1, 
         2: 2, 
         3: 5, 
         4: 6, 
         5: 7, 
         6: 9, 
         7: 10, 
         8: 11, 
         9: 12, 
         10: 13, 
         11: 15, 
         12: 19, 
         13: 20, 
         14: 21, 
         15: 24, 
         16: 30
        }
        >>> pobj(etagns)
        {
         0: 33, 
         1: 4, 
         2: 3, 
         3: 32, 
         4: 29, 
         5: 8, 
         6: 28, 
         7: 27, 
         8: 18, 
         9: 17, 
         10: 14, 
         11: 16, 
         12: 26, 
         13: 23, 
         14: 22, 
         15: 25, 
         16: 31
        }
        >>> pobj(results)
        {
         0: 
            {}, 
         1: 
            {}, 
         2: None, 
         3: 
            {}, 
         4: 
            {}, 
         5: None, 
         6: 
            {}, 
         7: 
            {}, 
         8: 
            {}, 
         9: 
            {}, 
         10: None, 
         11: None, 
         12: 
             {}, 
         13: 
             {}, 
         14: 'personal settings', 
         15: None, 
         16: None
        }
        >>> 
        tmp = update_tags_info_with_results(stagns,etagns,results)
        {'stagns': {0: 0, 1: 1, 2: 2, 3: 5, 4: 6, 5: 7, 6: 9, 7: 10, 8: 11, 9: 12, 10: 13, 11: 15, 12: 19, 13: 20, 14: 21, 15: 25, 16: 31}, 'etagns': {0: 34, 1: 4, 2: 3, 3: 33, 4: 30, 5: 8, 6: 29, 7: 28, 8: 18, 9: 17, 10: 14, 11: 16, 12: 27, 13: 24, 14: 23, 15: 26, 16: 32}, 'textns': {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: 22, 15: None, 16: None}}
        pobj(tmp)
                {
         'stagns': 
                   {
                    0: 0, 
                    1: 1, 
                    2: 2, 
                    3: 5, 
                    4: 6, 
                    5: 7, 
                    6: 9, 
                    7: 10, 
                    8: 11, 
                    9: 12, 
                    10: 13, 
                    11: 15, 
                    12: 19, 
                    13: 20, 
                    14: 21, 
                    15: 25, 
                    16: 31
                   }, 
         'etagns': 
                   {
                    0: 34, 
                    1: 4, 
                    2: 3, 
                    3: 33, 
                    4: 30, 
                    5: 8, 
                    6: 29, 
                    7: 28, 
                    8: 18, 
                    9: 17, 
                    10: 14, 
                    11: 16, 
                    12: 27, 
                    13: 24, 
                    14: 23, 
                    15: 26, 
                    16: 32
                   }, 
         'textns': 
                   {
                    0: None, 
                    1: None, 
                    2: None, 
                    3: None, 
                    4: None, 
                    5: None, 
                    6: None, 
                    7: None, 
                    8: None, 
                    9: None, 
                    10: None, 
                    11: None, 
                    12: None, 
                    13: None, 
                    14: 22, 
                    15: None, 
                    16: None
                   }
        }
    '''
    textns = {}
    for i in range(0,results.__len__()):
        if((results[i] == None) | (results[i] == {})):
            textns[i] = None
        else:
            textns[i] = stagns[i] + 1
            label = stagns[i]
            for j in range(0,results.__len__()):
                if(stagns[j]>label):
                    stagns[j] = stagns[j] + 1
                if(etagns[j]>label):
                    etagns[j] = etagns[j] + 1
    rslt = {}
    rslt['stagns'] = stagns
    rslt['etagns'] = etagns
    rslt['textns'] = textns
    return(rslt)

def get_html_lines_from_cmdlines_ltdict_and_tags_info(cmds,stagns,etagns,results,attribs,**kwargs):
    '''
        tmp = get_tags_info_from_cmdlines_ltdict(cmds)
        stagns = tmp['stagns']    
        etagns = tmp['etagns']        
        >>> pobj(cmds)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 
        >>> 
        >>> pobj(stagns)
        {
         0: 0, 
         1: 1, 
         2: 2, 
         3: 5, 
         4: 6, 
         5: 7, 
         6: 9, 
         7: 10, 
         8: 11, 
         9: 12, 
         10: 13, 
         11: 15, 
         12: 19, 
         13: 20, 
         14: 21, 
         15: 24, 
         16: 30
        }
        >>> 
        >>> 
        >>> pobj(etagns)
        {
         0: 33, 
         1: 4, 
         2: 3, 
         3: 32, 
         4: 29, 
         5: 8, 
         6: 28, 
         7: 27, 
         8: 18, 
         9: 17, 
         10: 14, 
         11: 16, 
         12: 26, 
         13: 23, 
         14: 22, 
         15: 25, 
         16: 31
        }
        >>> 
        >>> 
        >>> 
        >>> pobj(attribs)
        {
         0: 
            {
             'class': '', 
             'lang': 'zh'
            }, 
         1: 
            {}, 
         2: 
            {
             'http-equiv': 'X-UA-Compatible', 
             'content': 'IE=EDGE,chrome=1'
            }, 
         3: 
            {
             'class': 'zh'
            }, 
         4: 
            {
             'class': 'section-heading accordion-title', 
             'id': 'ctl00_leftColumn_PersonalSectionTitle'
            }, 
         5: 
            {
             'name': 'personal'
            }, 
         6: 
            {}, 
         7: 
            {
             'class': 'row-flex row-flex--middle'
            }, 
         8: 
            {}, 
         9: 
            {
             'class': 'accordion-icons'
            }, 
         10: 
             {
              'class': 'icon-159'
             }, 
         11: 
             {
              'class': 'icon-160'
             }, 
         12: 
             {
              'class': 'row-flex row-flex--middle'
             }, 
         13: 
             {
              'class': 'fl0 fs12'
             }, 
         14: 
             {
              'class': 'h4'
             }, 
         15: 
             {
              'class': 'align--right fs12'
             }, 
         16: 
             {
              'type': 'text/javascript', 
              'src': '//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99'
             }
        }
        >>> 
        >>> 
        >>> 
        >>> pobj(results)
        {
         0: 
            {}, 
         1: 
            {}, 
         2: None, 
         3: 
            {}, 
         4: 
            {}, 
         5: None, 
         6: 
            {}, 
         7: 
            {}, 
         8: 
            {}, 
         9: 
            {}, 
         10: None, 
         11: None, 
         12: 
             {}, 
         13: 
             {}, 
         14: 'personal settings', 
         15: None, 
         16: None
        }
        >>> 
        
        >>> html_lines = get_html_lines_from_cmdlines_ltdict_and_tags_info(cmds,stagns,etagns,results,attribs)
        >>> pobj(html_lines)
        {
         0: '      <html class lang="zh">', 
         1: '            <head>', 
         2: '                  <meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1">', 
         3: '                  </meta>', 
         4: '            </head>', 
         5: '            <body class="zh">', 
         6: '                    <header class="section-heading accordion-title" id="ctl00_leftColumn_PersonalSectionTitle">', 
         7: '                       <a name="personal">', 
         8: '                       </a>', 
         9: '                        <ul>', 
         10: '                            <li class="row-flex row-flex--middle">', 
         11: '                                 <div>', 
         12: '                                      <div class="accordion-icons">', 
         13: '                                         <i class="icon-159">', 
         14: '                                         </i>', 
         15: '                                         <i class="icon-160">', 
         16: '                                         </i>', 
         17: '                                      </div>', 
         18: '                                 </div>', 
         19: '                                 <div class="row-flex row-flex--middle">', 
         20: '                                      <div class="fl0 fs12">', 
         21: '                                           <div class="h4">', 
         22: '                                                personal settings', 
         23: '                                           </div>', 
         24: '                                      </div>', 
         25: '                                      <div class="align--right fs12">', 
         26: '                                      </div>', 
         27: '                                 </div>', 
         28: '                            </li>', 
         29: '                        </ul>', 
         30: '                    </header>', 
         31: '                    <script type="text/javascript" src="//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99">', 
         32: '                    </script>', 
         33: '            </body>', 
         34: '      </html>'
        }
        >>> 
    '''
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent = 0
    if('indent' in kwargs):
        indent = kwargs['indent']
    else:
        indent = 4
    if('path_sp' in kwargs):
        path_sp = kwargs['path_sp']
    else:
        path_sp = '/'
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    #
    max_stagns = max(ltdict.to_list(stagns))
    max_etagns = max(ltdict.to_list(etagns))
    max_seq = max(max_stagns,max_etagns)
    cond = max_seq -  (stagns.__len__() + etagns.__len__() - 1)
    if(cond == 0):
        updated = update_tags_info_with_results(stagns,etagns,results)
        textns = updated['textns']
    else:
        textns = kwargs['textns']
    html_lines = {}
    for i in range(0,cmds.__len__()):
        cmd_pl = cmds[i].split(cmd_sp)
        pl = hdict_object.get_path_list(cmd_pl,path_sp)
        ppl = copy.deepcopy(pl)
        ppl.pop(-1)
        prepend = hdict_object.xml_indent_prepend(ppl)
        tag = pl[-1]
        stagn = stagns[i]
        etagn = etagns[i]
        attrib = attribs[i]
        if(utils.is_dict(attrib)):
            attrib = attrib_dict_to_str(attrib)
        else:
            pass
        textn = textns[i]
        html_lines[stagn] = ''.join((prepend,'<',str(tag),attrib,'>'))
        html_lines[etagn] = ''.join((prepend,'</',str(tag),'>'))
        if(textn == None):
            pass
        else:
            prepend = ''.join((prepend,' '*(str(tag).__len__()+2)))
            html_lines[textn] = ''.join((prepend,str(results[i])))
    return(html_lines)

def cmdlines_full_dict_to_html_text(cmdlines_full_dict,**kwargs):
    '''
    >>> 
    >>> cmdlines_full_dict.keys()
        dict_keys(['results', 'attribs', 'cmds'])
        >>> pobj(cmdlines_full_dict['cmds'])
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }

        >>> >>> 
        >>> pobj(cmdlines_full_dict['attribs'])
        {
         0: 
            {
             'class': '', 
             'lang': 'zh'
            }, 
         1: 
            {}, 
         2: 
            {
             'http-equiv': 'X-UA-Compatible', 
             'content': 'IE=EDGE,chrome=1'
            }, 
         3: 
            {
             'class': 'zh'
            }, 
         4: 
            {
             'class': 'section-heading accordion-title', 
             'id': 'ctl00_leftColumn_PersonalSectionTitle'
            }, 
         5: 
            {
             'name': 'personal'
            }, 
         6: 
            {}, 
         7: 
            {
             'class': 'row-flex row-flex--middle'
            }, 
         8: 
            {}, 
         9: 
            {
             'class': 'accordion-icons'
            }, 
         10: 
             {
              'class': 'icon-159'
             }, 
         11: 
             {
              'class': 'icon-160'
             }, 
         12: 
             {
              'class': 'row-flex row-flex--middle'
             }, 
         13: 
             {
              'class': 'fl0 fs12'
             }, 
         14: 
             {
              'class': 'h4'
             }, 
         15: 
             {
              'class': 'align--right fs12'
             }, 
         16: 
             {
              'type': 'text/javascript', 
              'src': '//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99'
             }
        }
        >>> 
        >>> 
        >>> pobj(cmdlines_full_dict['results'])
        {
         0: 
            {}, 
         1: 
            {}, 
         2: None, 
         3: 
            {}, 
         4: 
            {}, 
         5: None, 
         6: 
            {}, 
         7: 
            {}, 
         8: 
            {}, 
         9: 
            {}, 
         10: None, 
         11: None, 
         12: 
             {}, 
         13: 
             {}, 
         14: 'personal settings', 
         15: None, 
         16: None
        }
        >>> 
        >>> 
        >>> html_text = cmdlines_full_dict_to_html_text(cmdlines_full_dict)
        >>> print(html_text)
              <html class lang="zh">
                    <head>
                          <meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=1">
                          </meta>
                    </head>
                    <body class="zh">
                            <header class="section-heading accordion-title" id="ctl00_leftColumn_PersonalSectionTitle">
                               <a name="personal">
                               </a>
                                <ul>
                                    <li class="row-flex row-flex--middle">
                                         <div>
                                              <div class="accordion-icons">
                                                 <i class="icon-159">
                                                 </i>
                                                 <i class="icon-160">
                                                 </i>
                                              </div>
                                         </div>
                                         <div class="row-flex row-flex--middle">
                                              <div class="fl0 fs12">
                                                   <div class="h4">
                                                        personal settings
                                                   </div>
                                              </div>
                                              <div class="align--right fs12">
                                              </div>
                                         </div>
                                    </li>
                                </ul>
                            </header>
                            <script type="text/javascript" src="//webapi.amap.com/maps?v=1.3&key=efbfdf421dca99bfa5b703841c57ee99">
                            </script>
                    </body>
              </html>
        >>> 
        >>> 
    '''
    def html_ltdict_to_html_text(html_lines,line_sp):
        html_text = ''
        for i in range(0,html_lines.__len__()):
            if(html_lines[i] == ''):
                pass
            else:
                html_text = ''.join((html_text,html_lines[i],line_sp))
        html_text = utils.str_rstrip(html_text,line_sp,1)
        return(html_text)
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('html_lines' in cmdlines_full_dict):
        html_lines = cmdlines_full_dict['html_lines']
        html_text = html_ltdict_to_html_text(html_lines,line_sp)
        return(html_text)
    elif(('slines' in cmdlines_full_dict) & ('elines' in cmdlines_full_dict) & ('tlines' in cmdlines_full_dict)):
        stagns =  cmdlines_full_dict['stagns']
        textns = cmdlines_full_dict['textns']
        etagns = cmdlines_full_dict['etagns']
        slines = cmdlines_full_dict['slines']
        elines = cmdlines_full_dict['elines']
        tlines = cmdlines_full_dict['tlines']
        html_lines = {}
        for i in range(0,stagns.__len__()):
            seq = stagns[i]
            line = slines[i]
            html_lines[seq] = line
            seq = etagns[i]
            line = elines[i]
            html_lines[seq] = line
            seq = textns[i]
            line = tlines[i]
            if(seq == None):
                pass
            else:
                html_lines[seq] = line
        html_text = html_ltdict_to_html_text(html_lines,line_sp)
        return(html_text)
    elif('stagns' in cmdlines_full_dict):
        stagns =  cmdlines_full_dict['stagns']
        cmds = cmdlines_full_dict['cmds']
        results = cmdlines_full_dict['results']
        attribs = cmdlines_full_dict['attribs']
        tmp = []
        for i in range(0,stagns.__len__()):
            t = (stagns[i],cmds[i],results[i],attribs[i])
            tmp.append(t)
        tmp.sort(key=itemgetter(0))
        for i in range(0,tmp.__len__()):
            cmd = tmp[i][1]
            result = tmp[i][2]
            attrib = tmp[i][3]
            if(type(attrib) == type({})):
                attrib = hdict_object.attrib_dict_to_str(attrib)
            else:
                pass
            cmds[i] = cmd
            results[i] = result
            attribs[i] = attrib
        tmp = get_tags_info_from_cmdlines_ltdict(cmds)
        stagns = tmp['stagns']
        etagns = tmp['etagns']
        html_lines = get_html_lines_from_cmdlines_ltdict_and_tags_info(cmds,stagns,etagns,results,attribs)
        html_text = html_ltdict_to_html_text(html_lines,line_sp)
        return(html_text)
    else:
        if(reorder):
            cmds = cmdlines_full_dict['cmds']
            ltdict.sort(cmds)
        else:
            cmds = cmdlines_full_dict['cmds']
        results = cmdlines_full_dict['results']
        attribs = cmdlines_full_dict['attribs']
        tmp = get_tags_info_from_cmdlines_ltdict(cmds)
        stagns = tmp['stagns']
        etagns = tmp['etagns']
        for i in range(0,attribs.__len__()):
            if(type(attribs[i]) == type({})):
                attribs[i] = hdict_object.attrib_dict_to_str(attribs[i])
            else:
                pass
        html_lines = get_html_lines_from_cmdlines_ltdict_and_tags_info(cmds,stagns,etagns,results,attribs)
        html_text = html_ltdict_to_html_text(html_lines,line_sp)
        return(html_text)

def cmdlines_full_dict_to_hdict(cmdlines_full_dict,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    html_text = cmdlines_full_dict_to_html_text(cmdlines_full_dict)
    hdict = hdict_xml.html_to_hdict(html_text=html_text)
    return(hdict)

def get_obj_value_via_cmd(cmd,obj,**kwargs):
    '''
        >>> 
        >>> 
        >>> d.keys()
        dict_keys(['userDeviceId', 'defaultComponents', 'customModeSortingEnabled', 'config', 'guideModal2', 'device', 'client', 'userActivityIds', 'deviceFields', 'graphDeviceFieldIds', 'limitations', 'compatibleApps', 'guideModal'])
        >>> d['client'].keys()
        dict_keys(['id', 'username', 'defaultActivityID', 'formattingOptions', 'publicity', 'userActivityIDs', 'userImage', 'gender', 'geoIPLocation', 'isCoach', 'mapProvider'])
        >>> d['client']['formattingOptions'].keys()
        dict_keys(['unitSystem', 'startOfWeek', 'decimalSeparator', 'language'])
        >>> 
        >>> get_obj_value_via_cmd('client formattingOptions language',d)
        'en'
        >>> get_obj_value_via_cmd('client formattingOptions unitSystem',d)
        'metric'
        >>> get_obj_value_via_cmd('client formattingOptions startOfWeek',d)
        1
        >>> 
        >>> 
    '''
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
        s2n = kwargs['s2n']
    else:
        s2n = 0
    cmd = format_cmd_str(cmd,cmd_sp=cmd_sp)
    path_list = cmd.split(cmd_sp)
    rslt = utils.dict_getitem_via_path_list(obj,path_list,n2s=n2s,s2n=s2n)
    return(rslt)

def get_cmdlines_ltdict_duplines_stats(cmdlines_ltdict):
    '''
        >>> pobj(cmds)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> vkltd = get_cmdlines_ltdict_duplines_stats(cmds)
        >>> pobj(vkltd,fixed_indent=1)
        {
            'html body header ul li div div': [9, 13, 15],
            'html head meta': [2],
            'html body header ul': [6],
            'html body header': [4],
            'html body header a': [5],
            'html': [0],
            'html body header ul li div div i': [10, 11],
            'html body': [3],
            'html body script': [16],
            'html head': [1],
            'html body header ul li div': [8, 12],
            'html body header ul li div div div': [14],
            'html body header ul li': [7]
        }
    '''
    ltd = cmdlines_ltdict
    vkltd = {}
    for i in range(0,ltd.__len__()):
        k = ltd[i]
        if(k in vkltd):
            vkltd[k].append(i)
        else:
            vkltd[k] = [i]
    return(vkltd)

def get_cmdlines_ltdict_leaf_stats(cmdlines_ltdict,**kwargs):
    '''
    
    >>> pobj(get_cmdlines_ltdict_leaf_stats(cmds))
    {
     0: 0, 
     1: 0, 
     2: 1, 
     3: 0, 
     4: 0, 
     5: 1, 
     6: 0, 
     7: 0, 
     8: 0, 
     9: 0, 
     10: 1, 
     11: 1, 
     12: 0, 
     13: 0, 
     14: 1, 
     15: 1, 
     16: 1
    }
    >>> 
    
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    leaf_dict = {}
    prev_cmd = ltd[0]
    leaf_dict[0] = 1
    for i in range(1,ltd.__len__()):
        curr_cmd = ltd[i]
        prev_pl = cmd_str_to_cmd_pl(prev_cmd,cmd_sp = cmd_sp)
        curr_pl = cmd_str_to_cmd_pl(curr_cmd,cmd_sp = cmd_sp)
        cond = utils.path_list_is_parent(prev_pl,curr_pl)
        if(cond):
            leaf_dict[i-1] = 0
        else:
            leaf_dict[i-1] = 1
        prev_cmd = curr_cmd
    leaf_dict[ltd.__len__() - 1] = 1
    return(leaf_dict)

def get_cmdlines_ltdict_parent_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 
        >>> 
        >>> 
        >>> pobj(get_cmdlines_ltdict_parent_stats(ltd))
        {
         1: 0, 
         2: 1, 
         3: 0, 
         4: 3, 
         5: 4, 
         6: 4, 
         7: 6, 
         8: 7, 
         9: 8, 
         10: 9, 
         11: 9, 
         12: 7, 
         13: 12, 
         14: 13, 
         15: 12, 
         16: 3
        }
        >>> 
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    parent_dict = {}
    for i in range(0,ltd.__len__()):
        curr_cmd = ltd[i]
        curr_pl = cmd_str_to_cmd_pl(curr_cmd,cmd_sp = cmd_sp)
        for j in range(0,i):
            prev_cmd = ltd[j]
            prev_pl = cmd_str_to_cmd_pl(prev_cmd,cmd_sp = cmd_sp)
            cond = utils.path_list_is_parent(prev_pl,curr_pl)
            if(cond):
                parent_dict[i] = j
            else:
                pass
    for i in range(0,ltd.__len__()):
        if(i in parent_dict):
            pass
        else:
            parent_dict[i] = None
    return(parent_dict)

def get_cmdlines_ltdict_son_stats(cmdlines_ltdict,**kwargs):
    '''>>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> sltd = get_cmdlines_ltdict_son_stats(ltd)
        >>> pobj(sltd,fixed_indent=1)
        {
            0: [1, 3],
            1: [2],
            3: [4, 16],
            4: [5, 6],
            6: [7],
            7: [8, 12],
            8: [9],
            9: [10, 11],
            12: [13, 15],
            13: [14]
        }
        >>> 
    >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    sltd = {}
    for k in pltd:
        p = pltd[k]
        if(p in sltd):
            sltd[p].append(k)
        else:
            sltd[p] = [k]
    return(sltd)

def get_cmdlines_ltdict_hierarchy_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 
        >>> root = get_cmdlines_ltdict_hierarchy_stats(ltd)
        >>> pobj(root)
        [
         [
          [
           2
          ], 
          [
           [
            5, 
            [
             [
              [
               [
                10, 
                11
               ]
              ], 
              [
               [
                14
               ], 
               15
              ]
             ]
            ]
           ], 
           16
          ]
         ]
        ]
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    sltd = get_cmdlines_ltdict_son_stats(ltd,cmd_sp = cmd_sp)
    root = ltdict.list2ltdict(list(ltd.keys()))
    for k in pltd:
        del root[k]
    root = ltdict.to_list(root)
    next_unhandled_layer = [root]
    nlen = next_unhandled_layer.__len__()
    while(nlen >0):
        new_next_unhandled_layer = []
        for i in range(0,nlen):
            unhandled = next_unhandled_layer[i]
            for j in range(0,unhandled.__len__()):
                p = unhandled[j]
                if(p in sltd):
                    unhandled[j] = sltd[p]
                    new_next_unhandled_layer.append(sltd[p])
        next_unhandled_layer = new_next_unhandled_layer
        nlen = next_unhandled_layer.__len__()
    return(root)

def get_cmdlines_ltdict_breadth_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> breadths = get_cmdlines_ltdict_breadth_stats(ltd)
        >>> pobj(breadths,fixed_indent=1)
        {
            0: [0],
            1: [1, 3],
            2: [2, 4, 16],
            3: [5, 6],
            4: [7],
            5: [8, 12],
            6: [9, 13, 15],
            7: [10, 11, 14]
        }
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    sltd = get_cmdlines_ltdict_son_stats(ltd,cmd_sp = cmd_sp)
    root = ltdict.list2ltdict(list(ltd.keys()))
    for k in pltd:
        del root[k]
    root = ltdict.to_list(root)
    next_unhandled_layer = [root]
    nlen = next_unhandled_layer.__len__()
    depth = 0
    breadths = {}
    while(nlen >0):
        breadths[depth] = []
        new_next_unhandled_layer = []
        for i in range(0,nlen):
            unhandled = next_unhandled_layer[i]
            for j in range(0,unhandled.__len__()):
                p = unhandled[j]
                breadths[depth].append(p)
                if(p in sltd):
                    new_next_unhandled_layer.append(sltd[p])
        next_unhandled_layer = new_next_unhandled_layer
        nlen = next_unhandled_layer.__len__()
        depth = depth + 1
    return(breadths)
 
def get_cmdlines_ltdict_ancestors_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> ltd = copy.deepcopy(cmds)
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> altd = get_cmdlines_ltdict_ancestors_stats(ltd)
        >>> 
        >>> pobj(altd,fixed_indent=1)
        {
            0: [],
            1: [0],
            2: [1, 0],
            3: [0],
            4: [3, 0],
            5: [4, 3, 0],
            6: [4, 3, 0],
            7: [6, 4, 3, 0],
            8: [7, 6, 4, 3, 0],
            9: [8, 7, 6, 4, 3, 0],
            10: [9, 8, 7, 6, 4, 3, 0],
            11: [9, 8, 7, 6, 4, 3, 0],
            12: [7, 6, 4, 3, 0],
            13: [12, 7, 6, 4, 3, 0],
            14: [13, 12, 7, 6, 4, 3, 0],
            15: [12, 7, 6, 4, 3, 0],
            16: [3, 0]
        }
        
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    altd = {}
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    for seq in cmdlines_ltdict:
        if(seq in pltd):
            p = pltd[seq]
            altd[seq] = [p]
            while(p in pltd):
                p = pltd[p]
                altd[seq].append(p)
        else:
            altd[seq] = []
    return(altd)

def get_cmdlines_ltdict_descedants_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> 
        >>> ltd = copy.deepcopy(cmds)
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 
        >>> 
        >>> dltd = get_cmdlines_ltdict_descedants_stats(ltd)
        >>> pobj(dltd,fixed_indent=1)
        {
            0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            1: [2],
            3: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            4: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            6: [7, 8, 9, 10, 11, 12, 13, 14, 15],
            7: [8, 9, 10, 11, 12, 13, 14, 15],
            8: [9, 10, 11],
            9: [10, 11],
            12: [13, 14, 15],
            13: [14]
        }
        >>> 



    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    sltd = get_cmdlines_ltdict_son_stats(ltd,cmd_sp = cmd_sp)
    altd = get_cmdlines_ltdict_ancestors_stats(ltd)
    dltd = {}
    for seq in altd:
        al = altd[seq]
        for i in range(0,al.__len__()):
            a = al[i]
            if(a in dltd):
                dltd[a].append(seq)
            else:
                dltd[a] = [seq]
    return(dltd)

def get_cmdlines_ltdict_roots_stats(cmdlines_ltdict,**kwargs):
    '''
    >>> 
    >>> 
    >>> pobj(ltd)
    {
     0: 'html', 
     1: 'html head', 
     2: 'html head meta', 
     3: 'html body', 
     4: 'html body header', 
     5: 'html body header a', 
     6: 'html body header ul', 
     7: 'html body header ul li', 
     8: 'html body header ul li div', 
     9: 'html body header ul li div div', 
     10: 'html body header ul li div div i', 
     11: 'html body header ul li div div i', 
     12: 'html body header ul li div', 
     13: 'html body header ul li div div', 
     14: 'html body header ul li div div div', 
     15: 'html body header ul li div div', 
     16: 'html body script'
    }
    >>> 
    >>> roots = get_cmdlines_ltdict_roots_stats(ltd)
    >>> roots
    [0]
    >>> 
    >>> 

    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('only_dup' in kwargs):
        only_dup = kwargs['only_dup']
    else:
        only_dup = 0
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    root = ltdict.list2ltdict(list(ltd.keys()))
    for k in pltd:
        del root[k]
    root = ltdict.to_list(root)
    return(root)

def get_cmdlines_ltdict_siblings_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> 
        >>> ltd = copy.deepcopy(cmds)
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> sibltd = get_cmdlines_ltdict_siblings_stats(ltd)
        >>> pobj(sibltd)
        {
         0: 0, 
         1: 0, 
         2: 0, 
         3: 1, 
         4: 0, 
         5: 0, 
         6: 1, 
         7: 0, 
         8: 0, 
         9: 0, 
         10: 0, 
         11: 1, 
         12: 1, 
         13: 0, 
         14: 0, 
         15: 1, 
         16: 1
        }

        >>> 
        >>> sibltd = get_cmdlines_ltdict_siblings_stats(ltd,only_dup=1)
        >>> pobj(sibltd,fixed_indent=1)
        {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: 0,
            9: None,
            10: 0,
            11: 1,
            12: 1,
            13: 0,
            14: None,
            15: 1,
            16: None
        }
        >>> 
        
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('only_dup' in kwargs):
        only_dup = kwargs['only_dup']
    else:
        only_dup = 0
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    sltd = get_cmdlines_ltdict_son_stats(ltd,cmd_sp = cmd_sp)
    #
    roots = get_cmdlines_ltdict_roots_stats(ltd)
    #
    sibltd = {}
    for i in range(0,roots.__len__()):
        sibltd[roots[i]] = 0
    for each in sltd:
        sons = sltd[each]
        for i in range(0,sons.__len__()):
            seq = sons[i]
            if(only_dup):
                if(sons.__len__()==1):
                    sibltd[seq] = None
                else:
                    sibltd[seq] = i
            else:
                sibltd[seq] = i
    if(only_dup):
        vkltd = get_cmdlines_ltdict_duplines_stats(ltd)
        undup_seqs = []
        for cmd in vkltd:
            seqs = vkltd[cmd]
            for i in range(0,seqs.__len__()):
                seq = seqs[i]
                if(seqs.__len__()==1):
                    pass
                else:
                    if(seq in undup_seqs):
                        pass
                    else:
                        undup_seqs.append(seq)
        undup_seqs = sorted(undup_seqs)
        for useq in ltd:
            if(useq in undup_seqs):
                pass
            else:
                sibltd[useq] = None
        for i in range(0,roots.__len__()):
            sibltd[roots[i]] = None
    else:
        pass
    return(sibltd)

def get_cmdlines_ltdict_depths_stats(cmdlines_ltdict,**kwargs):
    '''
        >>> 
        >>> ltd = copy.deepcopy(cmds)
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> depths_desc = get_cmdlines_ltdict_depths_stats(ltd)
        >>> pobj(depths_desc,fixed_indent=1)
        {
            0: [0],
            1: [1, 3],
            2: [2, 4, 16],
            3: [5, 6],
            4: [7],
            5: [8, 12],
            6: [9, 13, 15],
            7: [10, 11, 14]
        }
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('only_dup' in kwargs):
        only_dup = kwargs['only_dup']
    else:
        only_dup = 0
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    depths_desc = {}
    for seq in ltd:
        cmd_str = ltd[seq]
        cmd_pl = cmd_str_to_cmd_pl(cmd_str,cmd_sp=cmd_sp)
        depth = cmd_pl.__len__() - 1
        if(depth in depths_desc):
            depths_desc[depth].append(seq)
        else:
            depths_desc[depth] =[seq]
    return(depths_desc)

def undup_cmdlines_ltdict(cmdlines_ltdict,**kwargs):
    '''
        >>> ltd = copy.deepcopy(cmds)
        >>> pobj(ltd)
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div', 
         9: 'html body header ul li div div', 
         10: 'html body header ul li div div i', 
         11: 'html body header ul li div div i', 
         12: 'html body header ul li div', 
         13: 'html body header ul li div div', 
         14: 'html body header ul li div div div', 
         15: 'html body header ul li div div', 
         16: 'html body script'
        }
        >>> 
        >>> 
        >>> pobj(undup_cmdlines_ltdict(ltd))
        {
         0: 'html', 
         1: 'html head', 
         2: 'html head meta', 
         3: 'html body', 
         4: 'html body header', 
         5: 'html body header a', 
         6: 'html body header ul', 
         7: 'html body header ul li', 
         8: 'html body header ul li div [0]', 
         9: 'html body header ul li div [0] div', 
         10: 'html body header ul li div [0] div i [0]', 
         11: 'html body header ul li div [0] div i [1]', 
         12: 'html body header ul li div [1]', 
         13: 'html body header ul li div [1] div [0]', 
         14: 'html body header ul li div [1] div [0] div', 
         15: 'html body header ul li div [1] div [1]', 
         16: 'html body script'
        }

        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if(reorder):
        ltd = ltdict.sort(cmdlines_ltdict)
    else:
        ltd = cmdlines_ltdict
    vkltd = get_cmdlines_ltdict_duplines_stats(ltd)
    pltd = get_cmdlines_ltdict_parent_stats(ltd,cmd_sp = cmd_sp)
    # sltd = get_cmdlines_ltdict_son_stats(ltd,cmd_sp = cmd_sp)
    # bltd = get_cmdlines_ltdict_breadth_stats(ltd,cmd_sp = cmd_sp)
    # dltd = get_cmdlines_ltdict_descedants_stats(ltd,cmd_sp = cmd_sp)
    sibltd = get_cmdlines_ltdict_siblings_stats(ltd,cmd_sp = cmd_sp,only_dup=1)
    dpltd = get_cmdlines_ltdict_depths_stats(ltd,cmd_sp = cmd_sp)
    ltd_s1 = copy.deepcopy(ltd)
    for depth in range(0,dpltd.__len__()):
        layer = dpltd[depth]
        for i in range(0,layer.__len__()):
            seq = layer[i]
            sibseq = sibltd[seq]
            if(sibseq == None):
                if(seq in pltd):
                    p = pltd[seq]
                    #root node s parent = None
                    #None node have no sib
                    if(p == None):
                        pass
                    elif(sibltd[p]==None):
                        pass
                    else:
                        tag = cmd_str_to_cmd_pl(ltd_s1[seq],cmd_sp=cmd_sp)[-1]
                        ltd_s1[seq] = ''.join((ltd_s1[p],cmd_sp,tag))
                else:
                    pass
            else:
                p = pltd[seq]
                cmd_str = ltd[p]
                bs = vkltd[cmd_str]
                if(bs.__len__() == 1):
                    ltd_s1[seq] = ''.join((ltd_s1[seq],cmd_sp,'[',str(sibseq),']'))
                else:
                    tag = cmd_str_to_cmd_pl(ltd_s1[seq],cmd_sp=cmd_sp)[-1]
                    ltd_s1[seq] = ''.join((ltd_s1[p],cmd_sp,tag,cmd_sp,'[',str(sibseq),']'))
    return(ltd_s1)

def cmdlines_str_to_obj(cmdlines_str,**kwargs):
    '''
        >>> 
        >>> print(cmdlines_str)
        html
        html head
        html head meta
        html body
        html body header
        html body header a
        html body header ul
        html body header ul li
        html body header ul li div
        html body header ul li div div
        html body header ul li div div i
        html body header ul li div div i
        html body header ul li div
        html body header ul li div div
        html body header ul li div div div
        html body header ul li div div
        html body script
        >>> obj = cmdlines_str_to_obj(cmdlines_str)
        >>> 
        >>> obj
        >>> pobj(obj,fixed_indent=1)
        {
            'html': {
                'body': {
                    'script': {},
                    'header': {
                        'a': {},
                        'ul': {
                            'li': {
                                'div': {
                                    '[0]': {
                                        'div': {
                                            'i': {
                                                '[0]': {},
                                                '[1]': {}
                                            }
                                        }
                                    },
                                    '[1]': {
                                        'div': {
                                            '[0]': {
                                                'div': {}
                                            },
                                            '[1]': {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'head': {
                    'meta': {}
                }
            }
        }
        >>> 
        >>> 
        
    '''
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
    if('keep_order' in kwargs):
        keep_order = kwargs['keep_order']
    else:
        keep_order = 1
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('undup' in kwargs):
        undup = kwargs['undup']
    else:
        undup = 1
    ltd = cmdlines_str_to_ltdict(cmdlines_str,line_sp=line_sp)
    if(undup):
        ltd = undup_cmdlines_ltdict(ltd,reorder=reorder,cmd_sp=cmd_sp)
    else:
        pass
    obj = {}
    for i in range(0,ltd.__len__()):
        pl = hdict_object.get_path_list(ltd[i],sp=cmd_sp)
        utils.dict_setdefault_via_path_list(obj,pl,n2s=n2s,s2n=s2n)
        if(results=={}):
            pass
        else:
            if(results[i] == {}):
                pass
            else:
                utils.dict_setitem_via_path_list(obj,pl,results[i],n2s=n2s,s2n=s2n)
    return(obj)

def cmdlines_str_to_html_text(cmdlines_str,**kwargs):
    '''
    >>> print(cmdlines_str)
        html
        html head
        html head meta
        html body
        html body header
        html body header a
        html body header ul
        html body header ul li
        html body header ul li div
        html body header ul li div div
        html body header ul li div div i
        html body header ul li div div i
        html body header ul li div
        html body header ul li div div
        html body header ul li div div div
        html body header ul li div div
        html body script
        >>> 
        >>> html_text = cmdlines_str_to_html_text(cmdlines_str)
        >>> print(html_text)
              <html>
                    <head>
                          <meta>
                          </meta>
                    </head>
                    <body>
                            <header>
                               <a>
                               </a>
                                <ul>
                                    <li>
                                         <div>
                                              <div>
                                                 <i>
                                                 </i>
                                                 <i>
                                                 </i>
                                              </div>
                                         </div>
                                         <div>
                                              <div>
                                                   <div>
                                                   </div>
                                              </div>
                                              <div>
                                              </div>
                                         </div>
                                    </li>
                                </ul>
                            </header>
                            <script>
                            </script>
                    </body>
              </html>
        >>> 
    '''
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
    cmdlines_ltdict = cmdlines_str_to_ltdict(cmdlines_str,line_sp=line_sp)
    cmdlines_full_dict = {}
    cmdlines_full_dict['cmds'] = cmdlines_ltdict
    cmdlines_full_dict['attribs'] = {}
    cmdlines_full_dict['results'] = {}
    for seq in cmdlines_ltdict:
        cmdlines_full_dict['attribs'][seq] = {}
        cmdlines_full_dict['results'][seq] = {}
    html_text = cmdlines_full_dict_to_html_text(cmdlines_full_dict,line_sp=line_sp)
    return(html_text)

def html_text_to_cmdlines_full_dict(**kwargs):
    '''
         >>> print(html_text)
               <html>
                     <head>
                           <meta>
                           </meta>
                     </head>
                     <body>
                             <header>
                                <a>
                                </a>
                                 <ul>
                                     <li>
                                          <div>
                                               <div>
                                                  <i>
                                                  </i>
                                                  <i>
                                                  </i>
                                               </div>
                                          </div>
                                          <div>
                                               <div>
                                                    <div>
                                                    </div>
                                               </div>
                                               <div>
                                               </div>
                                          </div>
                                     </li>
                                 </ul>
                             </header>
                             <script>
                             </script>
                     </body>
               </html>
         >>> 
        >>> cfd = html_text_to_cmdlines_full_dict(html_text=html_text)
        >>> pobj(cfd)
        {
         'results': 
                    {
                     0: 
                        {}, 
                     1: 
                        {}, 
                     2: None, 
                     3: 
                        {}, 
                     4: 
                        {}, 
                     5: '\n                       ', 
                     6: 
                        {}, 
                     7: 
                        {}, 
                     8: 
                        {}, 
                     9: 
                        {}, 
                     10: '\n                                         ', 
                     11: '\n                                         ', 
                     12: 
                         {}, 
                     13: 
                         {}, 
                     14: '\n                                           ', 
                     15: '\n                                      ', 
                     16: '\n                    '
                    }, 
         'attribs': 
                    {
                     0: 
                        {}, 
                     1: 
                        {}, 
                     2: 
                        {}, 
                     3: 
                        {}, 
                     4: 
                        {}, 
                     5: 
                        {}, 
                     6: 
                        {}, 
                     7: 
                        {}, 
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
                     13: 
                         {}, 
                     14: 
                         {}, 
                     15: 
                         {}, 
                     16: 
                         {}
                    }, 
         'cmds': 
                 {
                  0: 'html', 
                  1: 'html head', 
                  2: 'html head meta', 
                  3: 'html body', 
                  4: 'html body header', 
                  5: 'html body header a', 
                  6: 'html body header ul', 
                  7: 'html body header ul li', 
                  8: 'html body header ul li div', 
                  9: 'html body header ul li div div', 
                  10: 'html body header ul li div div i', 
                  11: 'html body header ul li div div i', 
                  12: 'html body header ul li div', 
                  13: 'html body header ul li div div', 
                  14: 'html body header ul li div div div', 
                  15: 'html body header ul li div div', 
                  16: 'html body script'
                 }
        }
        >>> 
        
    '''
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
    temp = hdict_xml.html_to_hdict(root=root)
    hdict=temp['hdict']
    sdict=temp['sdict']
    prdict=temp['prdict']
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    rslt = hdict_to_cmdlines_full_dict(hdict,sdict=sdict,prdict=prdict,s2n=s2n,n2s=n2s,disable_type=disable_type,cmd_sp=cmd_sp,path_list_cmd=path_list_cmd,reorder=reorder)
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


def show_html_text_via_cmd(cmd,**kwargs):
    '''
        >>> print(html_text)
        <html>
              <head>
                    <meta>
                    </meta>
              </head>
              <body>
                      <header>
                         <a>
                         </a>
                          <ul>
                              <li>
                                   <div>
                                        <div>
                                           <i>
                                           </i>
                                           <i>
                                           </i>
                                        </div>
                                   </div>
                                   <div>
                                        <div>
                                             <div>
                                             </div>
                                        </div>
                                        <div>
                                        </div>
                                   </div>
                              </li>
                          </ul>
                      </header>
                      <script>
                      </script>
              </body>
        </html>
        >>> 
        >>> tmp = show_html_text_via_cmd('html body',html_text=html_text)
        html body
        html body header
        html body header a
        html body header ul
        html body header ul li
        html body header ul li div
        html body header ul li div div
        html body header ul li div div i
        html body header ul li div div i
        html body header ul li div
        html body header ul li div div
        html body header ul li div div div
        html body header ul li div div
        html body script
        html body
        html body header
        html body header a
        html body header ul
        html body header ul li
        html body header ul li div
        html body header ul li div div
        html body header ul li div div i
        html body header ul li div div i
        html body header ul li div
        html body header ul li div div
        html body header ul li div div div
        html body header ul li div div
        html body script
        
        >>> 
        >>> 
        >>> tmp.keys()
        dict_keys(['seqs', 'rslt'])
        >>> print(tmp['rslt'])
        html body
        html body header
        html body header a
        html body header ul
        html body header ul li
        html body header ul li div
        html body header ul li div div
        html body header ul li div div i
        html body header ul li div div i
        html body header ul li div
        html body header ul li div div
        html body header ul li div div div
        html body header ul li div div
        html body script
        
        >>> print(tmp['seqs'])
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        >>> 

    '''
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
        pass
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
        get_all = 1
    if('style' in kwargs):
        style = kwargs['style']
    else:
        style = 'flat'
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    if('cmdlines_full_dict' in kwargs):
        temp = kwargs['cmdlines_full_dict']
    else:
        temp = html_text_to_cmdlines_full_dict(root=root,s2n=s2n,n2s=n2s,disable_type=1,cmd_sp=cmd_sp,line_sp=line_sp,reorder=reorder)
    cmdlines_ltdict = temp['cmds']
    results = temp['results']
    attribs = temp['attribs']
    rslt_seqs = show_prompt_from_cmdlines_ltdict(cmd,cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    if(get_all):
            rslt = {}
            howmany = rslt_seqs.__len__()
            print("\n-Found {0} matched:".format(howmany))
            for i in range(0,howmany):
                seq = rslt_seqs[i]
                rslt[i] = {'cmd':cmdlines_ltdict[seq],'result':results[seq],'attrib':attribs[seq],'seq':seq}
                print("-----------------------------------------------------")
                if(style == 'flat'):
                    cmd = str(cmdlines_ltdict[seq])
                    spaint.slpaint('   [cmd]: ','white',cmd,'yellow')
                    result = str(results[seq])
                    spaint.slpaint('[result]: ','white',result,'red')
                    attrib = str(attribs[seq])
                    spaint.slpaint('[attrib]: ','white',attrib,'cyan1')
                    spaint.slpaint('   [seq]: ','white',str(seq),'magenta1')
                else:
                    jprint.pobj(rslt[i])
            print("-----------------------------------------------------")
            return(rslt)
    else:
        if(rslt_seqs.__len__()==1):
            seq = rslt_seqs[0]
            #cmd = jprint.paint_str(str(cmdlines_ltdict[seq]),single_color='yellow')
            #result = jprint.paint_str(str(results[seq]),single_color='blue')
            #attrib = jprint.paint_str(str(attribs[seq]),single_color='green')
            #print('cmd: {0}'.format(cmd))
            #print('result: {0}'.format(result))
            #print('attrib: {0}'.format(attrib))
            cmd = str(cmdlines_ltdict[seq])
            spaint.slpaint('cmd: ','white',cmd,'yellow')
            result = str(results[seq])
            spaint.slpaint('result: ','white',result,'red')
            attrib = str(attribs[seq])
            spaint.slpaint('attrib: ','white',attrib,'cyan1')
            #@@@@
            return({'cmd':cmdlines_ltdict[seq],'result':results[seq],'attrib':attribs[seq],'seq':seq})
        else:
            rslt = ''
            for i in range(0,rslt_seqs.__len__()):
                seq = rslt_seqs[i]
                rslt = ''.join((rslt,cmdlines_ltdict[seq],line_sp))
            #print(jprint.paint_str(rslt,single_color='yellow'))
            #spaint.paint(rslt,single_color='yellow')
            return({'rslt':rslt, 'seqs':rslt_seqs})    

def obj_to_cmdlines_full_dict(obj,**kwargs):
    '''
        >>> pobj(obj)
        {
         'userActivityIDs': 
                            [], 
         'username': 'Ihgazni', 
         'gender': 'm', 
         'weight': 80.0, 
         'publicity': 2, 
         'id': 1489059, 
         'isCoach': False, 
         'geoIPLocation': 
                          {
                           'lat': 35.0, 
                           'lon': 105.0
                          }, 
         'mapProvider': 'amap', 
         'height': 1.71, 
         'defaultActivityID': 1, 
         'userImage': 
                      {
                       'default': 
                                  {
                                   'size128': 
                                              {
                                               'url': '//content.static.movescount.cn/1a344c5/img/members/member_m_128.png'
                                              }, 
                                   'size222': 
                                              {
                                               'url': '//content.static.movescount.cn/1a344c5/img/members/member_m_222.png'
                                              }, 
                                   'size60': 
                                             {
                                              'url': '//content.static.movescount.cn/1a344c5/img/members/member_m.png'
                                             }
                                  }
                      }, 
         'birthDate': '1980-12-03T00:00:00Z'
        }
        >>> 
        >>> obj=d['client']
        >>> cfd = obj_to_cmdlines_full_dict(obj)
        >>> cfd.keys()
        dict_keys(['attribs', 'cmds', 'results'])
        >>> pobj(cfd['cmds'])
        {
         0: 'userActivityIDs', 
         1: 'username', 
         2: 'gender', 
         3: 'weight', 
         4: 'publicity', 
         5: 'id', 
         6: 'isCoach', 
         7: 'geoIPLocation', 
         8: 'geoIPLocation lat', 
         9: 'geoIPLocation lon', 
         10: 'mapProvider', 
         11: 'height', 
         12: 'defaultActivityID', 
         13: 'userImage', 
         14: 'userImage default', 
         15: 'userImage default size128', 
         16: 'userImage default size128 url', 
         17: 'userImage default size222', 
         18: 'userImage default size222 url', 
         19: 'userImage default size60', 
         20: 'userImage default size60 url', 
         21: 'birthDate'
        }
        >>> 
        >>> pobj(cfd['attribs'])
        {
         0: 
            {
             'type': 'list'
            }, 
         1: 
            {
             'type': 'str'
            }, 
         2: 
            {
             'type': 'str'
            }, 
         3: 
            {
             'type': 'float'
            }, 
         4: 
            {
             'type': 'int'
            }, 
         5: 
            {
             'type': 'int'
            }, 
         6: 
            {
             'type': 'bool'
            }, 
         7: 
            {
             'type': 'dict'
            }, 
         8: 
            {
             'type': 'float'
            }, 
         9: 
            {
             'type': 'float'
            }, 
         10: 
             {
              'type': 'str'
             }, 
         11: 
             {
              'type': 'float'
             }, 
         12: 
             {
              'type': 'int'
             }, 
         13: 
             {
              'type': 'dict'
             }, 
         14: 
             {
              'type': 'dict'
             }, 
         15: 
             {
              'type': 'dict'
             }, 
         16: 
             {
              'type': 'str'
             }, 
         17: 
             {
              'type': 'dict'
             }, 
         18: 
             {
              'type': 'str'
             }, 
         19: 
             {
              'type': 'dict'
             }, 
         20: 
             {
              'type': 'str'
             }, 
         21: 
             {
              'type': 'str'
             }
        }
        >>> 
        
        >>> pobj(cfd['results'])
        {
         0: 
            [], 
         1: 'Ihgazni', 
         2: 'm', 
         3: 80.0, 
         4: 2, 
         5: 1489059, 
         6: False, 
         7: 
            {}, 
         8: 35.0, 
         9: 105.0, 
         10: 'amap', 
         11: 1.71, 
         12: 1, 
         13: 
             {}, 
         14: 
             {}, 
         15: 
             {}, 
         16: '//content.static.movescount.cn/1a344c5/img/members/member_m_128.png', 
         17: 
             {}, 
         18: '//content.static.movescount.cn/1a344c5/img/members/member_m_222.png', 
         19: 
             {}, 
         20: '//content.static.movescount.cn/1a344c5/img/members/member_m.png', 
         21: '1980-12-03T00:00:00Z'
        }
        >>> 

    '''
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    temp = hdict_object.obj_to_hdict(obj)
    hdict = temp['hdict']
    cmdlines_dict = hdict_to_cmdlines_full_dict(hdict,path_list_cmd=path_list_cmd,reorder=reorder)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']
    return(cmdlines_dict)

def show_obj_via_cmd(cmd,obj,**kwargs):
    '''
        >>> 
        >>> obj
        {'userActivityIDs': [], 'username': 'Ihgazni', 'gender': 'm', 'weight': 80.0, 'publicity': 2, 'id': 1489059, 'isCoach': False, 'geoIPLocation': {'lat': 35.0, 'lon': 105.0}, 'mapProvider': 'amap', 'height': 1.71, 'defaultActivityID': 1, 'userImage': {'default': {'size128': {'url': '//content.static.movescount.cn/1a344c5/img/members/member_m_128.png'}, 'size222': {'url': '//content.static.movescount.cn/1a344c5/img/members/member_m_222.png'}, 'size60': {'url': '//content.static.movescount.cn/1a344c5/img/members/member_m.png'}}}, 'birthDate': '1980-12-03T00:00:00Z'}
        >>> show_obj_via_cmd('erImage default',obj)
        userImage default
        userImage default size128
        userImage default size128 url
        userImage default size222
        userImage default size222 url
        userImage default size60
        userImage default size60 url
        [14, 15, 16, 17, 18, 19, 20]
        >>> show_obj_via_cmd('userImage default size128 url',obj)
        '//content.static.movescount.cn/1a344c5/img/members/member_m_128.png'
        >>> show_obj_via_cmd('size',obj)
        userImage default size128
        userImage default size128 url
        userImage default size222
        userImage default size222 url
        userImage default size60
        userImage default size60 url
        [15, 16, 17, 18, 19, 20]
        >>> show_obj_via_cmd('geoIPLocation lat',obj)
        35.0
        >>> show_obj_via_cmd('geoIPLocation lon',obj)
        105.0
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
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
    #@
    cmdlines_dict = obj_to_cmdlines_full_dict(obj,path_list_cmd=path_list_cmd,reorder=0)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']    
    try:
        rslt = get_obj_value_via_cmd(cmd,obj,line_sp=line_sp,cmd_sp=cmd_sp,s2n=s2n,n2s=n2s)
    except:
        prompt = show_prompt_from_cmdlines_ltdict(cmd,cmdlines)
        return(prompt)
    else:
        return(rslt)








def show_hdict_via_cmd(cmd,hdict,**kwargs):
    '''
        >>> 
        >>> show_hdict_via_cmd('clien',hdict)
        client
        client userActivityIDs
        client username
        client gender
        client weight
        client publicity
        client id
        client isCoach
        client geoIPLocation
        client geoIPLocation lat
        client geoIPLocation lon
        client mapProvider
        client height
        client defaultActivityID
        client userImage
        client userImage default
        client userImage default size128
        client userImage default size128 url
        client userImage default size222
        client userImage default size222 url
        client userImage default size60
        client userImage default size60 url
        client birthDate
        [1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535]
        >>> show_hdict_via_cmd('client id',hdict)
        {'text': 1489059, 'siblings_seq': 5, 'tag': 'id', 'breadth_path': [4, 10], 'path': [4, 'children', 5], 'orig_obj_path': ['client', 'id'], 'children': {}, 'attrib': {'type': 'int'}, 'breadth': 10, 'depth': 1}
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
    if('prdict' in kwargs):
        prdict = kwargs['prdict']
    else:
        prdict = hdict_object.hdict_get_paths_relationship(hdict)
    if('path_list_cmd' in kwargs):
        path_list_cmd = kwargs['path_list_cmd']
    else:
        path_list_cmd = 0
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 0
    cmdlines_full_dict = hdict_to_cmdlines_full_dict(hdict,path_list_cmd=path_list_cmd,reorder=reorder)
    cmdlines = cmdlines_full_dict['cmds']
    results = cmdlines_full_dict['results']
    attribs = cmdlines_full_dict['attribs']    
    try:
        pl = cmd_str_to_cmd_pl(cmd,cmd_sp)
        rslt = hdict_object.hdict_get_value(hdict,pl,prdict=prdict) 
    except:
        prompt = show_prompt_from_cmdlines_ltdict(cmd,cmdlines)
        return(prompt)
    else:
        return(rslt)


#-------------------------------#
#-------------- to optimize performance
def del_cmdlines_strict_full_dict(cfd,path_list,**kwargs):
    '''
        cfd = {'cmds': {0: 'AutoPauseSpeed', 1: 'Displays', 2: 'Displays 0', 3: 'Displays 0 RequiresHRBelt', 4: 'Displays 0 Row1', 5: 'Displays 0 Row1 Row', 6: 'Displays 0 Row1 RuleID', 7: 'Displays 0 Row2', 8: 'Displays 0 Row2 Row', 9: 'Displays 0 Row2 RuleID', 10: 'Displays 0 Type', 11: 'Displays 0 Views', 12: 'Displays 0 Views 0', 13: 'Displays 0 Views 0 Row', 14: 'Displays 0 Views 0 RuleID', 15: 'Displays 1', 16: 'Displays 1 RequiresHRBelt', 17: 'Displays 1 Row1', 18: 'Displays 1 Row1 Row', 19: 'Displays 1 Row1 RuleID', 20: 'Displays 1 Row2', 21: 'Displays 1 Row2 Row', 22: 'Displays 1 Row2 RuleID', 23: 'Displays 1 Type', 24: 'Displays 1 Views', 25: 'Displays 1 Views 0', 26: 'Displays 1 Views 0 Row', 27: 'Displays 1 Views 0 RuleID', 28: 'Name'}, 'attribs': {0: {'type': 'int'}, 1: {'type': 'list'}, 2: {'type': 'dict'}, 3: {'type': 'NoneType'}, 4: {'type': 'dict'}, 5: {'type': 'int'}, 6: {'type': 'NoneType'}, 7: {'type': 'dict'}, 8: {'type': 'int'}, 9: {'type': 'NoneType'}, 10: {'type': 'int'}, 11: {'type': 'list'}, 12: {'type': 'dict'}, 13: {'type': 'int'}, 14: {'type': 'NoneType'}, 15: {'type': 'dict'}, 16: {'type': 'NoneType'}, 17: {'type': 'dict'}, 18: {'type': 'int'}, 19: {'type': 'NoneType'}, 20: {'type': 'dict'}, 21: {'type': 'int'}, 22: {'type': 'NoneType'}, 23: {'type': 'int'}, 24: {'type': 'list'}, 25: {'type': 'dict'}, 26: {'type': 'int'}, 27: {'type': 'NoneType'}, 28: {'type': 'str'}}, 'pathlists': {0: ['AutoPauseSpeed'], 1: ['Displays'], 2: ['Displays', 0], 3: ['Displays', 0, 'RequiresHRBelt'], 4: ['Displays', 0, 'Row1'], 5: ['Displays', 0, 'Row1', 'Row'], 6: ['Displays', 0, 'Row1', 'RuleID'], 7: ['Displays', 0, 'Row2'], 8: ['Displays', 0, 'Row2', 'Row'], 9: ['Displays', 0, 'Row2', 'RuleID'], 10: ['Displays', 0, 'Type'], 11: ['Displays', 0, 'Views'], 12: ['Displays', 0, 'Views', 0], 13: ['Displays', 0, 'Views', 0, 'Row'], 14: ['Displays', 0, 'Views', 0, 'RuleID'], 15: ['Displays', 1], 16: ['Displays', 1, 'RequiresHRBelt'], 17: ['Displays', 1, 'Row1'], 18: ['Displays', 1, 'Row1', 'Row'], 19: ['Displays', 1, 'Row1', 'RuleID'], 20: ['Displays', 1, 'Row2'], 21: ['Displays', 1, 'Row2', 'Row'], 22: ['Displays', 1, 'Row2', 'RuleID'], 23: ['Displays', 1, 'Type'], 24: ['Displays', 1, 'Views'], 25: ['Displays', 1, 'Views', 0], 26: ['Displays', 1, 'Views', 0, 'Row'], 27: ['Displays', 1, 'Views', 0, 'RuleID'], 28: ['Name']}, 'results': {0: 0, 1: {}, 2: {}, 3: None, 4: {}, 5: 54, 6: None, 7: {}, 8: 56, 9: None, 10: 5, 11: {}, 12: {}, 13: 57, 14: None, 15: {}, 16: None, 17: {}, 18: 58, 19: None, 20: {}, 21: 59, 22: None, 23: 5, 24: {}, 25: {}, 26: 12, 27: None, 28: 'Pool swimming'}}
        pobj(cfd['cmds'],fixed_indent=0)
        pobj(cfd['pathlists'],fixed_indent=1)
        pobj(cfd['results'],fixed_indent=1)
        pobj(cfd['attribs'],fixed_indent=1)
        
        
        # this can be applied to sorted or non-sorted:
        del_cmdlines_strict_full_dict(cfd,['Displays'])
        pobj(cfd['cmds'],fixed_indent=0)
        pobj(cfd['pathlists'],fixed_indent=1)
        pobj(cfd['results'],fixed_indent=1)
        pobj(cfd['attribs'],fixed_indent=1)
        
        cfd = {'cmds': {0: 'AutoPauseSpeed', 1: 'Displays', 2: 'Displays 0', 3: 'Displays 0 RequiresHRBelt', 4: 'Displays 0 Row1', 5: 'Displays 0 Row1 Row', 6: 'Displays 0 Row1 RuleID', 7: 'Displays 0 Row2', 8: 'Displays 0 Row2 Row', 9: 'Displays 0 Row2 RuleID', 10: 'Displays 0 Type', 11: 'Displays 0 Views', 12: 'Displays 0 Views 0', 13: 'Displays 0 Views 0 Row', 14: 'Displays 0 Views 0 RuleID', 15: 'Displays 1', 16: 'Displays 1 RequiresHRBelt', 17: 'Displays 1 Row1', 18: 'Displays 1 Row1 Row', 19: 'Displays 1 Row1 RuleID', 20: 'Displays 1 Row2', 21: 'Displays 1 Row2 Row', 22: 'Displays 1 Row2 RuleID', 23: 'Displays 1 Type', 24: 'Displays 1 Views', 25: 'Displays 1 Views 0', 26: 'Displays 1 Views 0 Row', 27: 'Displays 1 Views 0 RuleID', 28: 'Name'}, 'attribs': {0: {'type': 'int'}, 1: {'type': 'list'}, 2: {'type': 'dict'}, 3: {'type': 'NoneType'}, 4: {'type': 'dict'}, 5: {'type': 'int'}, 6: {'type': 'NoneType'}, 7: {'type': 'dict'}, 8: {'type': 'int'}, 9: {'type': 'NoneType'}, 10: {'type': 'int'}, 11: {'type': 'list'}, 12: {'type': 'dict'}, 13: {'type': 'int'}, 14: {'type': 'NoneType'}, 15: {'type': 'dict'}, 16: {'type': 'NoneType'}, 17: {'type': 'dict'}, 18: {'type': 'int'}, 19: {'type': 'NoneType'}, 20: {'type': 'dict'}, 21: {'type': 'int'}, 22: {'type': 'NoneType'}, 23: {'type': 'int'}, 24: {'type': 'list'}, 25: {'type': 'dict'}, 26: {'type': 'int'}, 27: {'type': 'NoneType'}, 28: {'type': 'str'}}, 'pathlists': {0: ['AutoPauseSpeed'], 1: ['Displays'], 2: ['Displays', 0], 3: ['Displays', 0, 'RequiresHRBelt'], 4: ['Displays', 0, 'Row1'], 5: ['Displays', 0, 'Row1', 'Row'], 6: ['Displays', 0, 'Row1', 'RuleID'], 7: ['Displays', 0, 'Row2'], 8: ['Displays', 0, 'Row2', 'Row'], 9: ['Displays', 0, 'Row2', 'RuleID'], 10: ['Displays', 0, 'Type'], 11: ['Displays', 0, 'Views'], 12: ['Displays', 0, 'Views', 0], 13: ['Displays', 0, 'Views', 0, 'Row'], 14: ['Displays', 0, 'Views', 0, 'RuleID'], 15: ['Displays', 1], 16: ['Displays', 1, 'RequiresHRBelt'], 17: ['Displays', 1, 'Row1'], 18: ['Displays', 1, 'Row1', 'Row'], 19: ['Displays', 1, 'Row1', 'RuleID'], 20: ['Displays', 1, 'Row2'], 21: ['Displays', 1, 'Row2', 'Row'], 22: ['Displays', 1, 'Row2', 'RuleID'], 23: ['Displays', 1, 'Type'], 24: ['Displays', 1, 'Views'], 25: ['Displays', 1, 'Views', 0], 26: ['Displays', 1, 'Views', 0, 'Row'], 27: ['Displays', 1, 'Views', 0, 'RuleID'], 28: ['Name']}, 'results': {0: 0, 1: {}, 2: {}, 3: None, 4: {}, 5: 54, 6: None, 7: {}, 8: 56, 9: None, 10: 5, 11: {}, 12: {}, 13: 57, 14: None, 15: {}, 16: None, 17: {}, 18: 58, 19: None, 20: {}, 21: 59, 22: None, 23: 5, 24: {}, 25: {}, 26: 12, 27: None, 28: 'Pool swimming'}}
        # the below will be faster than the upper,but can only be applied to sorted:
        del_cmdlines_strict_full_dict(cfd,['Displays',0],already_sorted=1)
        pobj(cfd['cmds'],fixed_indent=0)
        pobj(cfd['pathlists'],fixed_indent=1)
        pobj(cfd['results'],fixed_indent=1)
        pobj(cfd['attribs'],fixed_indent=1)
        
    '''
    if('already_sorted' in kwargs):
        already_sorted = kwargs['already_sorted']
    else:
        already_sorted = 0
    nseq = 0
    ncfd = {}
    ncfd['pathlists'] = {}
    ncfd['cmds'] = {}
    ncfd['results'] = {}
    ncfd['attribs'] = {}
    if(already_sorted):
        start = 0
        for seq in range(0,cfd['pathlists'].__len__()):
            cmdpl = cfd['pathlists'][seq]
            cond =  cmdline.cmdpl_in_cmdpl(path_list,cmdpl,mode='strict')
            if(cond):
                start = seq
            else:
                ncfd['pathlists'][nseq] = cfd['pathlists'][seq]
                ncfd['cmds'][nseq] = cfd['cmds'][seq]
                ncfd['results'][nseq] = cfd['results'][seq]
                ncfd['attribs'][nseq] = cfd['attribs'][seq]
                nseq = nseq + 1
        for seq in range(start,cfd['pathlists'].__len__()):
            cmdpl = cfd['pathlists'][seq]
            cond =  cmdline.cmdpl_in_cmdpl(path_list,cmdpl,mode='strict')
            if(cond):
                pass
            else:
                start = seq
        for seq in range(start,cfd['pathlists'].__len__()):
            start = seq
            ncfd['pathlists'][nseq] = cfd['pathlists'][seq]
            ncfd['cmds'][nseq] = cfd['cmds'][seq]
            ncfd['results'][nseq] = cfd['results'][seq]
            ncfd['attribs'][nseq] = cfd['attribs'][seq]
            nseq = nseq + 1
    else:
        for seq in cfd['pathlists']:
            cmdpl = cfd['pathlists'][seq]
            cond =  cmdline.cmdpl_in_cmdpl(path_list,cmdpl,mode='strict')
            if(cond):
                pass
            else:
                ncfd['pathlists'][nseq] = cfd['pathlists'][seq]
                ncfd['cmds'][nseq] = cfd['cmds'][seq]
                ncfd['results'][nseq] = cfd['results'][seq]
                ncfd['attribs'][nseq] = cfd['attribs'][seq]
                nseq = nseq + 1
    ncfd['pathlists'] = ltdict.naturalize_intkeydict(ncfd['pathlists'])
    ncfd['cmds'] = ltdict.naturalize_intkeydict(ncfd['cmds'])
    ncfd['results'] = ltdict.naturalize_intkeydict(ncfd['results'])
    ncfd['attribs'] = ltdict.naturalize_intkeydict(ncfd['attribs'])
    cfd['pathlists'] = ncfd['pathlists']
    cfd['cmds'] = ncfd['cmds']
    cfd['results'] = ncfd['results'] 
    cfd['attribs'] = ncfd['attribs'] 
    return(cfd)


def set_cmdlines_strict_full_dict(cfd,path_list,value,attrib,**kwargs):
    '''
        cfd = {'cmds': {0: 'AutoPauseSpeed', 1: 'Displays', 2: 'Displays 0', 3: 'Displays 0 RequiresHRBelt', 4: 'Displays 0 Row1', 5: 'Displays 0 Row1 Row', 6: 'Displays 0 Row1 RuleID', 7: 'Displays 0 Row2', 8: 'Displays 0 Row2 Row', 9: 'Displays 0 Row2 RuleID', 10: 'Displays 0 Type', 11: 'Displays 0 Views', 12: 'Displays 0 Views 0', 13: 'Displays 0 Views 0 Row', 14: 'Displays 0 Views 0 RuleID', 15: 'Displays 1', 16: 'Displays 1 RequiresHRBelt', 17: 'Displays 1 Row1', 18: 'Displays 1 Row1 Row', 19: 'Displays 1 Row1 RuleID', 20: 'Displays 1 Row2', 21: 'Displays 1 Row2 Row', 22: 'Displays 1 Row2 RuleID', 23: 'Displays 1 Type', 24: 'Displays 1 Views', 25: 'Displays 1 Views 0', 26: 'Displays 1 Views 0 Row', 27: 'Displays 1 Views 0 RuleID', 28: 'Name'}, 'attribs': {0: {'type': 'int'}, 1: {'type': 'list'}, 2: {'type': 'dict'}, 3: {'type': 'NoneType'}, 4: {'type': 'dict'}, 5: {'type': 'int'}, 6: {'type': 'NoneType'}, 7: {'type': 'dict'}, 8: {'type': 'int'}, 9: {'type': 'NoneType'}, 10: {'type': 'int'}, 11: {'type': 'list'}, 12: {'type': 'dict'}, 13: {'type': 'int'}, 14: {'type': 'NoneType'}, 15: {'type': 'dict'}, 16: {'type': 'NoneType'}, 17: {'type': 'dict'}, 18: {'type': 'int'}, 19: {'type': 'NoneType'}, 20: {'type': 'dict'}, 21: {'type': 'int'}, 22: {'type': 'NoneType'}, 23: {'type': 'int'}, 24: {'type': 'list'}, 25: {'type': 'dict'}, 26: {'type': 'int'}, 27: {'type': 'NoneType'}, 28: {'type': 'str'}}, 'pathlists': {0: ['AutoPauseSpeed'], 1: ['Displays'], 2: ['Displays', 0], 3: ['Displays', 0, 'RequiresHRBelt'], 4: ['Displays', 0, 'Row1'], 5: ['Displays', 0, 'Row1', 'Row'], 6: ['Displays', 0, 'Row1', 'RuleID'], 7: ['Displays', 0, 'Row2'], 8: ['Displays', 0, 'Row2', 'Row'], 9: ['Displays', 0, 'Row2', 'RuleID'], 10: ['Displays', 0, 'Type'], 11: ['Displays', 0, 'Views'], 12: ['Displays', 0, 'Views', 0], 13: ['Displays', 0, 'Views', 0, 'Row'], 14: ['Displays', 0, 'Views', 0, 'RuleID'], 15: ['Displays', 1], 16: ['Displays', 1, 'RequiresHRBelt'], 17: ['Displays', 1, 'Row1'], 18: ['Displays', 1, 'Row1', 'Row'], 19: ['Displays', 1, 'Row1', 'RuleID'], 20: ['Displays', 1, 'Row2'], 21: ['Displays', 1, 'Row2', 'Row'], 22: ['Displays', 1, 'Row2', 'RuleID'], 23: ['Displays', 1, 'Type'], 24: ['Displays', 1, 'Views'], 25: ['Displays', 1, 'Views', 0], 26: ['Displays', 1, 'Views', 0, 'Row'], 27: ['Displays', 1, 'Views', 0, 'RuleID'], 28: ['Name']}, 'results': {0: 0, 1: {}, 2: {}, 3: None, 4: {}, 5: 54, 6: None, 7: {}, 8: 56, 9: None, 10: 5, 11: {}, 12: {}, 13: 57, 14: None, 15: {}, 16: None, 17: {}, 18: 58, 19: None, 20: {}, 21: 59, 22: None, 23: 5, 24: {}, 25: {}, 26: 12, 27: None, 28: 'Pool swimming'}}
        pobj(cfd['cmds'],fixed_indent=0)
        pobj(cfd['pathlists'],fixed_indent=1)
        pobj(cfd['results'],fixed_indent=1)
        pobj(cfd['attribs'],fixed_indent=1)
        
        set_cmdlines_strict_full_dict(cfd,['Displays',2,'RequiresHRBelt'],False,{'type':'bool'},already_sorted=1)
        
        set_cmdlines_strict_full_dict(cfd,['Displays',2],{},{'type':'dict'},already_sorted=1)
        pobj(cfd['cmds'],fixed_indent=0)
        pobj(cfd['pathlists'],fixed_indent=1)
        pobj(cfd['results'],fixed_indent=1)
        pobj(cfd['attribs'],fixed_indent=1)
    '''
    if(path_list == []):
        cfd.clear()
        return(cfd)
    else:
        ppl = copy.deepcopy(path_list)
        ppl.pop(-1)
    if('already_sorted' in kwargs):
        already_sorted = kwargs['already_sorted']
    else:
        already_sorted = 0
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    ppl_seq = -1
    self_seq = -1
    inserted_seq = -1
    if(already_sorted):
        for seq in range(0,cfd['pathlists'].__len__()):
            cmdpl = cfd['pathlists'][seq]
            cond =  (ppl == cmdpl)
            if(cond):
                ppl_seq = seq
            else:
                pass
        if(ppl_seq == -1):
            raise KeyError(ppl)
        else:
            if(path_list > cfd['pathlists'][cfd['pathlists'].__len__()-1]):
                inserted_seq = cfd['pathlists'].__len__()
            else:
                pass
            for seq in range(ppl_seq+1,cfd['pathlists'].__len__()):
                cmdpl = cfd['pathlists'][seq]
                cond =  (path_list == cmdpl)
                if(cond):
                    self_seq = seq
                else:
                    prev_cmdpl = cfd['pathlists'][seq - 1]
                    condx = ( (path_list > prev_cmdpl) & (path_list < cmdpl))
                    if(condx):
                        inserted_seq = seq
                    else:
                        pass
            if(self_seq == -1):
                ltdict.insert(cfd['pathlists'],inserted_seq,path_list)
                ltdict.insert(cfd['results'],inserted_seq,value)
                ltdict.insert(cfd['attribs'],inserted_seq,attrib)
                ltdict.insert(cfd['cmds'],inserted_seq,path_to_cmd_str(path_list,cmd_sp=cmd_sp))
                return(cfd)
            else:
                cfd['pathlists'][self_seq] = path_list
                cfd['results'][self_seq] = value
                cfd['attribs'][self_seq] = attrib
                cfd['cmds'][self_seq] = path_to_cmd_str(path_list,cmd_sp=cmd_sp)
                return(cfd)
    else:
        for seq in range(0,cfd['pathlists'].__len__()):
            cmdpl = cfd['pathlists'][seq]
            cond =  (ppl == cmdpl)
            if(cond):
                ppl_seq = seq
            else:
                pass
        if(ppl_seq == -1):
            raise KeyError(ppl)
        else:
            for seq in range(ppl_seq+1,cfd['pathlists'].__len__()):
                cmdpl = cfd['pathlists'][seq]
                cond =  (path_list == cmdpl)
                if(cond):
                    self_seq = seq
                else:
                    pass
            if(self_seq == -1):
                inserted_seq = max(cfd['pathlists'].keys()) + 1
                cfd['pathlists'][self_seq] = path_list
                cfd['results'][self_seq] = value
                cfd['attribs'][self_seq] = attrib
                cfd['cmds'][self_seq] = path_to_cmd_str(path_list,cmd_sp=cmd_sp)
                return(cfd)
            else:
                cfd['pathlists'][self_seq] = path_list
                cfd['results'][self_seq] = value
                cfd['attribs'][self_seq] = attrib
                cfd['cmds'][self_seq] = path_to_cmd_str(path_list,cmd_sp=cmd_sp)
                return(cfd)
    return(cfd)



class cmdict():
    '''
        # the internal 
        from xdict import cmdline
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'Name': 'Pool swimming', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}]}
        cmdt = cmdline.cmdict(dict=currd)
        cmdt
        cmdt.keys()
        cmdt.dict
        cmdt.cmd_sp
        cmdt.line_sp
        #automatically convert str(such as '1')-key to number(such as 1)-key
        #by default = 1
        cmdt.s2n
        #automatically convert number(such as 1)-key to str(such as '1')
        #by default = 0
        cmdt.n2s
        pobj(cmdt.cmdlines)
        pobj(cmdt.pathlists,fixed_indent=1)
        pobj(cmdt.attribs,fixed_indent=1)
        pobj(cmdt.results,fixed_indent=1)
    '''
    def __init__(self,**kwargs):
        '''
            from xdict import cmdline
            from xdict.jprint import pobj
            currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
            
            cmdt = cmdline.cmdict(dict=currd)
        '''
        self.dict = kwargs['dict']
        if('debug' in kwargs):
            debug = kwargs['debug']
        else:
            debug = 0
        if('line_sp' in kwargs):
            line_sp = kwargs['line_sp']
        else:
            line_sp = '\n'
        if('cmd_sp' in kwargs):
            cmd_sp = kwargs['cmd_sp']
        else:
            cmd_sp = ' '
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 1
        if('reorder' in kwargs):
            reorder = kwargs['reorder']
        else:
            reorder = 0
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=reorder)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
        self.n2s = 0
        self.s2n = 1
        self.line_sp = line_sp
        self.cmd_sp = cmd_sp
        self.debug = debug
    def __repr__(self):
        return(self.dict.__repr__())
    def __getitem__(self,cmd):
        '''
            # use cmd seperated by space as keys sequence:
            cmdt['Displays 6 Views 0 Row']
            cmdt['Displays 6 Views 0']
            cmdt['Displays 6 Views']
            cmdt['Displays 6']
            cmdt['Displays']
            
            # use paths list as keys sequence:
            cmdt[['Displays',6,'Views',0,'Row']]
            cmdt[['Displays',6,'Views',0]]
            cmdt[['Displays',6,'Views']]
            cmdt[['Displays',6]]
            cmdt[['Displays']]
            
            # use traditional keys sequence:
            cmdt.dict['Displays'][6]['Views'][0]['Row']
            cmdt.dict['Displays'][6]['Views'][0]
            cmdt.dict['Displays'][6]['Views']
            cmdt.dict['Displays'][6]
            cmdt.dict['Displays']
            
            
            # search most similiar key:
            cmdt['isplays 1']
            cmdt['RuleID']
            cmdt['LoggedRuleIDs']
            cmdt['LoggedRuleIDs 0']
            cmdt['LoggedRuleIDs 1']
            cmdt['LoggedRuleIDs 2']
            
            # give prompt indication for exact key,
            # for example: wrongly input 0 as '0':
            cmdt[['Displays',6,'Views','0','Row']]
            
            cmdt[['Displays', 6, 'Views', 0, 'Row']]
            cmdt.dict['Displays'][6]['Views'][0]['Row']
        '''
        if(utils.is_str(cmd)):
            try:
                rslt = get_obj_value_via_cmd(cmd,self.dict,line_sp=self.line_sp,cmd_sp=self.cmd_sp,s2n=self.s2n,n2s=self.n2s)
            except:
                prompt = show_prompt_from_cmdlines_ltdict(cmd,self.cmdlines)
                rslt = []
                for each in prompt:
                    t = (each,self.pathlists[each])
                    if(self.debug >=1):
                        print("------the exact path to getitem as below----------------------")
                        print("using:")
                        #print('    cmdict[{0}]'.format(jprint.paint_str(self.pathlists[each].__repr__(),single_color='blue')))
                        s = '    cmdict[{0}]'.format(self.pathlists[each].__repr__())
                        paint_len = self.pathlists[each].__repr__().__len__()
                        color_sec = {1:(0,10,'white'),2:(11,10+paint_len,'blue'),3:(11+paint_len,12+paint_len,'white')}
                        spaint.paint(s,color_sec=color_sec)
                        print("or:")
                        #print('    cmdict.dict{0}'.format(jprint.paint_str(utils.path_list_to_getitem_string(self.pathlists[each]),single_color='blue')))
                        s = utils.path_list_to_getitem_string(self.pathlists[each])
                        paint_len = s.__len__()
                        s = '    cmdict.dict{0}'.format(s)
                        color_sec = {1:(0,14,'white'),2:(15,14+paint_len,'blue'),3:(15+paint_len,16+paint_len,'white')}
                        spaint.paint(s,color_sec=color_sec)
                        print("to get value")
                        print("--------------------------------------------------------------")
                    rslt.append(t)
                if(self.debug >=2):
                    raise KeyError('should be',rslt)
                else:
                    return((prompt,rslt))
            else:
                return(rslt)
        else:
            try:
                rslt = utils.dict_getitem_via_path_list(self.dict,cmd)
            except:
                cmd_str = path_to_cmd_str(cmd,cmd_sp=self.cmd_sp)
                prompt = show_prompt_from_cmdlines_ltdict(cmd_str,self.cmdlines)
                rslt = []
                for each in prompt:
                    t = (each,self.pathlists[each])
                    if(self.debug>=1):
                        print("------the exact path to getitem as below----------------------")
                        print("using:")
                        #print('    cmdict[{0}]'.format(jprint.paint_str(self.pathlists[each].__repr__(),single_color='blue')))
                        s = '    cmdict[{0}]'.format(self.pathlists[each].__repr__())
                        paint_len = self.pathlists[each].__repr__().__len__()
                        color_sec = {1:(0,10,'white'),2:(11,10+paint_len,'blue'),3:(11+paint_len,12+paint_len,'white')}
                        spaint.paint(s,color_sec=color_sec)
                        print("or:")
                        #print('    cmdict.dict{0}'.format(jprint.paint_str(utils.path_list_to_getitem_string(self.pathlists[each]),single_color='blue')))
                        s = utils.path_list_to_getitem_string(self.pathlists[each])
                        paint_len = s.__len__()
                        s = '    cmdict.dict{0}'.format(s)
                        color_sec = {1:(0,14,'white'),2:(15,14+paint_len,'blue'),3:(15+paint_len,16+paint_len,'white')}
                        spaint.paint(s,color_sec=color_sec)
                        print("to get value")
                        print("--------------------------------------------------------------")
                    rslt.append(t)
                if(self.debug>=2):
                    raise KeyError('should be',rslt)
                else:
                    return((prompt,rslt))
            else:
                return(rslt)
    def __setitem__(self,cmd,value):
        '''
            cmdt['owner nameIDs uid'] = 'dli_u1'
            cmdt['owner'] = {}
            cmdt['owner nameIDs'] = {}
            cmdt['owner nameIDs uid'] = 'dli_u1'
            cmdt['owner nameIDs uid']
        '''
        if(utils.is_str(cmd)):
            cmd_str = path_to_cmd_str(cmd,cmd_sp=self.cmd_sp)
            cmd_str = format_cmd_str(cmd_str,cmd_sp=self.cmd_sp)
            cmdpl = cmd_str_to_cmd_pl(cmd_str,cmd_sp = self.cmd_sp,n2s=self.n2s,s2n=self.s2n)
            utils.dict_setitem_via_path_list(self.dict,cmdpl,value)
        else:
            utils.dict_setitem_via_path_list(self.dict,cmd,value)
        #keep order
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
    def __delitem__(self,cmd):
        '''
            del cmdt['owner']
            cmdt['owner nameIDs uid'] = 'dli_u1'
        '''
        if(utils.is_str(cmd)):
            cmd_str = path_to_cmd_str(cmd,cmd_sp=self.cmd_sp)
            cmd_str = format_cmd_str(cmd_str,cmd_sp=self.cmd_sp)
            cmdpl = cmd_str_to_cmd_pl(cmd_str,cmd_sp = self.cmd_sp,n2s=self.n2s,s2n=self.s2n)
            utils.dict_delitem_via_path_list(self.dict,cmdpl)
        else:
            utils.dict_delitem_via_path_list(self.dict,cmd)
        #reorder = 0 
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
    def clear(self):
        '''
        cmdt2 = cmdt.copy()
        >>> cmdt2.clear()
        >>> cmdt2
        {}
        >>> 
        '''
        self.dict = {}
        self.pathlists = {}
        self.cmdlines = {}
        self.results = {}
        self.attribs = {}
    def copy(self):
        '''
            cmdt2 = cmdt.copy()
        '''
        return(copy.deepcopy(self))
    def items(self):
        '''
            cmdt.items()
        '''
        return(self.dict.items())
    def keys(self):
        '''
            cmdt.keys()
        '''
        return(self.dict.keys())
    def values(self):
        '''
            cmdt.values()
        '''
        return(self.dict.values())
    def pop(self,cmd):
        '''
            pobj(cmdt['Displays 6'])
            cmdt.pop('Displays 6')
            cmdt['Displays 6']
        '''
        rslt = self.__getitem__(cmd)
        self.__delitem__(cmd)
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
        return(rslt)
    def popitem(self):
        '''
            cmdt.keys()
            cmdt.popitem()
            cmdt.popitem()
            cmdt.popitem()
        '''
        rslt = self.dict.popitem()
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
        return(rslt)
    def setdefault(self,cmd):
        '''
            cmdt['Displays 5']
            cmdt.setdefault('Displays 5')
            cmdt['Displays 5']
        '''
        self.__setitem__(cmd,None)
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']
    def update(self,value):
        '''
            cmdt['UseHRBelt']
            cmdt.update({'UseHRBelt':True})
            cmdt['UseHRBelt']
        '''
        self.dict.update(value)
        cfd = obj_to_cmdlines_full_dict(self.dict,path_list_cmd=1,reorder=0)
        self.pathlists = cfd['cmds']
        self.cmdlines = {}
        for i in range(0,self.pathlists.__len__()):
            cmdline = path_to_cmd_str(self.pathlists[i],cmd_sp=self.cmd_sp)
            self.cmdlines[i] = cmdline
        self.results = cfd['results']
        self.attribs = cfd['attribs']


###############################################################################################################
###############################################################################################################
# need to add jquery-like api

class Hentry():
    '''
        currently only support path query
        jquery-like APIs still in progress
        based on lxml
    '''
    def __init__(self,**kwargs):
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
            pass
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('s2n' in kwargs):
            s2n = kwargs['n2s']
        else:
            s2n = 0
        if('line_sp' in kwargs):
            self.line_sp = kwargs['line_sp']
        else:
            self.line_sp = '\n'
        if('cmd_sp' in kwargs):
            self.cmd_sp = kwargs['cmd_sp']
        else:
            self.cmd_sp = ' '
        if('reorder' in kwargs):
            reorder = kwargs['reorder']
        else:
            reorder = 0
        if('cmdlines_full_dict' in kwargs):
            temp = kwargs['cmdlines_full_dict']
        else:
            temp = html_text_to_cmdlines_full_dict(root=root,s2n=s2n,n2s=n2s,disable_type=1,cmd_sp=self.cmd_sp,line_sp=self.line_sp,reorder=reorder)
        self.cmds = temp['cmds']
        self.texts = temp['results']
        self.attribs = temp['attribs']
    def qmask(self,*args,**kwargs):
        '''
           
        '''
        cmdslt_prompt(self.cmds,*args,**kwargs)
    ##########################################
    #__getitem__ parser
    ##########################################
    def query(self,cmd,**kwargs):
        if('style' in kwargs):
            style = kwargs['style']
        else:
            style = 'flat'
        rslt_seqs = show_prompt_from_cmdlines_ltdict(cmd,self.cmds,cmd_sp=self.cmd_sp,line_sp=self.line_sp)
        rslt = {}
        howmany = rslt_seqs.__len__()
        print("\n-Found {0} matched:".format(howmany))
        for i in range(0,howmany):
            seq = rslt_seqs[i]
            rslt[i] = {'cmd':self.cmds[seq],'result':self.texts[seq],'attrib':self.attribs[seq],'seq':seq}
            print("-----------------------------------------------------")
            if(style == 'flat'):
                cmd = str(self.cmds[seq])
                spaint.slpaint('   [cmd]: ','white',cmd,'yellow')
                result = str(self.texts[seq])
                spaint.slpaint('[result]: ','white',result,'red')
                attrib = str(self.attribs[seq])
                spaint.slpaint('[attrib]: ','white',attrib,'cyan1')
                spaint.slpaint('   [seq]: ','white',str(seq),'magenta1')
                #spaint.slpaint(cmd,'yellow',prefix='   [cmd]: ')
                #result = str(self.texts[seq])
                #spaint.slpaint(result,'red',prefix='[result]: ')
                #attrib = str(self.attribs[seq])
                #spaint.slpaint(attrib,'cyan1',prefix='[attrib]: ')
                #spaint.slpaint(str(seq),'magenta1',prefix='   [seq]: ')
            else:
                jprint.pobj(rslt[i])
        print("-----------------------------------------------------")
        return(rslt)
    ###
    def query_attribs(self,x,**kwargs):
        '''
        '''
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'loose'
        if('via' in kwargs):
            via = kwargs['via']
        else:
            via = 'value'
        ####
        def cond_match(x,arr,mode):
            rslt = False
            for each in arr:
                if(mode == 'loose'):
                    cond = (str.lower(x) in each)
                elif(mode == 'middle'):
                    cond = (str.lower(x) == each)
                else:
                    cond = (x == each)
                if(cond):
                    rslt = True
                    break
                else:
                    pass
            return(rslt)
        ####
        selected_seqs = []
        length = self.attribs.__len__()        
        for i in range(0,length):
            attrib = self.attribs[i]
            keys = list(attrib.keys())
            values = list(attrib.values())
            if(via == 'value'):
                values = elel.array_map(values,str.lower)
                cond = cond_match(x,values,mode)
                if(cond):
                    selected_seqs.append(i)
                else:
                    pass
            elif(via == 'key'):
                keys = elel.array_map(keys,str.lower)
                cond = cond_match(x,keys,mode)
                if(cond):
                    selected_seqs.append(i)
                else:
                    pass
            else:
                values = elel.array_map(values,str.lower)
                keys = elel.array_map(keys,str.lower)
                cond1 = cond_match(x,keys,mode)
                cond2 = cond_match(x,values,mode)
                cond = (cond1 | cond2)
                if(cond):
                    selected_seqs.append(i)
                else:
                    pass
    ###############################
        rslt_seqs = selected_seqs
        howmany = rslt_seqs.__len__()
        print("\n-Found {0} matched:".format(howmany))
        for i in range(0,howmany):
            seq = rslt_seqs[i]
            rslt[i] = {'cmd':self.cmds[seq],'result':self.texts[seq],'attrib':self.attribs[seq],'seq':seq}
            print("-----------------------------------------------------")
            if(style == 'flat'):
                cmd = str(self.cmds[seq])
                #spaint.slpaint(cmd,'yellow',prefix='   [cmd]: ')
                #result = str(self.texts[seq])
                #spaint.slpaint(result,'red',prefix='[result]: ')
                #attrib = str(self.attribs[seq])
                #spaint.slpaint(attrib,'cyan1',prefix='[attrib]: ')
                #spaint.slpaint(str(seq),'magenta1',prefix='   [seq]: ')
                spaint.slpaint('   [cmd]: ','white',cmd,'yellow')
                result = str(self.texts[seq])
                spaint.slpaint('[result]: ','white',result,'red')
                attrib = str(attribs[seq])
                spaint.slpaint('[attrib]: ','white',attrib,'cyan1')
                spaint.slpaint('   [seq]: ','white',str(seq),'magenta1')
            else:
                jprint.pobj(rslt[i])
        print("-----------------------------------------------------")
        return(rslt)
    ###
    def query_texts(self,**kwargs):
        '''
        '''
        pass
    



     
