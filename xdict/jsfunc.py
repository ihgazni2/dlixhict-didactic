import time

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



def toString(n,radix,**kwargs):
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




