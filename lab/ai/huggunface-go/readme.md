# Installation
Install the library and its Hugging Face Hub dependency:
```sh
go mod init sd-example
go get github.com/seasonjs/stable-diffusion
go get github.com/seasonjs/hf-hub/api
go get github.com/seasonjs/hf-hub
go get github.com/seasonjs/hf-hub/api@v0.0.5

go mod download github.com/seasonjs/hf-hub
```