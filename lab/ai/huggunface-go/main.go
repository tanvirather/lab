package main

import (
	"fmt"
	"io"
	"os"

	"github.com/seasonjs/hf-hub/api"
	sd "github.com/seasonjs/stable-diffusion"
)

func main() {
	// Create model with default options (supports CPU/GPU via dynamic libs)
	model, err := sd.NewAutoModel(sd.DefaultOptions)
	if err != nil {
		fmt.Printf("Failed to create model: %v\n", err)
		return
	}
	defer model.Close()

	// Download model from Hugging Face (use a compatible checkpoint)
	// Note: dreamlike-photoreal-2.0 needs conversion to .ckpt format for this lib
	hapi, err := api.NewApi()
	if err != nil {
		fmt.Printf("Failed to create HF API: %v\n", err)
		return
	}

	// Use a known compatible model like miniSD (replace with converted dreamlike model)
	modelPath, err := hapi.Model("justinpinkney/miniSD").Get("miniSD.ckpt")
	if err != nil {
		fmt.Printf("Failed to download model: %v\n", err)
		return
	}

	// Load model
	err = model.LoadFromFile(modelPath)
	if err != nil {
		fmt.Printf("Failed to load model: %v\n", err)
		return
	}

	// Generate one image matching the Python loop
	prompt := "an astronaut"
	writers := make([]io.Writer, 0)

	file, err := os.Create("output/image-0.png")
	if err != nil {
		fmt.Printf("Failed to create output file: %v\n", err)
		return
	}
	defer file.Close()
	writers = append(writers, file)

	// Generate image (equivalent to pipeline(prompt).images[0].save())
	err = model.Predict(prompt, sd.DefaultFullParams, writers)
	if err != nil {
		fmt.Printf("Prediction failed: %v\n", err)
		return
	}

	fmt.Println("Image saved to output/image-0.png")
}
