from ollama import Client

OLLAMA_URL="http://localhost:11434"
MODEL = "codellama:latest"

client = Client(host=OLLAMA_URL)
result = client.chat(model = MODEL, messages=[
    {"role": "system", "content": "Your are an expert golang developer. I want you to write golang files that I can copy in to go file. "},
    {"role": "user", "content": "create a hello world program"}
])
print(result.message.content)

