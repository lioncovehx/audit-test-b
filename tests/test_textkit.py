from textkit import slugify, truncate


def test_slugify():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_truncate():
    assert truncate("abcdef", 4) == "abc…"
