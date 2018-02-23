import copy
from operator import itemgetter

def append(ol,ele,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        append(ol,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = append(ol,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.append(ele)
        return(new)
    else:
        ol.append(ele)
        return(ol)

def append_some(ol,*eles,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        append_some(ol,5,6,7,8,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = append_some(ol,5,6,7,8)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(extend(ol,list(eles),mode=mode))

def extend(ol,nl,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        extend(ol,nl,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        new = extend(ol,nl)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        cpnl = copy.deepcopy(nl)
        new.extend(cpnl)
        return(new)
    else:
        ol.extend(nl)
        return(ol)

def deepcopy(ol):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        new = deepcopy(ol)
        new
        id(new)
    '''
    return(copy.deepcopy(ol))

def prextend(ol,nl,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        id(nl)
        prextend(ol,nl,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        id(nl)
        new = prextend(ol,nl)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(nl)
        cpol = copy.deepcopy(ol)
        new.extend(cpol)
        return(new)
    else:
        length = ol.__len__()
        nl_len = nl.__len__()
        for i in range(0,nl_len):
            ol.append(None)
        for i in range(length-1,-1,-1):
            ol[i+nl_len] = ol[i]
        for i in range(0,nl_len):
            ol[i] = nl[i]
        return(ol)

def prepend(ol,ele,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        prepend(ol,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = prepend(ol,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = [ele]
        cpol = copy.deepcopy(ol)
        new.extend(cpol)
        return(new)
    else:
        length = ol.__len__()
        ol.append(None)
        for i in range(length-1,-1,-1):
            ol[i+1] = ol[i]
        ol[0] = ele
        return(ol)

def prepend_some(ol,*eles,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        prepend_some(ol,5,6,7,8,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = prepend_some(ol,5,6,7,8)
        new
        id(new)
        #####unshift is the same as prepend_some
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(prextend(ol,list(eles),mode=mode))

unshift = prepend_some

def uniform_index(index,length):
    '''
        uniform_index(0,3)
        uniform_index(-1,3)
        uniform_index(-4,3)
        uniform_index(-3,3)
        uniform_index(5,3)
    '''
    if(index<0):
        rl = length+index
        if(rl<0):
            index = 0
        else:
            index = rl
    elif(index>=length):
        index = length
    else:
        index = index
    return(index)

def insert(ol,start_index,ele,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        insert(ol,2,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = insert(ol,2,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        length = ol.__len__()
        cpol = copy.deepcopy(ol)
        si = uniform_index(start_index,length)
        new = copy.deepcopy(cpol[0:si])
        new.append(ele)
        new.extend(cpol[si:])
        return(new)
    else:
        ol.insert(start_index,ele)
        return(ol)

def insert_some(ol,*eles,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        insert_some(ol,5,6,7,8,index=2,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = insert_some(ol,5,6,7,8,index=2)
        new
        id(new)
    '''
    start_index = kwargs['index']
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    if(mode == "new"):
        si = uniform_index(start_index,length)
        new = copy.deepcopy(cpol[0:si])
        new.extend(list(eles))
        new.extend(cpol[si:])
        return(new)
    else:
        si = uniform_index(start_index,length)
        new = cpol[0:si]
        new.extend(list(eles))
        new.extend(cpol[si:])
        ol.clear()
        for i in range(0,new.__len__()):
            ol.append(new[i])
        return(ol)

def sorted_refer_to(l,referer,reverse=False,**kwargs):
    '''
        from xdict.elist import *
        l = ["a","b","c"]
        referer = [7,8,6]
        sorted_refer_to(l,referer)
        {'list': ['c', 'a', 'b'], 'referer': [6, 7, 8]}
        l
        referer
        >>>
    '''
    if("mode" in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "both"
    tl =[]
    length = l.__len__()
    for i in range(0,length):
        ele = (l[i],referer[i])
        tl.append(ele)
    tl = sorted(tl,key=itemgetter(1),reverse=reverse)
    sorted_l =[]
    sorted_r = []
    for i in range(0,length):
        sorted_l.append(tl[i][0])
        sorted_r.append(tl[i][1])
    if(mode == "only-list"):
        return(sorted_l)
    elif(mode == "only-referer"):
        return(referer)
    else:
        return({"list":sorted_l,"referer":sorted_r})

def insert_many(ol,eles,locs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4,5]
        eles = [7,77,777]
        locs = [0,2,4]
        id(ol)
        new = insert_many(ol,eles,locs)
        ol
        new
        id(new)
        ####
        ol = [1,2,3,4,5]
        eles = [7,77,777]
        locs = [0,2,4]
        id(ol)
        rslt = insert_many(ol,eles,locs,mode="original")
        ol
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    eles = copy.deepcopy(eles)
    locs = copy.deepcopy(locs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,locs.__len__()):
        if(locs[i]>=length):
            pass
        else:
            locs[i] = uniform_index(locs[i],length)
    tmp = sorted_refer_to(eles,locs)
    eles = tmp['list']
    locs = tmp['referer']
    label = eles.__len__()
    si = 0
    ei = 0
    for i in range(0,locs.__len__()):
        if(locs[i]>=length):
            label = i
            break
        else:
            ei = locs[i]
            new.extend(cpol[si:ei])
            new.append(eles[i])
            si = ei
    for i in range(label,locs.__len__()):
        new.append(eles[i])
    new.extend(cpol[ei:])
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def index_first(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_first(ol,'a')
        ####index_first, array_index, indexOf  are the same
    '''
    return(ol.index('a'))

array_index = index_first
indexOf = index_first

def index_firstnot(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_firstnot(ol,'a')
        ####index_firstnot, array_indexnot, indexOfnot  are the same
    '''
    length = ol.__len__()
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            return(i)
    return(None)

array_indexnot = index_firstnot
indexOfnot = index_firstnot

def index_last(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_last(ol,'a')
        ####lastIndexOf is the same as index_last
    '''
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        if(value == ol[i]):
            return(i)
        else:
            pass
    return(None)

lastIndexOf = index_last

def index_lastnot(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_lastnot(ol,'a')
        ####lastIndexOfnot is the same as index_lastnot
    '''
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        if(value == ol[i]):
            pass
        else:
            return(i)
    return(None)

lastIndexOfnot = index_lastnot


def index_which(ol,value,which):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_which(ol,'a',0)
        index_which(ol,'a',1)
        index_which(ol,'a',2)
        index_which(ol,'a',3) == None
    '''
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            seq = seq + 1
            if(seq == which):
                return(i)
            else:
                pass
        else:
            pass
    return(None)

def index_whichnot(ol,value,which):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_whichnot(ol,'a',0)
        index_whichnot(ol,'a',1)
        index_whichnot(ol,'a',2)
    '''
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            seq = seq + 1
            if(seq == which):
                return(i)
            else:
                pass
    return(None)

def indexes_all(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_all(ol,'a')
    '''
    length = ol.__len__()
    indexes =[]
    for i in range(0,length):
        if(value == ol[i]):
            indexes.append(i)
        else:
            pass
    return(indexes)

def indexes_allnot(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_allnot(ol,'a')
    '''
    length = ol.__len__()
    indexes =[]
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            indexes.append(i)
    return(indexes)

def indexes_some(ol,value,*seqs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_some(ol,'a',0,2)
        indexes_some(ol,'a',0,1)
        indexes_some(ol,'a',1,2)
        indexes_some(ol,'a',3,4)
    '''
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
        else:
            pass
    return(indexes)

def indexes_somenot(ol,value,*seqs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_somenot(ol,'a',0,2)
        indexes_somenot(ol,'a',0,1)
        indexes_somenot(ol,'a',1,2)
        indexes_somenot(ol,'a',3,4)
    '''
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
    return(indexes)

def indexes_seqs(ol,value,seqs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_seqs(ol,'a',{0,2})
        indexes_seqs(ol,'a',{0,1})
        indexes_seqs(ol,'a',{1,2})
        indexes_seqs(ol,'a',{3,4})
    '''
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
        else:
            pass
    return(indexes)

def indexes_seqsnot(ol,value,seqs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        indexes_seqsnot(ol,'a',{0,2})
        indexes_seqsnot(ol,'a',{0,1})
        indexes_seqsnot(ol,'a',{1,2})
        indexes_seqsnot(ol,'a',{3,4})
    '''
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
    return(indexes)

def first_continuous_indexes_slice(ol,value):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        first_continuous_indexes_slice(ol,"a")
    '''
    length = ol.__len__()
    begin = None
    slice = []
    for i in range(0,length):
        if(ol[i]==value):
            begin = i
            break
        else:
            pass
    if(begin == None):
        return(None)
    else:
        slice.append(begin)
        for i in range(begin+1,length):
            if(ol[i]==value):
                slice.append(i)
            else:
                break
    return(slice)

def first_continuous_indexesnot_slice(ol,value):
    '''
        from xdict.elist import *
        ol = ["a",0,1,"a","a",2,3,"a",4,"a","a","a",5]
        first_continuous_indexesnot_slice(ol,"a")
    '''
    length = ol.__len__()
    begin = None
    slice = []
    for i in range(0,length):
        if(not(ol[i]==value)):
            begin = i
            break
        else:
            pass
    if(begin == None):
        return(None)
    else:
        slice.append(begin)
        for i in range(begin+1,length):
            if(not(ol[i]==value)):
                slice.append(i)
            else:
                break
    return(slice)

def last_continuous_indexes_slice(ol,value):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        last_continuous_indexes_slice(ol,"a")
    '''
    length = ol.__len__()
    end = None
    slice = []
    for i in range(length-1,-1,-1):
        if(ol[i]==value):
            end = i
            break
        else:
            pass
    if(end == None):
        return(None)
    else:
        slice.append(end)
        for i in range(end-1,-1,-1):
            if(ol[i]==value):
                slice.append(i)
            else:
                break
    slice.reverse()
    return(slice)

def last_continuous_indexesnot_slice(ol,value):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        last_continuous_indexesnot_slice(ol,"a")
    '''
    length = ol.__len__()
    end = None
    slice = []
    for i in range(length-1,-1,-1):
        if(not(ol[i]==value)):
            end = i
            break
        else:
            pass
    if(end == None):
        return(None)
    else:
        slice.append(end)
        for i in range(end-1,-1,-1):
            if(not(ol[i]==value)):
                slice.append(i)
            else:
                break
    slice.reverse()
    return(slice)

def which_continuous_indexes_slice(ol,value,which):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        which_continuous_indexes_slice(ol,"a",0)
        which_continuous_indexes_slice(ol,"a",1)
        which_continuous_indexes_slice(ol,"a",2)
        which_continuous_indexes_slice(ol,"a",3)
        which_continuous_indexes_slice(ol,"b",0)
    '''
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
            cursor = cursor + 1
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
            cursor = cursor + 1
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq == which):
                return(slice)
            else:
                cursor = cursor + 1
                begin = None
                slice = []
        else:
            cursor = cursor + 1
    if(slice):
        seq = seq + 1
    else:
        pass
    if(seq == which):
        return(slice)
    else:
        return([])

def which_continuous_indexesnot_slice(ol,value,which):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        which_continuous_indexesnot_slice(ol,"a",0)
        which_continuous_indexesnot_slice(ol,"a",1)
        which_continuous_indexesnot_slice(ol,"a",2)
        which_continuous_indexesnot_slice(ol,"a",3)
        which_continuous_indexesnot_slice(ol,"b",0)
    '''
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
            cursor = cursor + 1
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
            cursor = cursor + 1
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq == which):
                return(slice)
            else:
                cursor = cursor + 1
                begin = None
                slice = []
        else:
            cursor = cursor + 1
    if(slice):
        seq = seq + 1
    else:
        pass
    if(seq == which):
        return(slice)
    else:
        return([])

def some_continuous_indexes_slices(ol,value,*seqs):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        some_continuous_indexes_slices(ol,"a",0,2)
    '''
    seqs = list(seqs)
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def some_continuous_indexesnot_slices(ol,value,*seqs):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        some_continuous_indexesnot_slices(ol,"a",0,2)
    '''
    seqs = list(seqs)
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def seqs_continuous_indexes_slices(ol,value,seqs):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        seqs_continuous_indexes_slices(ol,"a",{0,2})
    '''
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def seqs_continuous_indexesnot_slices(ol,value,seqs):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        seqs_continuous_indexesnot_slices(ol,"a",{0,2})
    '''
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def all_continuous_indexes_slices(ol,value):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        all_continuous_indexes_slices(ol,"a")
    '''
    rslt = []
    length = ol.__len__()
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            rslt.append(slice)
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def all_continuous_indexesnot_slices(ol,value):
    '''
        from xdict.elist import *
        ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
        all_continuous_indexesnot_slices(ol,"a")
    '''
    rslt = []
    length = ol.__len__()
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            rslt.append(slice)
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)

def pop(ol,index,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        rslt = pop(ol,2)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = pop(ol,2,mode="original")
        rslt
        ol
        id(ol)
    '''
    index = uniform_index(index,ol.__len__())
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        popped = new.pop(index)
        return({'popped':popped,'list':new})
    else:
        popped = ol.pop(index)
        return(popped)

def pop_range(ol,start_index,end_index,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_range(ol,2,4)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_range(ol,2,4,mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    start_index = uniform_index(start_index,length)
    end_index = uniform_index(end_index,length)
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,start_index):
            new.append(cpol[i])
        for i in range(start_index,end_index):
            popped.append(cpol[i])
        for i in range(end_index,length):
            new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,start_index):
            tmp.append(ol[i])
        for i in range(start_index,end_index):
            popped.append(ol[i])
        for i in range(end_index,length):
            tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)

def pop_some(ol,*indexes,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_some(ol,0,2,5)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_some(ol,0,2,5,mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    indexes = list(map(lambda index:uniform_index(index,length),list(indexes)))
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(cpol[i])
            else:
                new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(ol[i])
            else:
                tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)

def pop_indexes(ol,indexes,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_indexes(ol,{0,-3,5})
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_indexes(ol,{0,-3,5},mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    indexes = list(map(lambda index:uniform_index(index,length),list(indexes)))
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(cpol[i])
            else:
                new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(ol[i])
            else:
                tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)

def remove_first(ol,value,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_first(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_first(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
        ####array_remove is the same as remove_first
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.remove(value)
        return(new)
    else:
        ol.remove(value)
        return(ol)

array_remove = remove_first

def remove_firstnot(ol,value,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_firstnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_firstnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
        ####array_removenot is the same as remove_firstnot
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    if(mode == "new"):
        new = copy.deepcopy(ol)
        for i in range(0,length):
            if(new[i] == value):
                pass
            else:
                new.pop(i)
                return(new)
        return(new)
    else:
        for i in range(0,length):
            if(ol[i] == value):
                pass
            else:
                ol.pop(i)
                return(ol)
        return(ol)

array_removenot = remove_firstnot

def remove_last(ol,value,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_last(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_last(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    new.reverse()
    new.remove(value)
    new.reverse()
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_lastnot(ol,value,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_lastnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_lastnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    if(mode == "new"):
        new = copy.deepcopy(ol)
        for i in range(length-1,-1,-1):
            if(new[i] == value):
                pass
            else:
                new.pop(i)
                return(new)
        return(new)
    else:
        for i in range(length-1,-1,-1):
            if(ol[i] == value):
                pass
            else:
                ol.pop(i)
                return(ol)
        return(ol)

def remove_which(ol,value,which,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_which(ol,'a',1)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_which(ol,'a',1,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    length = ol.__len__()
    if(mode == "new"):
        l = new 
    else:
        l = ol
    seq = -1
    for i in range(0,length):
        if(ol[i]==value):
            seq = seq + 1
            if(seq == which):
                l.pop(i)
                break
            else:
                pass
        else:
            pass
    return(l)

def remove_whichnot(ol,value,which,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_whichnot(ol,'a',1)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_whichnot(ol,'a',1,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    length = ol.__len__()
    if(mode == "new"):
        l = new 
    else:
        l = ol
    seq = -1
    for i in range(0,length):
        if(not(ol[i]==value)):
            seq = seq + 1
            if(seq == which):
                l.pop(i)
                break
            else:
                pass
        else:
            pass
    return(l)

def remove_some(ol,value,*seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_some(ol,'a',1,3)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_some(ol,'a',1,3,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    seq = -1
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_somenot(ol,value,*seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_somenot(ol,'a',1,3)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_somenot(ol,'a',1,3,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    seq = -1
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(not(cpol[i]==value)):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_seqs(ol,value,seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_seqs(ol,'a',{1,3})
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_seqs(ol,'a',{1,3},mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    seq = -1
    for i in range(0,length):
        if(cpol[i]==value):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_seqsnot(ol,value,seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_seqsnot(ol,'a',{1,3})
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_seqsnot(ol,'a',{1,3},mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    seq = -1
    for i in range(0,length):
        if(not(cpol[i]==value)):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_all(ol,value,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_all(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_all(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            pass
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_allnot(ol,value,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_allnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_allnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_many(ol,values,seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        new = remove_many(ol,['a','b'],[1,2])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        rslt = remove_many(ol,['a','b'],[1,2],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    values = copy.deepcopy(values)
    seqs = copy.deepcopy(seqs)
    cursors = [-1] * values.__len__()
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        label = True
        for j in range(0,cursors.__len__()):
            which = seqs[j]
            value = values[j]
            if(cpol[i] == value):
                cursors[j] = cursors[j] + 1
                if(cursors[j] == which):
                    label = False
                    break
                else:
                    pass
            else:
                pass
        if(label):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_manynot(ol,values,seqs,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        new = remove_manynot(ol,['a','b'],[1,2])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        rslt = remove_manynot(ol,['a','b'],[1,2],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    values = copy.deepcopy(values)
    seqs = copy.deepcopy(seqs)
    cursors = [-1] * values.__len__()
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        label = True
        for j in range(0,cursors.__len__()):
            which = seqs[j]
            value = values[j]
            if(not(cpol[i] == value)):
                cursors[j] = cursors[j] + 1
                if(cursors[j] == which):
                    label = False
                    break
                else:
                    pass
            else:
                pass
        if(label):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def reverse(ol,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        new = reverse(ol)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = reverse(ol,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.reverse()
        return(new) 
    else:
        ol.reverse()
        return(ol)


    'reverse',
    'sort'

def sort(ol,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,3,4,2]
        id(ol)
        new = sort(ol)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,3,4,2]
        id(ol)
        rslt = sort(ol,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.sort()
        return(new) 
    else:
        ol.sort()
        return(ol)

def comprise(list1,list2,**kwargs):
    '''
        from xdict.elist import *
        comprise([1,2,3,4,5],[2,3,4],mode="loose")
        comprise([1,2,3,4,5],[2,3,4])
        comprise([1,2,3,4,5],[2,3,4],mode="strict")
        comprise([1,2,3,4,5],[1,2,3,4],mode="strict")
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "loose"
    len_1 = list1.__len__()
    len_2 = list2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        if(mode=="strict"):
            if(list2 == list1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(list2 == list1[i:(i+len_2)]):
                    return(True)
                else:
                    pass
    return(False)

def car(ol):
    '''
        from xdict.elist import *
        ol=[1,2,3,4]
        car(ol)
    '''
    return(ol[0])

def cdr(ol,**kwargs):
    '''
        from xdict.elist import *
        ol=[1,2,3,4]
        id(ol)
        new = cdr(ol)
        new
        id(new)
        ####
        ol=[1,2,3,4]
        id(ol)
        rslt = cdr(ol,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        return(cpol[1:])
    else:
        ol.pop(0)
        return(ol)

def cons(head_ele,l,**kwargs):
    '''
        from xdict.elist import *
        ol=[1,2,3,4]
        id(ol)
        new = cons(5,ol)
        new
        id(new)
        ####
        ol=[1,2,3,4]
        id(ol)
        rslt = cons(5,ol,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    return(prepend(l,head_ele,mode=mode))

def array_from(obj,func,*args):
    '''
        from xdict.elist import *
        array_from("abcd")
        #####
        def map_func(ele,x,y):
            return(int(ele)+x+y)
        
        array_from("1234",map_func,1000,100)
        
        def map_func(ele):
            return(int(ele)*2)
        
        array_from("1234",map_func)
        
        array_from("1234",None)
    '''
    if(func):
        l = list(obj)
        rslt = list(map(lambda ele:func(ele,*args),l))
        return(rslt)
    else:
        return(list(obj))

def array_of(*eles):
    '''
        from xdict.elist import *
        array_of(1,2,4,5,6)
    '''
    return(list(eles))

def concat(*arrays):
    '''
        from xdict.elist import *
        l1 = [1,2,3]
        l2 = ["a","b","c"]
        l3 = [100,200]
        id(l1)
        id(l2)
        id(l3)
        arrays = [l1,l2,l3]
        new = concat(arrays)
        new
        id(new)
    '''
    new = []
    length = arrays.__len__()
    for i in range(0,length):
        array = copy.deepcopy(arrays[i])
        new.extend(array)
    return(new)

def copy_within(ol,target, start=None, end=None):
    '''
        from xdict.elist import *
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,0,3,4)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,0,3)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,-2)
        rslt
        id(rslt)
        ####copyWithin is the same as copy_within
    '''
    length = ol.__len__()
    if(start==None):
        start = 0
    else:
        pass
    if(end==None):
        end = length
    else:
        pass
    target = uniform_index(target,length)
    start = uniform_index(start,length)
    end = uniform_index(end,length)
    cplen = end - start
    cpend = target+cplen
    if(target+cplen > length):
        cpend = length
    else:
        pass
    shift = start - target
    if(shift>=0):
        for i in range(target,cpend):
            ol[i] = ol[i+shift]
    else:
        for i in range(cpend-1,target-1,-1):
            ol[i] = ol[i+shift]
    return(ol)

copyWithin = copy_within

def entries(ol):
    '''
        from xdict.elist import *
        ol = ['a','b','c']
        rslt = entries(ol)
        rslt
    '''
    rslt = []
    length = ol.__len__()
    for i in range(0,length):
        entry = [i,ol[i]]
        rslt.append(entry)
    return(rslt)

def every(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        every(ol,test_func,3)
        
        ol = [10,20,30,40]
        every(ol,test_func,3)
        
    '''
    rslt = (True,None)
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            return((False,i))
    return(rslt)

def fill(ol,value,start=None, end=None,**kwargs):
    '''
        from xdict.elist import *
        ol = [1, 2, 3]
        id(ol)
        rslt = fill(ol,4)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3]
        id(ol)
        rslt = fill(ol,4,1)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3]
        id(ol)
        rslt = fill(ol,4,1,2,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    if(start==None):
        start = 0
    else:
        pass
    if(end==None):
        end = length
    else:
        pass
    start = uniform_index(start,length)
    end = uniform_index(end,length)
    new = copy.deepcopy(ol)
    for i in range(start,end):
        new[i] = value
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def filter(ol,test_func,*args,**kwargs):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        id(ol)
        new = filter(ol,test_func,3)
        new
        id(new)
        #####
        ol = [10,20,30,40]
        id(ol)
        rslt = filter(ol,test_func,3,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    new = []
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        cond = test_func(cpol[i],*args)
        if(cond):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def find_first(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        first = find_first(ol,test_func,3)
        first
        #####
        ol = [10,20,30,40]
        first = find_first(ol,test_func,3)
        first
        ####find is the same as find_first
    '''
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return({'index':None,'value':None})

find = find_first

def find_firstnot(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        first = find_firstnot(ol,test_func,3)
        first
        #####
        ol = [10,20,30,40]
        first = find_firstnot(ol,test_func,3)
        first
        ####findnot is the same as find_firstnot
    '''
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            return({'index':i,'value':ol[i]})
    return({'index':None,'value':None})

findnot = find_firstnot

def find_last(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        last = find_last(ol,test_func,3)
        last
        #####
        ol = [10,20,30,40]
        last = find_last(ol,test_func,3)
        last
    '''
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return({'index':None,'value':None})

def find_lastnot(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        last = find_lastnot(ol,test_func,3)
        last
        #####
        ol = [10,20,30,40]
        last = find_lastnot(ol,test_func,3)
        last
    '''
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            return({'index':i,'value':ol[i]})
    return({'index':None,'value':None})

def find_which(ol,which,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        last = find_which(ol,0,test_func,3)
        last
        last = find_which(ol,2,test_func,3)
        last
    '''
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            seq = seq + 1
            if(seq == which):
                return({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return({'index':None,'value':None})

def find_whichnot(ol,which,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        last = find_whichnot(ol,0,test_func,3)
        last
        last = find_whichnot(ol,2,test_func,3)
        last
    '''
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = not(test_func(ol[i],*args))
        if(cond):
            seq = seq + 1
            if(seq == which):
                return({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return({'index':None,'value':None})

def find_seqs(ol,seqs,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        some = find_seqs(ol,[0,3],test_func,3)
        some
        some = find_some(ol,[0,1,2],test_func,3)
        some
        #find_some is the same as find_seqs
    '''
    rslt =[]
    seqs = list(seqs)
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            seq = seq + 1
            if(seq in seqs):
                rslt.append({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(rslt)

find_some = find_seqs

def find_seqsnot(ol,seqs,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        some = find_seqsnot(ol,[0,3],test_func,3)
        some
        some = find_somenot(ol,[0,1,2],test_func,3)
        some
        #find_somenot is the same as find_seqsnot
    '''
    rslt =[]
    seqs = list(seqs)
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = not(test_func(ol[i],*args))
        if(cond):
            seq = seq + 1
            if(seq in seqs):
                rslt.append({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(rslt)

find_somenot = find_seqsnot

def find_all(ol,test_func,*args):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        rslt = find_all(ol,test_func,3)
        pobj(rslt)
    '''
    rslt =[]
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            rslt.append({'index':i,'value':ol[i]})
        else:
            pass
    return(rslt)

def find_allnot(ol,test_func,*args):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        rslt = find_allnot(ol,test_func,3)
        pobj(rslt)
    '''
    rslt =[]
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            rslt.append({'index':i,'value':ol[i]})
    return(rslt)

def push(l,*eles,**kwargs):
    '''
        from xdict.elist import *
        ol=[1,2,3,4]
        id(ol)
        new = push(ol,5,6,7)
        new
        id(new)
        ####
        ol=[1,2,3,4]
        id(ol)
        rslt = push(ol,5,6,7,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    eles = list(eles)
    return(extend(ol,eles,mode=mode))

def includes(ol,value):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        includes(ol,3)
        includes(ol,5)
    '''
    return((value in ol))

def toString(ol):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        toString(ol)
    '''
    return(ol.__str__())

def toSource(ol):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        toSource(ol)
    '''
    return(ol.__repr__())

def splice(ol,start,deleteCount,*eles,**kwargs):
    '''
        from xdict.elist import *
        ol = ["angel", "clown", "mandarin", "surgeon"]
        id(ol)
        new = splice(ol,2,0,"drum")
        new
        id(new)
        ####
        ol = ["angel", "clown", "mandarin", "surgeon"]
        id(ol)
        new = splice(ol,2,1,"drum",mode="original")
        new
        id(new)
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        new = splice(ol,2,2,77,777)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    new = copy.deepcopy(ol)
    if(start >= length):
        eles = list(eles)
        new.extend(eles)
    else:
        start = uniform_index(start,length)
        end = start + deleteCount
        tmp = pop_range(new,start,end,mode="new")['list']
        new = insert_some(tmp,*eles,index=start,mode="new")
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def some(ol,test_func,*args):
    '''
        from xdict.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        some(ol,test_func,3)
        
        ol = [1,2,1,3]
        some(ol,test_func,3)
        
    '''
    rslt = {'cond':False,'index':None}
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'cond':True,'index':i})
        else:
            pass
    return(rslt)

def slice(ol,start,end=None,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4,5]
        id(ol)
        new = slice(ol,2,4)
        new
        id(new)
        ####
        id(ol)
        rslt = slice(ol,1,-2,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    new = copy.deepcopy(ol)
    if(end == None):
        end = length
    else:
        end = uniform_index(end,length)
    start = uniform_index(start,length)
    if(mode == "new"):
        return(new[start:end])
    else:
        ol.clear()
        ol.extend(new[start:end])
        return(ol)

def shift(ol,**kwargs):
    '''
        from xdict.jprint import pobj
        from xdict.elist import *
        ol = [1,2,3,4]
        id(ol)
        rslt = shift(ol)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = shift(ol,mode="original")
        rslt
        ol
        id(ol)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    rslt = pop(ol,0,mode=mode)
    return(rslt)

def reduce_left(ol,callback,initialValue):
    '''
        from xdict.elist import *
        def callback(accumulator,currentValue):
            accumulator.append(currentValue[0])
            accumulator.append(currentValue[1])
            return(accumulator)
        
        ol = [(1,2),("a","b"),("x","y")]
        reduce_left(ol,callback,[])
        #array_reduce, reduceLeft ,reduce_left  are the same
    '''
    length = ol.__len__()
    accumulator = initialValue
    for i in range(0,length):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)

array_reduce = reduce_left
reduceLeft = reduce_left

def reduce_right(ol,callback,initialValue):
    '''
        from xdict.elist import *
        def callback(accumulator,currentValue):
            accumulator.append(currentValue[0])
            accumulator.append(currentValue[1])
            return(accumulator)
        
        ol = [(1,2),("a","b"),("x","y")]
        reduce_right(ol,callback,[])
        #reduceRight,reduce_right are the same 
    '''
    length = ol.__len__()
    accumulator = initialValue
    for i in range(length-1,-1,-1):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)

reduceRight = reduce_right

def array_map(ol,map_func,*args):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        def map_func(ele,mul,plus):
            return(ele*mul+plus)
        
        array_map(ol,map_func,2,100)
    '''
    rslt = list(map(lambda ele:map_func(ele,*args),ol))
    return(rslt)

def join(ol,separator=","):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        join(ol,separator="-")
    '''
    rslt =""
    length = ol.__len__()
    for i in range(0,length-1):
        rslt = rslt + str(ol[i]) + separator
    rslt = rslt + str(ol[length - 1])
    return(rslt)

def for_each(ol,test_func,*args):
    '''
        from xdict.elist import *
        def show_func(ele):
            print("<{0}>".format(ele))
        
        ol = [1,2,3,4]
        for_each(ol,show_func)
        
        ####forEach is the same as for_each
    '''
    rslt = (True,None)
    length = ol.__len__()
    for i in range(0,length):
        test_func(ol[i],*args)

forEach = for_each

# Array.prototype.flatten()


def help(func_name):
    if(func_name == "extend"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> nl = [5,6,7,8]
            >>> id(ol)
            140004175540616
            >>> extend(ol,nl,mode="original")
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> ol
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> id(ol)
            140004175540616
            >>> ####
            ... ol = [1,2,3,4]
            >>> nl = [5,6,7,8]
            >>> id(ol)
            140004168355400
            >>> new = extend(ol,nl)
            >>> new
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> id(new)
            140004172033160
            >>>
        '''
        print(doc)
    elif(func_name == "append"):
        doc = '''
            >>> from xdict.elist import *
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ImportError: No module named 'xdict.elist'
            >>> ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140004175608712
            >>> append(ol,ele,mode="original")
            [1, 2, 3, 4, 5]
            >>> ol
            [1, 2, 3, 4, 5]
            >>> id(ol)
            140004175608712
            >>> ####
            ... ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140004172033160
            >>> new = append(ol,ele)
            >>> new
            [1, 2, 3, 4, 5]
            >>> id(new)
            140004175608712
        '''
        print(doc)
    elif(func_name == "append_some"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140004175608712
            >>> append_some(ol,5,6,7,8,mode="original")
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> ol
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> id(ol)
            140004175608712
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140004168355400
            >>> new = append_some(ol,5,6,7,8)
            >>> new
            [1, 2, 3, 4, 5, 6, 7, 8]
            >>> id(new)
            140004175608712
            >>>
        '''
        print(doc)
    elif(func_name == "deepcopy"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140004172033160
            >>> new = deepcopy(ol)
            >>> new
            [1, 2, 3, 4]
            >>> id(new)
            140004175540616
            >>>
        '''
        print(doc)
    elif(func_name == "prextend"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> nl = [5,6,7,8]
            >>> id(ol)
            140004168355400
            >>> id(nl)
            140004175608712
            >>> prextend(ol,nl,mode="original")
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> ol
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> id(ol)
            140004168355400
            >>> ####
            ... ol = [1,2,3,4]
            >>> nl = [5,6,7,8]
            >>> id(ol)
            140004175540616
            >>> id(nl)
            140004168355400
            >>> new = prextend(ol,nl)
            >>> new
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> id(new)
            140004175608712
        '''
        print(doc)
    elif(func_name == "prepend"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140004175608712
            >>> prepend(ol,ele,mode="original")
            [5, 1, 2, 3, 4]
            >>> ol
            [5, 1, 2, 3, 4]
            >>> id(ol)
            140004175608712
            >>> ####
            ... ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140004175540616
            >>> new = prepend(ol,ele)
            >>> new
            [5, 1, 2, 3, 4]
            >>> id(new)
            140004175608712
        '''
        print(doc)
    elif((func_name == "prepend_some")|(func_name == "unshift")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140507015081416
            >>> prepend_some(ol,5,6,7,8,mode="original")
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> ol
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> id(ol)
            140507015081416
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140507007933832
            >>> new = prepend_some(ol,5,6,7,8)
            >>> new
            [5, 6, 7, 8, 1, 2, 3, 4]
            >>> id(new)
            140507015081416
            #####unshift is the same as prepend_some
        '''
        print(doc)
    elif(func_name == "uniform_index"):
        doc = '''
            >>> uniform_index(0,3)
            0
            >>> uniform_index(-1,3)
            2
            >>> uniform_index(-4,3)
            0
            >>> uniform_index(-3,3)
            0
            >>> uniform_index(5,3)
            3
            >>>
        '''
        print(doc)
    elif(func_name == "insert"):
        doc = '''
            >>> from xdict.elist import *
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ImportError: No module named 'xdict.elist'
            >>> ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140489401366088
            >>> insert(ol,2,ele,mode="original")
            [1, 2, 5, 3, 4]
            >>> ol
            [1, 2, 5, 3, 4]
            >>> id(ol)
            140489401366088
            >>> ####
            ... ol = [1,2,3,4]
            >>> ele = 5
            >>> id(ol)
            140489404837960
            >>> new = insert(ol,2,ele)
            >>> new
            [1, 2, 5, 3, 4]
            >>> id(new)
            140489404596552
            >>>
        '''
        print(doc)
    elif(func_name == "insert_some"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140660491488328
            >>> insert_some(ol,5,6,7,8,index=2,mode="original")
            [1, 2, 5, 6, 7, 8, 3, 4]
            >>> ol
            [1, 2, 5, 6, 7, 8, 3, 4]
            >>> id(ol)
            140660491488328
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140660489874376
            >>> new = insert_some(ol,5,6,7,8,index=2)
            >>> new
            [1, 2, 5, 6, 7, 8, 3, 4]
            >>> id(new)
            140660491494536
            >>>
        '''
        print(doc)
    elif(func_name == 'insert_many'):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4,5]
            >>> eles = [7,77,777]
            >>> locs = [0,2,4]
            >>> id(ol)
            140623820873352
            >>> new = insert_many(ol,eles,locs)
            >>> ol
            [1, 2, 3, 4, 5]
            >>> new
            [7, 1, 2, 77, 3, 4, 777, 5]
            >>> id(new)
            140623819361160
            >>> ####
            ... ol = [1,2,3,4,5]
            >>> eles = [7,77,777]
            >>> locs = [0,2,4]
            >>> id(ol)
            140623821862856
            >>> rslt = insert_many(ol,eles,locs,mode="original")
            >>> ol
            [7, 1, 2, 77, 3, 4, 777, 5]
            >>> rslt
            [7, 1, 2, 77, 3, 4, 777, 5]
            >>> id(rslt)
            140623821862856
            >>>
        '''
        print(doc)
    elif(func_name == "sorted_refer_to"):
        doc = '''
            >>> from xdict.elist import *
            >>> l = ["a","b","c"]
            >>> referer = [7,8,6]
            >>> sorted_refer_to(l,referer)
            {'list': ['c', 'a', 'b'], 'referer': [6, 7, 8]}
            >>> {'list': ['c', 'a', 'b'], 'referer': [6, 7, 8]}
            {'list': ['c', 'a', 'b'], 'referer': [6, 7, 8]}
            >>> l
            ['a', 'b', 'c']
            >>> referer
            [7, 8, 6]
            >>>
        '''
        print(doc)
    elif((func_name == "index_first")|(func_name == "indexOf")|(func_name == "array_index")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_first(ol,'a')
            1
            >>>
            ####index_first, array_index, indexOf  are the same
        '''
        print(doc)
    elif((func_name == "index_firstnot")|(func_name == "indexOfnot")|(func_name == "array_indexnot")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_firstnot(ol,'a')
            0
            >>> ####index_firstnot, array_indexnot, indexOfnot  are the same
        '''
        print(doc)
    elif((func_name == "index_last")|(func_name == "lastIndexOf")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_last(ol,'a')
            5
            >>>
            ####lastIndexOf is the same as index_last
        '''
        print(doc)
    elif((func_name == "index_lastnot")|(func_name == "lastIndexOfnot")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_lastnot(ol,'a')
            6
            >>> ####lastIndexOfnot is the same as index_lastnot
        '''
        print(doc)
    elif(func_name == "index_which"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_which(ol,'a',0)
            1
            >>> index_which(ol,'a',1)
            3
            >>> index_which(ol,'a',2)
            5
            >>> index_which(ol,'a',3) == None
            True
            >>>
        '''
        print(doc)
    elif(func_name == "index_whichnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> index_whichnot(ol,'a',0)
            0
            >>> index_whichnot(ol,'a',1)
            2
            >>> index_whichnot(ol,'a',2)
            4
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_all"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_all(ol,'a')
            [1, 3, 5]
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_allnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_allnot(ol,'a')
            [0, 2, 4, 6]
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_some"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_some(ol,'a',0,2)
            [1, 5]
            >>> indexes_some(ol,'a',0,1)
            [1, 3]
            >>> indexes_some(ol,'a',1,2)
            [3, 5]
            >>> indexes_some(ol,'a',3,4)
            []
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_somenot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_somenot(ol,'a',0,2)
            [0, 4]
            >>> indexes_somenot(ol,'a',0,1)
            [0, 2]
            >>> indexes_somenot(ol,'a',1,2)
            [2, 4]
            >>> indexes_somenot(ol,'a',3,4)
            [6]
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_seqs"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_seqs(ol,'a',{0,2})
            [1, 5]
            >>> indexes_seqs(ol,'a',{0,1})
            [1, 3]
            >>> indexes_seqs(ol,'a',{1,2})
            [3, 5]
            >>> indexes_seqs(ol,'a',{3,4})
            []
            >>>
        '''
        print(doc)
    elif(func_name == "indexes_seqsnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',4,'a',5]
            >>> indexes_seqsnot(ol,'a',{0,2})
            [0, 4]
            >>> indexes_seqsnot(ol,'a',{0,1})
            [0, 2]
            >>> indexes_seqsnot(ol,'a',{1,2})
            [2, 4]
            >>> indexes_seqsnot(ol,'a',{3,4})
            [6]
            >>>
        '''
        print(doc)
    elif(func_name == "first_continuous_indexes_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> first_continuous_indexes_slice(ol,"a")
            [1, 2]
            >>>
        '''
        print(doc)
    elif(func_name == "first_continuous_indexesnot_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = ["a",0,1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> first_continuous_indexesnot_slice(ol,"a")
            [1, 2]
            >>>
        '''
        print(doc)
    elif(func_name == "last_continuous_indexes_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> last_continuous_indexes_slice(ol,"a")
            [7, 8, 9]
            >>>
        '''
        print(doc)
    elif(func_name == "last_continuous_indexesnot_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> last_continuous_indexesnot_slice(ol,"a")
            [10]
            >>>
        '''
        print(doc)
    elif(func_name == "which_continuous_indexes_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> which_continuous_indexes_slice(ol,"a",0)
            [1, 2]
            >>> which_continuous_indexes_slice(ol,"a",1)
            [5]
            >>> which_continuous_indexes_slice(ol,"a",2)
            [7, 8, 9]
            >>> which_continuous_indexes_slice(ol,"a",3)
            []
            >>> which_continuous_indexes_slice(ol,"b",0)
            []
            >>>
        '''
        print(doc)
    elif(func_name == "which_continuous_indexesnot_slice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> which_continuous_indexesnot_slice(ol,"a",0)
            [0]
            >>> which_continuous_indexesnot_slice(ol,"a",1)
            [3, 4]
            >>> which_continuous_indexesnot_slice(ol,"a",2)
            [6]
            >>> which_continuous_indexesnot_slice(ol,"a",3)
            [10]
            >>> which_continuous_indexesnot_slice(ol,"b",0)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            >>>
        '''
        print(doc)
    elif(func_name == "seqs_continuous_indexes_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> seqs_continuous_indexes_slices(ol,"a",{0,2})
            [[1, 2], [7, 8, 9]]
            >>>
        '''
        print(doc)
    elif(func_name == "seqs_continuous_indexesnot_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> seqs_continuous_indexesnot_slices(ol,"a",0,2)
            [[0], [6]]
            >>>
        '''
        print(doc)
    elif(func_name == "some_continuous_indexes_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> some_continuous_indexes_slices(ol,"a",0,2)
            [[1, 2], [7, 8, 9]]
            >>>
        '''
        print(doc)
    elif(func_name == "some_continuous_indexesnot_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> some_continuous_indexesnot_slices(ol,"a",{0,2})
            [[0], [6]]
            >>>
        '''
        print(doc)
    elif(func_name == "all_continuous_indexes_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> all_continuous_indexes_slices(ol,"a")
            [[1, 2], [5], [7, 8, 9]]
            >>>
        '''
        print(doc)
    elif(func_name == "all_continuous_indexesnot_slices"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,"a","a",2,3,"a",4,"a","a","a",5]
            >>> all_continuous_indexesnot_slices(ol,"a")
            [[0], [3, 4], [6], [10]]
            >>>
        '''
        print(doc)
    elif(func_name == "pop"):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140660487975432
            >>> rslt = pop(ol,2)
            >>> pobj(rslt)
            {
             'popped': 3,
             'list':
                     [
                      1,
                      2,
                      4
                     ]
            }
            >>> ol
            [1, 2, 3, 4]
            >>> id(ol)
            140660487975432
            >>> id(rslt['list'])
            140660491573128
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140660491494408
            >>> rslt = pop(ol,2,mode="original")
            >>> rslt
            3
            >>> ol
            [1, 2, 4]
            >>> id(ol)
            140660491494408
            >>>
        '''
        print(doc)
    elif(func_name == "pop_range"):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4,5,6]
            >>> id(ol)
            140623819361160
            >>> rslt = pop_range(ol,2,4)
            >>> pobj(rslt)
            {
             'popped':
                       [
                        3,
                        4
                       ],
             'list':
                     [
                      1,
                      2,
                      5,
                      6
                     ]
            }
            >>> ol
            [1, 2, 3, 4, 5, 6]
            >>> id(ol)
            140623819361160
            >>> id(rslt['list'])
            140623820567560
            >>> ####
            ... ol = [1,2,3,4,5,6]
            >>> id(ol)
            140623821863816
            >>> rslt = pop_range(ol,2,4,mode="original")
            >>> rslt
            [3, 4]
            >>> ol
            [1, 2, 5, 6]
            >>> id(ol)
            140623821863816
            >>>
        '''
        print(doc)
    elif(func_name == "pop_some"):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4,5,6]
            >>> id(ol)
            140660489580104
            >>> rslt = pop_some(ol,0,2,5)
            >>> pobj(rslt)
            {
             'popped':
                       [
                        1,
                        3,
                        6
                       ],
             'list':
                     [
                      2,
                      4,
                      5
                     ]
            }
            >>> ol
            [1, 2, 3, 4, 5, 6]
            >>> id(ol)
            140660489580104
            >>> id(rslt['list'])
            140660491493960
            >>> ####
            ... ol = [1,2,3,4,5,6]
            >>> id(ol)
            140660489875272
            >>> rslt = pop_some(ol,0,2,5,mode="original")
            >>> rslt
            [1, 3, 6]
            >>> ol
            [2, 4, 5]
            >>> id(ol)
            140660489875272
            >>>
        '''
        print(doc)
    elif(func_name == "pop_indexes"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4,5,6]
            >>> id(ol)
            140660491486024
            >>> rslt = pop_indexes(ol,{0,-3,5})
            >>> pobj(rslt)
            {
             'popped':
                       [
                        1,
                        4,
                        6
                       ],
             'list':
                     [
                      2,
                      3,
                      5
                     ]
            }
            >>> ol
            [1, 2, 3, 4, 5, 6]
            >>> id(ol)
            140660491486024
            >>> id(rslt['list'])
            140660491346696
            >>> ####
            ... ol = [1,2,3,4,5,6]
            >>> id(ol)
            140660491573448
            >>> rslt = pop_indexes(ol,{0,-3,5},mode="original")
            >>> rslt
            [1, 4, 6]
            >>> ol
            [2, 3, 5]
            >>> id(ol)
            140660491573448
        '''
        print(doc)
    elif((func_name == "remove_first")|(func_name == "array_remove")):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140660491494728
            >>> new = remove_first(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            [1, 3, 'a', 5, 'a']
            >>> id(ol)
            140660491494728
            >>> id(new)
            140660491573512
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140660489874056
            >>> rslt = remove_first(ol,'a',mode="original")
            >>> ol
            [1, 3, 'a', 5, 'a']
            >>> rslt
            [1, 3, 'a', 5, 'a']
            >>> id(ol)
            140660489874056
            >>> id(rslt)
            140660489874056
            ####array_remove is the same as remove_first
        '''
        print(doc)
    elif((func_name == "remove_firstnot")|(func_name == "array_removenot")):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623820657544
            >>> new = remove_firstnot(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            ['a', 3, 'a', 5, 'a']
            >>> id(ol)
            140623820657544
            >>> id(new)
            140623821822728
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623820643464
            >>> rslt = remove_firstnot(ol,'a',mode="original")
            >>> ol
            ['a', 3, 'a', 5, 'a']
            >>> rslt
            ['a', 3, 'a', 5, 'a']
            >>> id(ol)
            140623820643464
            >>> id(rslt)
            140623820643464
            >>> ####array_removenot is the same as remove_firstnot
        '''
        print(doc)
    elif(func_name == "remove_last"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623821862856
            >>> new = remove_last(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            [1, 'a', 3, 'a', 5]
            >>> id(ol)
            140623821862856
            >>> id(new)
            140623821822088
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623821864008
            >>> rslt = remove_last(ol,'a',mode="original")
            >>> ol
            [1, 'a', 3, 'a', 5]
            >>> rslt
            [1, 'a', 3, 'a', 5]
            >>> id(ol)
            140623821864008
            >>> id(rslt)
            140623821864008
        '''
        print(doc)
    elif(func_name == "remove_lastnot"):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623820657544
            >>> new = remove_lastnot(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            [1, 'a', 3, 'a', 'a']
            >>> id(ol)
            140623820657544
            >>> id(new)
            140623819970696
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623821822728
            >>> rslt = remove_lastnot(ol,'a',mode="original")
            >>> ol
            [1, 'a', 3, 'a', 'a']
            >>> rslt
            [1, 'a', 3, 'a', 'a']
            >>> id(ol)
            140623821822728
            >>> id(rslt)
            140623821822728
            >>>
        '''
        print(doc)
    elif(func_name == "remove_which"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623821864008
            >>> new = remove_which(ol,'a',1)
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            [1, 'a', 3, 5, 'a']
            >>> id(ol)
            140623821864008
            >>> id(new)
            140623819361160
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623821862856
            >>> rslt = remove_which(ol,'a',1,mode="original")
            >>> ol
            [1, 'a', 3, 5, 'a']
            >>> rslt
            [1, 'a', 3, 5, 'a']
            >>> id(ol)
            140623821862856
            >>> id(rslt)
            140623821862856
        '''
        print(doc)
    elif(func_name == "remove_whichnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623820643464
            >>> new = remove_whichnot(ol,'a',1)
            >>> ol
            [1, 'a', 3, 'a', 5, 'a']
            >>> new
            [1, 'a', 'a', 5, 'a']
            >>> id(ol)
            140623820643464
            >>> id(new)
            140623820657544
            >>> ####
            ... ol = [1,'a',3,'a',5,'a']
            >>> id(ol)
            140623819970696
            >>> rslt = remove_whichnot(ol,'a',1,mode="original")
            >>> ol
            [1, 'a', 'a', 5, 'a']
            >>> rslt
            [1, 'a', 'a', 5, 'a']
            >>> id(ol)
            140623819970696
            >>> id(rslt)
            140623819970696
            >>>
        '''
        print(doc)
    elif(func_name == "remove_some"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821822088
            >>> new = remove_some(ol,'a',1,3)
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            [1, 'a', 3, 5, 'a', 6]
            >>> id(ol)
            140623821822088
            >>> id(new)
            140623821864008
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623819361160
            >>> rslt = remove_some(ol,'a',1,3,mode="original")
            >>> ol
            [1, 'a', 3, 5, 'a', 6]
            >>> rslt
            [1, 'a', 3, 5, 'a', 6]
            >>> id(ol)
            140623819361160
            >>> id(rslt)
            140623819361160
            >>>
        '''
        print(doc)
    elif(func_name == "remove_somenot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821822728
            >>> new = remove_somenot(ol,'a',1,3)
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            [1, 'a', 'a', 5, 'a', 'a']
            >>> id(ol)
            140623821822728
            >>> id(new)
            140623820643464
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623820657544
            >>> rslt = remove_somenot(ol,'a',1,3,mode="original")
            >>> ol
            [1, 'a', 'a', 5, 'a', 'a']
            >>> rslt
            [1, 'a', 'a', 5, 'a', 'a']
            >>> id(ol)
            140623820657544
            >>> id(rslt)
            140623820657544
            >>>
        '''
        print(doc)
    elif(func_name == "remove_seqs"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623819361160
            >>> new = remove_seqs(ol,'a',{1,3})
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            [1, 'a', 3, 5, 'a', 6]
            >>> id(ol)
            140623819361160
            >>> id(new)
            140623821862856
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821822088
            >>> rslt = remove_seqs(ol,'a',{1,3},mode="original")
            >>> ol
            [1, 'a', 3, 5, 'a', 6]
            >>> rslt
            [1, 'a', 3, 5, 'a', 6]
            >>> id(ol)
            140623821822088
            >>> id(rslt)
            140623821822088
            >>>
        '''
        print(doc)
    elif(func_name == "remove_seqsnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623819970696
            >>> new = remove_seqsnot(ol,'a',{1,3})
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            [1, 'a', 'a', 5, 'a', 'a']
            >>> id(ol)
            140623819970696
            >>> id(new)
            140623819968328
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623820643464
            >>> rslt = remove_seqsnot(ol,'a',{1,3},mode="original")
            >>> ol
            [1, 'a', 'a', 5, 'a', 'a']
            >>> rslt
            [1, 'a', 'a', 5, 'a', 'a']
            >>> id(ol)
            140623820643464
            >>> id(rslt)
            140623820643464
            >>>
        '''
        print(doc)
    elif(func_name == "remove_all"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821864008
            >>> new = remove_all(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            [1, 3, 5, 6]
            >>> id(ol)
            140623821864008
            >>> id(new)
            140623820566728
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821862856
            >>> rslt = remove_all(ol,'a',mode="original")
            >>> ol
            [1, 3, 5, 6]
            >>> rslt
            [1, 3, 5, 6]
            >>> id(ol)
            140623821862856
            >>> id(rslt)
            140623821862856
            >>>
        '''
        print(doc)
    elif(func_name == "remove_allnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623819968328
            >>> new = remove_allnot(ol,'a')
            >>> ol
            [1, 'a', 3, 'a', 5, 'a', 6, 'a']
            >>> new
            ['a', 'a', 'a', 'a']
            >>> id(ol)
            140623819968328
            >>> id(new)
            140623820643464
            >>> ####
            ... ol = [1,'a',3,'a',5,'a',6,'a']
            >>> id(ol)
            140623821822728
            >>> rslt = remove_allnot(ol,'a',mode="original")
            >>> ol
            ['a', 'a', 'a', 'a']
            >>> rslt
            ['a', 'a', 'a', 'a']
            >>> id(ol)
            140623821822728
            >>> id(rslt)
            140623821822728
            >>>
        '''
        print(doc)
    elif(func_name == "remove_many"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
            >>> id(ol)
            140623820657544
            >>> new = remove_many(ol,['a','b'],[1,2])
            >>> ol
            [1, 'a', 3, 'b', 5, 'a', 6, 'a', 7, 'b', 8, 'b', 9]
            >>> new
            [1, 'a', 3, 'b', 5, 6, 'a', 7, 'b', 8, 9]
            >>> id(ol)
            140623820657544
            >>> id(new)
            140623821822728
            >>> ####
            ... ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
            >>> id(ol)
            140623820657736
            >>> rslt = remove_many(ol,['a','b'],[1,2],mode="original")
            >>> ol
            [1, 'a', 3, 'b', 5, 6, 'a', 7, 'b', 8, 9]
            >>> rslt
            [1, 'a', 3, 'b', 5, 6, 'a', 7, 'b', 8, 9]
            >>> id(ol)
            140623820657736
            >>> id(rslt)
            140623820657736
            >>>
        '''
        print(doc)
    elif(func_name == "remove_manynot"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
            >>> id(ol)
            140623820643464
            >>> new = remove_manynot(ol,['a','b'],[1,2])
            >>> ol
            [1, 'a', 3, 'b', 5, 'a', 6, 'a', 7, 'b', 8, 'b', 9]
            >>> new
            [1, 'a', 'b', 'a', 6, 'a', 7, 'b', 8, 'b', 9]
            >>> id(ol)
            140623820643464
            >>> id(new)
            140623820657992
            >>> ####
            ... ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
            >>> id(ol)
            140623820658056
            >>> rslt = remove_manynot(ol,['a','b'],[1,2],mode="original")
            >>> ol
            [1, 'a', 'b', 'a', 6, 'a', 7, 'b', 8, 'b', 9]
            >>> rslt
            [1, 'a', 'b', 'a', 6, 'a', 7, 'b', 8, 'b', 9]
            >>> id(ol)
            140623820658056
            >>> id(rslt)
            140623820658056
        '''
        print(doc)
    elif(func_name == "reverse"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140623821822088
            >>> new = reverse(ol)
            >>> ol
            [1, 2, 3, 4]
            >>> new
            [4, 3, 2, 1]
            >>> id(ol)
            140623821822088
            >>> id(new)
            140623820567112
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140623820873608
            >>> rslt = reverse(ol,mode="original")
            >>> ol
            [4, 3, 2, 1]
            >>> rslt
            [4, 3, 2, 1]
            >>> id(ol)
            140623820873608
            >>> id(rslt)
            140623820873608
            >>>
        '''
        print(doc)
    elif(func_name == "sort"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,3,4,2]
            >>> id(ol)
            140623821862856
            >>> new = sort(ol)
            >>> ol
            [1, 3, 4, 2]
            >>> new
            [1, 2, 3, 4]
            >>> id(ol)
            140623821862856
            >>> id(new)
            140623821822088
            >>> ####
            ... ol = [1,3,4,2]
            >>> id(ol)
            140623820567112
            >>> rslt = sort(ol,mode="original")
            >>> ol
            [1, 2, 3, 4]
            >>> rslt
            [1, 2, 3, 4]
            >>> id(ol)
            140623820567112
            >>> id(rslt)
            140623820567112
            >>>
        '''
        print(doc)
    elif(func_name == "comprise"):
        doc = '''
            >>> from xdict.elist import *
            >>> comprise([1,2,3,4,5],[2,3,4],mode="loose")
            True
            >>> comprise([1,2,3,4,5],[2,3,4])
            True
            >>> comprise([1,2,3,4,5],[2,3,4],mode="strict")
            False
            >>> comprise([1,2,3,4,5],[1,2,3,4],mode="strict")
            True
            >>>
        '''
        print(doc)
    elif(func_name == "car"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol=[1,2,3,4]
            >>> car(ol)
            1
            >>>
        '''
        print(doc)
    elif(func_name == "cdr"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol=[1,2,3,4]
            >>> id(ol)
            140623819361160
            >>> new = cdr(ol)
            >>> new
            [2, 3, 4]
            >>> id(new)
            140623820873608
            >>> ####
            ... ol=[1,2,3,4]
            >>> id(ol)
            140623821822088
            >>> rslt = cdr(ol,mode="original")
            >>> rslt
            [2, 3, 4]
            >>> id(rslt)
            140623821822088
            >>>
        '''
        print(doc)
    elif(func_name == "cons"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol=[1,2,3,4]
            >>> id(ol)
            140623821862856
            >>> new = cons(5,ol)
            >>> new
            [5, 1, 2, 3, 4]
            >>> id(new)
            140623819361160
            >>> ####
            ... ol=[1,2,3,4]
            >>> id(ol)
            140623820873608
            >>> rslt = cons(5,ol,mode="original")
            >>> rslt
            [5, 1, 2, 3, 4]
            >>> id(rslt)
            140623820873608
            >>>
        '''
        print(doc)
    elif(func_name == "array_from"):
        doc = '''
            >>> from xdict.elist import *
            >>> array_from("abcd")
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: array_from() missing 1 required positional argument: 'func'
            >>> #####
            ... def map_func(ele,x,y):
            ...     return(int(ele)+x+y)
            ...
            >>> array_from("1234",map_func,1000,100)
            [1101, 1102, 1103, 1104]
            >>>
            >>> def map_func(ele):
            ...     return(int(ele)*2)
            ...
            >>> array_from("1234",map_func)
            [2, 4, 6, 8]
            >>>
            >>> array_from("1234",None)
            ['1', '2', '3', '4']
            >>>
        '''
        print(doc)
    elif(func_name == "array_of"):
        doc = '''
            >>> from xdict.elist import *
            >>> array_of(1,2,4,5,6)
            [1, 2, 4, 5, 6]
        '''
        print(doc)
    elif(func_name == "concat"):
        doc = '''
            >>> l1 = [1,2,3]
            >>> l2 = ["a","b","c"]
            >>> l3 = [100,200]
            >>> id(l1)
            140623821822088
            >>> id(l2)
            140623821862856
            >>> id(l3)
            140623819968264
            >>> arrays = [l1,l2,l3]
            >>> new = concat(arrays)
            >>> new
            [[1, 2, 3], ['a', 'b', 'c'], [100, 200]]
            >>> id(new)
            140623820872008
        '''
        print(doc)
    elif((func_name == "copyWithin") | (func_name == "copy_within")):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1, 2, 3, 4, 5]
            >>> id(ol)
            140623820567560
            >>> rslt = copyWithin(ol,0,3,4)
            >>> rslt
            [4, 2, 3, 4, 5]
            >>> id(rslt)
            140623820567560
            >>> ####
            ... ol = [1, 2, 3, 4, 5]
            >>> id(ol)
            140623821864008
            >>> rslt = copyWithin(ol,0,3)
            >>> rslt
            [4, 5, 3, 4, 5]
            >>> id(rslt)
            140623821864008
            >>> ####
            ... ol = [1, 2, 3, 4, 5]
            >>> id(ol)
            140623820567560
            >>> rslt = copyWithin(ol,-2)
            >>> rslt
            [1, 2, 3, 1, 2]
            >>> id(rslt)
            140623820567560
            >>>
            ####copyWithin is the same as copy_within
        '''
        print(doc)
    elif(func_name == "entries"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = ['a','b','c']
            >>> rslt = entries(ol)
            >>> rslt
            [[0, 'a'], [1, 'b'], [2, 'c']]
            >>>
        '''
        print(doc)
    elif(func_name == "every"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> every(ol,test_func,3)
            (False, 0)
            >>>
            >>> ol = [10,20,30,40]
            >>> every(ol,test_func,3)
            (True, None)
            >>>
        '''
        print(doc)
    elif(func_name == "fill"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1, 2, 3]
            >>> id(ol)
            140623820568904
            >>> rslt = fill(ol,4)
            >>> rslt
            [4, 4, 4]
            >>> id(rslt)
            140623821863816
            >>> ####
            ... ol = [1, 2, 3]
            >>> id(ol)
            140623821864008
            >>> rslt = fill(ol,4,1)
            >>> rslt
            [1, 4, 4]
            >>> id(rslt)
            140623820568904
            >>> ####
            ... ol = [1, 2, 3]
            >>> id(ol)
            140623821863816
            >>> rslt = fill(ol,4,1,2,mode="original")
            >>> rslt
            [1, 4, 3]
            >>> id(rslt)
            140623821863816
            >>>
        '''
        print(doc)
    elif(func_name == "filter"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140623821863816
            >>> new = filter(ol,test_func,3)
            >>> new
            [4]
            >>> id(new)
            140623820568904
            >>> #####
            ... ol = [10,20,30,40]
            >>> id(ol)
            140623820566728
            >>> rslt = filter(ol,test_func,3,mode="original")
            >>> rslt
            [10, 20, 30, 40]
            >>> id(rslt)
            140623820566728
        '''
        print(doc)
    elif((func_name == "find_first") | (func_name == "find")):
        doc = '''
            from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> first = find_first(ol,test_func,3)
            >>> first
            {'index': 3, 'value': 4}
            >>> #####
            ... ol = [10,20,30,40]
            >>> first = find_first(ol,test_func,3)
            >>> first
            {'index': 0, 'value': 10}
            >>> ####find is the same as find_first
            ...
            >>>
        '''
        print(doc)
    elif((func_name == "find_firstnot") | (func_name == "findnot")):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> first = find_firstnot(ol,test_func,3)
            >>> first
            {'index': 0, 'value': 1}
            >>> #####
            ... ol = [10,20,30,40]
            >>> first = find_firstnot(ol,test_func,3)
            >>> first
            {'index': None, 'value': None}
            >>> ####findnot is the same as find_firstnot
            ...
            >>>
        '''
        print(doc)
    elif(func_name == "find_last"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> last = find_last(ol,test_func,3)
            >>> last
            {'index': 3, 'value': 4}
            >>> #####
            ... ol = [10,20,30,40]
            >>> last = find_last(ol,test_func,3)
            >>> last
            {'index': 3, 'value': 40}
            >>>
        '''
        print(doc)
    elif(func_name == "find_lastnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> last = find_lastnot(ol,test_func,3)
            >>> last
            {'index': 2, 'value': 3}
            >>> #####
            ... ol = [10,20,30,40]
            >>> last = find_lastnot(ol,test_func,3)
            >>> last
            {'index': None, 'value': None}
            >>>
        '''
        print(doc)
    elif(func_name == "find_which"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> last = find_which(ol,0,test_func,3)
            >>> last
            {'index': 3, 'value': 4}
            >>> last = find_which(ol,2,test_func,3)
            >>> last
            {'index': 5, 'value': 6}
            >>>
        '''
        print(doc)
    elif(func_name == "find_whichnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> last = find_whichnot(ol,0,test_func,3)
            >>> last
            {'index': 0, 'value': 1}
            >>> last = find_whichnot(ol,2,test_func,3)
            >>> last
            {'index': 2, 'value': 3}
            >>>
        '''
        print(doc)
    elif((func_name == "find_some")|(func_name == "find_seqs")):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> some = find_seqs(ol,[0,3],test_func,3)
            >>> some
            [{'index': 3, 'value': 4}, {'index': 6, 'value': 7}]
            >>> some = find_some(ol,[0,1,2],test_func,3)
            >>> some
            [{'index': 3, 'value': 4}, {'index': 4, 'value': 5}, {'index': 5, 'value': 6}]
            >>> #find_some is the same as find_seqs
        '''
        print(doc)
    elif((func_name == "find_somenot")|(func_name == "find_seqsnot")):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> some = find_seqsnot(ol,[0,3],test_func,3)
            >>> some
            [{'index': 0, 'value': 1}]
            >>> some = find_somenot(ol,[0,1,2],test_func,3)
            >>> some
            [{'index': 0, 'value': 1}, {'index': 1, 'value': 2}, {'index': 2, 'value': 3}]
            >>> #find_somenot is the same as find_seqsnot
        '''
        print(doc)
    elif(func_name == "find_all"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> rslt = find_all(ol,test_func,3)
            >>> pobj(rslt)
            [
             {
              'index': 3,
              'value': 4
             },
             {
              'index': 4,
              'value': 5
             },
             {
              'index': 5,
              'value': 6
             },
             {
              'index': 6,
              'value': 7
             }
            ]
            >>>
        '''
        print(doc)
    elif(func_name == "find_allnot"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4,5,6,7]
            >>> rslt = find_allnot(ol,test_func,3)
            >>> pobj(rslt)
            [
             {
              'index': 0,
              'value': 1
             },
             {
              'index': 1,
              'value': 2
             },
             {
              'index': 2,
              'value': 3
             }
            ]
            >>>
        '''
        print(doc)
    elif(func_name == "push"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol=[1,2,3,4]
            >>> id(ol)
            140623821822728
            >>> new = push(ol,5,6,7)
            >>> new
            [1, 2, 3, 4, 5, 6, 7]
            >>> id(new)
            140623820643464
            >>> ####
            ... ol=[1,2,3,4]
            >>> id(ol)
            140623820657992
            >>> rslt = push(ol,5,6,7,mode="original")
            >>> rslt
            [1, 2, 3, 4, 5, 6, 7]
            >>> id(rslt)
            140623820657992
        '''
        print(doc)
    elif(func_name == "includes"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> includes(ol,3)
            True
            >>> includes(ol,5)
            False
            >>>
        '''
        print(doc)
    elif(func_name == "toString"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> toString(ol)
            '[1, 2, 3, 4]'
            >>>
        '''
        print(doc)
    elif(func_name == "toSource"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> toSource(ol)
            '[1, 2, 3, 4]'
            >>>
        '''
        print(doc)
    elif(func_name == "splice"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = ["angel", "clown", "mandarin", "surgeon"]
            >>> id(ol)
            140623819990664
            >>> new = splice(ol,2,0,"drum")
            >>> new
            ['angel', 'clown', 'drum', 'mandarin', 'surgeon']
            >>> id(new)
            140623819969736
            >>> ####
            ... ol = ["angel", "clown", "mandarin", "surgeon"]
            >>> id(ol)
            140623820658056
            >>> new = splice(ol,2,1,"drum",mode="original")
            >>> new
            ['angel', 'clown', 'drum', 'surgeon']
            >>> id(new)
            140623820658056
            >>> ####
            ... ol = [1,2,3,4,5,6]
            >>> id(ol)
            140623821822728
            >>> new = splice(ol,2,2,77,777)
            >>> new
            [1, 2, 77, 777, 5, 6]
            >>> id(new)
            140623820838920
            >>>
        '''
        print(doc)
    elif(func_name == "some"):
        doc = '''
            >>> from xdict.elist import *
            >>> def test_func(ele,x):
            ...     cond = (ele > x)
            ...     return(cond)
            ...
            >>> ol = [1,2,3,4]
            >>> some(ol,test_func,3)
            {'index': 3, 'cond': True}
            >>>
            >>> ol = [1,2,1,3]
            >>> some(ol,test_func,3)
            {'index': None, 'cond': False}
            >>>
        '''
        print(doc)
    elif(func_name == "slice"):
        doc = '''
            >>> ol = [1,2,3,4,5]
            >>> id(ol)
            140623820658056
            >>> new = slice(ol,2,4)
            >>> new
            [3, 4]
            >>> id(new)
            140623819972232
            >>> ####
            ... id(ol)
            140623820658056
            >>> rslt = slice(ol,1,-2,mode="original")
            >>> rslt
            [2, 3]
            >>> id(rslt)
            140623820658056
            >>>
        '''
        print(doc)
    elif(func_name == "shift"):
        doc = '''
            >>> from xdict.jprint import pobj
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> id(ol)
            140623820838920
            >>> rslt = shift(ol)
            >>> pobj(rslt)
            {
             'popped': 1,
             'list':
                     [
                      2,
                      3,
                      4
                     ]
            }
            >>> ol
            [1, 2, 3, 4]
            >>> id(ol)
            140623820838920
            >>> id(rslt['list'])
            140623821822728
            >>> ####
            ... ol = [1,2,3,4]
            >>> id(ol)
            140623819990664
            >>> rslt = shift(ol,mode="original")
            >>> rslt
            1
            >>> ol
            [2, 3, 4]
            >>> id(ol)
            140623819990664
            >>>
        '''
        print(doc)
    elif((func_name == "reduce_left")|(func_name == "array_reduce")|(func_name == "reduceLeft")):
        doc = '''
            >>> from xdict.elist import *
            >>> def callback(accumulator,currentValue):
            ...     accumulator.append(currentValue[0])
            ...     accumulator.append(currentValue[1])
            ...     return(accumulator)
            ...
            >>> ol = [(1,2),("a","b"),("x","y")]
            >>> reduce_left(ol,callback,[])
            [1, 2, 'a', 'b', 'x', 'y']
            >>> #array_reduce, reduceLeft ,reduce_left  are the same
        '''
        print(doc)
    elif((func_name == "reduceRight")|(func_name == "reduce_right")):
        doc = '''
            >>> from xdict.elist import *
            >>> def callback(accumulator,currentValue):
            ...     accumulator.append(currentValue[0])
            ...     accumulator.append(currentValue[1])
            ...     return(accumulator)
            ...
            >>> ol = [(1,2),("a","b"),("x","y")]
            >>> reduce_right(ol,callback,[])
            ['x', 'y', 'a', 'b', 1, 2]
            >>> #reduceRight,reduce_right are the same
        '''
        print(doc)
    elif(func_name == "array_map"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> def map_func(ele,mul,plus):
            ...     return(ele*mul+plus)
            ...
            >>> array_map(ol,map_func,2,100)
            [102, 104, 106, 108]
        '''
        print(doc)
    elif(func_name == "join"):
        doc = '''
            >>> from xdict.elist import *
            >>> ol = [1,2,3,4]
            >>> join(ol,separator="-")
            '1-2-3-4'
            >>>
        '''
        print(doc)
    elif(func_name == "for_each"):
        doc = '''
            >>> from xdict.elist import *
            >>> def show_func(ele):
            ...     print("<{0}>".format(ele))
            ...
            >>> ol = [1,2,3,4]
            >>> for_each(ol,show_func)
            <1>
            <2>
            <3>
            <4>
            >>>
            >>> ####forEach is the same as for_each
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
        '''
        print(doc)
