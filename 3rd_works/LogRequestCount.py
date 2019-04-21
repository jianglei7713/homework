#!/usr/bin/env python3

logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''

l = logs.replace('"', '').split()

requestlist = [l[x].upper() for x in range(1, len(l), 5)]

request = ['POST', 'GET', 'DELETE', 'PUT', 'HEAD', 'TRACE', 'OPTIONS']
for x in request:
    output = (x, requestlist.count(x))
    if output[1] > 0:
        print(*output)
