


deepcopy and search  and creat_regex_from_arr   cost many time



####
sp = '/'
spaces = [' ','\t']
colons = [':']
commas = [',']
line_sps = ['\r','\n']
block_op_pairs_dict=get_block_op_pairs('{}[]()')
quotes_pairs_dict=get_quotes_pairs('""\'\'')
path_sps = ['/']
fixed_indent =0
indent =4



lines = lps['lines']
paths = lps['paths']

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
    
    
    
    
    
    
    
    
with_color= 1
start = 0 
end = lines.__len__()-1
key_color=KEY_COLOR
value_color=VALUE_COLOR
list_ele_color=LIST_ELE_COLOR
op_color=OP_COLOR
default_color=DEFAULT_COLOR

def tst():
    painted_lines = {}
    
    for i in range(start,end+1):
        line = lines[i]
        if(with_color):
            color_sec = get_line_color_sec(line,paths[i],block_op_pairs=block_op_pairs_dict,quotes_pairs=quotes_pairs_dict,key_color=key_color,value_color=value_color,list_ele_color=list_ele_color,op_color=op_color,default_color=default_color,spaces=spaces,colons=colons,commas=commas,line_sps = line_sps,path_sps = path_sps,sp=sp)
            painted_string = paint_str(line,color_sec=color_sec)
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
