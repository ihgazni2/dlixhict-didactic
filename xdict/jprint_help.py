def help(fname=None):
    if(fname == None):
        print('''html_number_escape_char(ch)''')
        print('''html_number_escape_str(s)''')
        print('''get_block_op_pairs(pairs_str)''')
        print('''get_jdict_token_set(**kwargs)''')
        print('''convert_token_in_quote(j_str,**kwargs)''')
        print('''format_j_str(j_str,block_op_pairs_dict=get_block_op_pairs('{}[]()'),**kwargs)''')
        print('''is_lop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''is_rop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''is_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''which_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''is_op_pair(ch1,ch2,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''is_ordered_op_pair(ch1,ch2,block_op_pairs_dict=get_block_op_pairs('{}[]()'))''')
        print('''is_comma(ch,commas=[','])''')
        print('''is_colon(ch,colons=[':'])''')
        print('''is_non_ordered_op(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()'),block_non_ordered_op_pairs_dict=get_block_op_pairs('{}'))''')
        print('''get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()"))''')
        print('''get_j_str_lvs_dict(j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()"))''')
        print('''get_line_start_index_in_j_str(orig_lines)''')
        print('''line_to_path_init(line,block_op_pairs_dict = get_block_op_pairs("{}[]()"),sp='/',commas=[','],colons=[':'])''')
        print('''line_to_path(line,curr_lv,prev_lv,prev_path,block_op_pairs_dict= get_block_op_pairs("{}[]()"),sp='/',commas=[','],colons=[':'])''')
        print('''get_print_lines_and_paths(j_str,**kwargs)''')
        print('''get_line_color_sec(line,path,**kwargs)''')
        print('''get_dynamic_indent_j_str(j_str,**kwargs)''')
        print('''print_j_str(j_str,**kwargs)''')
        print('''pobj(obj,**kwargs)''')
        print('''pdir(obj,**kwargs)''')
    elif(fname == "get_block_op_pairs"):
        info = '''PARAMS: pairs_str = "{}[]()"
                  EXEC:   get_block_op_pairs(pairs_str)
                  RESULT: {
                              1: ('{', '}'), 
                              2: ('[', ']'), 
                              3: ('(', ')')
                          }
               '''
        print(info)
        return(True)
    elif(fname == "get_jdict_token_set"):
        info = '''get_jdict_token_set(
                   spaces = [' ','\t'],
                   colons = [':'],
                   commas = [','],
                   path_sps = ['/'],
                   line_sps = ['\r','\n'],
                   block_op_pairs_dict={1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')')},
                   quotes_pairs_dict={1: ('"', '"'), 2: ("'", "'")}
                   )
               '''
        print(info)
        return(True)
    elif(fname == "convert_token_in_quote"):
        info = '''convert_token_in_quote(       
                   spaces = [' ','\t'],
                   colons = [':'],
                   commas = [','],
                   path_sps = ['/'],
                   line_sps = ['\r','\n'],
                   block_op_pairs_dict={1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')')},
                   quotes_pairs_dict={1: ('"', '"'), 2: ("'", "'")}
                   )
                '''
        print(info)
        return(True)
    else:
        print("NOT founded")
        #edit distance
        return(False)
