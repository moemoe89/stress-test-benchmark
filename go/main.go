package main

import (
    "fmt"
    "net/http"
)

func main() {
	port := "9100"
    fmt.Printf("Listening Go server on: %s\n", port)
    
    http.HandleFunc("/", Server)
    http.ListenAndServe(":"+port, nil)
}

func Server(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Go server")
}
