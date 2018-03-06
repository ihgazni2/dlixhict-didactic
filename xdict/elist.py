# class name initial is  uppercased 
import copy
from operator import itemgetter
from types import MethodType

def select_some(ol,seqs):
    '''
        from xdict.elist import *
        ol = ['a','b','c','d']
        select_some(ol,[1,2])
    '''
    rslt =[]
    for i in range(0,ol.__len__()):
        if(i in seqs):
            ele = ol[i]
            rslt.append(ele)
        else:
            pass
    return(rslt)

def select_seqs(ol,*seqs):
    '''
        from xdict.elist import *
        ol = ['a','b','c','d']
        select_seqs(ol,1,2)
    '''
    seqs = list(seqs)
    rslt =[]
    for i in range(0,ol.__len__()):
        if(i in seqs):
            ele = ol[i]
            rslt.append(ele)
        else:
            pass
    return(rslt)

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
        >>> unshift(ol,9,10,11,12)
        [9, 10, 11, 12, 1, 2, 3, 4]
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(prextend(ol,list(eles),mode=mode))

unshift = prepend_some

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

def push(ol,*eles,**kwargs):
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

def batsorted(referer,*lists,**kwargs):
    '''
        from xdict.elist import *
        referer = [4,2,3,1]
        l1 = ['a','b','c','d']
        l2 = [100,200,300,400]
        l3 = ['A','B','A','B']
        nl1,nl2,nl3 = batsorted(referer,l1,l2,l3)
        nl1
        nl2
        nl3
        nl1,nl2,nl3 = batsorted(referer,l1,l2,l3,reverse=True)
        nl1
        nl2
        nl3
        ####the batsorted will not modify the original lists
        l1
        l2
        l3
    '''
    if('reverse' in kwargs):
        reverse = kwargs['reverse']
    else:
        reverse = False
    length = referer.__len__()
    indexes = list(range(0,length))
    rslt = sorted_refer_to(indexes,referer,reverse=reverse)
    referer = rslt['referer']
    indexes = rslt['list']
    rslt = []
    lists = copy.deepcopy(list(lists))
    for i in range(0,lists.__len__()):
        l = lists[i]
        nl = []
        for j in range(0,length):
            loc = indexes[j]
            nl.append(l[loc])
        rslt.append(nl)
    return(tuple(rslt))

def index_first(ol,value):
    '''
        from xdict.elist import *
        ol = [1,'a',3,'a',4,'a',5]
        index_first(ol,'a')
        ####index_first, array_index, indexOf  are the same
        array_index(ol,'a')
        indexOf(ol,'a')
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
        array_indexnot(ol,'a')
        indexOfnot(ol,'a')
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
        lastIndexOf(ol,'a')
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
        lastIndexOfnot(ol,'a')
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
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
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
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
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
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
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
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
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

def init(len,default_element=None):
    '''
        from xdict.elist import *
        init(5)
        init(5,"x")
    '''
    rslt = []
    for i in range(0,len):
        rslt.append(default_element)
    return(rslt)

def intlize(l):
    '''
        from xdict.elist import *
        l = ["1","3","4","5"]
        intlize(l)
    '''
    return(list(map(lambda ele:int(ele),l)))

def strlize(l):
    '''
        from xdict.elist import *
        l = [1,3,4,5]
        strlize(l)
    '''
    return(list(map(lambda ele:str(ele),l)))

def array_from(obj,func,*args):
    '''
        from xdict.elist import *
        array_from("abcd",None)
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

def comprise(list1,list2,**kwargs):
    '''
        from xdict.elist import *
        comprise([1,2,3,4,5],[2,3,4],mode="loose")
        comprise([1,2,3,4,5],[2,3,4])
        comprise([1,2,3,4,5],[2,3,4],mode="strict")
        comprise([1,2,3,4,5],[1,2,3,4],mode="strict")
        #not recursive ,only one level
        #please refer to ListTree.search for recursive support
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

def join2(ol,*sps):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        join2(ol,"-","+","*")
    '''
    rslt =""
    length = ol.__len__()
    for i in range(0,length-1):
        rslt = rslt + str(ol[i]) + sps[i]
    rslt = rslt + str(ol[length - 1])
    return(rslt)

def htmljoin(ol,sp,**kwargs):
    '''
        ol = [1,2,3,4]
        htmljoin(ol,"option",outer="select")
        
    '''
    if('outer' in kwargs):
        outer = kwargs['outer']
    else:
        outer = ""
    if(outer):
        head = "<" + outer + ">"
        tail = "</" + outer + ">"
    else:
        head = ""
        tail = ""
    rslt = head
    length = ol.__len__()
    begin = "<" + sp + ">"
    end = "</" + sp + ">"
    for i in range(0,length):
        rslt = rslt + begin + str(ol[i]) + end
    rslt = rslt + tail
    return(rslt)

def uniqualize(l,**kwargs):
    '''
        from xdict.elist import *
        l = [1, 2, 2]
        new = uniqualize(l)
        new
        id(l)
        id(new)
        ####
        l = [1, 2, 2]
        rslt = uniqualize(l,mode="original")
        rslt
        id(l)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'new'
    pt = copy.deepcopy(l)
    seqs_for_del =[]
    vset = set({})
    for v in pt:
        vset.add(v)
    tslen = vset.__len__()
    freq = {}
    for i in range(0,pt.__len__()):
        v = pt[i]
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(i)
        else:
            freq[v] = 0
    npt = []
    for i in range(0,pt.__len__()):
        if(i in seqs_for_del):
            pass
        else:
            npt.append(pt[i])
    pt = npt
    if(mode == 'new'):
        return(npt)
    else:
        l.clear()
        l.extend(npt)
        return(l)

def interleave(*arrays,**kwargs):
    '''
        arr1 = [1,2,3,4]
        arr2 = ['a','b','c','d']
        arr3 = ['@','#','%','*']
        interleave(arr1,arr2,arr3)
    '''
    anum = arrays.__len__()
    rslt = []
    length = arrays[0].__len__()
    for j in range(0,length):
        for i in range(0,anum):
            array = arrays[i]
            rslt.append(array[j])
    return(rslt)

#@@@@@@@@@@@@@@@@@@

def for_each(ol,test_func,*args):
    '''
        from xdict.elist import *
        def show_func(ele):
            print("<{0}>".format(ele))
        
        ol = [1,2,3,4]
        for_each(ol,show_func)
        
        ####forEach is the same as for_each
        ####forEach have no return value
    '''
    rslt = (True,None)
    length = ol.__len__()
    for i in range(0,length):
        test_func(ol[i],*args)

forEach = for_each


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

def fill(ol,value,start=None, end=None,**kwargs):
    '''
        from xdict.elist import *
        ol = [1, 2, 3,4,5]
        id(ol)
        rslt = fill(ol,4)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3,4,5]
        id(ol)
        rslt = fill(ol,4,1)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3,4,5]
        id(ol)
        rslt = fill(ol,6,1,3,mode="original")
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


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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


#@@@@@@@@@@@@@@@@
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

def array_map2(*referls,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        refl1 = ['+','+','+','+']
        refl2 = [7,7,7,7]
        refl3 = ['=','=','=','=']
        def map_func(ele,ref_ele1,ref_ele2,ref_ele3,prefix,suffix):
            s = prefix+': ' + str(ele) + str(ref_ele1) + str(ref_ele2) + str(ref_ele3) + suffix
            return(s)
        
        ####
        rslt = array_map2(ol,refl1,refl2,refl3,map_func=map_func,map_func_args=['Q','?'])
        pobj(rslt)
    '''
    map_func = kwargs['map_func']
    if('map_func_args' in kwargs):
        map_func_args = kwargs['map_func_args']
    else:
        map_func_args = []
    length = referls.__len__()
    rslt = []
    anum = list(referls)[0].__len__()
    for j in range(0,anum):
        args = []
        for i in range(0,length):
            refl = referls[i]
            args.append(refl[j])
        args.extend(map_func_args)
        v = map_func(*args)
        rslt.append(v)
    return(rslt)

def array_dualmap(ol,value_map_func,**kwargs):
    '''
        from xdict.elist import *
        ol = ['a','b','c','d']
        def index_map_func(index,prefix,suffix):
            s = prefix +str(index+97)+ suffix
            return(s)
        
        def value_map_func(mapped_index,ele,prefix,suffix):
            s = prefix+mapped_index+': ' + str(ele) + suffix
            return(s)
        
        ####
        rslt = array_dualmap2(ol,index_map_func=index_map_func,index_map_func_args=[': ',' is '],value_map_func=value_map_func,value_map_func_args=['ord',' yes?'])
        pobj(rslt)
    '''
    def get_self(obj):
        return(obj)
    if('index_map_func_args' in kwargs):
        index_map_func_args = kwargs['index_map_func_args']
    else:
        index_map_func_args = []
    if('value_map_func_args' in kwargs):
        value_map_func_args = kwargs['value_map_func_args']
    else:
        value_map_func_args = []
    if('index_map_func' in kwargs):
        index_map_func = kwargs['index_map_func']
    else:
        index_map_func = get_self
    length = ol.__len__()
    il = list(range(0,length))
    nil = list(map(lambda ele:index_map_func(ele,*index_map_func_args),il))
    nvl = []
    for i in range(0,length):
        ele = ol[i]
        v = value_map_func(nil[i],ele,*value_map_func_args)
        nvl.append(v)
    return(nvl)

def array_dualmap2(*refls,**kwargs):
    '''
        from xdict.elist import *
        ol = [1,2,3,4]
        refl1 = ['+','+','+','+']
        refl2 = [7,7,7,7]
        refl3 = ['=','=','=','=']
        def index_map_func(index):
            s ="<"+str(index)+">"
            return(s)
        
        def value_map_func(mapped_index,ele,ref_ele1,ref_ele2,ref_ele3,prefix,suffix):
            s = prefix+mapped_index+': ' + str(ele) + str(ref_ele1) + str(ref_ele2) + str(ref_ele3) + suffix
            return(s)
        
        ####
        rslt = array_dualmap2(ol,refl1,refl2,refl3,index_map_func=index_map_func,value_map_func=value_map_func,value_map_func_args=['Q','?'])
        pobj(rslt)
    '''
    def get_self(obj,*args):
        return(obj)
    if('value_map_func_args' in kwargs):
        value_map_func_args = kwargs['value_map_func_args']
    else:
        value_map_func_args = []
    if('index_map_func' in kwargs):
        index_map_func = kwargs['index_map_func']
    else:
        index_map_func = get_self
    if('index_map_func_args' in kwargs):
        index_map_func_args = kwargs['index_map_func_args']
    else:
        index_map_func_args = []
    length = ol.__len__()
    il = list(range(0,length))
    nil = list(map(lambda ele:index_map_func(ele,*index_map_func_args),il))
    refls = list(refls)
    refls = prepend(refls,nil)
    nvl = array_map2(*refls,map_func = value_map_func,map_func_args=value_map_func_args)
    return(nvl)

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

#






def diff_indexes(l1,l2):
    '''
        from xdict.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        diff_indexes(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]!=l2[i]):
            rslt.append(i)
    return(rslt)

def diff_values(l1,l2):
    '''
        from xdict.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        diff_values(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]!=l2[i]):
            rslt.append(l1[i])
    return(rslt)

def same_indexes(l1,l2):
    '''
        from xdict.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        same_indexes(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]==l2[i]):
            rslt.append(i)
    return(rslt)

def same_values(l1,l2):
    '''
        from xdict.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        same_values(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]==l2[i]):
            rslt.append(l1[i])
    return(rslt)

def value_indexes_mapping(l):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        l = ['a','b','b','a','c','b']
        desc = value_indexes_mapping(l)
        pobj(desc)
    '''
    pt = copy.deepcopy(l)
    desc = {}
    vset = set({})
    for v in pt:
        vset.add(v)
    for v in vset:
        desc[v] = []
    for i in range(0,l.__len__()):
        desc[l[i]].append(i)
    return(desc)

def getitem_via_pathlist(ol,pathlist):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_pathlist(y,[1,1])
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def getitem_via_pathlist2(pathlist,ol):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_pathlist2([1,1],y)
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def getitem_via_sibseqs(ol,*sibseqs):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_sibseqs(y,1,1)
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def setitem_via_pathlist(ol,value,pathlist):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_pathlist(y,"500",[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)

def setitem_via_sibseqs(ol,value,*sibseqs):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_sibseqs(y,"500",1,1)
        y
    '''
    this = ol
    pathlist = list(sibseqs)
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)

def delitem_via_pathlist(ol,pathlist):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_pathlist(y,[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)

def delitem_via_sibseqs(ol,*sibseqs):
    '''
        from xdict.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_sibseqs(y,1,1)
        y
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)

def is_list(obj):
    '''
        from xdict.elist import *
        is_list([1,2,3])
        is_list(200)
    '''
    if(type(obj)==type([])):
        return(True)
    else:
        return(False)

isArray = is_list












#the below is for nested analysis

def is_leaf(obj):
    '''
        the below is for nested-list
        any type is not list will be treated as a leaf
        empty list will be treated as a leaf
        from xdict.elist import *
        is_leaf(1)
        is_leaf([1,2,3])
        is_leaf([])
    '''
    if(is_list(obj)):
        length = obj.__len__()
        if(length == 0):
            return(True)
        else:
            return(False)
    else:
        return(True)

class LevelCache():
    '''
        current level unhandled_data stored in .data
        current level unhandled_desc stored in .desc
        next level unhandled_data stored in .ndata
        next level unhandled_desc stored in .ndesc
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('datas' in kwargs):
            datas = kwargs['datas']
        else:
            datas = []
        if('descs' in kwargs):
            descs = kwargs['descs']
        else:
            descs = []
        self.data = [datas]
        self.desc = [descs]
        self.ndata = []
        self.ndesc = []
    def update(self):
        self.data = self.ndata
        self.desc = self.ndesc
        self.ndata = []
        self.ndesc = []
    def __repr__(self):
        print("data: {0}".format(self.data))
        print("desc: {0}".format(self.desc))
        print("ndata: {0}".format(self.ndata))
        print("ndesc: {0}".format(self.ndesc),end='')
        return("")
    def clear(self):
        self.data = []
        self.desc = []
        self.ndata = []
        self.ndesc = []

class StateCache():
    '''
        parent level handled_desc stored in .pdesc_level
        current level handled_desc stored in .desc_level
        过早优化乃万恶之源，之所以有LevelCache 和 StateCache 两个Cache 是为了利用我之前的旧代码，弃之可惜，尾大不掉
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,root_matrix):
        #there is only one level in root_matrix: level 0
        #there is only one element in root_matrix level 0 :element 0 
        self.matrix = root_matrix
        self.depth = 0
        self.pdesc_level = []
        self.desc_level = self.matrix[0]
    def update(self):
        self.pdesc_level = self.desc_level
        self.matrix.append([])
        self.depth = self.depth + 1
        self.desc_level = self.matrix[self.depth]
    def __repr__(self):
        print("depth: {0}".format(self.depth))
        print("pdesc_level: {0}".format(self.pdesc_level))
        print("desc_level: {0}".format(self.desc_level),end='')
        return("")

def pcache_bind_dynamic_method(pcache,**kwargs):
    '''
    '''
    mn = kwargs['method_name']
    func = kwargs['func']
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    cond = (mn in method_names)
    if(cond):
        pcache.__setattr__(mn, MethodType(func,pcache))
    else:
        pass
    return(pcache)

def init_pcache_handler_inline(kwargs):
    pcache = PointerCache()
    for mn in kwargs:
        cond = (mn in ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler'])
        if(cond):
            func = kwargs[mn]
            pcache.__setattr__(mn, MethodType(func,pcache))
        else:
            pass
    return(pcache)

def pcache_reset_methods(pcache,**kwargs):
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.leaf
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    funcs = [get_children_handler,parent_handler,child_begin_handler,leaf_handler,non_leaf_handler,child_end_handler]
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    for i in range(0,funcs.__len__()):
        mn = method_names[i]
        func = funcs[i]
        pcache.__setattr__(mn, MethodType(func,pcache))
    return(pcache)

class PointerCache():
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        pdesc['leaf_descendant_paths'] = []
        pdesc['non_leaf_descendant_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['non_leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    def update_pdesc(self,lcache,i):
        self.unhandled_seq = i
        self.pdata = lcache.data[i]
        self.children = self.get_children_handler(*self.get_children_handler_args)
        self.sibs_len = self.children.__len__()
        self.pdesc = self.parent_handler(lcache,i,*self.parent_handler_args)
    def update_desc(self,lcache,scache,sib_seq):
        self.sib_seq = sib_seq
        self.data = self.children[self.sib_seq]
        self.desc = self.child_begin_handler(scache)
        if(is_leaf(self.data)):
            self.leaf_handler()
        else:
            self.non_leaf_handler(lcache)
        self.child_end_handler(scache)
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('get_children_handler_args' in kwargs):
            self.get_children_handler_args = kwargs['get_children_handler_args']
        else:
            self.get_children_handler_args = []
        if('parent_handler_args' in kwargs):
            self.parent_handler_args = kwargs['parent_handler_args']
        else:
            self.parent_handler_args = []
        if('child_begin_handler_args' in kwargs):
            self.child_begin_handler_args = kwargs['child_begin_handler_args']
        else:
            self.child_begin_handler_args = []
        if('leaf_handler_args' in kwargs):
            self.leaf_handler_args = kwargs['leaf_handler_args']
        else:
            self.leaf_handler_args = []
        if('non_leaf_handler_args' in kwargs):
            self.non_leaf_handler_args = kwargs['non_leaf_handler_args']
        else:
            self.non_leaf_handler_args = []
        if('child_end_handler_args' in kwargs):
            self.child_end_handler_args = kwargs['child_end_handler_args']
        else:
            self.child_end_handler_args = []
        self.unhandled_seq = None
        self.children = None
        self.sibs_len = None
        self.pdesc = None
        self.sib_seq = None
        self.data = None
        self.desc = None

##the below is for each element desc handle
def new_ele_description(**kwargs):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        root_desc = new_ele_description(leaf=False,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
        pobj(root_desc)
        #None means not handled
    '''
    desc = {
        'leaf':None,
        'depth':None,
        'breadth':None,
        'breadth_path':None,
        'sib_seq':None,
        'path':None,
        'parent_path':None,
        'parent_breadth_path':None,
        'lsib_path':None,
        'rsib_path':None,
        'lcin_path':None,
        'rcin_path':None,
        'sons_count':None,
        'leaf_son_paths':None,
        'non_leaf_son_paths':None,
        'leaf_descendant_paths':None,
        'non_leaf_descendant_paths':None,
        'flat_offset':None,
        'flat_len':None
    }
    for key in kwargs:
        desc[key.lower()] = kwargs[key]
    return(desc)

def root_list(*args):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        root_list([1],2,[1,2,3])
    '''
    return(list(args))

def init_desc_matrix(l):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        pobj(desc_matrix)
    '''
    leaf = is_leaf(l)
    root_desc = new_ele_description(leaf=leaf,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
    if(leaf):
        root_desc['sons_count'] = 0
    else:
        pass
    desc_matrix = [
        [root_desc]
    ]
    return(desc_matrix)

def reset_parent_desc_template(desc):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        pobj(desc)
        tem = reset_parent_desc_template(desc)
        pobj(tem)
        #only inherit path  and breadth_path
    '''
    tem = new_ele_description()
    tem['path'] = desc['path']
    tem['breadth_path'] = desc['breadth_path']
    return(tem)

def _init_unhandled(l,inited_matrix):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        unhandled = _init_unhandled(l,desc_matrix)
        unhandled_data = unhandled['data']
        unhandled_desc = unhandled['desc']
        unhandled_data[0]
        unhandled_desc[0]
        unhandled_data[1]
        unhandled_desc[1]
    '''
    root_desc = inited_matrix[0][0]
    unhandled = {'data':[],'desc':[]}
    length = l.__len__()
    root_desc['sons_count'] = length
    root_desc['leaf_son_paths'] = []
    root_desc['non_leaf_son_paths'] = []    
    if(length == 0):
        pass
    else:
        inited_matrix.append([])
        level = inited_matrix[1]
        for i in range(0,length):
            child = l[i]
            desc = copy.deepcopy(root_desc)
            desc = reset_parent_desc_template(desc)
            desc['depth'] = 1
            desc['breadth'] = i
            desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
            desc['breadth_path'].append(i)
            desc['sib_seq'] = i
            desc['parent_path'] = copy.deepcopy(desc['path'])
            desc['path'].append(i)
            if(i==0):
                pass
            else:
                desc['lsib_path'] = [i-1]
            if(i == (length - 1)):
                pass
            else:
                desc['rsib_path'] = [i+1]
            if(is_leaf(child)):
                desc['leaf'] = True
                desc['sons_count'] = 0
                root_desc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
            else:
                desc['leaf'] = False
                root_desc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
                unhandled['data'].append(child)
                unhandled['desc'].append(desc)
            level.append(desc)
    return(unhandled)

def update_desc_lsib_path(desc):
    '''
        leftSibling
        previousSibling
        leftSib
        prevSib
        lsib
        psib
        
        have the same parent,and on the left
    '''
    if(desc['sib_seq']>0):
        lsib_path = copy.deepcopy(desc['path'])
        lsib_path[-1] = desc['sib_seq']-1
        desc['lsib_path'] = lsib_path
    else:
        pass
    return(desc)

def update_desc_rsib_path(desc,sibs_len):
    '''
        rightSibling
        nextSibling
        rightSib
        nextSib
        rsib
        nsib
        
        have the same parent,and on the right
    '''
    if(desc['sib_seq']<(sibs_len-1)):
        rsib_path = copy.deepcopy(desc['path'])
        rsib_path[-1] = desc['sib_seq']+1
        desc['rsib_path'] = rsib_path
    else:
        pass
    return(desc)

def update_desc_lcin_path(desc,pdesc_level):
    '''
        leftCousin
        previousCousin
        leftCin
        prevCin
        lcin
        pcin
        
        parents are neighbors,and on the left
    '''
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==0):
        if(parent_breadth==0):
            pass
        else:
            parent_lsib_breadth = parent_breadth - 1
            plsib_desc = pdesc_level[parent_lsib_breadth]
            if(plsib_desc['leaf']):
                pass
            else:
                lcin_path = copy.deepcopy(plsib_desc['path'])
                lcin_path.append(plsib_desc['sons_count'] - 1)
                desc['lcin_path'] = lcin_path
    else:
        pass
    return(desc)

def update_desc_rcin_path(desc,sibs_len,pdesc_level):
    '''
        rightCousin
        nextCousin
        rightCin
        nextCin
        rcin
        ncin
        
        parents are neighbors,and on the right
    '''
    psibs_len = pdesc_level.__len__()
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==(sibs_len - 1)):
        if(parent_breadth==(psibs_len -1)):
            pass
        else:
            parent_rsib_breadth = parent_breadth + 1
            prsib_desc = pdesc_level[parent_rsib_breadth]
            #because from left to right to handle each level
            #sons_count will only be updated in the next-round 
            if(prsib_desc['leaf']):
                pass
            else:
                rcin_path = copy.deepcopy(prsib_desc['path'])
                rcin_path.append(0)
                desc['rcin_path'] = rcin_path
    else:
        pass
    return(desc)

def scan(l,**kwargs):
    '''
        from xdict.elist import *
        from xdict.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc = description(l)
        l = [1,2,[4],[3,[5,6]]]
        desc = description(l)
    '''
    if('iter' in kwargs):
        iter = True
    else:
        iter = False
    ####level ==  0
    desc_matrix = init_desc_matrix(l)
    if(desc_matrix[0][0]['leaf'] == True):
        return(desc_matrix)
    else:
        pass
    ####cache
    lcache=LevelCache(datas=l,descs=desc_matrix[0][0])
    scache=StateCache(desc_matrix)
    pcache = init_pcache_handler_inline(kwargs)
    ####level > 0
    while(lcache.data.__len__() > 0):
        #add next desc_level 
        scache.update()
        for unhandled_seq in range(0,lcache.data.__len__()):
            #handle parent
            pcache.update_pdesc(lcache,unhandled_seq)
            for sib_seq in range(0,pcache.sibs_len):
                #handle child
                pcache.update_desc(lcache,scache,sib_seq)
        #update level lcache
        lcache.update()
    return(desc_matrix)

class DescMatrix():
    '''
    '''
    def __init__(self,matrix):
        self.matrix = matrix
    @classmethod
    def loc(cls,desc):
        return([desc['depth'],desc['breadth']])
    @classmethod
    def ploc(cls,desc):
        if(desc['parent_breadth_path'] == []):
            col = 0
        else:
            col = desc['parent_breadth_path'][-1]
        if(desc['depth'] == 0):
            row = 0
        else:
            row = desc['depth']-1
        return([row,col])
    def pdesc(self,desc):
        pd = getitem_via_pathlist(self.matrix,self.ploc(desc))
        return(pd)

def fullfill_descendants_info(desc_matrix):
    '''
       flat_offset
    '''
    pathloc_mapping = {}
    locpath_mapping = {}
    #def leaf_handler(desc,pdesc,offset):
    def leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+1)
        desc['non_leaf_son_paths'] = []
        desc['leaf_son_paths'] = []
        desc['non_leaf_descendant_paths'] = []
        desc['leaf_descendant_paths'] = []
        desc['flat_len'] = 1
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + 1
        else:
            pdesc['flat_len'] = 1
    #def non_leaf_handler(desc,pdesc,offset):
    def non_leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+desc['flat_len'])
        pdesc['non_leaf_descendant_paths'].extend(copy.deepcopy(desc['non_leaf_descendant_paths']))
        pdesc['leaf_descendant_paths'].extend(copy.deepcopy(desc['leaf_descendant_paths']))
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + desc['flat_len']
        else:
            pdesc['flat_len'] = desc['flat_len']
    def fill_path_mapping(desc):
        pmk = tuple(desc['path'])
        pmv = tuple(DescMatrix.loc(desc))
        pathloc_mapping[pmk] = pmv
        locpath_mapping[pmv] = pmk
    dm = DescMatrix(desc_matrix)
    depth = desc_matrix.__len__()
    desc_level = desc_matrix[depth - 1]
    length = desc_level.__len__()
    #the last level
    #offset = 0
    for j in range(length - 1,-1,-1):
        desc = desc_level[j]
        fill_path_mapping(desc)
        pdesc = dm.pdesc(desc)
        leaf_handler(desc,pdesc)
        #leaf_handler(desc,pdesc,offset)
        #offset = offset + 1
    for i in range(depth-2,0,-1):
        #offset = 0
        desc_level = desc_matrix[i]
        length = desc_level.__len__()
        for j in range(length-1,-1,-1):
            desc = desc_level[j]
            fill_path_mapping(desc)
            pdesc = dm.pdesc(desc)
            if(desc['leaf']):
                leaf_handler(desc,pdesc)
                #leaf_handler(desc,pdesc,offset)
                #offset = offset + 1
            else:
                non_leaf_handler(desc,pdesc)
                #non_leaf_handler(desc,pdesc,offset)
                #offset = offset + desc['flat_len']
    desc_matrix[0][0]['flat_offset'] = (0,desc_matrix[0][0]['flat_len'])
    for i in range(0,depth-1):
        pdesc_level = desc_matrix[i]
        length = pdesc_level.__len__()
        for j in range(0,length):
            pdesc = pdesc_level[j]
            si = pdesc['flat_offset'][0]
            for i in range(0,pdesc['sons_count']):
                spl = append(pdesc['path'],i,mode='new')
                pk = tuple(spl)
                locx,locy = pathloc_mapping[pk]
                son = desc_matrix[locx][locy]
                ei = si + son['flat_len']
                son['flat_offset'] = (si,ei)
                si = ei
    return(desc_matrix,pathloc_mapping,locpath_mapping)

def pathlist_to_getStr(path_list):
    '''
        >>> pathlist_to_getStr([1, '1', 2])
            "[1]['1'][2]"
        >>>
    '''
    t1 = path_list.__repr__()
    t1 = t1.lstrip('[')
    t1 = t1.rstrip(']')
    t2 = t1.split(", ")
    s = ''
    for i in range(0,t2.__len__()):
        s = ''.join((s,'[',t2[i],']'))
    return(s)


####from xdict.jprint

def get_block_op_pairs(pairs_str):
    '''
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

def get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    ''' the first-char is level-1
        when current is  non-op, next-char-level = curr-level
        when current is  lop,  non-paired-rop-next-char-level = lop-level+1;
        when current is  lop,  paired-rop-next-char-level = lop-level
        when current is  rop,  next-char-level = rop-level - 1
        # {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {......
        # 122222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333333333333334......
        # {\n"key_4_UF0aJJ6v": "value_1", \n"key_2_Hd0t": [\n"value_16", \n"value_8", \n"value_8", \n"value_15", \n"value_14", \n"value_19",...... 
        # 1 222222222222222222222222222222 2222222222222222 3333333333333 333333333333 333333333333 3333333333333 3333333333333 3333333333333...... 
        '''
    curr_ch = j_str[curr_seq]
    next_ch = j_str[curr_seq + 1]
    cond = 0
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(curr_ch == block_op_pairs_dict[i][0]):
            if(next_ch == block_op_pairs_dict[i][1]):
                next_lv = curr_lv               
            else:
                next_lv = curr_lv + 1
            cond = 1
            break
        elif(curr_ch == block_op_pairs_dict[i][1]):
            if(is_rop(next_ch,block_op_pairs_dict)):
                next_lv = curr_lv - 1
            else:
                next_lv = curr_lv
            cond = 1
            break
        else:
            pass
    if(cond == 1):
        pass
    elif(is_rop(next_ch,block_op_pairs_dict)):
        next_lv = curr_lv - 1
    else:    
        next_lv = curr_lv
    curr_lv = next_lv
    curr_seq = curr_seq + 1
    return(curr_lv,curr_lv,curr_seq)

def get_j_str_lvs_dict(j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    j_str_len = j_str.__len__()
    j_str_lvs_dict = {}
    if( j_str_len == 0):
        j_str_lvs_dict = {}
    elif(j_str_len == 1):
        j_str_lvs_dict = {0:1}
    else:
        curr_lv = 1
        j_str_lvs_dict = {0:1}
        seq = 1
        curr_seq = 0
        while(curr_seq < j_str_len - 1):
            level,curr_lv,curr_seq = get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict)
            j_str_lvs_dict[seq] =level
            seq = seq + 1
    return(j_str_lvs_dict)



####from xdict.utils
def str_display_width(s):
    '''
        from xdict.utils import *
        str_display_width('a')
        str_display_width('去')
    '''
    s= str(s)
    width = 0
    len = s.__len__()
    for i in range(0,len):
        sublen = s[i].encode().__len__()
        sublen = int(sublen/2 + 1/2)
        width = width + sublen
    return(width)

####from xdict.ltdict
def ltdict2list(ltdict):
    l = []
    length = ltdict.__len__()
    for i in range(0,length):
        l.append(ltdict[i])
    return(l)

####beautiful display
def spacize(s,lvnum):
    lvs = get_j_str_lvs_dict(s)
    lvs = ltdict2list(lvs)
    sl=list(s)
    length = sl.__len__()
    rslt =''
    for i in range(0,length):
        if(lvs[i]>=lvnum):
            rslt = rslt + sl[i]
        else:
            rslt = rslt + chr(32)*str_display_width(sl[i])
    return(rslt)

def table(l,depth,**kwargs):
    if('no_return' in kwargs):
        no_return = kwargs['no_return']
    else:
        no_return = True
    s = l.__str__()
    rslt = ''
    for i in range(1,depth+1):
        rslt = rslt + spacize(s,i) + '\n'
    rslt = rslt[:-1]
    if(no_return):
        print(rslt)
    else:
        return(rslt)

####

class ListTree():
    '''
        
        
        ltree.parent_path(3,1,0)
        ltree.parent(3,1,0)
        
        ltree.son_paths(3)
        ltree.sons(3)
        ltree.son_paths(3,leaf_only=True)
        ltree.son_paths(3,non_leaf_only=True)
        ltree.sons(3,leaf_only=True)
        ltree.sons(3,non_leaf_only=True)
        
        ltree.descendant_paths(3)
        ltree.descendants(3)
        ltree.descendant_paths(3,from_lv=3)
        ltree.descendants(3,from_lv=3)
        ltree.descendant_paths(3,from_lv=2,to_lv=2)
        ltree.descendants(3,from_lv=2,to_lv=2)
        ltree.descendant_paths(3,leaf_only=True)
        ltree.descendants(3,leaf_only=True)
        ltree.descendant_paths(3,non_leaf_only=True)
        ltree.descendants(3,non_leaf_only=True)
        
        ltree.ancestor_paths(3,1,0)
        ltree.ancestors(3,1,0)
    '''
    def __init__(self,l):
        self.list = l
        self.desc = scan(l)
        self.desc,self.pathloc_mapping,self.locpath_mapping= fullfill_descendants_info(self.desc)
        self.depth = self.desc.__len__()
        self.maxLevelWidth = max(array_map(self.desc,len))
        self.flatWidth = self.desc[0][0]['flat_len']
        self.total = self.desc[0][0]['leaf_descendant_paths'].__len__() + self.desc[0][0]['non_leaf_descendant_paths'].__len__()
        self.trace = self.tree(show=False)
        self.prevSibling = self.lsib
        self.prevSibPath = self.lsib_path
        self.nextSibling = self.rsib
        self.nextSibPath = self.rsib_path
        self.precedingSibPaths = self.preceding_sib_paths
        self.precedingSibs = self.preceding_sibs
        self.followingSibPaths = self.following_sib_paths
        self.followingSibs = self.following_sibs
        self.someSibPaths = self.some_sib_paths
        self.someSibs = self.some_sibs
        self.whichSibPath = self.which_sib_path
        self.whichSib = self.which_sib
        self.showlog = None
    def __repr__(self):
        s = table(self.list,self.depth,no_return=0)
        showl = s.split('\n')
        self.showlog = showl
        return(s)
    def tree(self,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        if('show' in kwargs):
            show = kwargs['show']
        else:
            show = True
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pathlist_to_getStr)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        if(show):
            forEach(showl,print)
            self.showlog = ['tree -'+prompt+' :']
            self.showlog.extend(showl)
        else:
            pass
        return(nrslt)
    def level(self,lvnum,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        desc_level = self.desc[lvnum]
        lpls = []
        nlpls = []
        for i in range(0,desc_level.__len__()):
            desc = desc_level[i]
            pathlist = copy.deepcopy(desc['path'])
            if(desc['leaf']):
                lpls.append(pathlist)
            else:
                nlpls.append(pathlist)
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        showl = array_map(rslt,pathlist_to_getStr)
        rslt,showl = batsorted(rslt,rslt,showl)
        forEach(showl,print)
        self.showlog = ['level -' +prompt+' ' +str(lvnum)+' :']
        self.showlog.extend(showl)
    def flatten(self):
        lpls = self.tree(leaf_only=True,show=False)
        flat = array_map(lpls,getitem_via_pathlist2,self.list)
        return(flat)
    def include(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        try:
            getitem_via_pathlist(self.list,pl)
        except:
            return(False)
        else:
            return(True)
    def __getitem__(self,*sibseqs):
        #this is a trick for __getitem__
        sibseqs = sibseqs[0]
        return(getitem_via_sibseqs(self.list,*sibseqs))
    def loc(self,*sibseqs):
        pl = list(sibseqs)
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def path(self,locx,locy):
        loc = (locx,locy)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    def path2loc(self,pathlist):
        pl = pathlist
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def loc2path(self,loc):
        loc = tuple(loc)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    @classmethod
    def showroute(cls,arr):
        def arrow(ele):
            return(str(ele)+' ->')
        arr = array_map(arr,arrow)
        forEach(arr,print)
        return(arr)
    def dig(self,howmanysteps=None):
        if(howmanysteps):
            pass
        else:
            howmanysteps = self.total
        self.showlog = ['dig -steps '+howmanysteps+' :']
        self.showlog.extend(self.showroute(self.trace[:howmanysteps]))
        return(self.trace[:howmanysteps])
    def parent(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        loc = self.path2loc(pl)
        ppl = self.desc[loc[0]][loc[1]]['parent_path']
        value = getitem_via_pathlist(self.list,ppl)
        return(value)
    def parent_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        return(ppl)
    def son_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= batsorted(rslt,rslt)
        return(rslt)
    def sons(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= batsorted(rslt,rslt)
        rslt = array_map(rslt,getitem_via_pathlist2,self.list)
        return(rslt)
    def descendant_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = batsorted(nrslt,nrslt)
        return(nrslt)
    def descendants(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = batsorted(nrslt,nrslt)
        nrslt = array_map(nrslt,getitem_via_pathlist2,self.list)
        return(nrslt)
    @classmethod
    def ancestlize(cls,l,**kwargs):
        length = l.__len__()
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = length - 2
        nrslt = []
        si = from_lv - 1
        ei = to_lv + 1
        for i in range(si,ei):
            pl = l[:(i+1)]
            nrslt.append(pl)
        return(nrslt)
    def ancestor_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        return(anps)
    def ancestors(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        ans = array_map(anps,getitem_via_pathlist2,self.list)
        return(ans)
    def lsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        return(lsibp)
    def lsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        lsibv = getitem_via_pathlist(self.list,lsibp) 
        return(lsibv)
    def rsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        return(rsibp)
    def rsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        rsibv = getitem_via_pathlist(self.list,rsibp) 
        return(rsibv)
    def lcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        return(lcinp)
    def lcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        lcinv = getitem_via_pathlist(self.list,lcinp) 
        return(lcinv)
    def rcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        return(rcinp)
    def rcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        rcinv = getitem_via_pathlist(self.list,rcinp) 
        return(rcinv)
    def sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        return(sibps)
    def sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibvs = array_map(sibps,getitem_via_pathlist2,self.list)
        return(sibvs)
    def preceding_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            return(sibps)
        else:
            return(sibps[:seq])
    def preceding_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            pre = sibps
        else:
            pre = sibps[:seq]
        sibvs = array_map(pre,getitem_via_pathlist2,self.list)
        return(sibvs)
    def following_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        return(follow)
    def following_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        sibvs = array_map(follow,getitem_via_pathlist2,self.list)
        return(sibvs)
    def some_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibps = select_some(sibps,some)
        return(sibps)
    def some_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibps = select_some(sibps,some)
        sibvs = array_map(sibps,getitem_via_pathlist2,self.list)
        return(sibvs)
    def which_sib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        return(sibp)
    def which_sib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        sibv = getitem_via_pathlist(self.list,sibp)
        return(sibv)
    def search(self,value,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = getitem_via_pathlist(self.list,pl)
            cond3 = (v == value)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pathlist_to_getStr)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        if(type(value)==type("")):
            vstr = '"' + str(value) + '"'
        else:
            vstr = str(value)
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl)
        forEach(showl,print)
        return(nrslt)
    def cond_search(self,**kwargs):
        ###
        cond_func = kwargs['cond_func']
        if('cond_func_args' in kwargs):
            cond_func_args = kwargs['cond_func_args']
        else:
            cond_func_args = []
        ###
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        nvs = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = getitem_via_pathlist(self.list,pl)
            cond3 = cond_func(v,pl,*cond_func_args)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
                nvs.append(v)
            else:
                pass
        def showlog_append(ele1,ele2,*args):
            return(ele1 + ' : ' + str(ele2))
        showl = array_map(nrslt,pathlist_to_getStr)
        showl2 = array_map2(showl,nvs,map_func=showlog_append)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        func_name = cond_func.__name__
        vstr = 'ele_value,ele_pathlist,' +str(cond_func_args)[1:-1]
        vstr = func_name + '(' + vstr + ')'
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl2)
        forEach(showl,print)
        return(nrslt)

def help(func_name):
    if(func_name == "select_some"):
        doc = '''
            from xdict.elist import *
            >>> ol = ['a','b','c','d']
            >>> select_some(ol,[1,2])
            ['b', 'c']
        '''
        print(doc)
    elif(func_name == "select_seqs"):
        doc = '''
            from xdict.elist import *
            >>> ol = ['a','b','c','d']
            >>> select_seqs(ol,[1,2])
            ['b', 'c']
        '''
        print(doc)
    elif(func_name == "extend"):
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
    elif(func_name == "batsorted"):
        doc = '''
            >>> referer = [4,2,3,1]
            >>> l1 = ['a','b','c','d']
            >>> l2 = [100,200,300,400]
            >>> l3 = ['A','B','A','B']
            >>> nl1,nl2,nl3 = batsorted(referer,l1,l2,l3)
            >>> nl1
            ['d', 'b', 'c', 'a']
            >>> nl2
            [400, 200, 300, 100]
            >>> nl3
            ['B', 'B', 'A', 'A']
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
    elif((func_name == "for_each")|(func_name == "forEach")):
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
    elif(func_name == "intlize"):
        doc = '''
            >>> from xdict.elist import *
            >>> l = [1,3,4,5]
            >>> intlize(l)
            [1, 3, 4, 5]
            >>>
        '''
        print(doc)
    elif(func_name == "strlize"):
        doc = '''
            >>> from xdict.elist import *
            >>> l = [1,3,4,5]
            >>> strlize(l)
            ['1', '3', '4', '5']
            >>>
        '''
        print(doc)
    elif(func_name == "diff_indexes"):
        doc = '''
            >>> from xdict.elist import *
            >>> l1 = [1,2,3,5]
            >>> l2 = [0,2,3,4]
            >>> diff_indexes(l1,l2)
            [0, 3]
            >>>
        '''
        print(doc)
    elif(func_name == "diff_values"):
        doc = '''
            >>> from xdict.elist import *
            >>> l1 = [1,2,3,5]
            >>> l2 = [0,2,3,4]
            >>> diff_values(l1,l2)
            [1, 5]
            >>>
        '''
        print(doc)
    elif(func_name == "same_indexes"):
        doc = '''
            >>> from xdict.elist import *
            >>> l1 = [1,2,3,5]
            >>> l2 = [0,2,3,4]
            >>> same_indexes(l1,l2)
            [1, 2]
            >>>
        '''
        print(doc)
    elif(func_name == "same_values"):
        doc = '''
            >>> from xdict.elist import *
            >>> l1 = [1,2,3,5]
            >>> l2 = [0,2,3,4]
            >>> same_values(l1,l2)
            [2, 3]
            >>>
        '''
        print(doc)
    elif(func_name == "init"):
        doc = '''
            >>> from xdict.elist import *
            >>> init(5)
            [None, None, None, None, None]
            >>> init(5,"x")
            ['x', 'x', 'x', 'x', 'x']
            >>>
        '''
        print(doc)
    elif(func_name == "uniqualize"):
        doc = '''
            >>> from xdict.elist import *
            >>> l = [1, 2, 2]
            >>> new = uniqualize(l)
            >>> new
            [1, 2]
            >>> id(l)
            140623819972232
            >>> id(new)
            140623819972104
            >>> ####
            ... l = [1, 2, 2]
            >>> rslt = uniqualize(l,mode="original")
            >>> rslt
            [1, 2]
            >>> id(l)
            140623819970696
            >>> id(rslt)
            140623819970696
            >>>
        '''
        print(doc)
    elif(func_name == "value_indexes_mapping"):
        doc = '''
            >>> from xdict.utils import *
            >>> from xdict.jprint import pobj
            >>> l = ['a','b','b','a','c','b']
            >>> desc = value_indexes_mapping(l)
            >>> pobj(desc)
            {
             'c':
                  [
                   4
                  ],
             'a':
                  [
                   0,
                   3
                  ],
             'b':
                  [
                   1,
                   2,
                   5
                  ]
            }
            >>>
        '''
        print(doc)
    elif(func_name == "getitem_via_pathlist"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> getitem_via_pathlist(y,[1,1])
            ['bb']
        '''
        print(doc)
    elif(func_name == "getitem_via_pathlist2"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> getitem_via_pathlist2([1,1],y)
            ['bb']
        '''
        print(doc)
    elif(func_name == "getitem_via_sibseqs"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> getitem_via_sibseqs(y,1,1)
            ['bb']
            >>>
        '''
        print(doc)
    elif(func_name == "setitem_via_pathlist"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> setitem_via_pathlist(y,"500",[1,1])
            ['a', ['b', '500'], 'c']
            >>> y
            ['a', ['b', '500'], 'c']
        '''
        print(doc)
    elif(func_name == "setitem_via_sibseqs"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> setitem_via_sibseqs(y,"500",1,1)
            ['a', ['b', '500'], 'c']
            >>> y
            ['a', ['b', '500'], 'c']
            >>>
        '''
        print(doc)
    elif(func_name == "delitem_via_pathlist"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> delitem_via_pathlist(y,[1,1])
            ['a', ['b'], 'c']
            >>> y
            ['a', ['b'], 'c']
        '''
        print(doc)
    elif(func_name == "delitem_via_sibseqs"):
        doc = '''
            >>> from xdict.elist import *
            >>> y = ['a',['b',["bb"]],'c']
            >>> y[1][1]
            ['bb']
            >>> delitem_via_sibseqs(y,1,1)
            ['a', ['b'], 'c']
            >>> y
            ['a', ['b'], 'c']
        '''
        print(doc)
    elif(func_name == "pathlist_to_getStr"):
        doc = '''
            >>> pathlist_to_getStr([1, '1', 2])
                "[1]['1'][2]"
            >>>
        '''
        print(doc)
    elif((func_name == "is_list")|(func_name == "isArray")):
        doc = '''
            >>> from xdict.elist import *
            >>> is_list([1,2,3])
            True
            >>> is_list(200)
            False
            >>>
        '''
        print(doc)
    elif(func_name == "is_leaf"):
        doc = '''
            >>> from xdict.elist import *
            >>> is_leaf(1)
            True
            >>> is_leaf([1,2,3])
            False
            >>> is_leaf([])
            True
            >>>
        '''
        print(doc)
    elif(func_name == "new_ele_description"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> root_desc = new_ele_description(leaf=False,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
            >>> pobj(root_desc)
            {
             'rcin_path': None,
             'sons_count': None,
             'lcin_path': None,
             'non_leaf_son_paths': None,
             'leaf': False,
             'breadth_path':
                             [],
             'rsib_path': None,
             'breadth': None,
             'flat_offset': None,
             'depth': 0,
             'path':
                     [],
             'leaf_descendant_paths': None,
             'parent_path':
                            [],
             'sib_seq': None,
             'leaf_son_paths': None,
             'lsib_path': None,
             'non_leaf_descendant_paths': None,
             'parent_breadth_path':
                                    [],
             'flat_len': None
            }
            >>> #None means not handled
            >>>
        '''
        print(doc)
    elif(func_name == "root_list"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> root_list([1],2,[1,2,3])
            [[1], 2, [1, 2, 3]]
            >>>
        '''
        print(doc)
    elif(func_name == "init_desc_matrix"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> l = [1,[4],2,[3,[5,6]]]
            >>> desc_matrix = init_desc_matrix(l)
            >>> pobj(desc_matrix)
            [
             [
              {
               'sib_seq': None,
               'non_leaf_descendant_paths': None,
               'flat_offset': None,
               'breadth_path':
                               [],
               'depth': 0,
               'parent_path':
                              [],
               'parent_breadth_path':
                                      [],
               'sons_count': None,
               'breadth': None,
               'leaf_descendant_paths': None,
               'rsib_path': None,
               'rcin_path': None,
               'flat_len': None,
               'path':
                       [],
               'lcin_path': None,
               'leaf': False,
               'non_leaf_son_paths': None,
               'lsib_path': None,
               'leaf_son_paths': None
              }
             ]
            ]
            >>>
        '''
        print(doc)
    elif(func_name == "reset_parent_desc_template"):
        doc = '''
            >>> pobj(desc)
            {
             'flat_offset': None,
             'leaf_descendant_paths':
                                      [],
             'breadth': 0,
             'lsib_path': None,
             'leaf': True,
             'sons_count': 4,
             'flat_len': None,
             'lcin_path': None,
             'parent_path':
                            [
                             0
                            ],
             'rsib_path':
                          [
                           1
                          ],
             'parent_breadth_path':
                                    [
                                     0
                                    ],
             'sib_seq': 0,
             'non_leaf_son_paths':
                                   [],
             'rcin_path': None,
             'leaf_son_paths': None,
             'path':
                     [
                      0
                     ],
             'non_leaf_descendant_paths': None,
             'depth': 1,
             'breadth_path':
                             [
                              0
                             ]
            }
            >>> tem = reset_parent_desc_template(desc)
            >>> pobj(tem)
            {
             'flat_offset': None,
             'flat_len': None,
             'leaf_descendant_paths': None,
             'breadth': None,
             'lsib_path': None,
             'leaf': None,
             'sons_count': None,
             'parent_path': None,
             'lcin_path': None,
             'rsib_path': None,
             'parent_breadth_path': None,
             'sib_seq': None,
             'non_leaf_son_paths':None,
             'rcin_path': None,
             'leaf_son_paths': None,
             'path':
                     [
                      0
                     ],
             'non_leaf_descendant_paths': None,
             'depth': None,
             'breadth_path':
                             [
                              0
                             ]
            }
            >>>
        '''
        print(doc)
    elif(func_name == "_init_unhandled"):
        doc = '''
            >>> from xdict.elist import *
            >>> from xdict.jprint import pobj
            >>> l = [1,[4],2,[3,[5,6]]]
            >>> desc_matrix = init_desc_matrix(l)
            >>> unhandled = _init_unhandled(l,desc_matrix)
            >>> unhandled_data = unhandled['data']
            >>> unhandled_desc = unhandled['desc']
            >>> unhandled_data[0]
            [4]
            >>> unhandled_desc[0]
            {'sib_seq': 1, 'non_leaf_descendant_paths': None, 'flat_offset': None, 'breadth_path': [1], 'depth': 1, 'parent_path': [], 'parent_breadth_path': [], 'sons_count': None, 'breadth': 1, 'leaf_descendant_paths': None, 'rsib_path': [2], 'rcin_path': None, 'flat_len': None, 'path': [1], 'lcin_path': None, 'leaf': False, 'non_leaf_son_paths': None, 'lsib_path': [0], 'leaf_son_paths': None}
            >>> unhandled_data[1]
            [3, [5, 6]]
            >>> unhandled_desc[1]
            {'sib_seq': 3, 'non_leaf_descendant_paths': None, 'flat_offset': None, 'breadth_path': [3], 'depth': 1, 'parent_path': [], 'parent_breadth_path': [], 'sons_count': None, 'breadth': 3, 'leaf_descendant_paths': None, 'rsib_path': None, 'rcin_path': None, 'flat_len': None, 'path': [3], 'lcin_path': None, 'leaf': False, 'non_leaf_son_paths': None, 'lsib_path': [2], 'leaf_son_paths': None}
            >>>
        '''
        print(doc)
    elif(func_name == "update_desc_lsib_path"):
        doc = '''
            leftSibling
            previousSibling
            leftSib
            prevSib
            lsib
            psib
            
            have the same parent,and on the left
        '''
        print(doc)
    elif(func_name == "update_desc_rsib_path"):
        doc = '''
            rightSibling
            nextSibling
            rightSib
            nextSib
            rsib
            nsib
            
            have the same parent,and on the right
        '''
        print(doc)
    elif(func_name == "update_desc_lcin_path"):
        doc = '''
            leftCousin
            previousCousin
            leftCin
            prevCin
            lcin
            pcin
            
            parents are neighbors,and on the left
        '''
        print(doc)
    elif(func_name == "update_desc_rcin_path"):
        doc = '''
            rightCousin
            nextCousin
            rightCin
            nextCin
            rcin
            ncin
            
            parents are neighbors,and on the right
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
    elif(func_name == "ListTree.__init__"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            [0]
            [1]
            [1][0]
            [2]
            [3]
            [3][0]
            [3][1]
            [3][1][0]
            [3][1][1]
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.__repr__"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            [0]
            [1]
            [1][0]
            [2]
            [3]
            [3][0]
            [3][1]
            [3][1][0]
            [3][1][1]
            >>> l
            [1, [4], 2, [3, [5, 6]]]
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> pobj(ltree.showlog)
            [
             '[1, [4], 2, [3, [5, 6]]]',
             ' 1, [4], 2, [3, [5, 6]] ',
             '     4       3, [5, 6]  ',
             '                 5, 6   '
            ]
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.tree"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            [0]
            [1]
            [1][0]
            [2]
            [3]
            [3][0]
            [3][1]
            [3][1][0]
            [3][1][1]
            >>> pathlists = ltree.tree()
            [0]
            [1]
            [1][0]
            [2]
            [3]
            [3][0]
            [3][1]
            [3][1][0]
            [3][1][1]
            >>> pathlists
            [[0], [1], [1, 0], [2], [3], [3, 0], [3, 1], [3, 1, 0], [3, 1, 1]]
            >>> pathlists = ltree.tree(leaf_only=True)
            [0]
            [1][0]
            [2]
            [3][0]
            [3][1][0]
            [3][1][1]
            >>> pathlists
            [[0], [1, 0], [2], [3, 0], [3, 1, 0], [3, 1, 1]]
            >>> pathlists = ltree.tree(leaf_only=True,from_lv=1,to_lv=2)
            [0]
            [1][0]
            [2]
            [3][0]
            >>> pathlists
            [[0], [1, 0], [2], [3, 0]]
            >>> pathlists = ltree.tree(non_leaf_only=True)
            [1]
            [3]
            [3][1]
            >>> pathlists
            [[1], [3], [3, 1]]
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.flatten"):
        doc = '''
            from xdict.elist import *
            l = [1, [4], 2, [3, [5, 6]]]
            ltree = ListTree(l)
            flat = ltree.flatten()
            flat
            ltree.flatWidth
            ltree.depth
        '''
        print(doc)
    elif(func_name == "ListTree.dig"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> depthfirst = ltree.dig()
            [0] ->
            [1] ->
            [1, 0] ->
            [2] ->
            [3] ->
            [3, 0] ->
            [3, 1] ->
            [3, 1, 0] ->
            [3, 1, 1] ->
            >>>
            >>> depthfirst = ltree.dig(2)
            [0] ->
            [1] ->
            >>> depthfirst = ltree.dig(5)
            [0] ->
            [1] ->
            [1, 0] ->
            [2] ->
            [3] ->
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.level"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> level = ltree.level(1)
            [0]
            [1]
            [2]
            [3]
            >>> level = ltree.level(1,leaf_only=True)
            [0]
            [2]
            >>> level = ltree.level(1,non_leaf_only=True)
            [1]
            [3]
            >>> level = ltree.level(2)
            [1][0]
            [3][0]
            [3][1]
            >>> level = ltree.level(3)
            [3][1][0]
            [3][1][1]
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.include"):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> l[3][1][0]
            5
            >>> ltree.include(3,1,0)
            True
            >>> l[3][1][2]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            IndexError: list index out of range
            >>> ltree.include(pathlist = [3,1,2])
            False
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.search"):
        doc = '''
            from xdict.elist import *
            from xdict.TestLib.genrand import gen_random_recursive_only_list_data as randlist
            l = randlist()
            ltree = ListTree(l)
            pathlists = ltree.search('v_4')
            pathlists.__len__()
            l[0]
            l[4][2][1][0][0][3]
            l[4][2][1][0][0][19][11]
            l[11][3]
        '''
        print(doc)
    elif((func_name == "ListTree.ancestor_paths")|(func_name == "ListTree.ancestors")):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> ltree.ancestor_paths(3,1,0)
            [[3], [3, 1]]
            >>> ltree.ancestors(3,1,0)
            [[3, [5, 6]], [5, 6]]
            >>> l[3]
            [3, [5, 6]]
            >>> l[3][1]
            [5, 6]
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.parent_paths")|(func_name == "ListTree.parents")):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> ltree.parent_path(3,1,0)
            [3, 1]
            >>> ltree.parent(3,1,0)
            [5, 6]
            >>> l[3][1]
            [5, 6]
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.descendant_paths")|(func_name == "ListTree.descendants")):
        doc = '''
            from xdict.elist import *
            >>> l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> ltree.descendant_paths(3)
            [[3, 0], [3, 1], [3, 1, 0], [3, 1, 1]]
            >>> ltree.descendants(3)
            [3, [5, 6], 5, 6]
            >>> ltree.descendant_paths(3,leaf_only=True)
            [[3, 0], [3, 1, 0], [3, 1, 1]]
            >>> ltree.descendants(3,leaf_only=True)
            [3, 5, 6]
            >>> ltree.descendant_paths(3,non_leaf_only=True)
            [[3, 1]]
            >>> ltree.descendants(3,non_leaf_only=True)
            [[5, 6]]
            >>> l[3][1]
            [5, 6]
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.son_paths")|(func_name == "ListTree.sons")):
        doc = '''
            from xdict.elist import *

        '''
        print(doc)
    elif((func_name == "ListTree.PrevSibPath")|(func_name == "ListTree.PrevSibling")|(func_name == "ListTree.lsib_path")|(func_name == "ListTree.lsib")):
        doc = '''
            from xdict.elist import *
            >>> #prevSib
            ... l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> # ltree.lsib_path
            ... ltree.prevSibPath(3,1,1)
            [3, 1, 0]
            >>> # ltree.lsib
            ... ltree.prevSibling(3,1,1)
            5
            >>> ltree.prevSibPath(3,1,0) == None
            True
            >>> #l[3][1][0] has no left sibling
            ...
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.NextSibPath")|(func_name == "ListTree.NextSibling")|(func_name == "ListTree.rsib_path")|(func_name == "ListTree.rsib")):
        doc = '''
            from xdict.elist import *
            >>>
            >>> #nextSib
            ... l = [1, [4], 2, [3, [5, 6]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6]]]
             1, [4], 2, [3, [5, 6]]
                 4       3, [5, 6]
                             5, 6
            >>> # ltree.rsib_path
            ... ltree.nextSibPath(3,1,0)
            [3, 1, 1]
            >>> # ltree.rsib
            ... ltree.nextSibling(3,1,0)
            6
            >>> ltree.nextSibPath(3,1,1) == None
            True
            >>> #l[3][1][1] has no right sibling
            ...
            >>>
        '''
        print(doc)
    elif(func_name == "ListTree.sibs"):
        doc = '''
            >>>
            >>> l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], 7, [8, 9]]]
             1, [4], 2, [3, [5, 6], 7, [8, 9]]
                 4       3, [5, 6], 7, [8, 9]
                             5, 6       8, 9
            >>> ltree.sib_paths(3,1)
            [[3, 0], [3, 1], [3, 2], [3, 3]]
            >>> ltree.sibs(3,1)
            [3, [5, 6], 7, [8, 9]]
            >>> ltree.sib_paths(3,1,leaf_only=True)
            [[3, 0], [3, 2]]
            >>> ltree.sibs(3,1,leaf_only=True)
            [3, 7]
            >>> ltree.sib_paths(3,1,non_leaf_only=True)
            [[3, 1], [3, 3]]
            >>> ltree.sibs(3,1,non_leaf_only=True)
            [[5, 6], [8, 9]]
            >>>
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.SomeSibPaths")|(func_name == "ListTree.SomeSibs")|(func_name == "ListTree.some_sib_paths")|(func_name == "ListTree.some_sibs")):
        doc = '''
            >>> #some_sibs
            ... l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], 7, [8, 9]]]
             1, [4], 2, [3, [5, 6], 7, [8, 9]]
                 4       3, [5, 6], 7, [8, 9]
                             5, 6       8, 9
            >>> #ltree.some_sib_paths
            ... ltree.someSibPaths(3,1,some=[0,3])
            [[3, 0], [3, 3]]
            >>> #ltree.some_sibs
            ... ltree.someSibs(3,1,some=[0,3])
            [3, [8, 9]]
            >>>
            >>> ltree.someSibPaths(3,1,some=[0,3],leaf_only=True)
            [[3, 0]]
            >>> ltree.someSibs(3,1,some=[0,3],leaf_only=True)
            [3]
            >>> ltree.someSibPaths(3,1,some=[0,3],non_leaf_only=True)
            [[3, 1]]
            >>> ltree.someSibs(3,1,some=[0,3],non_leaf_only=True)
            [[5, 6]]
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.whichSibPath")|(func_name == "ListTree.whichSib")|(func_name == "ListTree.which_sib_path")|(func_name == "ListTree.which_sib")):
        doc = '''
            from xdict.elist import *
            >>> #whichSib
            ... l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], 7, [8, 9]]]
             1, [4], 2, [3, [5, 6], 7, [8, 9]]
                 4       3, [5, 6], 7, [8, 9]
                             5, 6       8, 9
            >>> #ltree.which_sib_path
            ... ltree.whichSibPath(3,1,which=2)
            [3, 2]
            >>> #ltree.which_sib
            ... ltree.whichSib(3,1,which=2)
            7
            >>>
            >>> ltree.whichSibPath(3,1,which=1,leaf_only=True)
            [3, 2]
            >>> ltree.whichSib(3,1,which=1,leaf_only=True)
            7
            >>> ltree.whichSibPath(3,1,which=1,non_leaf_only=True)
            [3, 3]
            >>> ltree.whichSib(3,1,which=1,non_leaf_only=True)
            [8, 9]
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.precedingSibPaths")|(func_name == "ListTree.precedingSibs")|(func_name == "ListTree.preceding_sib_paths")|(func_name == "ListTree.preceding_sibs")):
        doc = '''
            from xdict.elist import *
            >>> #precedingSibs
            ... l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], 7, [8, 9]]]
             1, [4], 2, [3, [5, 6], 7, [8, 9]]
                 4       3, [5, 6], 7, [8, 9]
                             5, 6       8, 9
            >>> #ltree.preceding_sib_paths
            ... ltree.precedingSibPaths(3,1)
            [[3, 0]]
            >>> #ltree.preceding_sibs
            ... ltree.precedingSibs(3,1)
            [3]
            >>>
            >>> ltree.precedingSibPaths(3,1,leaf_only=True)
            [[3, 0], [3, 2]]
            >>> ltree.precedingSibs(3,1,leaf_only=True)
            [3, 7]
            >>> ltree.precedingSibPaths(3,1,non_leaf_only=True)
            []
            >>> ltree.precedingSibs(3,1,non_leaf_only=True)
            []
            >>>
        '''
        print(doc)
    elif((func_name == "ListTree.followingSibPaths")|(func_name == "ListTree.followingSibs")|(func_name == "ListTree.following_sib_paths")|(func_name == "ListTree.following_sibs")):
        doc = '''
            from xdict.elist import *
            >>> #followingSibs
            ... l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], 7, [8, 9]]]
             1, [4], 2, [3, [5, 6], 7, [8, 9]]
                 4       3, [5, 6], 7, [8, 9]
                             5, 6       8, 9
            >>> #ltree.following_sib_paths
            ... ltree.followingSibPaths(3,1)
            [[3, 2], [3, 3]]
            >>> #ltree.following_sibs
            ... ltree.followingSibs(3,1)
            [7, [8, 9]]
            >>>
            >>> ltree.followingSibPaths(3,1,leaf_only=True)
            [[3, 0], [3, 2]]
            >>> ltree.followingSibs(3,1,leaf_only=True)
            [3, 7]
            >>> ltree.followingSibPaths(3,1,non_leaf_only=True)
            [[3, 3]]
            >>> ltree.followingSibs(3,1,non_leaf_only=True)
            [[8, 9]]
            >>>
        '''
        print(doc)
    elif(func_name == "lcin"):
        doc = '''
            from xdict.elist import *
            >>> # lcin
            ... l = [1, [4], 2, [3, [5, 6],[8,9],7]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], [8, 9], 7]]
             1, [4], 2, [3, [5, 6], [8, 9], 7]
                 4       3, [5, 6], [8, 9], 7
                             5, 6    8, 9
            >>> ltree.lcin_path(3,2,0)
            [3, 1, 1]
            >>> l[3][1][1]
            6
            >>> ltree.lcin(3,2,0)
            6
            >>> l[3][2][0]
            8
            >>>
        '''
        print(doc)
    elif(func_name == "rcin"):
        doc = '''
            from xdict.elist import *
            >>> #rcin
            ... l = [1, [4], 2, [3, [5, 6],[8,9],7]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], [8, 9], 7]]
             1, [4], 2, [3, [5, 6], [8, 9], 7]
                 4       3, [5, 6], [8, 9], 7
                             5, 6    8, 9
            >>> ltree.rcin_path(3,1,1)
            [3, 2, 0]
            >>> l[3][2][0]
            8
            >>> ltree.rcin(3,1,1)
            8
            >>> l[3][1][1]
            6
            >>>
        '''
        print(doc)
    elif(func_name == "sons"):
        doc = '''
            from xdict.elist import *
            >>> #sons
            ... l = [1, [4], 2, [3, [5, 6],[8,9],7]]
            >>> ltree = ListTree(l)
            >>> ltree
            [1, [4], 2, [3, [5, 6], [8, 9], 7]]
             1, [4], 2, [3, [5, 6], [8, 9], 7]
                 4       3, [5, 6], [8, 9], 7
                             5, 6    8, 9
            >>> ltree.son_paths(3)
            [[3, 0], [3, 1], [3, 2], [3, 3]]
            >>> ltree.sons(3)
            [3, [5, 6], [8, 9], 7]
            >>> ltree.son_paths(3,leaf_only=True)
            [[3, 0], [3, 3]]
            >>> ltree.sons(3,leaf_only=True)
            [3, 7]
            >>> ltree.son_paths(3,non_leaf_only=True)
            [[3, 1], [3, 2]]
            >>> ltree.sons(3,non_leaf_only=True)
            [[5, 6], [8, 9]]
            >>>
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
            from xdict.elist import *
        '''
        print(doc)
    elif(func_name == ""):
        doc = '''
            from xdict.elist import *
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
