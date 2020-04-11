from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 9104

class server(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()
		msg = "Python server"
		self.wfile.write(msg.encode('utf-8'))
		return

try:
	print('Listening Python server on: ', PORT_NUMBER, flush=True)
	server = HTTPServer(('', PORT_NUMBER), server)
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the Python server')
	server.socket.close()