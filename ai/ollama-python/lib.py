import ollama

# MODEL = "llama3.1:8b"
MODEL = "codellama:latest"

# result = ollama.pull(model=MODEL)
# print(result)

# result = ollama.generate(model = MODEL, prompt="Hello, World")
# print(result.response)

result = ollama.chat(model = MODEL, messages=[
    {"role": "system", "content": "Your are an expert golang developer. I want you to write golang files that I can copy in to go file. "},
    {"role": "user", "content": "create a hello world program"}
])
print(result.message.content)

