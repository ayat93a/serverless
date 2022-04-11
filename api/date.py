
from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    message = f'\n Greetings from python version {platform.python_version()}'
    message2 = f'\n you will find a list of recommended books to learn Python if you fetch api/text link'
    message3 = f'\n these books are fron python.org'
    message4 = f'\n this trial serverless function is for lab 16'

            
    self.send_response(200)

    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    

    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(message.encode())
    self.wfile.write(message2.encode())
    self.wfile.write(message3.encode())
    self.wfile.write(message4.encode())
    return



# if __name__ == '__main__':
#     handl = handler()
#     handl.do_GET()