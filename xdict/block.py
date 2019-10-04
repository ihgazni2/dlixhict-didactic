def get_block_op_pairs(pairs_str):
    '''
        # operators ,such as {} [] ()  ......could be user-defined
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


def is_non_ordered_op(ch,
        block_op_pairs_dict=get_block_op_pairs('{}[]()'),
        block_non_ordered_op_pairs_dict=get_block_op_pairs('{}')):
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



