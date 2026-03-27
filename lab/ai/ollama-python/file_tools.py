
# file_tools.py
from pathlib import Path
import json
import os

# Configure your workspace root (absolute path recommended)
WORKSPACE = Path(os.environ.get("WORKSPACE_DIR", "./workspace")).resolve()
WORKSPACE.mkdir(parents=True, exist_ok=True)

# Optional: restrict to certain file types (set to None to allow all)
ALLOWED_EXTENSIONS = {".txt", ".md", ".py", ".json", ".csv", ".go"}

# Read cap to avoid accidentally loading multi-GB files
MAX_READ_BYTES = 5 * 1024 * 1024  # 5 MB

def _safe_path(rel_path: str) -> Path:
    """Return a path inside WORKSPACE or raise ValueError if outside."""
    p = (WORKSPACE / rel_path).resolve()
    if WORKSPACE != p and WORKSPACE not in p.parents:
        raise ValueError("Path escapes workspace")
    if ALLOWED_EXTENSIONS is not None and p.suffix and p.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Disallowed file extension: {p.suffix}")
    return p

def list_dir(rel_path: str = "."):
    p = _safe_path(rel_path)
    if not p.exists():
        return {"ok": False, "error": "Path does not exist", "path": str(p)}
    if not p.is_dir():
        return {"ok": False, "error": "Path is not a directory", "path": str(p)}
    items = []
    for entry in p.iterdir():
        items.append({
            "name": entry.name,
            "is_dir": entry.is_dir(),
            "size": entry.stat().st_size if entry.is_file() else None,
        })
    return {"ok": True, "path": str(p), "items": items}

def read_file(rel_path: str, encoding: str = "utf-8"):
    p = _safe_path(rel_path)
    if not p.exists() or not p.is_file():
        return {"ok": False, "error": "File not found", "path": str(p)}
    size = p.stat().st_size
    if size > MAX_READ_BYTES:
        # Read only the head to avoid overload
        with p.open("rb") as f:
            head = f.read(MAX_READ_BYTES)
        try:
            text = head.decode(encoding, errors="replace")
        except Exception:
            text = head.decode("utf-8", errors="replace")
        return {"ok": True, "path": str(p), "partial": True, "bytes_read": len(head), "content": text}
    with p.open("r", encoding=encoding, errors="replace") as f:
        content = f.read()
    return {"ok": True, "path": str(p), "partial": False, "bytes_read": size, "content": content}

def write_file(rel_path: str, content: str, encoding: str = "utf-8", overwrite: bool = False):
    p = _safe_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite:
        return {"ok": False, "error": "File exists; set overwrite=True to replace", "path": str(p)}
    with p.open("w", encoding=encoding) as f:
        f.write(content)
    return {"ok": True, "path": str(p), "bytes_written": len(content.encode(encoding))}

def append_file(rel_path: str, content: str, encoding: str = "utf-8"):
    p = _safe_path(rel_path)
    if not p.exists():
        return {"ok": False, "error": "File not found to append", "path": str(p)}
    with p.open("a", encoding=encoding) as f:
        f.write(content)
    return {"ok": True, "path": str(p), "bytes_appended": len(content.encode(encoding))}

def modify_file_replace(rel_path: str, old: str, new: str, encoding: str = "utf-8"):
    """Simple text replace within a file."""
    p = _safe_path(rel_path)
    if not p.exists():
        return {"ok": False, "error": "File not found", "path": str(p)}
    with p.open("r", encoding=encoding, errors="replace") as f:
        data = f.read()
    updated = data.replace(old, new)
    with p.open("w", encoding=encoding) as f:
        f.write(updated)
    return {"ok": True, "path": str(p), "replacements": data.count(old)}
