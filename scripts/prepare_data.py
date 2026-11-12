from main.data.dataset import download, load_text, split

download()
text = load_text()
train, val = split(text)

for name, part in [("train", train), ("val", val)]:
    with open(f"data/processed/{name}.txt", "w", encoding="utf-8") as f:
        f.write(part)

print("total:", len(text), "train:", len(train), "val:", len(val))
print(text[:200])