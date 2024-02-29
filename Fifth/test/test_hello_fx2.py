from hello_fifth import hello_f

# Making another test hello to treat the test folder as a package
def test_default():
    assert hello_f() == "hello, world"

def test_argument():
    assert hello_f("Philip") == "hello, Philip"

