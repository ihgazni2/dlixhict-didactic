import re
from xdict import block
import copy
from xdict.regextool import *


def format_j_str(j_str,block_op_pairs_dict=block.get_block_op_pairs('{}[]()'),**kwargs):
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
    colon_and_sps = copy.copy(colons)
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
    # such as {} [] ()
    for i in range(1,block_op_pairs_dict.__len__()+1):
        j_str = j_str.replace(
            ''.join((block_op_pairs_dict[i][0],'\n',block_op_pairs_dict[i][1])),
            ''.join((block_op_pairs_dict[i][0],block_op_pairs_dict[i][1]))
        )
    # format step 6: 
    j_str = j_str.replace("\n,",",")
    j_str = j_str.strip("\n")
    j_str = j_str.replace("\n\n","\n")
    return(j_str)
