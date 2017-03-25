import re
import copy
from xdict import utils
from xdict import ltdict
from xdict import hdict_object
from xdict import hdict_xml
from xdict import jprint



def cmd_in_cmd(cmd1,cmd2,**kwargs):
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
    cmd1 = format_cmd(cmd1,cmd_sp=cmd_sp1)
    cmd2 = format_cmd(cmd2,cmd_sp=cmd_sp2)
    cmd1_pl = cmd1.split(cmd1_sp))
    cmd2_pl = cmd2.split(cmd2_sp))
    return(cmdpl_in_cmdpl(cmdpl1,cmdpl2,mode=mode)




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
            start1 = cmdpl1[0]
            start2 = cmdpl2[0]
            cond = utils.str_at_end_of_str(start1,start2)
            if(cond):
                pass
            else:
                return(False)
            for i in range(1,cmdpl1_len-1):
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




def format_cmd(cmd,cmd_sp=' '):
    regex_str = ''.join(('[',cmd_sp,']','+'))
    regex = re.compile(regex_str)
    cmd = re.sub(regex,cmd_sp,cmd)
    cmd = utils.str_rstrip(cmd,cmd_sp,1)
    cmd = utils.str_lstrip(cmd,cmd_sp,1)
    return(cmd)

def path_list_to_cmd(path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    path_list = hdict_object.get_path_list(path_list_or_path_string,sp)
    cmd = ''
    for i in range(0,path_list.__len__()):
        cmd = ''.join((cmd,cmd_sp,str(path_list[i])))
    cmd = utils.str_rstrip(cmd,cmd_sp,1)
    cmd = utils.str_lstrip(cmd,cmd_sp,1)
    return(cmd)

def cmd_to_path_list(cmd,**kwargs):
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmd = format_cmd(cmd,cmd_sp=cmd_sp)
    path_list = cmd.split(cmd_sp)
    return(path_list)

def cmd_to_path_str(cmd,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmd = format_cmd(cmd,cmd_sp=cmd_sp)
    path_str = cmd.replace(cmd_sp,sp)
    return(path_str)

def deep_to_cmdlines_ltdict(deep,**kwargs):
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
        line = path_list_to_cmd(line,cmd_sp=cmd_sp)
        lines[i] = line
    return(lines)

def cmdlines_ltdict_to_deep(cmdlines_ltdict,**kwargs):
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
        line = format_cmd(line)
        line_lt = line.split(cmd_sp)
        line_lt = ltdict.list_to_ltdict(line_lt)
        lines[i] = line_lt
    return(lines)

def hdict_to_cmdlines_dict(hdict,**kwargs):
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
    lines = {}
    values = {}
    attribs = {}
    temp = {}
    seq = 0
    for key in  prdict['o:h']:
        if(key == ()):
            pass
        else:
            line = path_list_to_cmd(list(key),cmd_sp=cmd_sp)
            hp = prdict['o:h'][key]
            bp = prdict['h:b'][tuple(hp)]
            r,c = hdict_object.breadth_path_to_sdict_location(bp)
            leaf = sdict[r][c]['leaf']
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
            temp[line]=(value,attrib)
            seq = seq + 1
    lines = ltdict.list_to_ltdict(sorted(temp))
    for i in range(0,lines.__len__()):
        values[i] = temp[lines[i]][0]
        attribs[i] = temp[lines[i]][1]
    return({'cmds':lines,'results':values,'attribs':attribs})

def ltdict_to_cmdlines(cmdlines_ltdict,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmdlines = ''
    for i in range(0,cmdlines_ltdict.__len__()):
        cmdlines = ''.join((cmdlines,cmdlines_ltdict[i],line_sp))
    cmdlines = utils.str_rstrip(cmdlines,line_sp,1)
    return(cmdlines)

def cmdlines_to_ltdict(cmdlines,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('ltdict' in kwargs):
        lt = kwargs['ltdict']
    else:
        lt = 1
    lines = cmdlines.split(line_sp)
    for i in range(0,lines.__len__()):
        line = lines[i]
        line = format_cmd(line)
        lines[i] = line
    if(lt):
        lines = ltdict.list_to_ltdict(lines)
    else:
        pass
    return(lines)

def cmdlines_to_deep_ltdict(cmdlines,**kwargs):
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
    lines = cmdlines.split(line_sp)
    for i in range(0,lines.__len__()):
        line = lines[i]
        line = format_cmd(line)
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

def deep_ltdict_to_cmdlines(deep_ltdict,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmdlines_ltdict = deep_to_cmdlines_ltdict(deep_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    lines = ltdict_to_cmdlines(cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    return(lines)

def show_prompt_cmdlines(cmd,cmdlines,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmd = format_cmd(cmd,cmd_sp=cmd_sp)
    cmd_nocaps = cmd.lower()
    cmd_pl = cmd.split(cmd_sp)
    len_1 = cmd_pl.__len__()
    cmd_nocaps_pl = cmd_nocaps.split(cmd_sp.lower())
    cmdlines_deep = cmdlines_to_deep_ltdict(cmdlines,cmd_sp=cmd_sp,line_sp=line_sp)
    cmdlines_nocaps = cmdlines.lower()
    cmdlines_nocaps_deep = cmdlines_to_deep_ltdict(cmdlines_nocaps,cmd_sp=cmd_sp.lower(),line_sp=line_sp.lower())
    len_2  = cmdlines_nocaps_deep.__len__()
    rslt = ''
    orig_seqs = []
    for i in range(0,len_2):
        p = cmdlines_nocaps_deep[i]
        pnoc = cmdlines_deep[i]
        len_3 = p.__len__()
        if(len_1 > len_3):
            pass
        else:
            cond = 1
            tab = 0
            for j in range(0,len_1-1):
                if(p[j]==cmd_nocaps_pl[j]):
                    pass
                else:
                    cond = 0
                    break
            str_len = cmd_nocaps_pl[len_1-1].__len__()
            if(str_len > p[len_1-1].__len__()):
                cond = 0
            elif(str_len == p[len_1-1].__len__()):
                if(cmd_nocaps_pl[len_1-1] == p[len_1-1]):
                    pass
                else:
                    cond = 0
            else:
                if(cmd_nocaps_pl[len_1-1] == p[len_1-1][:str_len]):
                    tab = 1
                else:
                    cond = 0
            if(cond == 0):
                pass
            else:
                if(tab == 0):
                    start = len_1
                else:
                    start = len_1 - 1
                line = ''
                for k in range(start,len_3):
                    line = ''.join((line,pnoc[k],cmd_sp))
                line = utils.str_rstrip(line,cmd_sp,1)
                rslt = ''.join((rslt,line,line_sp))
                orig_seqs.append(i)
    rslt = utils.str_rstrip(rslt,line_sp,1)
    print(rslt)
    return(orig_seqs)

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
    cmd = format_cmd(cmd,cmd_sp=cmd_sp)
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
    ltd = cmdlines_to_ltdict(cmdlines,line_sp=line_sp,ltdict=lt)
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
    rslt = hdict_to_cmdlines_dict(hdict,sdict=sdict,prdict=prdict,s2n=s2n,n2s=n2s,disable_type=disable_type,cmd_sp=cmd_sp)
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

def show_prompt_cmdlines_ltdict(cmd,cmdlines_ltdict,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    cmd = format_cmd(cmd,cmd_sp=cmd_sp)
    cmd_nocaps = cmd.lower()
    cmd_pl = cmd.split(cmd_sp)
    len_1 = cmd_pl.__len__()
    cmd_nocaps_pl = cmd_nocaps.split(cmd_sp.lower())
    cmdlines_deep = cmdlines_ltdict_to_deep(cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
    cmdlines_nocaps_ltdict = {}
    for i in range(0,cmdlines_ltdict.__len__()):
        cmdlines_nocaps_ltdict[i] = cmdlines_ltdict[i].lower()
    cmdlines_nocaps_deep = cmdlines_ltdict_to_deep(cmdlines_nocaps_ltdict,cmd_sp=cmd_sp.lower(),line_sp=line_sp.lower())
    len_2  = cmdlines_nocaps_deep.__len__()
    rslt = ''
    orig_seqs = []
    for i in range(0,len_2):
        p = cmdlines_nocaps_deep[i]
        pnoc = cmdlines_deep[i]
        len_3 = p.__len__()
        if(len_1 > len_3):
            pass
        else:
            cond = 1
            tab = 0
            for j in range(0,len_1-1):
                if(p[j]==cmd_nocaps_pl[j]):
                    pass
                else:
                    cond = 0
                    break
            str_len = cmd_nocaps_pl[len_1-1].__len__()
            if(str_len > p[len_1-1].__len__()):
                cond = 0
            elif(str_len == p[len_1-1].__len__()):
                if(cmd_nocaps_pl[len_1-1] == p[len_1-1]):
                    pass
                else:
                    cond = 0
            else:
                if(cmd_nocaps_pl[len_1-1] == p[len_1-1][:str_len]):
                    tab = 1
                else:
                    cond = 0
            if(cond == 0):
                pass
            else:
                if(tab == 0):
                    start = len_1
                else:
                    start = len_1 - 1
                line = ''
                for k in range(start,len_3):
                    line = ''.join((line,pnoc[k],cmd_sp))
                line = utils.str_rstrip(line,cmd_sp,1)
                rslt = ''.join((rslt,line,line_sp))
                orig_seqs.append(i)
    rslt = utils.str_rstrip(rslt,line_sp,1)
    print(rslt)
    return(orig_seqs)

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
    rslt_seqs = show_prompt_cmdlines_ltdict(cmd,cmdlines_ltdict,cmd_sp=cmd_sp,line_sp=line_sp)
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
    cmdlines_dict = hdict_to_cmdlines_dict(hdict)
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
        prompt = show_prompt_cmdlines_ltdict(cmd,cmdlines)
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
    cmdlines_dict = hdict_to_cmdlines_dict(obj)
    cmdlines = cmdlines_dict['cmds']
    results = cmdlines_dict['results']
    attribs = cmdlines_dict['attribs']    
    try:
        pl = cmd_to_path_list(cmd,cmd_sp=cmd_sp)
        rslt =hdict_get_value(hdict,pl,prdict=prdict) 
    except:
        prompt = show_prompt_cmdlines_ltdict(cmd,cmdlines)
        return(prompt)
    else:
        return(rslt)
        
        



            
