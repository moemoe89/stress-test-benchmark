<?php

$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die('Failed to create socket!');
$port = 9103;

socket_bind($socket, 0, $port);
socket_listen($socket);
 
print_r("Listening Python server on: ".$port."\n");

for (;;) {
    if ($client = @socket_accept($socket)) {
        socket_write($client, "HTTP/1.1 200 OK\r\n" .
               "Content-length: " . strlen('PHP server') . "\r\n" .
               "Content-Type: text/html; charset=UTF-8\r\n\r\n" .
               $msg);
    }
    else usleep(100000);
}
