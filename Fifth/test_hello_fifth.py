from hello_fifth import hello_f

# Keep test simple and minimal - so they aren't prone to have errors themselves
def test_hello_f():
    assert hello_f() == "hello, world"

def test_argumenmt():
        assert hello_f("David") == "hello, David"

def test_argument_f():
      for name in ["Hermione", "Harry", "Ron"]:
            assert hello_f(name) == f"hello, {name}"
