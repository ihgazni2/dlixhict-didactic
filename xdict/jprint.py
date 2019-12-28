#windows 下 key值有空格时候颜色有bug
#{'others': 0, 'scanner of transparent type': 1, 'scanner of reflex type': 2, 'DSC': 3}


import time
import re
from xdict import utils
import html
import copy
from xdict import fsm
import os
import elist.elist as elel
from spaint.spaint import paint
from spaint.spaint import is_win
import efuntool.efuntool as eftl
import efuntool.eobjtool as eotl
from xdict.tokenize_quotes import convert_token_in_quote
import  xdict.quote as quote
import xdict.fmt_jstr as fmt_jstr
from xdict import escape
from xdict import block
from xdict import tokenize_block


IS_WIN = is_win()

def import_colors_md():
    if(IS_WIN):
        from spaint.spaint import WIN8_COLORS_MD as COLORS_MD
    else:
        from spaint.spaint import ANSI8_COLORS_MD as COLORS_MD
    return(COLORS_MD)

COLORS_MD = import_colors_md();
KEY_COLOR = COLORS_MD['lightgreen']
VALUE_COLOR = COLORS_MD['lightcyan']
LIST_ELE_COLOR =  COLORS_MD['yellow']
OP_COLOR = COLORS_MD['white']
DEFAULT_COLOR = COLORS_MD['white']



# lv_dict
## {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {"key_7_tl": [[], "value_2", "value_4", "value_4"], "key_13_TVj_lP": "value_6", "key_8_9vPp6PT": "value_9", "key_10_Uy": ["value_1"]
## 1222222222222222222222222222222222222222222223333333333333333333333333333333333333333333333333333333333333333333333344444444444445555555555555555555555555555555555544444444444444444444444444444444444444444444444444444444444444444444444445555555554
# attr_dict op,key,dict_value,list_value,tuple_value,set_value


def is_comma(ch,commas=[',']):
    if(ch in commas):
        return(True)
    else:
        return(False)

def is_colon(ch,colons=[':']):
    if(ch in colons):
        return(True)
    else:
        return(False)



def get_line_start_index_in_j_str(orig_lines):
    line_start_indexes = {}
    line_start_indexes[0] = 0
    for i in range(1,orig_lines.__len__()):
        nxt = line_start_indexes[i - 1] + orig_lines[i - 1].__len__() + 1
        line_start_indexes[i] = nxt
    return(line_start_indexes)

def line_to_path_init(
        line,
        block_op_pairs_dict = block.get_block_op_pairs("{}[]()"),
        sp='/',
        commas=[','],
        colons=[':']
    ):
    end = line.rstrip(' ')[-1]
    if(is_colon(end,colons)):
        curr_base_name = ''.join((line,sp))
    elif(block.is_lop(end,block_op_pairs_dict)):
        curr_base_name = ''.join((line,sp))
    elif(is_comma(end,commas)):
        curr_base_name = line
    elif(block.is_rop(end,block_op_pairs_dict)):
        curr_base_name = line
    else:
        curr_base_name = line
    curr_path = ''.join((sp,curr_base_name))
    return(curr_path)

def line_to_path(
        line,curr_lv,
        prev_lv,
        prev_path,
        block_op_pairs_dict= block.get_block_op_pairs("{}[]()"),
        sp='/',
        commas=[','],
        colons=[':']
    ):
    def no_space_tail(tail):
        tail_no_space = tail.rstrip(' ')
        for i in range(0,commas.__len__()):
            tail_no_space_2 = utils.str_rstrip(tail_no_space,commas[i],1)
            if(tail_no_space_2 == tail_no_space):
                pass
            else:
                tail_no_space = tail_no_space_2
                break
        tail_no_space = utils.str_rstrip(tail_no_space,sp,1)
        tail_no_space = tail_no_space.rstrip(' ')
        return(tail_no_space)
    # if end with path_sp sp,it means this is not a leaf, its recursived
    # '/{/'
    # "/'Error': None, "
    # "/'Value': /"
    # '/{/'
    # "/'MyRulesHtml': '<div><&#47;div>', "
    # "/'__type': 'RuleDesignerRuleResult', "
    curr_base_name = line_to_path_init(line,block_op_pairs_dict ,sp,commas,colons)
    curr_base_name = utils.str_lstrip(curr_base_name,'/',1)
    head = utils.path_string_get_head(prev_path,delimiter=sp)
    head_head = utils.path_string_get_head(head,delimiter=sp)
    head_tail = utils.path_string_get_tail(head,delimiter=sp)
    head_tail_no_space = no_space_tail(head_tail)
    #
    if(curr_lv > prev_lv):
        curr_path = ''.join((prev_path,curr_base_name))
    elif(curr_lv == prev_lv):
        prev_last_no_space = utils.str_rstrip(prev_path,sp,1)
        prev_last_no_space = prev_last_no_space.rstrip(' ')
        prev_last = prev_last_no_space[-1]
        prev_op = prev_path.rstrip(' ')
        for i in range(0,commas.__len__()):
            prev_rop = utils.str_rstrip(prev_op,commas[i],1)
            if(prev_op == prev_rop):
                pass
            else:
                prev_rop = prev_rop[-1]
                break
        # secarino_1:
        if(is_colon(prev_last)):
            curr_path = ''.join((prev_path,curr_base_name))
        elif(block.is_rop(prev_rop,block_op_pairs_dict)):
            tail = utils.path_string_get_tail(prev_path,delimiter=sp)
            tail_no_space = no_space_tail(tail)
            tail_len = tail_no_space.__len__()
            # secarino_2
            if( (tail_len == 1) & (is_colon(head_tail_no_space[-1]))):
                curr_path = ''.join((head_head,curr_base_name))
            # secarino_3
            elif(tail_len == 1):
                curr_path = ''.join((head,curr_base_name))
            # secarino_4
            elif((tail_len == 2) & (is_colon(head_tail_no_space[-1]))):
                curr_path = ''.join((head_head,curr_base_name))
            # secarino_5
            else:
                curr_path = ''.join((head,curr_base_name))
        #secarino_6:
        else:
            curr_path = ''.join((head,curr_base_name))
    else:
        if(is_colon(head_tail_no_space[-1])):
            #secarino_8
            curr_path = ''.join((utils.path_string_get_head(head_head,delimiter=sp),curr_base_name))
        else:
            #secarino_7
            curr_path = ''.join((head_head,curr_base_name))
    return(curr_path)

def get_print_lines_and_paths(j_str,**kwargs):
    ####
    sp = eftl.dflt_kwargs("sp",'/',**kwargs)
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs('block_op_pairs_dict',block.get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs('quotes_pairs_dict',quote.get_quotes_pairs('""\'\''))
    path_sps =  eftl.dflt_kwargs('path_sps',['/'],**kwargs)
    fixed_indent = eftl.dflt_kwargs('fixed_indent',0,**kwargs)
    indent = eftl.dflt_kwargs('indent',4,**kwargs)
    #step0  quote
    j_str = convert_token_in_quote(
        j_str,
        block_op_pairs_dict=block_op_pairs_dict,
        quotes_pairs_dict=quotes_pairs_dict,
        spaces=spaces,
        colons=colons,
        commas=commas,
        line_sps=line_sps,
        path_sps=path_sps
    )
    #step1 format
    j_str = fmt_jstr.format_j_str(j_str,block_op_pairs_dict)
    #step2 char-level-of-block
    j_lv_str = tokenize_block.get_j_str_lvs_dict(j_str,block_op_pairs_dict)
    orig_lines = j_str.split('\n')
    line_start_indexes = get_line_start_index_in_j_str(orig_lines)
    new_lines = {}
    #step 1: line 0 
    prev_lv = int(j_lv_str[line_start_indexes[0]])
    prev_path = line_to_path_init(orig_lines[0],block_op_pairs_dict,sp,commas,colons)
    #----------should not unescape here for secarino:{'resp_body_bytes': b'&#39;c'}
    #          which will cause {'resp_body_bytes': b''c'}
    new_lines[0] = orig_lines[0]
    #----------should not unescape here 
    paths = {}
    paths = {0: prev_path}
    for i in range(1, orig_lines.__len__()):
        curr_lv = int(j_lv_str[line_start_indexes[i]])
        curr_path = line_to_path(orig_lines[i],curr_lv,prev_lv,prev_path,block_op_pairs_dict,sp,commas,colons)
        paths[i] = curr_path
        curr_head = utils.path_string_get_head(curr_path,delimiter=sp)
        if(fixed_indent):
            prepend = " " * indent * (curr_head.count(sp) - 1)
        else:
            curr_head = curr_head.replace(sp,'')
            #---escaped to calculate the real prepend spaces
            curr_head = html.unescape(curr_head)
            #---escaped to calculate the real prepend spaces
            curr_head_len = curr_head.__len__()
            prepend = " " * curr_head_len
        #------------should not unescape here
        new_lines[i] = ''.join((prepend,orig_lines[i]))
        #------------should not unescape here
        prev_lv = curr_lv
        prev_path = curr_path
    return({'lines':new_lines,'paths':paths})


def get_line_color_sec(line,path,**kwargs):
    sp = eftl.dflt_kwargs("sp",'/',**kwargs)
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs('block_op_pairs_dict',block.get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs('quotes_pairs_dict',quote.get_quotes_pairs('""\'\''))
    path_sps =  eftl.dflt_kwargs('path_sps',['/'],**kwargs)
    fixed_indent = eftl.dflt_kwargs('fixed_indent',0,**kwargs)
    indent = eftl.dflt_kwargs('indent',4,**kwargs)
    ####
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = block.get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = block.get_block_op_pairs('{}[]()')
    if('block_non_ordered_op_pairs' in kwargs):
        block_non_ordered_op_pairs = kwargs['block_non_ordered_op_pairs']
        if(utils.is_dict(block_non_ordered_op_pairs)):
            block_non_ordered_op_pairs_dict = block_non_ordered_op_pairs
        else:
            block_non_ordered_op_pairs_dict = block.get_block_op_pairs(block_non_ordered_op_pairs)
    else:
        block_non_ordered_op_pairs_dict = block.get_block_op_pairs('{}')
    ####
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = quote.get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = quote.get_quotes_pairs('""\'\'')
    lquotes = []
    rquotes = []
    quotes = []
    for i in range(1,quotes_pairs_dict.__len__()+1):
        lquotes.append(quotes_pairs_dict[i][0])
        rquotes.append(quotes_pairs_dict[i][1])
        quotes.append(quotes_pairs_dict[i][0])
        quotes.append(quotes_pairs_dict[i][1])
    ####
    if('key_color' in kwargs):
        key_color = kwargs['key_color']
    else:
        key_color=KEY_COLOR
    if('value_color' in kwargs):
        value_color = kwargs['value_color']
    else:
        value_color=VALUE_COLOR
    if('list_ele_color' in kwargs):
        list_ele_color = kwargs['list_ele_color']
    else:
        list_ele_color=LIST_ELE_COLOR
    if('op_color' in kwargs):
        op_color = kwargs['op_color']
    else:
        op_color=OP_COLOR
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color=DEFAULT_COLOR
    #------------------------------------------------------------
    line_len = line.__len__()
    si = 0
    ei = 0
    color_sec = {}
    color_sec_seq = 1
    colon_meeted = 0
    byte_meeted = 0
    #-------------------------------------------------------------
    ops = []
    for i in range(1,block_op_pairs_dict.__len__()+1):
        ops.append(block_op_pairs_dict[i][0])
        ops.append(block_op_pairs_dict[i][1])
    ######
    machine = fsm.FSM()
    #
    #machine.enable_debug = True
    #
    regex_lquotes = fsm.creat_regex_from_arr(lquotes)
    regex_rquotes = fsm.creat_regex_from_arr(rquotes)
    regex_b = re.compile('b')
    regex_spaces = fsm.creat_regex_from_arr(spaces)
    regex_colons = fsm.creat_regex_from_arr(colons)
    regex_commas = fsm.creat_regex_from_arr(commas)
    regex_slash = re.compile("\\\\")
    regex_ops = fsm.creat_regex_from_arr(ops)
    LqRqBSpColComSlOp_arr = ['b','\\\\']
    LqRqBSpColComSlOp_arr = LqRqBSpColComSlOp_arr + lquotes + rquotes + spaces + colons+commas + ops
    regex_not_LqRqBSpColComSlOp = fsm.creat_regex_not_from_arr(LqRqBSpColComSlOp_arr)
    #-------------------------------------------------------------------
    head = utils.path_string_get_head(path)
    head_last = utils.str_rstrip(head,sp,1)
    head_last = utils.str_rstrip(head_last," ",1)
    if(head_last == ''):
        pass
    else:
        head_last = head_last[-1]
    #------------------------------------------------------
    def do_throw(curr_state,trigger_checker,input_symbol,line,path,index):
        msg = "curr_state: " + curr_state + "\n"
        msg = msg + "trigger_checker: "+trigger_checker.__str__() + "\n"
        msg = msg + "input_symbol: "+ input_symbol.__str__() + "\n"
        msg = msg + "triggered ERROR" + "\n"
        msg = msg + line + "\n"
        msg = msg + path + "\n"
        mas = msg + "index : " + str(index)
        raise Exception(msg)
    def do_open_quote(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        byte_meeted = 0
        ####
        ei = cursor 
        curr_color = default_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor + 1
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_close_quote(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        ei = cursor - 1
        if(colon_meeted):
            curr_color = value_color
        else:
            if(block.is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
                curr_color = key_color
            elif(is_colon(head_last)):
                curr_color = value_color
            elif(head_last==sp):
                curr_color = value_color
            else:
                curr_color = list_ele_color
        colon_meeted = 0
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_open_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        ei = cursor - 1
        curr_color = default_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_open_var_bytes(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        byte_meeted = 1
        ei = cursor - 1
        curr_color = default_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_clear_byte_meeted(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        byte_meeted = 0
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        ei = cursor - 1
        if(colon_meeted):
            curr_color = value_color
        else:
            if(block.is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
                curr_color = key_color
            elif(is_colon(head_last)):
                curr_color = value_color
            elif(head_last==sp):
                curr_color = value_color
            else:
                curr_color = list_ele_color
        colon_meeted = 0
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_colons(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        colon_meeted = 1
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_op(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        ei = cursor - 1
        curr_color = default_color
        if(ei >= si):
            color_sec[color_sec_seq] = (si,ei,curr_color)
            color_sec_seq = color_sec_seq + 1
        else:
            pass
        si = cursor 
        ei = cursor
        if(block.is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
            curr_color = value_color
        elif(is_colon(head_last)):
            curr_color = value_color
        elif(head_last==sp):
            curr_color = value_color
        else:
            curr_color = list_ele_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor + 1
        return(si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted)
    def do_close_var_colon(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted):
        colon_meeted = 1
        return(do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted))
    #---------------------------------------------------------------------------------------
    ####
    machine.add("INIT",regex_b,do_open_var_bytes,"BYTES")
    machine.add("INIT",regex_spaces,None,"INIT")
    machine.add("INIT",regex_colons,do_colons,"INIT")
    machine.add("INIT",regex_commas,None,"INIT")
    machine.add("INIT",regex_slash,do_open_var,"SLASHINIT")
    machine.add("INIT",regex_ops,do_op,"INIT")
    machine.add("INIT",regex_not_LqRqBSpColComSlOp,do_open_var,"OTHER")
    ####
    machine.add("BYTES",regex_b,do_clear_byte_meeted,"OTHER")
    machine.add("BYTES",regex_spaces,do_close_var,"BYTES")
    machine.add("BYTES",regex_ops,do_throw,"ERROR")
    machine.add("BYTES",regex_colons,do_close_var_colon,"INIT")
    machine.add("BYTES",regex_commas,do_close_var,"INIT")
    machine.add("BYTES",regex_slash,do_clear_byte_meeted,"SLASHBYTES")
    machine.add("BYTES",regex_not_LqRqBSpColComSlOp,do_clear_byte_meeted,"OTHER")
    ####
    ####
    machine.add("SLASHINIT",re.compile("."),None,"OTHER")
    ####
    machine.add("SLASHBYTES",re.compile("."),None,"OTHER")
    ####
    machine.add("OTHER",regex_b,None,"OTHER")
    machine.add("OTHER",regex_spaces,do_close_var,"OTHER")
    machine.add("OTHER",regex_ops,do_throw,"ERROR")
    machine.add("OTHER",regex_colons,do_close_var_colon,"INIT")
    machine.add("OTHER",regex_commas,do_close_var,"INIT")
    machine.add("OTHER",regex_slash,None,"SLASHOTHER")
    machine.add("OTHER",regex_not_LqRqBSpColComSlOp,None,"OTHER")
    ####
    machine.add("SLASHOTHER",re.compile("."),None,"OTHER")
    ####
    regex_lquote_array = fsm.creat_regexes_array(lquotes)
    regex_rquote_array = fsm.creat_regexes_array(rquotes)
    ###
    for i in range(0,lquotes.__len__()):
        ####INIT -lq_n-> LQ_n
        sn = ''.join(("LQ",'_',str(i)))
        machine.add("INIT",regex_lquote_array[i],do_open_quote,sn)
    for i in range(0,rquotes.__len__()):
        ####INIT -rq_n-> ERROR
        if(regex_rquote_array[i] == regex_lquote_array[i]):
            pass
        else:
            sn = ''.join(("LQ",'_',str(i)))
            machine.add("INIT",regex_rquote_array[i],do_throw,'ERROR')
    ####
    for i in range(0,lquotes.__len__()):
        ####BYTES -lq_n-> LQ_n
        sn = ''.join(("LQ",'_',str(i)))
        machine.add("BYTES",regex_lquote_array[i],do_open_quote,sn)
    for i in range(0,rquotes.__len__()):
        ####BYTES -rq_n-> ERROR
        if(rquotes[i] == lquotes[i]):
            pass
        else:
            sn = ''.join(("LQ",'_',str(i)))
            machine.add("BYTES",regex_rquote_array[i],do_throw,'ERROR')
    ####
    for i in range(0,lquotes.__len__()):
        ####OTHER -lq_n-> ERROR
        sn = ''.join(("LQ",'_',str(i)))
        machine.add("OTHER",regex_lquote_array[i],do_throw,'ERROR')
    for i in range(0,rquotes.__len__()):
        ####OTHER -rq_n-> ERROR
        if(rquotes[i] == lquotes[i]):
            pass
        else:
            sn = ''.join(("LQ",'_',str(i)))
            machine.add("OTHER",regex_rquote_array[i],do_throw,'ERROR')
    ####
    for i in range(0,lquotes.__len__()):
        ####LQ_n -lq_n-> ERROR
        sn = ''.join(("LQ",'_',str(i)))
        if(lquotes[i] == rquotes[i]):
            pass
        else:
            machine.add(sn,regex_lquote_array[i],do_throw,'ERROR')
        ####LQ_n -rq_n-> INIT
        machine.add(sn,regex_rquote_array[i],do_close_quote,'INIT')
        #####LQ_n -b-> LQ_n
        machine.add(sn,regex_b,None,sn)
        #####LQ_n -spaces-> LQ_n
        machine.add(sn,regex_spaces,None,sn)
        #####LQ_n -ops-> LQ_n
        machine.add(sn,regex_ops,do_throw,'ERROR')
        ####LQ_n -colons-> LQ_n
        machine.add(sn,regex_colons,do_throw,'ERROR')
        ####LQ_n -commas-> LQ_n
        machine.add(sn,regex_commas,do_throw,'ERROR')
        #####LQ_n -slash -> SLASHLQ_n
        slashlq = ''.join(("SLASHLQ",'_',str(i)))
        machine.add(sn,re.compile("\\\\"),None,slashlq)
        ####SLASHLQ_n -any-> LQ_n
        machine.add(slashlq,re.compile("."),None,sn)
        #####LQ_n -others-> LQ_n
        tmp_arr = ['b','\\\\'] + ops + colons + commas + spaces 
        tmp_arr_rq = [rquotes[i]]
        tmp_arr_lq = [lquotes[i]]
        if(lquotes[i] == rquotes[i]):
            tmp_arr_rq = []
        else:
            pass
        tmp_final_arr = tmp_arr + tmp_arr_rq + tmp_arr_lq
        ####
        tmp_regex = fsm.creat_regex_not_from_arr(tmp_final_arr)
        machine.add(sn,tmp_regex,None,sn)
        #####
    #----------------------------------------------------------------
    curr_state = "INIT"
    prev_symbol = ''
    for i in range(0,line.__len__()):
        cursor = i
        input_symbol = line[i]
        action,next_state,trigger_checker = machine.search(curr_state,input_symbol)
        #print('----------')
        #print(curr_state,trigger_checker,input_symbol,action,next_state)
        #print(line)
        #print(path)
        #print(i)
        if(action == do_throw):
            action(curr_state,trigger_checker,input_symbol,line,path,i)   
        elif(action == None):
            pass
        else:
            si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted = action(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted)
        curr_state = next_state
        prev_symbol = input_symbol
    #-----Final handle------------------------------------------------------------
    #######
    if(curr_state == "INIT"):
        cursor = cursor + 1
        if(block.is_op(input_symbol)):
            pass
        else:
            si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted = do_open_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted)
        curr_state = "INIT"
    #######
    state_is_bytes = (curr_state == "BYTES")
    state_is_other = (curr_state == "OTHER")
    state_is_slashinit = (curr_state == "SLASHINIT")
    state_is_slashbytes = (curr_state == "SLASHBYTES")
    state_is_slashother = (curr_state == "SLASHOTHER")
    cond = (state_is_bytes|state_is_other|state_is_slashinit|state_is_slashbytes|state_is_slashother)
    #######
    if(cond):
        cursor = cursor + 1
        si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted = do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted)
        curr_state = "INIT"
    ######
    cond = ("SLASHLQ" in curr_state)
    if(cond):
        cursor = cursor + 1
        si,ei,color_sec,color_sec_seq,colon_meeted,byte_meeted = do_open_quote(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol,byte_meeted)
        curr_state = "INIT"
    return(color_sec)

#------------------------------------------

def print_j_str(j_str,**kwargs):
    if('display' in kwargs):
        display = kwargs['display']
    else:
        display = 0
    if('spaces' in kwargs):
        spaces = kwargs['spaces']
    else:
        spaces = [' ','\t']
    if('colons' in kwargs):
        colons = kwargs['colons']
    else:
        colons = [':']
    if('commas' in kwargs):
        commas = kwargs['commas']
    else:
        commas = [',']
    if('line_sps' in kwargs):
        line_sps = kwargs['line_sps']
    else:
        line_sps = ['\r','\n']
    #if('quotes' in kwargs):
    #    quotes = kwargs['quotes']
    #else:
    #    quotes = ['"',"'"]
    ##########
    ############
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent =0
    if('indent' in kwargs):
        indent = kwargs['indent']
    else:
        indent =4
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if('with_color' in kwargs):
        with_color = kwargs['with_color']
    else:
        with_color = 1
    if(with_color):
        if('key_color' in kwargs):
            key_color = kwargs['key_color']
        else:
            key_color=KEY_COLOR
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=VALUE_COLOR
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=LIST_ELE_COLOR
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=OP_COLOR
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=DEFAULT_COLOR
    ######
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = quote.get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = quote.get_quotes_pairs('""\'\'')
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = block.get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = block.get_block_op_pairs('{}[]()')
    lps = get_print_lines_and_paths(j_str,sp=sp,block_op_pairs_dict=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,fixed_indent=fixed_indent,indent=indent)
    lines = lps['lines']
    paths = lps['paths']
    try:
        start = args[0]
    except:
        start = 0
    else:
        pass
    try:
        end = args[1]
    except:
        end = lines.__len__()-1
    else:
        pass
    if('start' in kwargs):
        start = kwargs['start']
    else:
        pass

    if('end' in kwargs):
        end = kwargs['end']
    else:
        pass
    if(end > lines.__len__()):
        end = lines.__len__()-1
    #-----------------------------------------careful  paths not escaped but lines escaped====>>>
    painted_lines = {}
    for i in range(start,end+1):
        line = lines[i]
        if(with_color):
            color_sec = get_line_color_sec(line,paths[i],block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp)
            painted_string = paint(line,color_sec=color_sec,rtrn=True,mode=8)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
            painted_string = html.unescape(painted_string)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
        else:
            color_sec = None
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
            painted_string = html.unescape(line)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
        #not implemented yet
        # if(fixed_indent):
            # indent_num = paths[i].split(sp).__len__()
            # curr_head_len = indent * indent_num
        # else:
        painted_lines[i] = painted_string
        ####
        #if(display):
        #    print(painted_lines[i])
        #else:
        #    pass
    if(IS_WIN):
        pass
    else:
        if(display):
            s = elel.join(painted_lines,"\n")
            print(s)
        else:
            pass
    return(painted_lines)


beautify=print_j_str


def get_dflt_quotes_pairs_dict(**kwargs):
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = quote.get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = quote.get_quotes_pairs('""\'\'')
    return(quotes_pairs_dict)

def get_dflt_block_op_pairs_dict(**kwargs):
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = block.get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = block.get_block_op_pairs('{}[]()')
    return(block_op_pairs_dict)



def pobj(obj,*args,**kwargs):
    '''
        pobj(eles,quotes_pairs="''\"\"<>")
        pobj(eles,block_op_pairs="{}[]()")
    '''
    try:
        start = args[0]
    except:
        start = 0
    else:
        pass
    try:
        end = args[1]
    except:
        end = 2 ** 32
    else:
        pass
    sp = eftl.dflt_kwargs("sp",'/',**kwargs)
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs('block_op_pairs_dict',block.get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs('quotes_pairs_dict',quote.get_quotes_pairs('""\'\''))
    path_sps =  eftl.dflt_kwargs('path_sps',['/'],**kwargs)
    fixed_indent = eftl.dflt_kwargs('fixed_indent',0,**kwargs)
    indent = eftl.dflt_kwargs('indent',4,**kwargs)
    quotes_pairs_dict = get_dflt_quotes_pairs_dict(**kwargs)
    block_op_pairs_dict = get_dflt_block_op_pairs_dict(**kwargs)
    if('with_color' in kwargs):
        with_color = kwargs['with_color']
    else:
        with_color = 1
    if(with_color):
        if('key_color' in kwargs):
            key_color = kwargs['key_color']
        else:
            key_color=KEY_COLOR
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=VALUE_COLOR
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=LIST_ELE_COLOR
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=OP_COLOR
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=DEFAULT_COLOR
    if('start' in kwargs):
        start = kwargs['start']
    else:
        pass
    ##########
    ############1
    if('end' in kwargs):
        end = kwargs['end']
    else:
        pass
    if(utils.is_str(obj)):
        s = obj
    else:
        s = obj.__str__()
    if(with_color):
        print_j_str(s,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,display=1,start=start,end=end,fixed_indent=fixed_indent,indent=indent)
    else:
        print_j_str(s,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,start=start,end=end,fixed_indent=fixed_indent,indent=indent,display=1)



def parr(arr):
    for i in range(len(arr)):
        print(arr[i])



def pattr(orb):
    attrs = eotl.get_all_visible_attrs(orb)
    for attr in attrs:
        print(attr,":",orb.__getattribute__(attr))



def pdir(obj,*args,**kwargs):
    '''
        >>> import os
        >>> from xdict.jprint import  pdir
        >>> pdir(os,range=(1,10))
        [
         'CLD_DUMPED', 
         'CLD_EXITED', 
         'CLD_TRAPPED', 
         'EX_CANTCREAT', 
         'EX_CONFIG', 
         'EX_DATAERR', 
         'EX_IOERR', 
         'EX_NOHOST', 
         'EX_NOINPUT'
        ]
        >>> 
    '''
    obj = dir(obj)
    try:
        start = args[0]
    except:
        start = 0
    else:
        pass
    try:
        end = args[1]
    except:
        end = 2 ** 32
    else:
        pass
    if('egrep' in kwargs):
        nobj = []
        for each in obj:
            if(kwargs['egrep'] in each):
                nobj.append(each)
            else:
                pass
        obj = nobj
    else:
        pass
    if('range' in kwargs):
        start = kwargs['range'][0]
        end = kwargs['range'][1]
    else:
        pass
    sp = eftl.dflt_kwargs("sp",'/',**kwargs)
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs('block_op_pairs_dict',block.get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs('quotes_pairs_dict',quote.get_quotes_pairs('""\'\''))
    path_sps =  eftl.dflt_kwargs('path_sps',['/'],**kwargs)
    fixed_indent = eftl.dflt_kwargs('fixed_indent',0,**kwargs)
    indent = eftl.dflt_kwargs('indent',4,**kwargs)
    quotes_pairs_dict = get_dflt_quotes_pairs_dict(**kwargs)
    block_op_pairs_dict = get_dflt_block_op_pairs_dict(**kwargs)
    if('with_color' in kwargs):
        with_color = kwargs['with_color']
    else:
        with_color = 1
    if(with_color):
        if('key_color' in kwargs):
            key_color = kwargs['key_color']
        else:
            key_color=KEY_COLOR
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=VALUE_COLOR
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=LIST_ELE_COLOR
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=OP_COLOR
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=DEFAULT_COLOR
    else:
        pass
    if('start' in kwargs):
        start = kwargs['start']
    else:
        pass
    if('end' in kwargs):
        end = kwargs['end']
    else:
        pass
    ###
    obj = obj[start:end]
    ###
    if(with_color):
        pobj(obj,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,display=1,fixed_indent=fixed_indent,indent=indent)
    else:
        pobj(obj,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,fixed_indent=fixed_indent,indent=indent,display=1)


