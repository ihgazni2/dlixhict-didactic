import re
import time
import datetime
import html


def detect_time_format(date_value):
    '''
        ####################HTTP-date###############
        # HTTP-date    = rfc1123-date | rfc850-date | asctime-date
               # rfc1123-date = wkday "," SP date1 SP time SP "GMT"
               # rfc850-date  = weekday "," SP date2 SP time SP "GMT"
               # asctime-date = wkday SP date3 SP time SP 4DIGIT
               # date1        = 2DIGIT SP month SP 4DIGIT
                              # ; day month year (e.g., 02 Jun 1982)
               # date2        = 2DIGIT "-" month "-" 2DIGIT
                              # ; day-month-year (e.g., 02-Jun-82)
               # date3        = month SP ( 2DIGIT | ( SP 1DIGIT ))
                              # ; month day (e.g., Jun  2)
               # time         = 2DIGIT ":" 2DIGIT ":" 2DIGIT
                              # ; 00:00:00 - 23:59:59
               # wkday        = "Mon" | "Tue" | "Wed"
                            # | "Thu" | "Fri" | "Sat" | "Sun"
               # weekday      = "Monday" | "Tuesday" | "Wednesday"
                            # | "Thursday" | "Friday" | "Saturday" | "Sunday"
    '''
    month = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
    weekday = 'Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday'
    wkday = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun'
    rfc1123 = ''.join(("(",wkday,")",", ","[0-9]{2} ","(",month,")"," [0-9]{4} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc1123 = re.compile(rfc1123)
    rfc1123_hypen = ''.join(("(",wkday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{4} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc1123_hypen = re.compile(rfc1123_hypen)
    rfc850 = ''.join(("(",weekday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{2} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc850 = re.compile(rfc850)
    rfc850_a = ''.join(("(",wkday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{2} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc850_a = re.compile(rfc850_a)
    asctime = ''.join(("(",wkday,")"," ","(",month,")","(( [0-9]{2})|(  [0-9]{1}))"," ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","[0-9]{4}"))
    regex_asctime = re.compile(asctime)
    if(regex_rfc1123.search(date_value)):
        return('rfc1123')
    elif(regex_rfc1123_hypen.search(date_value)):
        return('rfc1123_hypen')
    elif(regex_rfc850.search(date_value)):
        return('rfc850')
    elif(regex_rfc850_a.search(date_value)):
        return('rfc850_a')
    elif(regex_asctime.search(date_value)):
        return('asctime')
    else:
        return(None)

        


TIMEFMT = {
    'rfc1123':'%a, %d %b %Y %H:%M:%S GMT',
    'rfc1123_hypen':'%a, %d-%b-%Y %H:%M:%S GMT',
    'rfc850':'%A, %d-%b-%y %H:%M:%S GMT',
    'rfc850_a':'%a, %d-%b-%y %H:%M:%S GMT',
    'asctime':'%a, %b %d %H:%M:%S %Y',
    '%a, %d %b %Y %H:%M:%S GMT':'rfc1123',
    '%a, %d-%b-%Y %H:%M:%S GMT':'rfc1123_hypen',
    '%A, %d-%b-%y %H:%M:%S GMT':'rfc850',
    '%a, %d-%b-%y %H:%M:%S GMT':'rfc850_a',
    '%a, %b %d %H:%M:%S %Y':'asctime'
}


def fromat_asc(asc):
    asc = asc.replace("  "," 0")
    return(asc)

def standlize(s):
    regex = re.compile("[\s]+")
    s = re.sub(regex," ",s)
    return(s)


    


def get_format_name(format):
    return(TIMEFMT['format'])


def ts2dt(ts):
    '''
        only 6 bits keeped
    '''
    return(datetime.datetime.fromtimestamp(ts))

def dt2ts(dt,**kwargs):
    ''''''
    return(dt.timestamp())

def str2dt(s,**kwargs):
    if('format' in kwargs):
        format = kwargs['format']
    else:
        format_name = detect_time_format(s)
        format = TIMEFMT[format_name]
    if(format == 'asctime'):
        s = format_asc(s)
    else:
        s = standlize(s)
    return(datetime.datetime.strptime(s,format))

def dt2str(dt,**kwargs):
    if('format' in kwargs):
        format = kwargs['format']
    elif('format_name' in kwargs):
        format_name = kwargs['format_name']
        format = TIMEFMT[format_name]
    else:
        format = TIMEFMT['rfc1123']
    return(dt.strftime(format))

def str2ts(s,**kwargs):
    if('format' in kwargs):
        format = kwargs['format']
    else:
        format_name = detect_time_format(s)
        format = TIMEFMT[format_name]
    dt = str2dt(s,format=format)
    ts = dt2ts(dt)
    return(ts)


def ts2str(ts,**kwargs):
    dt = ts2dt(ts)
    if('format' in kwargs):
        format = kwargs['format']
    elif('format_name' in kwargs):
        format_name = kwargs['format_name']
        format = TIMEFMT[format_name]
    else:
        format = TIMEFMT['rfc1123']
    return(dt.strftime(format))

