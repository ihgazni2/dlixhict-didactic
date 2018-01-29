import time
import re
import jsbeautifier as jb
from xdict import utils
import html
import copy

# lv_dict
## {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {"key_7_tl": [[], "value_2", "value_4", "value_4"], "key_13_TVj_lP": "value_6", "key_8_9vPp6PT": "value_9", "key_10_Uy": ["value_1"]
## 1222222222222222222222222222222222222222222223333333333333333333333333333333333333333333333333333333333333333333333344444444444445555555555555555555555555555555555544444444444444444444444444444444444444444444444444444444444444444444444445555555554
# attr_dict op,key,dict_value,list_value,tuple_value,set_value

#1. use html.escape  to  escape all quote-operators appeared in single-quote or double-quote
#2. use html.escape  to  escape all paired-operators appeared in single-quote or double-quote : such as  "{,},[,],(,)" 
#3. use html.escape  to  escape all other operators appeared in single-quote or double-quote : such as : ':',','
#4. use html_escape  to  escape seperators-operators appeared in single-quote or double-quote: such as '\n'


__doc__ = '''
'''

#-----------------------------------------------
def html_number_escape_char(ch):
    '''
        >>> es = html_number_escape_char('a')
        >>> es
        '&#97;'
        >>> html.unescape(es)
        'a'
        >>> es = html_number_escape_char('用')
        >>> es
        '&#29992;'
        >>> html.unescape(es)
        '用'
        >>> 
    '''
    num = utils.char_str_to_unicode_num(ch)
    escaped = ''.join(('&#',str(num),';'))
    return(escaped)

def html_number_escape_str(s):
    '''
        >>> 
        >>> ess = html_number_escape_str('加强武器')
        >>> ess
        '&#21152;&#24378;&#27494;&#22120;'
        >>> html.unescape(ess)
        '加强武器'
        >>> ess = html_number_escape_str('xyzw')
        >>> ess
        '&#120;&#121;&#122;&#119;'
        >>> html.unescape(ess)
        'xyzw'
        >>> 
    '''
    escaped = ''
    for i in range(0,s.__len__()):
        esch = html_number_escape_char(s[i])
        escaped = ''.join((escaped,esch))
    return(escaped)

def get_block_op_pairs(pairs_str):
    '''
        # >>> get_block_op_pairs("{}[]")  
        # {1: ('{', '}'), 2: ('[', ']')}
        # >>> get_block_op_pairs("{}[]()")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')')}
        # >>> get_block_op_pairs("{}[]()<>")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')'), 4: ('<', '>')}
    '''
    pairs_str_len = pairs_str.__len__()
    pairs_len = pairs_str_len // 2
    pairs_dict = {}
    for i in range(1,pairs_len +1):
        pairs_dict[i] = pairs_str[i*2-2],pairs_str[i*2-1]
    return(pairs_dict)

##quotes_pairs
get_quotes_pairs = get_block_op_pairs
##



def get_jdict_token_set(**kwargs):
    def get_slashxs(ch):
        d = {1:ch}
        if('\\' in d.__str__()):
            return(True)
        else:
            return(False)
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
    ############        
    #if('quotes' in kwargs):
    #    quotes = kwargs['quotes']
    #else:
    #    quotes = ['"',"'"]
    if('block_op_pairs_dict' in kwargs):
        block_op_pairs_dict = kwargs['block_op_pairs_dict']
    else:
        block_op_pairs_dict=get_block_op_pairs('{}[]()')
    if('quotes_pairs_dict' in kwargs):
        quotes_pairs_dict = kwargs['quotes_pairs_dict']
    else:
        quotes_pairs_dict=get_quotes_pairs('""\'\'')
    lquotes = []
    rquotes = []
    for i in range(1,quotes_pairs_dict.__len__()+1):
        lquotes.append(quotes_pairs_dict[i][0])
        rquotes.append(quotes_pairs_dict[i][1])
    ###########
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
    #html.unescape("{1: '&#8;&#2;'}")  "{1: ''}"
    if('slashxs' in kwargs):
        slashxs = kwargs['slashxs']
    else:
        slashxs = []
        for i in range(0,256):
            if(get_slashxs(chr(i))):
                slashxs.append(chr(i))
            else:
                pass
    if('ctrls' in kwargs):
        ctrls = kwargs['ctrls']
    else:
        ctrls = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f']
    for each in spaces:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    for each in colons:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    for each in commas:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    for each in line_sps:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    #for each in quotes:
    #    try:
    #        ctrls.remove(each)
    #    except:
    #        pass
    #    else:
    #        pass
    #####
    for each in lquotes:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    for each in rquotes:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    ####
    for each in path_sps:
        try:
            ctrls.remove(each)
        except:
            pass
        else:
            pass
    d = {}
    s = set({})
    def add_bi_table(s,d,x):
        for each in x:
            k = each
            v = html_number_escape_str(k)
            d[k] = v
            d[v] = k
            s.add(k)
            s.add(v)
    add_bi_table(s,d,spaces)
    add_bi_table(s,d,colons)
    add_bi_table(s,d,commas)
    add_bi_table(s,d,line_sps)
    #add_bi_table(s,d,quotes)
    ####
    add_bi_table(s,d,lquotes)
    add_bi_table(s,d,rquotes)
    ####
    add_bi_table(s,d,path_sps)
    for i in range(1,block_op_pairs_dict.__len__()+1):
        s.add(block_op_pairs_dict[i][0])
        s.add(block_op_pairs_dict[i][1])
        recover_token_l = html_number_escape_str(block_op_pairs_dict[i][0])
        recover_token_r = html_number_escape_str(block_op_pairs_dict[i][1])
        s.add(recover_token_l)
        s.add(recover_token_r)
        d[block_op_pairs_dict[i][0]] = recover_token_l 
        d[block_op_pairs_dict[i][1]] = recover_token_r
        d[recover_token_l] = block_op_pairs_dict[i][0]
        d[recover_token_r] = block_op_pairs_dict[i][1]
    return({'token_set':s,'replace_ref_dict':d})

def convert_token_in_quote(j_str,**kwargs):
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
    if('block_op_pairs_dict' in kwargs):
        block_op_pairs_dict = kwargs['block_op_pairs_dict']
    else:
        block_op_pairs_dict=get_block_op_pairs('{}[]()')
    if('quotes_pairs_dict' in kwargs):
        quotes_pairs_dict = kwargs['quotes_pairs_dict']
    else:
        quotes_pairs_dict=get_quotes_pairs('""\'\'')
    lquotes = []
    rquotes = []
    for i in range(1,quotes_pairs_dict.__len__()+1):
        lquotes.append(quotes_pairs_dict[i][0])
        rquotes.append(quotes_pairs_dict[i][1])
    ###############
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
    temp = get_jdict_token_set(block_op_pairs_dict=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps)
    token_set = temp['token_set']
    replace_ref_dict = temp['replace_ref_dict']
    # ----------------------------------------------------------------- #
    #Q: QUOTE
    #PISIQ: PRE_IS_SLASH_IN_QUOTE
    
    
    #SQ:SINGLE_QUOTE
    #DQ:DOUBLE_QUOTE
    #PISIQ:PRE_IS_SLASH_IN_SQ
    #PISID:PRE_IS_SLASH_IN_DQ
    #input_symbol_array = ['"',"'",'\\']
    #states_array = ["INIT","Q","PIIQ"]
    
    def do_replace(ch):
        if(ch in token_set):
            ch = replace_ref_dict[ch]
        return(ch)
    
    #regex_quotes = []
    ####
    regex_lquotes = []
    regex_rquotes = []
    ####
    regex_nonlqses = []
    regex_nonrqses = []
    regex_nonqses = []
    non_regex_lquote_str = '[^'
    non_regex_rquote_str = '[^'
    non_regex_quote_str = '[^'
    
    for i in range(0,quotes.__len__()):
        #regex_quote_str = ''.join(('[',quotes[i],']'))
        #regex_quote = re.compile(regex_quote_str)
        #regex_quotes.append(regex_quote)
        regex_lquote_str = ''.join(('[',lquotes[i],']'))
        regex_lquote = re.compile(regex_lquote_str)
        regex_lquotes.append(regex_lquote)
        regex_rquote_str = ''.join(('[',rquotes[i],']'))
        regex_rquote = re.compile(regex_rquote_str)
        regex_rquotes.append(regex_rquote)
        #####
        regex_nonlqs_str = ''.join(('[^',lquotes[i],'\\\\]'))
        regex_nonlqs = re.compile(regex_nonlqs_str)
        regex_nonlqses.append(regex_nonlqs)
        non_regex_lquote_str = ''.join((non_regex_lquote_str,lquotes[i]))
        ####
        regex_nonrqs_str = ''.join(('[^',rquotes[i],'\\\\]'))
        regex_nonrqs = re.compile(regex_nonrqs_str)
        regex_nonrqses.append(regex_nonrqs)
        non_regex_rquote_str = ''.join((non_regex_rquote_str,rquotes[i]))
        ####
        regex_nonqs_str = ''.join(('[^',lquotes[i],rquotes[i],'\\\\]'))
        regex_nonqs = re.compile(regex_nonqs_str)
        regex_nonqses.append(regex_nonqs)
        non_regex_quote_str = ''.join((non_regex_quote_str,lquotes[i],rquotes[i]))
        #####
    non_regex_lquote_str = ''.join((non_regex_lquote_str,']'))
    non_regex_lquote = re.compile(non_regex_lquote_str)
    non_regex_rquote_str = ''.join((non_regex_rquote_str,']'))
    non_regex_rquote = re.compile(non_regex_rquote_str)
    non_regex_quote_str = ''.join((non_regex_quote_str,']'))
    non_regex_quote = re.compile(non_regex_quote_str)
    # ############################
    fsm_dict = {
        ("INIT",non_regex_quote) : (None,"INIT")
    }
    for i in range(0,regex_lquotes.__len__()):
        ####INIT -lq_n-> LQ_n
        k = ("INIT",regex_lquotes[i])
        sn = ''.join(("LQ",'_',str(i)))
        v = (None,sn)
        fsm_dict[k] = v
        #### LQ_n -rq_n-> INIT
        k = (sn,regex_rquotes[i])
        v = (None,"INIT")
        fsm_dict[k] = v
        #####LQ_n -pisiq_n-> PISIQ_n 
        pisiq = ''.join(("PISIQ",'_',str(i)))
        k = (sn,re.compile("\\\\"))
        v = (None,pisiq)
        fsm_dict[k] = v
        ####PISIQ_n -any-> LQ_n
        k = (pisiq,re.compile("."))
        v = (do_replace,sn)
        fsm_dict[k] = v
        #####LQ_n -nonq-> LQ_n
        if(lquotes[i] == rquotes[i]):
            k = (sn,regex_nonqses[i])
            v = (do_replace,sn)
            fsm_dict[k] = v
        else:
            #####LQ_n -nonrq-> LQ_n
            k = (sn,regex_nonrqses[i])
            v = (do_replace,sn)
            fsm_dict[k] = v
        #####
    # #################################
    def search_fsm(curr_state,input_symbol,fsm_dict):
        for key in fsm_dict:
            if(key[0] == curr_state):
                if(key[1].search(input_symbol)):
                    return(fsm_dict[key])
                else:
                    pass
            else:
                pass
        return(None)
    curr_state = "INIT"
    rslt = ''
    for i in range(0,j_str.__len__()):
        input_symbol = j_str[i]
        temp = search_fsm(curr_state,input_symbol,fsm_dict)
        action = temp[0]
        if(action):
            ch = action(input_symbol)
        else:
            ch = input_symbol
        rslt = ''.join((rslt,ch))
        curr_state = temp[1]
    return(rslt)

def format_j_str(j_str,block_op_pairs_dict=get_block_op_pairs('{}[]()'),**kwargs):
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
    if('quotes' in kwargs):
        quotes = kwargs['quotes']
    else:
        quotes = ['"',"'"]
    def get_rm_regexp(l):
        regex_remove_str = '['
        for i in range(0,l.__len__()):
            regex_remove_str = ''.join((regex_remove_str,l[i]))
        regex_remove_str = ''.join((regex_remove_str,']+'))
        regex_remove = re.compile(regex_remove_str)
        return(regex_remove)
    def get_insert_space_regexp(l):
        regex_insert_space_str = '['
        for i in range(0,l.__len__()):
            regex_insert_space_str = ''.join((regex_insert_space_str,l[i]))
        regex_insert_space_str = ''.join((regex_insert_space_str,']'))
        regex_insert_space = re.compile(regex_insert_space_str)
        return(regex_insert_space)
    # ----------------------------------------------------------------------------------
    # __str__  will make some difference :  eval will replace \\xXX wil \xXX
    # >>> js1 = "{'\x01': '\x02'}"
    # >>> js2 = "{'\\x01': '\\x02'}"
    # >>> 
    # >>> j1 = eval(js1)
    # >>> j1
    # {'\x01': '\x02'}
    # >>> j2 = eval(js2)
    # >>> j2
    # {'\x01': '\x02'}
    # >>> j1 == j2
    # True
    # >>> js1 == js2
    # False
    # >>> js3 = j1.__str__()
    # >>> js1 == js3
    # False
    # >>> js2 == js3
    # True
    # >>> js3
    # "{'\\x01': '\\x02'}"
    # >>>
    # format step 1: remove functinal-spaces(spaces not in quote) and functional-line_sp
    regex_remove_spaces = get_rm_regexp(spaces)
    j_str = regex_remove_spaces.sub("",j_str)
    regex_remove_line_sps = get_rm_regexp(line_sps)
    j_str = regex_remove_line_sps.sub("",j_str)
    # format step 2: replace functional-colons with "<colon> ",replace functional-sps with "<sp> \n"
    colon_and_sps = copy.deepcopy(colons)
    colon_and_sps.extend(commas)
    insert_space_regexp = get_insert_space_regexp(colon_and_sps)
    j_str = re.sub(insert_space_regexp,r'\g<0> ',j_str)
    # format step 3: seperate each elements in one line
    j_str = j_str.replace(", ",", \n")
    # format step 4: seerate recursive element in one new line 
    for i in range(1,block_op_pairs_dict.__len__()+1):
        j_str = j_str.replace(block_op_pairs_dict[i][0],''.join(("\n",block_op_pairs_dict[i][0],"\n")))
        j_str = j_str.replace(block_op_pairs_dict[i][1],''.join(("\n",block_op_pairs_dict[i][1],"\n")))
    j_str = j_str.replace("\n\n","\n")
    # format step 5: move empty to one line 
    for i in range(1,block_op_pairs_dict.__len__()+1):
        j_str = j_str.replace(''.join((block_op_pairs_dict[i][0],'\n',block_op_pairs_dict[i][1])),''.join((block_op_pairs_dict[i][0],block_op_pairs_dict[i][1])))
    # format step 6: 
    j_str = j_str.replace("\n,",",")
    j_str = j_str.strip("\n")
    j_str = j_str.replace("\n\n","\n")
    return(j_str)

def is_lop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
    # is_lop('{',block_op_pairs_dict)
    # is_lop('[',block_op_pairs_dict)
    # is_lop('}',block_op_pairs_dict)
    # is_lop(']',block_op_pairs_dict)
    # is_lop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][0]):
            return(True)
        else:
            pass
    return(False)

def is_rop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_rop('{',block_op_pairs_dict)
        # is_rop('[',block_op_pairs_dict)
        # is_rop('}',block_op_pairs_dict)
        # is_rop(']',block_op_pairs_dict)
        # is_rop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][1]):
            return(True)
        else:
            pass
    return(False)

def is_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_op('{',block_op_pairs_dict)
        # is_op('[',block_op_pairs_dict)
        # is_op('}',block_op_pairs_dict)
        # is_op(']',block_op_pairs_dict)
        # is_op('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][0]):
            return(-1)
        elif(ch == block_op_pairs_dict[i][1]):
            return(1)
        else:
            pass
    return(0)

def which_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # which_op('{',block_op_pairs_dict)
        # which_op('[',block_op_pairs_dict)
        # which_op('}',block_op_pairs_dict)
        # which_op(']',block_op_pairs_dict)
        # which_op('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][0]):
            return((i,0))
        elif(ch == block_op_pairs_dict[i][1]):
            return((i,1))
        else:
            pass
    return((-1,-1))

def is_op_pair(ch1,ch2,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_op_pair('{','}',block_op_pairs_dict)
        # is_op_pair('[',']',block_op_pairs_dict)
        # is_op_pair('}','{',block_op_pairs_dict)
        # is_op_pair(']','[',block_op_pairs_dict)
        # is_op_pair('{',']',block_op_pairs_dict)
        # is_op_pair('a','a',block_op_pairs_dict)
    '''
    x1,y1 = which_op(ch1,block_op_pairs_dict)
    x2,y2 = which_op(ch2,block_op_pairs_dict)
    if((x1 == -1) | (x2 == -1)):
        return(False)
    elif((x1 == x2) & (not(y1 == y2))):
        return(True)
    else:
        return(False)

def is_ordered_op_pair(ch1,ch2,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_Strict_Pair('{','}',block_op_pairs_dict)
        # is_Strict_Pair('[',']',block_op_pairs_dict)
        # is_Strict_Pair('}','{',block_op_pairs_dict)
        # is_Strict_Pair(']','[',block_op_pairs_dict)
        # is_Strict_Pair('{',']',block_op_pairs_dict)
        # is_Strict_Pair('a','a',block_op_pairs_dict)
    '''
    x1,y1 = which_op(ch1,block_op_pairs_dict)
    x2,y2 = which_op(ch2,block_op_pairs_dict)
    if((x1 == -1) | (x2 == -1)):
        return(False)
    elif((x1 == x2) & (y1 == 0)& (y2 == 1)):
        return(True)
    else:
        return(False)

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

def is_non_ordered_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'),block_non_ordered_op_pairs_dict=get_block_op_pairs('{}')):
    if(is_op(ch,block_op_pairs_dict)):
        for i in range(1,block_non_ordered_op_pairs_dict.__len__()+1):
            if(ch == block_non_ordered_op_pairs_dict[i][0]):
                return(-1)
            elif(ch == block_non_ordered_op_pairs_dict[i][1]):
                return(1)
            else:
                return(0)
    else:
        return(0)
        
def get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    ''' the first-char is level-1
        when current is  non-op, next-char-level = curr-level
        when current is  lop,  non-paired-rop-next-char-level = lop-level+1;
        when current is  lop,  paired-rop-next-char-level = lop-level
        when current is  rop,  next-char-level = rop-level - 1
        # {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {......
        # 122222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333333333333334......
        # {\n"key_4_UF0aJJ6v": "value_1", \n"key_2_Hd0t": [\n"value_16", \n"value_8", \n"value_8", \n"value_15", \n"value_14", \n"value_19",...... 
        # 1 222222222222222222222222222222 2222222222222222 3333333333333 333333333333 333333333333 3333333333333 3333333333333 3333333333333...... 
        '''
    curr_ch = j_str[curr_seq]
    next_ch = j_str[curr_seq + 1]
    cond = 0
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(curr_ch == block_op_pairs_dict[i][0]):
            if(next_ch == block_op_pairs_dict[i][1]):
                next_lv = curr_lv               
            else:
                next_lv = curr_lv + 1
            cond = 1
            break
        elif(curr_ch == block_op_pairs_dict[i][1]):
            if(is_rop(next_ch,block_op_pairs_dict)):
                next_lv = curr_lv - 1
            else:
                next_lv = curr_lv
            cond = 1
            break
        else:
            pass
    if(cond == 1):
        pass
    elif(is_rop(next_ch,block_op_pairs_dict)):
        next_lv = curr_lv - 1
    else:    
        next_lv = curr_lv
    curr_lv = next_lv
    curr_seq = curr_seq + 1
    return(curr_lv,curr_lv,curr_seq)

def get_j_str_lvs_dict(j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    j_str_len = j_str.__len__()
    j_str_lvs_dict = {}
    if( j_str_len == 0):
        j_str_lvs_dict = {}
    elif(j_str_len == 1):
        j_str_lvs_dict = {0:1}
    else:
        curr_lv = 1
        j_str_lvs_dict = {0:1}
        seq = 1
        curr_seq = 0
        while(curr_seq < j_str_len - 1):
            level,curr_lv,curr_seq = get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict)
            j_str_lvs_dict[seq] =level
            seq = seq + 1
    return(j_str_lvs_dict)

def get_line_start_index_in_j_str(orig_lines):
    line_start_indexes = {}
    line_start_indexes[0] = 0
    for i in range(1,orig_lines.__len__()):
        next = line_start_indexes[i - 1] + orig_lines[i - 1].__len__() + 1
        line_start_indexes[i] = next
    return(line_start_indexes)

def line_to_path_init(line,block_op_pairs_dict = get_block_op_pairs("{}[]()"),sp='/',commas=[','],colons=[':']):
    end = line.rstrip(' ')[-1]
    if(is_colon(end,colons)):
        curr_base_name = ''.join((line,sp))
    elif(is_lop(end,block_op_pairs_dict)):
        curr_base_name = ''.join((line,sp))
    elif(is_comma(end,commas)):
        curr_base_name = line
    elif(is_rop(end,block_op_pairs_dict)):
        curr_base_name = line
    else:
        curr_base_name = line
    curr_path = ''.join((sp,curr_base_name))
    return(curr_path)

def line_to_path(line,curr_lv,prev_lv,prev_path,block_op_pairs_dict= get_block_op_pairs("{}[]()"),sp='/',commas=[','],colons=[':']):
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
        # {
        #  'Error': None, #curr_lv > prev_lv : prev_path = /{/   curr_path = /{/'Error': None, 
        #  'Value':       #curr_lv == prev_lv ,secarino_6 : prev_path = /{/'Error': None,    curr_path = /{/'Value':/
        #           {     #curr_lv == prev_lv ,secarino_1 : prev_path =  /{/'Value': /  curr_path =  /{/'Value':/{/ 
        #            'MyRulesHtml': '<div></div>', #curr_lv > prev_lv :prev_path =  /{/'Value': /{/  curr_path =   /{/'Value': /{/'MyRulesHtml': '<div></div>', 
        #            '__type': 'RuleDesignerRuleResult', #curr_lv == prev_lv,secarino_6 :prev_path = /{/'Value': /{/'MyRulesHtml': '<div></div>', curr_path = /{/'Value': /{/'__type': 'RuleDesignerRuleResult',
        #################################################
        #'SimulationValues': 
        #                    {
        #                     'Name': 'SWIMMING_POOL_LENGTH', 
        #                     'Value': '100'
        #                    },  
        #'Pair': # curr_lv == prev_lv ,secarino_2  :  prev_path = .../'SimulationValues': /},    curr_path = .../'Pair': 
        #        (
        #         'swimming', 
        #         'cadence'
        #        )
        #################################################
        # 'UserVariables': 
        #                  [
        #                   {
        #                    'Name': 'OWNVAR1', 
        #                    'Value': '0'
        #                   },
        #                   {# curr_lv == prev_lv ,secarino_3  :  prev_path = .../[/},,    curr_path = .../{/ 
        #                    'Name': 'OWNVAR2', 
        #                    'Value': '200'
        #                   }
        #                  ]
        ######################################################
        # 'UserVariables': 
        #                  [
        #                   {},
        #                   {# curr_lv == prev_lv ,secarino_4  :  prev_path = .../[/{},,    curr_path = .../{/ 
        #                    'Name': 'OWNVAR2', 
        #                    'Value': '200'
        #                   }
        #                  ] # curr_lv < prev_lv,secarino_7  :   prev_path = .../[/},,    curr_path = .../
        ######################################################
        #'xx': 
        #     {
        #      'head': 
        #              {}
        #     }# curr_lv < prev_lv,secarino_8  :   prev_path = /xx: /{/head: /{},    curr_path = /xx: /}
        ########################################################################
        # secarino_1:
        if(is_colon(prev_last)):
            curr_path = ''.join((prev_path,curr_base_name))
        elif(is_rop(prev_rop,block_op_pairs_dict)):
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
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ####
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
    if('block_op_pairs_dict' in kwargs):
        block_op_pairs_dict = kwargs['block_op_pairs_dict']
    else:
        block_op_pairs_dict=get_block_op_pairs('{}[]()')
    if('quotes_pairs_dict' in kwargs):
        quotes_pairs_dict = kwargs['quotes_pairs_dict']
    else:
        quotes_pairs_dict=get_quotes_pairs('""\'\'')
    ############
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
    j_str = convert_token_in_quote(j_str,block_op_pairs_dict=block_op_pairs_dict,quotes_pair_dict=quotes_pair_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps)
    j_str = format_j_str(j_str,block_op_pairs_dict)
    j_lv_str = get_j_str_lvs_dict(j_str,block_op_pairs_dict)
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
        curr_head = utils.path_string_get_head(curr_path,delimiter=sp).replace(sp,'')
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

def get_line_color_sec(line,path,**kwargs):
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
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    if('block_non_ordered_op_pairs' in kwargs):
        block_non_ordered_op_pairs = kwargs['block_non_ordered_op_pairs']
        if(utils.is_dict(block_non_ordered_op_pairs)):
            block_non_ordered_op_pairs_dict = block_non_ordered_op_pairs
        else:
            block_non_ordered_op_pairs_dict = get_block_op_pairs(block_non_ordered_op_pairs)
    else:
        block_non_ordered_op_pairs_dict = get_block_op_pairs('{}')
    ####
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = get_quotes_pairs('{}[]()')
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
        key_color=3
    if('value_color' in kwargs):
        value_color = kwargs['value_color']
    else:
        value_color=7
    if('list_ele_color' in kwargs):
        list_ele_color = kwargs['list_ele_color']
    else:
        list_ele_color=4
    if('op_color' in kwargs):
        op_color = kwargs['op_color']
    else:
        op_color=8
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color=9
    #------------------------------------------------------------
    line_len = line.__len__()
    si = 0
    ei = 0
    color_sec = {}
    color_sec_seq = 1
    colon_meeted = 0
    #-------------------------------------------------------------
    ops = []
    for i in range(1,block_op_pairs_dict.__len__()+1):
        ops.append(block_op_pairs_dict[i][0])
        ops.append(block_op_pairs_dict[i][1])
    ######
    def creat_regexes_array(quotes):
        regex_quotes = []
        for i in range(0,quotes.__len__()):
            regex_quote_str = ''.join(('[',quotes[i],']'))
            regex_quote = re.compile(regex_quote_str)
            regex_quotes.append(regex_quote)
        return(regex_quotes)
    #####
    def creat_nonqses_regexes_array(quotes):
        regex_nonqses =[]
        for i in range(0,quotes.__len__()):
            regex_nonqs_str = ''.join(('[^',quotes[i],'\\\\]'))
            regex_nonqs = re.compile(regex_nonqs_str)
            regex_nonqses.append(regex_nonqs)
        return(regex_nonqses)
    def creat_regex(quotes):
        regex_quote_str = '['
        for i in range(0,quotes.__len__()):
            regex_quote_str = ''.join((regex_quote_str,'\\',quotes[i]))
        regex_quote_str = ''.join((regex_quote_str,']'))
        return(re.compile(regex_quote_str))
    def creat_not_regex(quotes):
        regex_quote_str = '[^'
        for i in range(0,quotes.__len__()):
            regex_quote_str = ''.join((regex_quote_str,'\\',quotes[i]))
        regex_quote_str = ''.join((regex_quote_str,']'))
        return(re.compile(regex_quote_str))
    def creat_others_regexes(quotes,colons,ops,commas,spaces,bchars):
        non_regex_qco_str = '[^'
        for i in range(0,quotes.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,quotes[i]))
        for i in range(0,colons.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,colons[i]))
        for i in range(0,ops.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,'\\',ops[i]))
        for i in range(0,commas.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,commas[i]))
        for i in range(0,spaces.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,spaces[i]))
        for i in range(0,bchars.__len__()):
            non_regex_qco_str = ''.join((non_regex_qco_str,bchars[i]))
        non_regex_qco_str = ''.join((non_regex_qco_str,']'))
        non_regex_qco = re.compile(non_regex_qco_str)
        return(non_regex_qco)
    #-------------------------------------------------------------------------------------
    regex_quotes_array = creat_regexes_array(quotes)
    regex_nonqses_array = creat_nonqses_regexes_array(quotes)
    regex_lquotes_array = creat_regexes_array(lquotes)
    regex_nonlqses_array = creat_nonqses_regexes_array(lquotes)
    regex_rquotes_array = creat_regexes_array(rquotes)
    regex_nonrqses_array = creat_nonqses_regexes_array(rquotes)
    #-------------------------------------------------------------------------------------
    regex_colons = creat_regex(colons)
    regex_commas = creat_regex(commas)
    regex_spaces = creat_regex(spaces)
    #-------------------------------------------------------------------------------------
    regex_ops = creat_regex(ops)
    regex_others = creat_others_regexes(quotes,colons,ops,commas,spaces,[])
    ##--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
    regex_b = re.compile('b')
    regex_others_without_b = creat_others_regexes(quotes,colons,ops,commas,spaces,['b'])
    ##--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
    #-------------------------------------------------------------------
    head = utils.path_string_get_head(path)
    head_last = utils.str_rstrip(head,sp,1)
    head_last = utils.str_rstrip(head_last," ",1)
    if(head_last == ''):
        pass
    else:
        head_last = head_last[-1]
    #------------------------------------------------------
    def do_open_quote(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        ei = cursor 
        curr_color = default_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor + 1
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_close_quote(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        ei = cursor - 1
        if(colon_meeted):
            curr_color = value_color
        else:
            if(is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
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
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_open_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        ei = cursor - 1
        if(prev_symbol == 'b'):
            ei = ei - 1
        else:
            pass
        curr_color = default_color
        color_sec[color_sec_seq] = (si,ei,curr_color)
        color_sec_seq = color_sec_seq + 1
        si = cursor
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        ei = cursor - 1
        if(colon_meeted):
            curr_color = value_color
        else:
            if(is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
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
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_colons(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        colon_meeted = 1
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_op(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        ei = cursor - 1
        curr_color = default_color
        if(ei >= si):
            color_sec[color_sec_seq] = (si,ei,curr_color)
            color_sec_seq = color_sec_seq + 1
        else:
            pass
        si = cursor 
        ei = cursor 
        if(is_non_ordered_op(head_last,block_op_pairs_dict,block_non_ordered_op_pairs_dict)):
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
        return(si,ei,color_sec,color_sec_seq,colon_meeted)
    def do_close_var_colon(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol):
        colon_meeted = 1
        return(do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol))
    #----------------------------------------------------------------------------------------
    fsm_dict = {
        ("INIT",regex_colons) : (do_colons,"INIT"),
        ("INIT",regex_commas) : (None,"INIT"),
        ("INIT",regex_spaces) : (None,"INIT"),
        ("INIT",regex_ops) : (do_op,"INIT"),
        ("INIT",regex_others_without_b) : (do_open_var,"OTHER"),
        ##--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
        ("INIT",regex_b) : (None,"BYTES"),
        ("BYTES",regex_others) : (do_open_var,"OTHER"),
        ##--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
        ("OTHER",regex_others) : (None,"OTHER"),
        ("OTHER",regex_colons) : (do_close_var_colon,"INIT"),
        ("OTHER",regex_commas) : (do_close_var,"INIT"),
        ("OTHER",regex_spaces) : (do_close_var,"INIT")
    }    
    for i in range(0,regex_lquotes_array.__len__()):
        ####INIT -lq_n-> LQ_n
        k = ("INIT",regex_lquotes_array[i])
        sn = ''.join(("LQ",'_',str(i)))
        v = (do_open_quote,sn)
        fsm_dict[k] = v
        ####LQ_n -rq_n-> INIT
        k = (sn,regex_rquotes_array[i])
        v = (do_close_quote,"INIT")
        fsm_dict[k] = v
        ####LQ_n -pisiq_n-> PISIQ_n
        pisiq = ''.join(("PISIQ",'_',str(i)))
        k = (sn,re.compile("\\\\"))
        v = (None,pisiq)
        fsm_dict[k] = v
        ####PISIQ_n -any-> LQ_n
        k = (pisiq,re.compile("."))
        v = (None,sn)
        fsm_dict[k] = v
        ####
        #####LQ_n -nonq-> LQ_n
        if(lquotes[i] == rquotes[i]):
            k = (sn,regex_nonqses_array[i])
            v = (None,sn)
            fsm_dict[k] = v
        else:
            #####LQ_n -nonrq-> LQ_n
            k = (sn,regex_nonrqses_array[i])
            v = (None,sn)
            fsm_dict[k] = v
        ####
    #--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
    for i in range(0,regex_lquotes_array.__len__()):
        k = ("BYTES",regex_lquotes_array[i])
        sn = ''.join(("BLQ",'_',str(i)))
        v = (do_open_quote,sn)
        fsm_dict[k] = v
        ####
        k = (sn,regex_rquotes_array[i])
        v = (do_close_quote,"INIT")
        fsm_dict[k] = v
        ####
        bpisiq = ''.join(("BPISIQ",'_',str(i)))
        k = (sn,re.compile("\\\\"))
        v = (None,bpisiq)
        fsm_dict[k] = v
        ####
        k = (bpisiq,re.compile("."))
        v = (None,sn)
        fsm_dict[k] = v
        ####
        if(regex_lquotes_array[i] == regex_rquotes_array[i]):
            k = (sn,regex_nonqses_array[i])
            v = (None,sn)
            fsm_dict[k] = v
        else:
            k = (sn,regex_nonrqses_array[i])
            v = (None,sn)
            fsm_dict[k] = v
        ####
    #--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"
    #----------------------------------------------------------------
    def search_fsm(curr_state,input_symbol,fsm_dict):
        for key in fsm_dict:
            if(key[0] == curr_state):
                if(key[1].search(input_symbol)):
                    return(fsm_dict[key])
                else:
                    pass
            else:
                pass
        return(None)
    curr_state = "INIT"
    prev_symbol = ''
    for i in range(0,line.__len__()):
        cursor = i
        input_symbol = line[i]
        temp = search_fsm(curr_state,input_symbol,fsm_dict)
        action = temp[0]
        if(action):
            si,ei,color_sec,color_sec_seq,colon_meeted = action(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol)
        else:
            pass
        curr_state = temp[1]
        prev_symbol = input_symbol
    #-------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"--------------------------------
    if(curr_state == "BYTES"):
        cursor = cursor + 1
        si,ei,color_sec,color_sec_seq,colon_meeted = do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol)
        curr_state = "INIT"
    #--------------fix issues caused by bytes such as {'a': b'a'} whose str is : "{'a': b'a'}"-------------------------------
    if(curr_state == "OTHER"):
        cursor = cursor + 1
        si,ei,color_sec,color_sec_seq,colon_meeted = do_close_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol)
        curr_state = "INIT"
    if(curr_state == "INIT"):
        cursor = cursor + 1
        if(is_op(input_symbol)):
            pass
        else:
            si,ei,color_sec,color_sec_seq,colon_meeted = do_open_var(cursor,si,ei,color_sec,color_sec_seq,colon_meeted,prev_symbol)
        curr_state = "INIT"
    return(color_sec)

#------------------------------------------
def get_dynamic_indent_j_str(j_str,**kwargs):
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
    if('block_op_pairs_dict' in kwargs):
        block_op_pairs_dict = kwargs['block_op_pairs_dict']
    else:
        block_op_pairs_dict=get_block_op_pairs('{}[]()')
    if('quotes_pairs_dict' in kwargs):
        quotes_pairs_dict = kwargs['quotes_pairs_dict']
    else:
        quotes_pairs_dict=get_quotes_pairs('""\'\'')
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
    if('save' in kwargs):
        save = kwargs['save']
    else:
        save = 0
    if('with_color' in kwargs):
        with_color = kwargs['with_color']
    else:
        with_color = 0
    if('fn' in kwargs):
        fn = kwargs['fn']
    else:
        if(with_color):
            fn = ''.join(('./',str(time.time())[:10],'_colored.js'))
        else:
            fn = ''.join(('./',str(time.time())[:10],'_plain.js'))
    if(with_color):
        if('key_color' in kwargs):
            key_color = kwargs['key_color']
        else:
            key_color=3
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=7
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=4
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=8
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=9
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
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    lps = get_print_lines_and_paths(j_str,sp=sp,block_op_pairs_dict=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps)
    lines = lps['lines']
    paths = lps['paths']
    if('end' in kwargs):
        end = kwargs['end']
    else:
        end = lines.__len__()-1
    if(end > lines.__len__()):
        end = lines.__len__()-1
    #-----------------------------------------careful  paths not escaped but lines escaped====>>>
    painted_lines = {}
    for i in range(start,end+1):
        line = lines[i]
        if(with_color):
            color_sec = get_line_color_sec(line,paths[i],block_op_pairs=block_op_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,sp=sp)
            painted_string = paint_str(line,color_sec=color_sec,colors=colors)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
            painted_string = html.unescape(painted_string)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
        else:
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
            painted_string = html.unescape(line)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
        #not implemented yet
        # if(fixed_indent):
           # indent_num = paths[i].split(sp).__len__()
           # curr_head_len = indent * indent_num
        # else:
        painted_lines[i] = painted_string
    rslt = ''
    for i in range(start,end+1):
        rslt =''.join((rslt,painted_lines[i],'\n'))
    if(save):
        fd =open(fn,'w')
        fd.write(rslt)
        fd.close()
    else:
        pass
    return(rslt)

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
            key_color=3
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=7
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=4
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=8
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=9
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
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    ######
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = get_quotes_pairs('{}[]()')
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    lps = get_print_lines_and_paths(j_str,sp=sp,block_op_pairs_dict=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps)
    lines = lps['lines']
    paths = lps['paths']
    if('end' in kwargs):
        end = kwargs['end']
    else:
        end = lines.__len__()-1
    if(end > lines.__len__()):
        end = lines.__len__()-1
    #-----------------------------------------careful  paths not escaped but lines escaped====>>>
    painted_lines = {}
    for i in range(start,end+1):
        line = lines[i]
        if(with_color):
            color_sec = get_line_color_sec(line,paths[i],block_op_pairs=block_op_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,sp=sp)
            painted_string = paint_str(line,color_sec=color_sec,colors=colors)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
            painted_string = html.unescape(painted_string)
            #-------fix issues--- when pobj({'resp_body_bytes': b'&#39;c'})
        else:
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
    ####
    if(display):
        for i in range(start,end+1):
            print(painted_lines[i])
    else:
        pass
    return(painted_lines)


beautify=get_dynamic_indent_j_str


def pobj(obj,**kwargs):
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
    if('block_op_pairs_dict' in kwargs):
        block_op_pairs_dict = kwargs['block_op_pairs_dict']
    else:
        block_op_pairs_dict=get_block_op_pairs('{}[]()')
    if('quotes_pairs_dict' in kwargs):
        quotes_pairs_dict = kwargs['quotes_pairs_dict']
    else:
        quotes_pairs_dict=get_quotes_pairs('""\'\'')
    ############
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
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
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent =0
    if('indent_bumber' in kwargs):
        indent_number = kwargs['indent_number']
    else:
        indent_number =4
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
            key_color=3
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=7
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=4
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=8
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=9
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
    else:
        pass
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    ##########
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = get_quotes_pairs('{}[]()')
    ############
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    ############1
    if('end' in kwargs):
        end = kwargs['end']
    else:
        end = 2**32
    if(utils.is_str(obj)):
        s = obj
    else:
        s = obj.__str__()
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent =0
    if(fixed_indent):
        opts = jb.default_options()
        opts.indent_size = indent_number
        print(jb.beautify(s,opts))
    else:
        if(with_color):
            print_j_str(s,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,with_color=with_color,block_op_pairs=block_op_pairs,quotes_pairs=quotes_pairs,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,display=1,start=start,end=end)
        else:
            print_j_str(s,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,with_color=with_color,block_op_pairs=block_op_pairs,quotes_pairs=quotes_pairs,start=start,end=end)








def pdir(obj,**kwargs):
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
        obj = obj[start:end]
    else:
        pass
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
    if('path_sps' in kwargs):
        path_sps = kwargs['path_sps']
    else:
        path_sps = ['/']
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
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent =0
    if('indent_bumber' in kwargs):
        indent_number = kwargs['indent_number']
    else:
        indent_number =4
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
            key_color=3
        if('value_color' in kwargs):
            value_color = kwargs['value_color']
        else:
            value_color=7
        if('list_ele_color' in kwargs):
            list_ele_color = kwargs['list_ele_color']
        else:
            list_ele_color=4
        if('op_color' in kwargs):
            op_color = kwargs['op_color']
        else:
            op_color=8
        if('default_color' in kwargs):
            default_color = kwargs['default_color']
        else:
            default_color=9
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
    else:
        pass
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    #if('quotes' in kwargs):
    #    quotes = kwargs['quotes']
    #else:
    #    quotes = ['"',"'"]
    ##########
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = get_quotes_pairs('{}[]()')
    ############
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    ############
    if('end' in kwargs):
        end = kwargs['end']
    else:
        end = 2**32
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent =0
    if(with_color):
        pobj(obj,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,display=1)
    else:
        pobj(obj,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,with_color=with_color,block_op_pairs=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict)

