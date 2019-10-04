



def get_quotes_pairs(pairs_str):
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




def get_lrquotes(quotes_pairs_dict):
    lquotes = []
    rquotes = []
    quotes = []
    for i in range(1,quotes_pairs_dict.__len__()+1):
        lquotes.append(quotes_pairs_dict[i][0])
        rquotes.append(quotes_pairs_dict[i][1])
        quotes.append(quotes_pairs_dict[i][0])
        quotes.append(quotes_pairs_dict[i][1])
    return((lquotes,rquotes,quotes))




