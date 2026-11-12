import torch
from main.data.dataset import load_text
from main.tokenizer.char import CharTokenizer

tok = CharTokenizer(load_text())

for name in ["train", "val"]:
    with open(f"data/processed/{name}.txt", encoding="utf-8") as f:
        ids = torch.tensor(tok.encode(f.read()))
    torch.save(ids, f"data/processed/{name}.pt")
    print(name, ids.shape, ids[:10].tolist())

print("vocab size:", tok.vocab_size)
print(repr("".join(tok.chars)))