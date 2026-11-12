from main.tokenizer.char import CharTokenizer

def test_roundtrip():
    tok = CharTokenizer("hello world")
    assert tok.decode(tok.encode("hello")) == "hello"

def test_vocab_size():
    assert CharTokenizer("aabbc").vocab_size == 3