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

