
from http.server import BaseHTTPRequestHandler

from urllib import parse


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
   
    self.send_response(200)

    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    
    books_path = 'text_file/books.txt'
    content = open(books_path, 'r').read()
    self.wfile.write(content)
    return



# if __name__ == '__main__':
#     handl = handler()
#     handl.do_GET()