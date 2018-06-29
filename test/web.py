from wsgiref.simple_server import make_server
from pyquery import PyQuery

def app(env,response):
    response('200 ok', [('content-type','text/html')])
    return 'hello'


httpd = make_server('',8000,app)
print 'server on 8000 start'
httpd.serve_forever()