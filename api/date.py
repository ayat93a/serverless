
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
    message2 = f'\n here a list of recommended books tp learn Python'
    books_path = '.../text_file/books.txt'
            
    self.send_response(200)

    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    content = open(books_path, 'r').read()
    

    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(message.encode())
    # self.wfile.write(message2.encode())
    # self.wfile.write(content)
    return



# if __name__ == '__main__':
#     handl = handler()
#     handl.do_GET()