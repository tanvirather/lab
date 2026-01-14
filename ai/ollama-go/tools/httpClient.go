package tools

import (
	"fmt"
)

type HttpClient struct {
	BaseUrl string
}

// func New(url string) *HttpClient {
// 	return &HttpClient{url: url}
// }

func (httpClient *HttpClient) Get(url string) {
	fmt.Println(httpClient.BaseUrl + "/" + url)
}

// import (
// 	"bytes"
// 	"errors"
// 	"io"
// 	"net/http"
// 	"time"
// )

// // HttpClient is a lightweight HTTP utility for Go.
// type HttpClient struct {
// 	Client  *http.Client
// 	Headers map[string]string
// }

// // New creates a new HttpClient with a configurable timeout.
// func New(timeout time.Duration) *HttpClient {
// 	return &HttpClient{
// 		Client: &http.Client{
// 			Timeout: timeout,
// 		},
// 		Headers: make(map[string]string),
// 	}
// }

// // SetHeader sets a default header for all requests.
// func (h *HttpClient) SetHeader(key, value string) {
// 	h.Headers[key] = value
// }

// // Get sends a HTTP GET request to the specified URL.
// func (h *HttpClient) Get(url string) (string, int, error) {
// 	req, err := http.NewRequest("GET", url, nil)
// 	if err != nil {
// 		return "", 0, err
// 	}
// 	for k, v := range h.Headers {
// 		req.Header.Set(k, v)
// 	}
// 	resp, err := h.Client.Do(req)
// 	if err != nil {
// 		return "", 0, err
// 	}
// 	defer resp.Body.Close()

// 	bodyBytes, err := io.ReadAll(resp.Body)
// 	if err != nil {
// 		return "", resp.StatusCode, err
// 	}
// 	return string(bodyBytes), resp.StatusCode, nil
// }

// // Post sends a HTTP POST request to the specified URL and body.
// func (h *HttpClient) Post(url, contentType string, body []byte) (string, int, error) {
// 	req, err := http.NewRequest("POST", url, bytes.NewBuffer(body))
// 	if err != nil {
// 		return "", 0, err
// 	}
// 	for k, v := range h.Headers {
// 		req.Header.Set(k, v)
// 	}
// 	if contentType != "" {
// 		req.Header.Set("Content-Type", contentType)
// 	}
// 	resp, err := h.Client.Do(req)
// 	if err != nil {
// 		return "", 0, err
// 	}
// 	defer resp.Body.Close()

// 	respBody, err := io.ReadAll(resp.Body)
// 	if err != nil {
// 		return "", resp.StatusCode, err
// 	}
// 	return string(respBody), resp.StatusCode, nil
// }

// // Do sends a custom http.Request using current HttpClient settings.
// func (h *HttpClient) Do(req *http.Request) (*http.Response, error) {
// 	if h.Client == nil {
// 		return nil, errors.New("http client is nil")
// 	}
// 	for k, v := range h.Headers {
// 		req.Header.Set(k, v)
// 	}
// 	return h.Client.Do(req)
// }
