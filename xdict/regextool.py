import re
from elist.elist import fcp as fcopy

operators = {'.','^','$','*','+','?','{','}','[',']','(',')','|','-','<','>','!',':'}
slash = '\\'

def creat_noOPregex_from_str(regex_str):
    regex_str = regex_str.replace('\\',"\\\\")
    for each in operators:
        regex_str = regex_str.replace(each,"\\"+each)
    regex = re.compile(regex_str)
    return(regex)


def creat_regexes_array(chars_arr):
    '''
        >>> creat_regexes_array(['"',"'",'<','>'])
        [re.compile('["]'), re.compile("[']"), re.compile('[<]'), re.compile('[>]')]
        >>> 
    '''
    #chars_arr = fcopy(chars_arr)
    chars_arr = fcopy(chars_arr)
    regex_chars_arr = []
    for i in range(0,chars_arr.__len__()):
        if(chars_arr[i] in operators):
            chars_arr[i] = '\\'+chars_arr[i]
        elif(chars_arr[i] == slash):
            chars_arr[i] = '\\\\'
        else:
            pass
        regex_str = ''.join(('[',chars_arr[i],']'))
        regex = re.compile(regex_str)
        regex_chars_arr.append(regex)
    return(regex_chars_arr)



def creat_regexes_not_array(chars_arr):
    '''
        >>> creat_regexes_not_array(['"',"'",'<','>'])
        [re.compile('[^"]'), re.compile("[^']"), re.compile('[^<]'), re.compile('[^>]')]
        >>>
    '''
    chars_arr = fcopy(chars_arr)
    regex_chars_arr = []
    for i in range(0,chars_arr.__len__()):
        if(chars_arr[i] in operators):
            chars_arr[i] = '\\'+chars_arr[i]
        elif(chars_arr[i] == slash):
            chars_arr[i] = '\\\\'
        else:
            pass
        regex_str = ''.join(('[^',chars_arr[i],']'))
        regex = re.compile(regex_str)
        regex_chars_arr.append(regex)
    return(regex_chars_arr)


def creat_regex_from_arr(chars_arr):
    '''
        >>> creat_regex_from_arr(['"',"'",'<','>'])
        re.compile('["\'<>]')
        >>> 
    '''
    chars_arr = fcopy(chars_arr)
    regex_str = '['
    for i in range(0,chars_arr.__len__()):
        if(chars_arr[i] in operators):
            chars_arr[i] = '\\'+chars_arr[i]
        elif(chars_arr[i] == slash):
            chars_arr[i] = '\\\\'
        else:
            pass
        regex_str = ''.join((regex_str,chars_arr[i]))
    regex_str = ''.join((regex_str,']'))
    return(re.compile(regex_str))



def creat_regex_not_from_arr(chars_arr):
    '''
        >>> creat_regex_not_from_arr(['"',"'",'<','>'])
        re.compile('[^"\'<>]')
        >>> 
    '''
    chars_arr = fcopy(chars_arr)
    regex_str = '[^'
    for i in range(0,chars_arr.__len__()):
        if(chars_arr[i] in operators):
            chars_arr[i] = '\\'+chars_arr[i]
        elif(chars_arr[i] == slash):
            chars_arr[i] = '\\\\'
        else:
            pass
        regex_str = ''.join((regex_str,chars_arr[i]))
    regex_str = ''.join((regex_str,']'))
    return(re.compile(regex_str))



def get_rm_regexp(l):
    regex_remove_str = '['
    for i in range(0,l.__len__()):
        regex_remove_str = ''.join((regex_remove_str,l[i]))
    regex_remove_str = ''.join((regex_remove_str,']+'))
    regex_remove = re.compile(regex_remove_str)
    return(regex_remove)

def get_insert_space_regexp(l):
    regex_insert_space_str = '['
    for i in range(0,l.__len__()):
        regex_insert_space_str = ''.join((regex_insert_space_str,l[i]))
    regex_insert_space_str = ''.join((regex_insert_space_str,']'))
    regex_insert_space = re.compile(regex_insert_space_str)
    return(regex_insert_space)
