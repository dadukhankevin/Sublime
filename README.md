# Sublime 🍋‍🟩

Smart sub-line segmented embeddings that leave you feeling *sublime*.

Sublime offers two uniquely powerful features:
1. **Line-by-line embeddings** segmented as-needed to get exactly the code snippets required, nothing more or less
2. **Negative prompting** - just like image generation, searching over embeddings should include negative prompts

## How it works

Instead of chunking code arbitrarily, Sublime embeds every line of code individually. When you search, it uses ML clustering (similar to audio segmentation) to group nearby high-scoring lines into coherent code segments that target exactly what you've searched for.

## Quick Start

```python
from embedings import Embeddings

# Index your codebase
emb = Embeddings("./my_project")

# Search with semantic queries
results = emb.search("user authentication and login validation flow", top_n=1)

# Search with negative prompting to exclude unwanted patterns
results = emb.search("database connection and query execution", negative_query="test mocks and unit testing", top_n=1)

# Negative-only search to find problematic code
results = emb.search(negative_query="clean well-documented modern code", top_n=1)

# Print results
for result in results:
    print(f"File: {result.file_path}")
    print(f"Lines {result.start_line}-{result.end_line}")
    print(result)
```

## Usage Notes

- Use from Python by importing `Embeddings`.
- Control file types with `supported_extensions` and ignores with an `.embedignore` file.
- `top_n` returns the best segments globally across all files.

## Configuration

```python
# Custom file types and ignore patterns
emb = Embeddings(
    "./project",
    supported_extensions={".py", ".js", ".rs"}, 
    ignore_file=".embedignore"
)
```

Create `.embedignore` file:
```
node_modules
*.log
test_*
__pycache__
```

## Install

```bash
pip install -r requirements.txt
```