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

