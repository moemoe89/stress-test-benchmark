require 'webrick'

$stdout.sync = true

port = 9105

puts "Listening Ruby server on: #{port}"

dev_null = WEBrick::Log::new("/dev/null", 7)
server = WEBrick::HTTPServer.new({ :Port => port, :Logger => dev_null, :AccessLog => dev_null })
server.mount_proc('/') {|request, response| response.body = "Ruby server"}
trap("INT") {server.shutdown}
server.start