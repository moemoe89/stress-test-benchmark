require 'webrick'

port = 9105

puts "Listening Ruby server on: #{port}"

server = WEBrick::HTTPServer.new(:Port => port)
server.mount_proc('/') {|request, response| response.body = "Ruby server"}
trap("INT") {server.shutdown}
server.start