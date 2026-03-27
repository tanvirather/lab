package main

import (

	// "io"
	// "log"
	// "net/http"

	"zuhid.com/ai/tools"
)

func main() {
	httpClient := tools.HttpClient{BaseUrl: "http://localhost:11434/api"}
	httpClient.Get("generate")

	// URL = "http://localhost:11434"
	// MODEL = "codellama:latest"
	// fmt.Println("Hello, world")
	// resp, err := http.Get("https://www.google.com")
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// defer resp.Body.Close()

	// body, err := io.ReadAll(resp.Body)
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// fmt.Println("Status:", resp.Status)
	// fmt.Println("Body:", string(body))
}

// import (
// 	"bytes"
// 	"encoding/json"
// 	"fmt"
// 	"io/ioutil"
// 	"net/http"
// )

// // OllamaRequest represents the request payload for Ollama API.
// type OllamaRequest struct {
// 	Model   string `json:"model"`
// 	Prompt  string `json:"prompt"`
// 	Stream  bool   `json:"stream,omitempty"`
// 	Options map[string]interface{} `json:"options,omitempty"`
// }

// // OllamaResponse represents a typical response from Ollama API.
// // You may need to adjust this according to actual API response structure.
// type OllamaResponse struct {
// 	Response string `json:"response"`
// }

// // CallOllamaAPI calls the Ollama API with specified model, prompt, and optional options.
// // apiURL is the full URL to the Ollama endpoint (e.g., "http://localhost:11434/api/generate").
// func CallOllamaAPI(apiURL, model, prompt string, options map[string]interface{}) (string, error) {
// 	payload := OllamaRequest{
// 		Model:   model,
// 		Prompt:  prompt,
// 		Options: options,
// 	}

// 	body, err := json.Marshal(payload)
// 	if err != nil {
// 		return "", fmt.Errorf("failed to marshal request payload: %w", err)
// 	}

// 	resp, err := http.Post(apiURL, "application/json", bytes.NewBuffer(body))
// 	if err != nil {
// 		return "", fmt.Errorf("failed to send request to Ollama API: %w", err)
// 	}
// 	defer resp.Body.Close()

// 	if resp.StatusCode != http.StatusOK {
// 		respBody, _ := ioutil.ReadAll(resp.Body)
// 		return "", fmt.Errorf("Ollama API error: %s", respBody)
// 	}

// 	var ollamaResp OllamaResponse
// 	decoder := json.NewDecoder(resp.Body)
// 	if err := decoder.Decode(&ollamaResp); err != nil {
// 		return "", fmt.Errorf("failed to decode response: %w", err)
// 	}

// 	return ollamaResp.Response, nil
// }
