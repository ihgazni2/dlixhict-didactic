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
    ##########
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
        start = 0
    if('block_op_pairs' in kwargs):
        block_op_pairs = kwargs['block_op_pairs']
        if(utils.is_dict(block_op_pairs)):
            block_op_pairs_dict = block_op_pairs
        else:
            block_op_pairs_dict = get_block_op_pairs(block_op_pairs)
    else:
        block_op_pairs_dict = get_block_op_pairs('{}[]()')
    if('quotes_pairs' in kwargs):
        quotes_pairs = kwargs['quotes_pairs']
        if(utils.is_dict(quotes_pairs)):
            quotes_pairs_dict = quotes_pairs
        else:
            quotes_pairs_dict = get_quotes_pairs(quotes_pairs)
    else:
        quotes_pairs_dict = get_quotes_pairs('""\'\'')
    lps = get_print_lines_and_paths(j_str,sp=sp,block_op_pairs_dict=block_op_pairs_dict,quotes_pairs_dict=quotes_pairs_dict,spaces=spaces,colons=colons,commas=commas,line_sps=line_sps,path_sps=path_sps,fixed_indent=fixed_indent,indent=indent)
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
            color_sec = get_line_color_sec(line,paths[i],block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp)
            painted_string = paint(line,color_sec=color_sec,rtrn=True)
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
