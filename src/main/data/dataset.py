import urllib.request

URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
PATH = "data/raw/shakespeare.txt"

def download(path=PATH):
    urllib.request.urlretrieve(URL, path)

def load_text(path=PATH):
    with open(path, encoding="utf-8") as f:
        return f.read()

def split(text, frac=0.9):
    n = int(len(text) * frac)
    return text[:n], text[n:]
