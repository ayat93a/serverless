from email import message
from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    name = dic.get('name')

    if name :
        message = f'\naloha{name}'
    else :
        message = '\naloha stranger'

    message += f'\n Greetings from python version {platform.python_version()}'
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(message.encode())
    return


""""
- if the request is correct and there are no problems: 2XX
- if the request is not correct or there is something wrong from client side: 4XX 404 403
- if the req/res are not correct or something wrong happened from server: 5XX 500
"""
