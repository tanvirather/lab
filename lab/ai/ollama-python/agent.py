# agent.py
import json
import ollama
from file_tools import (
    list_dir, read_file, write_file, append_file, modify_file_replace
)

SYSTEM_PROMPT = """You are a helpful engineering assistant.
You have access to tools for file I/O inside a sandboxed workspace.
- Only operate within the workspace via tools.
- Prefer listing before reading large folders.
- Be explicit about changes you plan to make.
- For modifications, describe intent and then call a tool.
"""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_dir",
            "description": "List files/directories in a workspace subfolder",
            "parameters": {
                "type": "object",
                "properties": {
                    "rel_path": {"type": "string", "description": "Relative path under workspace", "default": "."}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a text file within workspace with size guard",
            "parameters": {
                "type": "object",
                "properties": {
                    "rel_path": {"type": "string"},
                    "encoding": {"type": "string", "default": "utf-8"}
                },
                "required": ["rel_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Create or overwrite a file with given content",
            "parameters": {
                "type": "object",
                "properties": {
                    "rel_path": {"type": "string"},
                    "content": {"type": "string"},
                    "encoding": {"type": "string", "default": "utf-8"},
                    "overwrite": {"type": "boolean", "default": False}
                },
                "required": ["rel_path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "append_file",
            "description": "Append text to an existing file",
            "parameters": {
                "type": "object",
                "properties": {
                    "rel_path": {"type": "string"},
                    "content": {"type": "string"},
                    "encoding": {"type": "string", "default": "utf-8"}
                },
                "required": ["rel_path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "modify_file_replace",
            "description": "Replace occurrences of 'old' with 'new' in a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "rel_path": {"type": "string"},
                    "old": {"type": "string"},
                    "new": {"type": "string"},
                    "encoding": {"type": "string", "default": "utf-8"}
                },
                "required": ["rel_path", "old", "new"]
            }
        }
    },
]

def call_tool(name: str, args: dict):
    if name == "list_dir":
        return list_dir(**args)
    if name == "read_file":
        return read_file(**args)
    if name == "write_file":
        return write_file(**args)
    if name == "append_file":
        return append_file(**args)
    if name == "modify_file_replace":
        return modify_file_replace(**args)
    return {"ok": False, "error": f"Unknown tool: {name}"}

def run_chat():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "List the files in the workspace and read README.md if it exists."},
        # {"role": "user", "content": "Create notes/todo.md containing a checklist."},
    ]

    while True:
        response = ollama.chat(
            model="llama3.1:8b",  # or your preferred local model
            messages=messages,
            tools=TOOLS,
            stream=False
        )

        msg = response.get("message", {})
        content = msg.get("content")
        tool_calls = msg.get("tool_calls", [])

        if tool_calls:
            # Execute each tool call, then send tool result back into the conversation
            for tc in tool_calls:
                fn = tc.get("function", {})
                name = fn.get("name")
                # Arguments may already be dict, or str-JSON; normalize
                args = fn.get("arguments")
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception:
                        args = {"raw": args}
                result = call_tool(name, args or {})
                # Attach tool result with the same tool_call_id so the model can reference it
                messages.append({
                    "role": "tool",
                    "content": json.dumps(result),
                    "name": name,
                    "tool_call_id": tc.get("id")  # include if present
                })
        else:
            # No tool calls -> model produced a final answer
            print(content)
            # You can break, or continue the loop for interactive sessions
            user_in = input("\nYou: ").strip()
            messages.append({"role": "user", "content": user_in})
            continue

        # After tool execution, ask model to continue with the new context
        messages.append({"role": "assistant", "content": ""})  # some clients prefer explicit step




if __name__ == "__main__":
    run_chat()