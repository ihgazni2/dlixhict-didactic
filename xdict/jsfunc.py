import time
import xdict.utils
import re
from xdict.utils import num_to_bin_str

def bitnum(num):
    if(num < 0):
        num = -num
    else:
        pass
    n = bin(num).__len__()-2
    return(n)

def mask(num):
    if(num>=0):
        b = bin(num)[2:]
    else:
        b = bin(num)[3:]
    m = b.replace('0','1')
    m = '0b'+m
    n = int(m,2)
    return(n)

def complement(num,model=32):
    if(num >= 0):
        return(num)
    else:
        m = bitnum(num)
        if(m > model):
            m = m
        else:
            m = model
        com = 2 ** m +num
    return(com)

def decomplement(com,model=32,sign=-1):
    if(sign == -1):
        com = 2 ** model - com
        return(-com)
    else:
        return(com)

def xor(num1,num2):
    #补码com1,com2 都当做正整数处理
    com1 = complement(num1)
    com2 = complement(num2)
    #只保留32位
    com1 = '0x' + hex(com1)[2:][-8:]
    com2 = '0x' + hex(com2)[2:][-8:]
    com1 = int(com1,16)
    com2 = int(com2,16)
    #
    com = com1 ^ com2
    #
    s = com >>31
    if(s == 1):
        com = complement(-com)
        return(-com)
    else:
        return(com)


def math_abs(n):
    if(n<0):
        return(-n)
    else:
        return(n)


def unshift(l,*args):
    length = l.__len__()
    args_len = args.__len__()
    for i in range(0,args_len):
        l.append(None)
    for i in range(length-1,-1,-1):
        l[i+args_len] = l[i]
    for i in range(0,args_len):
        l[i] = args[i]
    return(l)

def logical_or(x,y):
    if(x):
        return(x)
    else:
        return(y)

def logical_and(x,y):
    if(x):
        return(y)
    else:
        return(x)


def newDate_num(**kwargs):
    n = time.time()
    s = str(n)
    arr = s.split(".")
    sec_bitsnum = arr[0].__len__()
    ms_bitsnum = sec_bitsnum + 3
    us_bitsnum = ms_bitsnum + 3
    s = s.replace(".","")
    if('bitsnum' in kwargs):
        bitsnum = kwargs['bitsnum']
    else:
        bitsnum = ms_bitsnum
        if('unit' in kwargs):
            unit = kwargs['unit']
        else:
            unit = "ms"
        if(unit == "s"):
            bitsnum = sec_bitsnum     
        elif(unit == "ms"):
            bitsnum = ms_bitsnum
        elif(unit == "us"):
            bitsnum = us_bitsnum
        else:
            return(int(s))
    return(int(s[:bitsnum]))


def clock_seconds_with_accuracy(accuracy):
    accuracy = int(accuracy) - 1
    now = str(time.time())
    now = now.replace('.','')
    now = now[0:accuracy]
    return(int(now))

#number-to-string
def toString(n,radix,**kwargs):
    if(type(n) == type("")):
        return(n)
    else:
        pass
    if('char_set' in kwargs):
        char_set = kwargs['char_set']
    else:
        char_set = "0123456789abcdefghijklmnopqrstuvwxyz"
    r = n % radix
    q = n // radix
    rslt = char_set[r]
    n = q
    while(q>=radix):
        r = n % radix
        q = n // radix
        rslt = rslt + char_set[r]
        n = q
    rslt = rslt + str(char_set[q])
    rslt = rslt[::-1]
    return(rslt)

num2String = toString

def uint2str(ui,**kwargs):
    if('LE' in kwargs):
        LE = kwargs['LE']
    else:
        LE=False
    if('length' in kwargs):
        length = kwargs['length']
    else:
        length = None
    rslt = ''
    while(ui>0):
        c = chr(ui & 0xff)
        ui = ui >> 8
        rslt = rslt + c
    if(LE):
        pass
    else:
        rslt = rslt[::-1]
    if(length):
        if(LE):
            rslt = rslt + '\x00' * (length-rslt.__len__())
        else:
            rslt = '\x00' * (length-rslt.__len__()) + rslt
    else:
        pass
    return(rslt)


def str2uint(s,**kwargs):
    if('LE' in kwargs):
        LE = kwargs['LE']
    else:
        LE=False
    if(LE):
        s = s[::-1]
    rslt = 0
    for i in range(0,s.__len__()):
        rslt = rslt + ord(s[i])*(256**(s.__len__()-i-1))
    return(rslt)

#refer to estring
def fromCharCode(*args,**kwargs):
    if('style' in kwargs):
        style = kwargs['style']
    else:
        style = 'js'
    rslt =''
    if(style == 'py'):
        for i in range(0,args.__len__()):
            rslt = rslt + xdict.utils.unicode_num_to_char_str(args[i])
    else:
        for i in range(0,args.__len__()):
            rslt = rslt + xdict.utils.unicode_num_to_char_str(0x0000ffff & args[i])
    return(rslt)


#num
#refer to MDN Number Object methods
#toFixed()
#toExponential()
#toPrecesion()

def scinumstr2numstr(sci):
    '''
        >>> scinumstr2numstr("123.43(e1)")
        '1234.3'
        >>> scinumstr2numstr("123.43(e-1)")
        '12.343'
        >>> scinumstr2numstr("123.43(e+1)")
        '1234.3'
        >>> scinumstr2numstr("123.43(e5)")
        '12343000'
        >>> scinumstr2numstr("123.43(e-5)")
        '0.0012343'
        >>> scinumstr2numstr("123.43(e0)")
        '123.43'
        >>> scinumstr2numstr("123.43(e-3)")
        '0.12343'
        >>> scinumstr2numstr("123(e-3)")
        '0.123'
        >>> scinumstr2numstr("123(e3)")
        '123000'
        >>> 
    '''
    regex_im = re.compile("^([\d]+)\(e([\d]+)\)$")
    regex_ex = re.compile("^([\d]+)\(e\+([\d]+)\)$")
    regex_mi = re.compile("^([\d]+)\(e\-([\d]+)\)$")
    regex_im_dot = re.compile("^([\d]*)\.([\d]*)\(e([\d]+)\)$")
    regex_ex_dot = re.compile("^([\d]*)\.([\d]*)\(e\+([\d]+)\)$")
    regex_mi_dot = re.compile("^([\d]*)\.([\d]*)\(e\-([\d]+)\)$")
    im = regex_im.search(sci)
    ex = regex_ex.search(sci)
    mi = regex_mi.search(sci)
    im_dot = regex_im_dot.search(sci)
    ex_dot = regex_ex_dot.search(sci)
    mi_dot = regex_mi_dot.search(sci)
    regex_rm_zero = re.compile("([0]*)([0-9]\..*)")
    if(im):
        p1 = im.group(1)
        p2 = im.group(2)
        ns = p1 + "0" * int(p2)
    elif(ex):
        p1 = ex.group(1)
        p2 = ex.group(2)
        ns = p1 + "0" * int(p2)
    elif(mi):
        p1 = mi.group(1)
        p2 = mi.group(2)
        l = int(p2) - p1.__len__()
        if(l<0):
            ns = p1[0:-l] + "." + p1[-l:p1.__len__()]    
        elif(l==0):
            ns = "0."+ p1
        else:
            ns = "0."+"0"*l + p1
    elif(im_dot):
        p1 = im_dot.group(1)
        p2 = im_dot.group(2)
        p3 = im_dot.group(3)
        if(p1 == ""):
            p1 = "0"
        else:
            pass
        l = int(p3) - p2.__len__()
        if(l > 0):
            ns = p1 + p2 + "0" * l
            m = regex_rm_zero.search(ns)
            if(m):
                ns = m.group(2)
            else:
                pass
        elif(l == 0):
            ns = p1 + p2
        else:
            ns = p1 + p2[0:l] + "." + p2[l:] 
    elif(ex_dot):
        p1 = ex_dot.group(1)
        p2 = ex_dot.group(2)
        p3 = ex_dot.group(3)
        if(p1 == ""):
            p1 = "0"
        else:
            pass
        l = int(p3) - p2.__len__()
        if(l > 0):
            ns = p1 + p2 + "0" * l
            m = regex_rm_zero.search(ns)
            if(m):
                ns = m.group(2)
            else:
                pass
        elif(l == 0):
            ns = p1 + p2
        else:
            ns = p1 + p2[0:l] + "." + p2[l:] 
    elif(mi_dot):
        p1 = mi_dot.group(1)
        p2 = mi_dot.group(2)
        p3 = mi_dot.group(3)
        l = int(p3) - p1.__len__()
        if(p1 == ""):
            p1 = "0"
        else:
            pass
        if(l > 0):
            ns =  "0." +"0" * l +p1 + p2
        elif(l == 0):
            ns = "0." +p1 + p2
        else:
            ns =  p1[0:-l] + "." + p1[-l:] + p2
    else:
        ns = sci
    return(ns)


def parseInt(nstr,radix=10,**kwargs):
    if('char_set' in kwargs):
        char_set = kwargs['char_set']
    else:
        char_set = "0123456789abcdefghijklmnopqrstuvwxyz"
    real_char_set = char_set[0:radix]
    rs = ''
    for i in range(0,nstr.__len__()):
        if(nstr[i] in real_char_set):
            rs = rs + nstr[i]
        else:
            break
    if(rs==''):
        return(None)
    else:
        return(int(rs,radix)) 


def unsigned_right_shift(num,shift_num,**kwargs):
    if(num >=0):
        return(num>>shift_num)
    else:
        if("length" in kwargs):
            length = kwargs['length']
        else:
            length = 32
        b = num_to_bin_str(2**length + num,length=length)
        return(int(b,2)>> shift_num)
