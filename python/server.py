from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 9104

class server(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Python server")
		return

try:
	server = HTTPServer(('', PORT_NUMBER), server)
	print 'Listening Python server on:' , PORT_NUMBER
	
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the Python server'
	server.socket.close()