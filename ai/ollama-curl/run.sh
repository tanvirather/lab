
clear
rm -rf output
mkdir -p output

curl --location 'http://localhost:11434/api/chat' -sS --header 'Content-Type: application/json' \
--data '{
    "model": "codellama",
    "stream": false,
    "messages": [
        {
            "role": "system",
            "content": "You are a go lang developer. You will give me the content that I can paste into a .go file. Only return the contents of the .go file"
        },
        {
            "role": "user",
            "content": "Write a hello world program"
        }
    ]
}' | jq -r '.message.content' > output/chat.go


curl --location 'http://localhost:11434/api/generate' -sS --header 'Content-Type: application/json' \
--data '{
    "model": "codellama",
    "stream": false,
    "system": "You are a go lang developer. You will give me the content that I can paste into a .go file",
    "prompt": "Write a hello world program"
}' | jq -r '.response' > output/generate.go
