def staircase(n,display='#'):
    result = ''
    for i in range(1,n+1):
        result += (' ' * ( n-i ) + display * i + ('\n' if n > 1 else ''))
    return result 
