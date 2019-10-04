from xdict.quote import get_quotes_pairs,get_lrquotes
from xdict.block import get_block_op_pairs
from xdict import escape
from xdict import fsm
import xdict.quote as quote
import xdict.block as block
import re
import efuntool.efuntool as eftl


def get_jdict_token_set(**kwargs):
    '''
        from xdict.jprint import get_jdict_token_set
        get_jdict_token_set(quotes_pairs_dict={1: ('"', '"'), 2: ("<", ">")})
    '''
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs("block_op_pairs_dict",block.get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs("quotes_pairs_dict",quote.get_quotes_pairs('""\'\''),**kwargs)
    lquotes,rquotes,quotes = quote.get_lrquotes(quotes_pairs_dict)
    path_sps = eftl.dflt_kwargs("path_sps",['/'])
    #######
    d = {}
    s = set({})
    def add_bi_table(s,d,x):
        for each in x:
            k = each
            v = escape.html_number_escape_str(k)
            d[k] = v
            d[v] = k
            s.add(k)
    add_bi_table(s,d,spaces)
    add_bi_table(s,d,colons)
    add_bi_table(s,d,commas)
    add_bi_table(s,d,line_sps)
    add_bi_table(s,d,lquotes)
    add_bi_table(s,d,rquotes)
    add_bi_table(s,d,path_sps)
    for i in range(1,block_op_pairs_dict.__len__()+1):
        s.add(block_op_pairs_dict[i][0])
        s.add(block_op_pairs_dict[i][1])
        recover_token_l = escape.html_number_escape_str(block_op_pairs_dict[i][0])
        recover_token_r = escape.html_number_escape_str(block_op_pairs_dict[i][1])
        d[block_op_pairs_dict[i][0]] = recover_token_l
        d[block_op_pairs_dict[i][1]] = recover_token_r
        d[recover_token_l] = block_op_pairs_dict[i][0]
        d[recover_token_r] = block_op_pairs_dict[i][1]
    return({'token_set':s,'replace_ref_dict':d})



def prepare_quotes_token_machine(j_str,**kwargs):
    '''
        >>> from xdict.jprint import convert_token_in_quote
        >>> from xdict.jprint import help
        >>> 
        >>> convert_token_in_quote('"a b":"cd"')
        '"a&#32;b":"cd"'
        >>> import html
        >>> html.unescape('"a&#32;b":"cd"')
        '"a b":"cd"'
        >>> convert_token_in_quote('"a b":cd')
        '"a&#32;b":cd'
        >>> 
        >>> #help(convert_token_in_quote)
        convert_token_in_quote('<a b>:"cd"',quotes_pairs_dict={1: ('"', '"'), 2: ("<", ">")})
        '<a&#32;b>:"cd"'
    '''
    ####
    spaces = eftl.dflt_kwargs("spaces",[' ','\t'],**kwargs)
    colons = eftl.dflt_kwargs("colons",[':'],**kwargs)
    commas = eftl.dflt_kwargs("commas",[','],**kwargs)
    line_sps = eftl.dflt_kwargs("line_sps",['\r','\n'],**kwargs)
    block_op_pairs_dict = eftl.dflt_kwargs("block_op_pairs_dict",get_block_op_pairs('{}[]()'),**kwargs)
    quotes_pairs_dict = eftl.dflt_kwargs("quotes_pairs_dict",get_quotes_pairs('""\'\''),**kwargs)
    lquotes,rquotes,quotes = get_lrquotes(quotes_pairs_dict)
    path_sps = eftl.dflt_kwargs("path_sps",['/'])
    ####
    temp = get_jdict_token_set(**kwargs)
    token_set = temp['token_set']
    replace_ref_dict = temp['replace_ref_dict']
    ####
    # ----------------------------------------------------------------- #
    ####
    def do_replace(ch):
        if(ch in token_set):
            ch = replace_ref_dict[ch]
        return(ch)
    def do_throw(curr_state,trigger_checker,input_symbol):
        msg = "curr_state: " + curr_state + "\n"
        msg = msg + "trigger_checker: "+trigger_checker.__str__() + "\n"
        msg = msg + "input_symbol: "+ input_symbol.__str__() + "\n"
        msg = msg + "triggered ERROR" + "\n"
        raise Exception(msg)
    ####
    machine = fsm.FSM()
    regex_lquotes = fsm.creat_regex_from_arr(lquotes)
    regex_rquotes = fsm.creat_regex_from_arr(rquotes) 
    regex_b = re.compile('b')
    regex_spaces = fsm.creat_regex_from_arr(spaces)
    regex_colons = fsm.creat_regex_from_arr(colons)
    regex_commas = fsm.creat_regex_from_arr(commas)
    regex_slash = re.compile("\\\\")
    ######
    ops = []
    for i in range(1,block_op_pairs_dict.__len__()+1):
        ops.append(block_op_pairs_dict[i][0])
        ops.append(block_op_pairs_dict[i][1])
    ######
    regex_ops = fsm.creat_regex_from_arr(ops)
    LqRqBSpColComSlOp_arr = ['b','\\\\']
    LqRqBSpColComSlOp_arr = LqRqBSpColComSlOp_arr + lquotes + rquotes + spaces + colons+commas + ops
    regex_not_LqRqBSpColComSlOp = fsm.creat_regex_not_from_arr(LqRqBSpColComSlOp_arr) 
    # ############################
    # ############################
    machine.add("INIT",regex_b,None,"BYTES")
    machine.add("INIT",regex_spaces,None,"INIT")
    machine.add("INIT",regex_ops,None,"INIT")
    machine.add("INIT",regex_colons,None,"INIT")
    machine.add("INIT",regex_commas,None,"INIT")
    machine.add("INIT",regex_slash,None,"SLASHINIT")
    machine.add("INIT",regex_not_LqRqBSpColComSlOp,do_replace,"OTHER")
    ####
    machine.add("BYTES",regex_b,None,"OTHER")
    machine.add("BYTES",regex_spaces,None,"BYTES")
    machine.add("BYTES",regex_ops,None,"INIT")
    machine.add("BYTES",regex_colons,None,"INIT")
    machine.add("BYTES",regex_commas,None,"INIT")
    machine.add("BYTES",regex_slash,None,"SLASHBYTES")
    machine.add("BYTES",regex_not_LqRqBSpColComSlOp,do_replace,"OTHER")
    ####
    machine.add("SLASHINIT",re.compile("."),do_replace,"OTHER")
    ####
    machine.add("SLASHBYTES",re.compile("."),do_replace,"OTHER")
    ####
    machine.add("OTHER",regex_b,None,"OTHER")
    machine.add("OTHER",regex_spaces,None,"OTHER")
    machine.add("OTHER",regex_ops,None,"INIT")
    machine.add("OTHER",regex_colons,None,"INIT")
    machine.add("OTHER",regex_commas,None,"INIT")
    machine.add("OTHER",regex_slash,None,"SLASHOTHER")
    machine.add("OTHER",regex_not_LqRqBSpColComSlOp,do_replace,"OTHER")
    ####
    machine.add("SLASHOTHER",re.compile("."),do_replace,"OTHER")
    ####
    regex_lquote_array = fsm.creat_regexes_array(lquotes)
    regex_rquote_array = fsm.creat_regexes_array(rquotes)
    ###@@@@@@@@@@@@@@@
    for i in range(0,lquotes.__len__()):
        ####INIT -lq_n-> LQ_n
        sn = ''.join(("LQ",'_',str(i)))
        machine.add("INIT",regex_lquote_array[i],None,sn)
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
        machine.add("BYTES",regex_lquote_array[i],None,sn)
    for i in range(0,rquotes.__len__()):
        ####BYTES -rq_n-> ERROR
        if(rquotes[i] == lquotes[i]):
            pass
        else:
            sn = ''.join(("LQ",'_',str(i)))
            machine.add("BYTES",regex_rquote_array[i],do_throw,'ERROR')
    ####
    for i in range(0,lquotes.__len__()):
        ####OTHER -lq_n-> LQ_n
        sn = ''.join(("LQ",'_',str(i)))
        machine.add("OTHER",regex_lquote_array[i],None,sn)
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
        ####LQ_n -rq_n-> READY
        machine.add(sn,regex_rquote_array[i],None,'INIT')
        #####LQ_n -b-> LQ_n
        machine.add(sn,regex_b,None,sn)
        #####LQ_n -spaces-> LQ_n
        machine.add(sn,regex_spaces,do_replace,sn)
        #####LQ_n -ops-> LQ_n
        machine.add(sn,regex_ops,do_replace,sn)
        ####LQ_n -colons-> LQ_n
        machine.add(sn,regex_colons,do_replace,sn)
        ####LQ_n -commas-> LQ_n
        machine.add(sn,regex_commas,do_replace,sn)
        #####LQ_n -slash -> SLASHLQ_n
        slashlq = ''.join(("SLASHLQ",'_',str(i)))
        machine.add(sn,re.compile("\\\\"),None,slashlq)
        ####SLASHLQ_n -any-> LQ_n
        machine.add(slashlq,re.compile("."),do_replace,sn)
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
        machine.add(sn,tmp_regex,do_replace,sn)
    ####
    machine.orig_str = j_str
    machine.do_replace = do_replace
    machine.do_throw = do_throw
    ####
    return(machine)
