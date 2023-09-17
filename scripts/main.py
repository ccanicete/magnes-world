import datetime as dt

def current_time():
    try:
        now = dt.datetime.now()
        span = Element("current-time")
        span.write(now.strftime("%A, %B %d, %Y %H:%M:%S"))
    except:
        span.write("date not accessed")

def current_year():
    try:
        now = dt.datetime.now()
        span2 = Element("current-year")
        span2.write(now.strftime("%Y"))
    except:
        span2.write("date")
        
# function that clears the display 
def clr():
    Element('result').element.value = ''

# function that display value 
def dis(val):
    if Element('result').element.value == 'error':
        Element('result').element.value = val
    else:
        Element('result').element.value += val
        
# function that evaluates the digits and return result 
def solve():
    try:
        x = Element('result').element.value
        y = eval(x)
        Element('result').element.value = '{:G}'.format(y)
    except:
        Element('result').element.value = 'error'

current_time()
current_year()
