import ollama
import re

m = ollama.generate(
    model="tinyllama",
    prompt="Return only one filename ending in .txt",
)

response = m["response"]

match = re.search(r"[\w\-]+\.txt", response)

if match:
    filename = match.group(0)

    with open(filename, "w") as f:
        f.write("")

    print("Created:", filename)

else:
    print("No valid filename found")
