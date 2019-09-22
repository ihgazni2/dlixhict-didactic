import random
import math
from xdict import utils
#####
def gen_random_ascii_chr():
    return(chr(math.floor(random.random() * 256 + 1) % 256))

def gen_random_ascii_str(length):
    rslt = ""
    for i in range(0,length):
        rslt = rslt + gen_random_ascii_chr()
    return(rslt)


def gen_random_str_of_length(length,**kwargs):
    '''JZ._$'''
    if('char_set' in kwargs):
        char_set = kwargs['char_set']
    else:
        char_set = "0123456789abcdefghijklmnopqrstuvwxyz"
    rslt = ''
    for i in range(0,length):
        seq = math.floor(random.random()*36+1) % 36
        c = char_set[seq]
        rslt = rslt + c
    return(rslt)



######
def gen_random_word(**kwargs):
    if('max_word_length' in kwargs):
        max_word_length = kwargs['max_word_length']
    else:
        max_word_length = 10
    length_range = random.randrange(max_word_length+1)
    if('char_set' in kwargs):
        char_set = kwargs['char_set']
    else:
        char_set = 'abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if('fixed_word_length' in kwargs):
        length_range = kwargs['fixed_word_length']
    else:
        pass
    len = char_set.__len__()
    word = ''
    for i in range(length_range):
        word = ''.join((word,char_set[random.randrange(len)]))
    return(word)

def gen_random_root():
    rand_num = random.randrange(3)
    if(rand_num == 0):
        return({})
    elif(rand_num == 1):
        return([])
    elif(rand_num == 2):
        return(())
    else:
        return({})

def gen_random_type_via_ratio(**kwargs):
    if('d' in kwargs):
        rd = kwargs['d']
    else:
        rd = 0
    if('l' in kwargs):
        rl = kwargs['l']
    else:
        rl = 0
    if('t' in kwargs):
        rt = kwargs['t']
    else:
        rt = 0
    if('s' in kwargs):
        rs = kwargs['s']
    else:
        rs = 0
    if('v' in kwargs):
        rv = kwargs['v']
    else:
        rv = 0
    if((rd+rl+rt+rs+rv) == 0):
        rd = 1
        rl = 1
        rt = 1
        rs = 1
        rv = 1
    total = rd + rl + rt + rs + rv 
    rand_num = random.randrange(1,total+1)
    bd = rd + 1
    bl = bd + rl
    bt = bl + rt
    bs = bt + rs
    bv = bs + rv
    if(rand_num in range(1,bd)):
        return('d')
    elif(rand_num in range(bd,bl)):
        return('l')
    elif(rand_num in range(bl,bt)):
        return('t')
    elif(rand_num in range(bt,bs)):
        return('s')
    elif(rand_num in range(bs,bv)):
        return('v')

def gen_random_depth(min_dep,max_dep):
    rand_num = random.randrange(min_dep,max_dep+1)
    return(rand_num)

def gen_random_siblings_size(min_size,max_size):
    rand_num = random.randrange(min_size,max_size+1)
    return(rand_num)

def gen_random_prefix_array(prefix,size,max_word_length=10):
    l = []
    for i in range(0,size):
        l.append(i)
    new_l = []
    while(l.__len__()>0):
        rand_num = random.randrange(0,l.__len__())
        ele = l.pop(rand_Num)
        ele = ''.join((prefix,'_',str(ele+1),'_',gen_random_word(max_word_length)))
        new_L.append(ele)
    return(new_l)

def gen_random_prefix_array(prefix,size,max_word_length=10):
    l = []
    for i in range(0,size):
        l.append(i)
    new_l = []
    while(l.__len__()>0):
        rand_num = random.randrange(0,l.__len__())
        ele = l.pop(rand_num)
        ele = ''.join((prefix,'_',str(ele+1),'_',gen_random_word(max_word_length=max_word_length)))
        new_l.append(ele)
    return(new_l)

def gen_random_fixed_word_length_prefix_array(prefix,size,fixed_word_length=10):
    l = []
    for i in range(0,size):
        l.append(i)
    new_l = []
    while(l.__len__()>0):
        rand_num = random.randrange(0,l.__len__())
        ele = l.pop(rand_num)
        ele = ''.join((prefix,'_',str(ele+1),'_',gen_random_word(fixed_word_length=fixed_word_length)))
        new_l.append(ele)
    return(new_l)

def gen_possible_leaf(data_type,max_value_seq):
    if(data_type=='d'):
        return({})
    elif(data_type=='l'):
        return([])
    elif(data_type=='t'):
        return(())
    elif(data_type=='s'):
        return(set({}))
    else:
        rand_num = random.randrange(1,max_value_seq+1)
        value = ''.join(('v','_',str(rand_num)))
        return(value)

def gen_children(recursive,**kwargs):
    if('max_value_seq' in kwargs):
        max_value_seq = kwargs['max_value_seq']
    else:
        max_value_seq = 8
    if('max_siblings' in kwargs):
        max_siblings = kwargs['max_siblings']
    else:
        max_siblings = 19
    if('d' in kwargs):
        rd = kwargs['d']
    else:
        rd = 5
    if('l' in kwargs):
        rl = kwargs['l']
    else:
        rl = 5
    if('t' in kwargs):
        rt = kwargs['t']
    else:
        rt = 1
    if('s' in kwargs):
        rs = kwargs['s']
    else:
        rs = 1
    if('v' in kwargs):
        rv = kwargs['v']
    else:
        rv = 25
    max_siblings = gen_random_siblings_size(1,max_siblings+1)
    if(utils.is_list(recursive)):
        for i in range(0,max_siblings):
            data_type = gen_random_type_via_ratio(d=rd,l=rl,t=rt,s=rs,v=rv)
            next = gen_possible_leaf(data_type,max_value_seq)
            recursive.append(next)
    elif(utils.is_tuple(recursive)):
        temp = list(recursive)
        for i in range(0,max_siblings):
            data_type = gen_random_type_via_ratio(d=rd,l=rl,t=rt,s=rs,v=rv)
            next = gen_possible_leaf(data_type,max_value_seq)
            temp.append(next)
        recursive = tuple(temp)
    elif(utils.is_set(recursive)):
        for i in range(0,max_siblings):
            data_type = gen_random_type_via_ratio(d=0,l=0,t=0,s=0,v=rv)
            next = gen_possible_leaf(data_type,max_value_seq)
            recursive.add(next)
    if(utils.is_dict(recursive)):
        keys = gen_random_prefix_array('key',max_siblings)
        for i in range(0,max_siblings):
            data_type = gen_random_type_via_ratio(d=rd,l=rl,t=rt,s=rs,v=rv)
            next = gen_possible_leaf(data_type,max_value_seq)
            recursive[keys[i]] = next
    else:
        pass
    return(recursive)


def gen_random_recursive_data(**kwargs):
    # tuple can only be leaf , coz tuple mechanism is a little different
    if('max_depth' in kwargs):
        max_depth = kwargs['max_depth']
    else:
        max_depth = 6
    if('root' in kwargs):
        if(utils.is_recursive_type(kwargs['root'])):
            root = kwargs['root']
            try:
                root.clear()
            except:
                root = ()
            else:
                pass
        else:
            root = gen_random_root()
    else:
        root = gen_random_root()
    unhandled = [root] 
    if(utils.is_tuple(root)):
        root = unhandled
        root_is_tuple = 1
    else:
        root_is_tuple = 0
    lv = -1
    while(lv<max_depth):
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            if(utils.is_recursive_type(unhandled[i])):
                unhandled[i] = gen_children(unhandled[i])
                if(utils.is_dict(unhandled[i])):
                    for key in unhandled[i]:
                        v = unhandled[i][key]
                        if(utils.is_recursive_type(v)):
                            next_unhandled.append(v)
                elif(utils.is_list(unhandled[i])):
                    for j in range(0,unhandled[i].__len__()):
                        v = unhandled[i][j]
                        if(utils.is_recursive_type(v)):
                            next_unhandled.append(v)
                elif(utils.is_tuple(unhandled[i])):
                    for j in range(0,unhandled[i].__len__()):
                        v = unhandled[i][j]
                        if(utils.is_recursive_type(v)):
                            next_unhandled.append(v)
                else:
                    pass
            else:
                pass
        unhandled = next_unhandled
        lv=lv+1
    if(root_is_tuple):
        root = root[0]
    else:
        pass
    return(root)



def gen_random_recursive_only_dict_data(**kwargs):
    if('d' in kwargs):
        rd = kwargs['d']
    else:
        rd = 1
    if('v' in kwargs):
        rv = kwargs['v']
    else:
        rv = 5
    if('max_depth' in kwargs):
        max_depth = kwargs['max_depth']
    else:
        max_depth = 6
    root = {}
    unhandled = [root] 
    lv = -1
    while(lv<max_depth):
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            if(utils.is_recursive_type(unhandled[i])):
                unhandled[i] = gen_children(unhandled[i],d=rd,l=0,t=0,s=0,v=rv)
                for key in unhandled[i]:
                    v = unhandled[i][key]
                    if(utils.is_recursive_type(v)):
                        next_unhandled.append(v)
            else:
                pass
        unhandled = next_unhandled
        lv=lv+1
    return(root)
    

def gen_random_recursive_only_list_data(**kwargs):
    if('l' in kwargs):
        rl = kwargs['l']
    else:
        rl = 1
    if('v' in kwargs):
        rv = kwargs['v']
    else:
        rv = 5
    if('max_depth' in kwargs):
        max_depth = kwargs['max_depth']
    else:
        max_depth = 6
    root = []
    unhandled = [root]
    lv = -1
    while(lv<max_depth):
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            if(utils.is_recursive_type(unhandled[i])):
                unhandled[i] = gen_children(unhandled[i],d=0,l=rl,t=0,s=0,v=rv)
                for j in range(0,unhandled[i].__len__()):
                    v = unhandled[i][j]
                    if(utils.is_recursive_type(v)):
                        next_unhandled.append(v)
            else:
                pass
        unhandled = next_unhandled
        lv=lv+1
    return(root)



def gen_cowrol_table(total_rows,total_cols):
    matrix = {}
    for i in range(0,total_rows):
        matrix[i] = {}
        for j in range(0,total_cols):
            matrix[i][j] = gen_random_word()
    return(matrix)


################
################

import efuntool.efuntool as eftl
import random
import elist.elist as elel

def get_rand_name(**kwargs):
    dflt_init_chars = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dflt_other_chars = "_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lngth = eftl.dflt_kwargs("len",4,**kwargs)
    init_chs = eftl.dflt_kwargs("init",dflt_init_chars,**kwargs)
    other_chs = eftl.dflt_kwargs("other",dflt_other_chars,**kwargs)
    init_ch =  random.choice(init_chs)
    others = random.choices(other_chs,k=lngth-1)
    other  = elel.join(others,"")
    return(init_ch +other)
