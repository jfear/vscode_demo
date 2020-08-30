from pathlib import Path

from my_cool_pkg import io


def test_hello_world():
    assert io.hello_world() == "Hello World!"


def test_current_path():
    assert isinstance(io.current_path(), Path)


def test_fooBar():
    assert io.fooBar()[0] == "Foo"
