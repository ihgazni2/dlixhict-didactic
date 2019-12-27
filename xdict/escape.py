import estring.estring as eses

def html_number_escape_char(ch):
    '''
        >>> es = html_number_escape_char('a')
        >>> es
        '&#97;'
        >>> html.unescape(es)
        'a'
        >>> es = html_number_escape_char('用')
        >>> es
        '&#29992;'
        >>> html.unescape(es)
        '用'
        >>>
    '''
    num = int(eses.str2us(ch,style="js")[2:],16)
    escaped = '&#' + str(num) +';'
    return(escaped)


def html_number_escape_str(s):
    '''
        >>>
        >>> ess = html_number_escape_str('加强武器')
        >>> ess
        '&#21152;&#24378;&#27494;&#22120;'
        >>> html.unescape(ess)
        '加强武器'
        >>> ess = html_number_escape_str('xyzw')
        >>> ess
        '&#120;&#121;&#122;&#119;'
        >>> html.unescape(ess)
        'xyzw'
        >>>
    '''
    escaped = ''
    for i in range(0,s.__len__()):
        esch = html_number_escape_char(s[i])
        escaped = escaped+esch
    return(escaped)
