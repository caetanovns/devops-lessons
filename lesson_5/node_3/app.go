package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Message struct {
	Text string `json:"text"`
}

func main() {
	http.HandleFunc("/", helloHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	message := Message{"Ola, sou uma aplicacao em GO e posso responder requisicoes</h1>"}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(message)
}
