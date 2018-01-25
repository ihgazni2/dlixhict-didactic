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


