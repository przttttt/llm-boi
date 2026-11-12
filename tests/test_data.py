from main.data.dataset import split

def test_split():
    train, val = split("a" * 100)
    assert len(train) == 90
    assert len(val) == 10

def test_split_loses_nothing():
    text = "hello world"
    train, val = split(text)
    assert train + val == text